import os

def check_non_png_images(root_dir):
    # Ekstensi gambar yang umum (selain .png)
    image_extensions = ['.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.PNG', '.JPG', '.JPEG', '.GIF', '.BMP', '.TIFF', '.WEBP']
    
    # List untuk menyimpan hasil temuan
    non_png_files = []

    # Berjalan melalui semua folder dan subfolder
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            # Dapatkan ekstensi file
            _, ext = os.path.splitext(file)
            
            # Cek jika file adalah gambar tapi bukan .png
            if ext in image_extensions:
                full_path = os.path.join(root, file)
                non_png_files.append(full_path)

    # Tampilkan hasil
    if non_png_files:
        print("Ditemukan file gambar selain .png:")
        for file_path in non_png_files:
            print(file_path)
        print(f"\nTotal file ditemukan: {len(non_png_files)}")
    else:
        print("Tidak ditemukan file gambar selain .png")

# Gunakan script
if __name__ == "__main__":
    # Ganti dengan path folder yang ingin diperiksa
    folder_path = "."  # Gunakan "." untuk folder saat ini
    check_non_png_images(folder_path)
