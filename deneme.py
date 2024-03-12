
import gdown

# İndirme bağlantısı
url = ''

# Dosya adı
output = 'test.zip'

# Dosyayı indir
gdown.download(url, output, quiet=False)
