# MLflow ile Elastik Ağ Modeli Kullanarak Şarap Kalitesi Tahmini
Bu proje, MLflow'un izleme ve model yönetimi yeteneklerini kullanarak, ElasticNet regresyon modelini kullanarak kırmızı şarap kalitesini tahmin etmek için bir makine öğrenimi modeli eğitir ve değerlendirir.

## Proje Yapısı
Proje, Python programlama dili kullanılarak geliştirilmiştir. İşte proje dosyalarının yapısı:

**mlflow_elasticnet_wine.ipynb**: Jupyter Notebook dosyası, veri analizi, model eğitimi ve MLflow kullanarak sonuçların izlenmesi ve değerlendirilmesi için kullanılan kodları içerir.

**requirements.txt**: Projenin çalışması için gereken Python paketlerini içeren bir gereksinimler dosyasıdır.

**README.md**: Proje hakkında genel bilgileri ve nasıl kullanılacağına dair kılavuzu içeren bu dosyadır.

## Kurulum
Projeyi çalıştırmak için aşağıdaki adımları izleyin:

Bu depoyu klonlayın: **git clone https://github.com/enesagu/MLflow-Basic-Operations.git**
Anaconda veya pip kullanarak gerekli Python paketlerini yükleyin: **pip install -r requirements.txt**
Jupyter Notebook dosyasını açın ve kodları çalıştırın.
## MLflow Entegrasyonu
Bu proje MLflow'u kullanarak model eğitimi ve sonuçların izlenmesini sağlar. MLflow, her bir modelin performansını değerlendirmek için kullanılan metrikleri ve parametreleri izlemenizi sağlar. Ayrıca, eğitilen modelleri kaydetmenize, sürümlemesine ve paylaşmanıza olanak tanır.

## Eğitim ve Değerlendirme
Proje, kırmızı şarap kalitesini tahmin etmek için ElasticNet regresyon modeli kullanır. Model, veri kümesinin bir kısmını eğitim için kullanır ve geri kalanını test etmek için ayrır. Ardından, modelin performansını ölçmek için RMSE (Karekök Ortalama Kare Hatası), MAE (Ortalama Mutlak Hata) ve R2 skorları gibi metrikler kullanılır.

## MLflow UI
Projeyi çalıştırdıktan sonra, MLflow UI'yı kullanarak eğitim deneylerini ve sonuçlarını görselleştirebilirsiniz. MLflow UI, model performansını karşılaştırmak, parametre ayarlarını gözden geçirmek ve eğitim deneylerinin geçmişini incelemek için güçlü bir araçtır.

## Daha Fazla Bilgi

Proje hakkında daha fazla bilgi edinmek için lütfen MLflow belgelerine bakın veya proje sahibiyle iletişime geçin.

---

# Predicting Wine Quality Using Elastic Net Model with MLflow Integration

This project trains and evaluates a machine learning model using the ElasticNet regression model to predict the quality of red wine, leveraging the tracking and model management capabilities of MLflow.

## Project Structure
The project is developed using the Python programming language. Here's the structure of the project files:

**mlflow_elasticnet_wine.ipynb**: A Jupyter Notebook file containing the code for data analysis, model training, and tracking and evaluation of results using MLflow.

**requirements.txt**: A requirements file containing the necessary Python packages for the project to run.

**README.md**: This file provides general information about the project and serves as a guide on how to use it.

## Installation
To run the project, follow these steps:

Clone this repository: **git clone https://github.com/enesagu/MLflow-Basic-Operations.git**
Install the required Python packages using Anaconda or pip: **pip install -r requirements.txt**
Open the Jupyter Notebook file and run the code.

## MLflow Integration
This project utilizes MLflow to facilitate model training and tracking of results. MLflow allows you to track metrics and parameters used to evaluate the performance of each model. Additionally, it enables you to save, version, and share trained models.

## Training and Evaluation
The project uses the ElasticNet regression model to predict the quality of red wine. The model trains on a portion of the dataset and reserves the rest for testing. Metrics such as RMSE (Root Mean Squared Error), MAE (Mean Absolute Error), and R2 score are used to measure the model's performance.

## MLflow UI
After running the project, you can visualize training experiments and results using the MLflow UI. MLflow UI is a powerful tool for comparing model performance, reviewing parameter settings, and examining the history of training experiments.

## More Information
For more information about the project, please refer to the MLflow documentation or contact the project owner.
