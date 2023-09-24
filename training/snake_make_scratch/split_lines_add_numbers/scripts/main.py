
from faker import Faker
import sys, os, re
import shutil

# Faker.seed(1)
fake = Faker()

# TODO 
# change print function to logging
# refactor

def generate_text():
    generated = ""
    directory_path = "data"
    file_path = f"{directory_path}/generated_text.txt"
    
    for _ in range(10):
        generated+= fake.paragraph(nb_sentences=4) + "\n"
    
    make_directory(directory_path)
    fill_file(file_path, generated)

def split_file_line():
    file_path = "data/generated_text.txt"
    if path_exists(file_path):
        with open(file_path, "r") as file:
            for index,line in enumerate(file):
                # f = open(f"data/split_text_{index}.txt","w")
                line_content = f"{index}-{line.strip().upper()}"
                fill_file(f"data/split_text_{index}.txt",line_content)
    print("Generated files successfully")

def join_files():
    pattern = r"\d+\.txt"
    regex = re.compile(pattern)
    # list all files in the current directory
    all_files = os.listdir("data")
    matching_files = [f"data/{file}" for file in all_files if regex.search(file)]
    file_contents = ""
    for file_path in sorted(matching_files):
        try:
            with open(file_path,"r") as file:
                file_contents+= f"{file.read()}\n" 
        except FileNotFoundError:
            print(f"File {file_path} not found.\n")
    fill_file("data/joined_text.txt", file_contents)
    
def remove_directory():
    directory_path = "data"
    if path_exists(directory_path):
        try:
            shutil.rmtree(directory_path)
            print(f"Directory {directory_path} and its contents have been removed successfully.")
        except OSError as e:
            print(f"Error removing directory: {e}")
    else:
        print(f"Path not exists: {e}")
    
def clean_files():
    all_files = os.listdir("data")
    keyword = "text"
    matching_files = [file for file in all_files if keyword in file]
    print(f"file to remove: {sorted(matching_files)}")
    # Loop through the filenames and remove files containing the keyword
    for file_path in matching_files:
            try:
                os.remove(file_path)
                print(f"File {file_path} has been removed.")
            except FileNotFoundError:
                print(f"File {file_path} not found.")

# Utils functions
def make_directory(directory_path):
    try:
        if not os.path.exists(directory_path):    
            os.makedirs(directory_path)
            print(f"Directory {directory_path} created successfully.")
        else:
            print(f"Directory {directory_path} exists")        
    except OSError as e:
        print(f"Error creating directory: {e}")
        
def fill_file(filename, content):
    try:
        f = open(filename, "w")
        f.write(content)
        f.close()
        print(f"File {filename} fill successfully.")
    except OSError as e:
        print(f"Error fill file: {e}")
        
def path_exists(file_path):
    return os.path.exists(file_path) 
                
if __name__ == "__main__":
    function_map = {
        "generate_text": generate_text,
        "split_file": split_file_line,
        "join_files": join_files,
        "remove_directory": remove_directory        
    }
    
    func_name = sys.argv[1]
    selected_func = function_map.get(func_name)
    if selected_func:
        selected_func()
    else:
        print("Invalid function name")
    