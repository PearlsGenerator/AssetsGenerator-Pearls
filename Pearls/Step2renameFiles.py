import os

def rename_images_in_folder(folder_path):
    # Mendapatkan list file gambar dalam folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    # Mengurutkan file
    image_files.sort()
    
    # Mengganti nama file
    for index, old_name in enumerate(image_files, start=1):
        # Mendapatkan ekstensi file
        file_extension = os.path.splitext(old_name)[1]
        # Membuat nama baru
        new_name = f"{index}{file_extension}"
        # Path lengkap untuk file lama dan baru
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        # Mengganti nama file
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")

def process_all_folders(root_path):
    # Mendapatkan semua folder di root path
    folders = [f.path for f in os.scandir(root_path) if f.is_dir()]
    
    # Memproses setiap folder
    for folder in folders:
        print(f"\nProcessing folder: {folder}")
        rename_images_in_folder(folder)
        
if __name__ == "__main__":
    # Gunakan current directory sebagai root path
    root_path = "."
    process_all_folders(root_path)
