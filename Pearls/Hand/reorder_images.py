import os
import shutil

def reorder_images(folder_path, source_num, target_num):
    # Mendapatkan daftar file PNG
    files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    
    # Mengubah nama file sementara untuk menghindari konflik
    temp_prefix = 'temp_'
    
    if source_num > target_num:
        # Bergerak maju
        for i in range(target_num, source_num):
            current_file = f'{i}.png'
            next_file = f'{i+1}.png'
            if current_file in files:
                temp_name = temp_prefix + current_file
                shutil.move(os.path.join(folder_path, current_file), 
                          os.path.join(folder_path, temp_name))
    else:
        # Bergerak mundur
        for i in range(source_num, target_num + 1)[::-1]:
            current_file = f'{i}.png'
            prev_file = f'{i-1}.png'
            if current_file in files:
                temp_name = temp_prefix + current_file
                shutil.move(os.path.join(folder_path, current_file), 
                          os.path.join(folder_path, temp_name))
    
    # Memindahkan file sumber ke posisi target
    source_file = f'{source_num}.png'
    if source_file in files:
        shutil.move(os.path.join(folder_path, source_file), 
                   os.path.join(folder_path, f'{target_num}.png'))
    
    # Mengembalikan nama file yang diubah sementara
    temp_files = [f for f in os.listdir(folder_path) if f.startswith(temp_prefix)]
    for temp_file in temp_files:
        original_num = int(temp_file.replace(temp_prefix, '').replace('.png', ''))
        if source_num > target_num:
            new_num = original_num + 1
        else:
            new_num = original_num - 1
        shutil.move(os.path.join(folder_path, temp_file), 
                   os.path.join(folder_path, f'{new_num}.png'))

# Contoh penggunaan
folder_path = '.'  # Gunakan folder saat ini
source_num = 61    # Nomor file yang ingin dipindahkan
target_num = 62    # Nomor tujuan

reorder_images(folder_path, source_num, target_num)