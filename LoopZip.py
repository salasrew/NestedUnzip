import os
import zipfile

# 指定要讀取的目錄路徑
# folder_path = 'E:/Lab3_小組報告/'
folder_path = 'C:/Users/salasrew/Downloads/Lab5_小組報告/'

# 遍歷目錄下的所有資料夾
for dirpath, dirnames, filenames in os.walk(folder_path):
    # 對於每個資料夾，列出所有以".zip"為副檔名的檔案
    for filename in filenames:
        if filename.endswith('.zip') or filename.endswith('.rar') or filename.endswith('.7z') :
            # 計算zip檔案的完整路徑
            zip_path = os.path.join(dirpath, filename)

            # 解壓縮zip檔案到與zip檔案同名的目錄中
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.splitext(zip_path)[0])

            print(f'已解壓縮{zip_path}到{os.path.splitext(zip_path)[0]}目錄中。')
