import zipfile

def extract_archive(file_path,dest_directory):
    with zipfile.ZipFile(file_path, 'r') as file:
        file.extractall(dest_directory)

if __name__=="__main__":
    extract_archive()

