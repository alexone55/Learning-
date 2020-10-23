import zipfile
import os
import sys

def get_cmd_files(arg_list):
    files = []
    
    for filename in arg_list[1:]: # start from second item in command line
        files.append(filename)

    return files    

def get_all_files():
    current_dir = os.getcwd()
    files = []

    for filename in os.listdir(current_dir):
        if filename.startswith("."): # skip hidden files and folders
            continue
        
        files.append(filename)

    return files

def zip_all_in_dir(files):
    with zipfile.ZipFile('arch.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip_arch: 
        for fname in files:
            zip_arch.write(fname)
        
        zip_arch.close()

def main():
    input_files = sys.argv
    
    if len(input_files) >= 2:
        files = get_cmd_files(input_files)
        zip_all_in_dir(files)
    
    else:
        files = get_all_files()
        zip_all_in_dir(files)


if __name__ == "__main__":
    main()