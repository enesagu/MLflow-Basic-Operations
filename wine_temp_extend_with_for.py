import os 
import warnings
import sys

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import mlflow
from mlflow.models.signature import infer_signature
import mlflow.sklearn

import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_absolute_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Wine-quality CSV dosyasını URL'den oku
    csv_url = "https://raw.githubusercontent.com/mlflow/mlflow/master/tests/datasets/winequality-red.csv"

    try:
        data = pd.read_csv(csv_url, sep=";")
    except Exception as e:
        logger.exception("Eğitim ve test CSV'si indirilemedi, internet bağlantınızı kontrol edin. Hata: %s", e)

    # Veriyi eğitim ve test kümelerine ayır (0.75 , 0.25)
    train, test = train_test_split(data, test_size=0.25)

    # Tahmin edilecek sütun "quality", bu sütun [3, 9] aralığında bir skaler
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train["quality"]
    test_y = test["quality"]



    # Take commandline arguments
    exp_name = sys.argv[1] if len(sys.argv) > 1 else "Default"
    
    
    try:
        exp_id = mlflow.create_experiment(exp_name)
    except Exception as e:
        exp_id = mlflow.get_experiment_by_name(exp_name).experiment_id
        
    

    for alpha in [1,2]:
        for l1_ratio in [0.1, 0.5, 0.8]:
            
    
            with mlflow.start_run():
                lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
                lr.fit(train_x, train_y)

                predicted_qualities = lr.predict(test_x)

                (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

                print("Elasticnet model ( alpha = {:f}, l1_ratio={:f} ): ".format(alpha, l1_ratio))
                print(" RMSE: %s" % rmse)
                print(" MAE: %s" % mae)
                print(" R2: %s" % r2)

                mlflow.log_param("alpha", alpha)
                mlflow.log_param("l1_ratio", l1_ratio)
                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("r2", r2)
                mlflow.log_metric("mae", mae)



                tracking_url_type_store = urlparse(mlflow.get_artifact_uri()).scheme

                


                # Model kaydı dosya deposuyla çalışmaz
                if tracking_url_type_store != "file":
                    # Modeli kaydet
                    mlflow.sklearn.log_model(lr, "model", registered_model_name="ElasticnetWineModel")
                else:
                    mlflow.sklearn.log_model(lr, "model")
