import os
import shutil


from_dir = "/Users/ppl20/Downloads"  
to_dir = "/Users/ppl20/Desktop/Document_Files"  

list_of_files = os.listdir(from_dir)
print("List of files in the source directory:", list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue

    if extension.lower() in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(to_dir, "Document_Files", file_name)

        if os.path.exists(path2):
            print(f"Moving {file_name} to {path3}")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print(f"Created directory: {path2}")
            print(f"Moving {file_name} to {path3}")
            shutil.move(path1, path3)
