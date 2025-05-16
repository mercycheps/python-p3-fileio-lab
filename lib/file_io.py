def write_file(file_name, file_content):
    full_path = f'{file_name}.txt'
    with open(full_path, "w") as files:
        files.write(file_content)

def append_file(file_name, append_content):
    full_path = f'{file_name}.txt'
    with open(full_path, "a") as files:
        files.write(append_content)

def read_file(file_name):
   full_path = f'{file_name}.txt'
   with open (full_path, "r") as files:
       return files.read().strip()
