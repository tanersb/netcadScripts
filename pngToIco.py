import os
from PIL import Image

def convert_pngs_to_ico(input_folder, output_folder):
    # Giriş klasöründeki tüm dosyaları listele
    files = os.listdir(input_folder)
    
    # Her dosya için döngü
    for file in files:
        # Dosyanın tam yolunu oluştur
        file_path = os.path.join(input_folder, file)
        
        # Dosya uzantısını kontrol et (sadece PNG dosyalarını işle)
        if file.lower().endswith('.png'):
            # PNG dosyasını aç
            img = Image.open(file_path)
            
            # Yeni dosya adını oluştur (uzantıyı değiştir)
            new_file_name = os.path.splitext(file)[0] + '.ico'
            
            # Yeni dosyanın tam yolunu oluştur
            new_file_path = os.path.join(output_folder, new_file_name)
            
            # PNG dosyasını ICO olarak kaydet
            img.save(new_file_path)
            
            print(f"{file} başarıyla ICO olarak kaydedildi.")

if __name__ == "__main__":
    input_folder = "png"   # Giriş klasörü
    output_folder = "ICO"  # Çıkış klasörü
    
    convert_pngs_to_ico(input_folder, output_folder)
