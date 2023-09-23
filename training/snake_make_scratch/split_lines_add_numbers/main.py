from faker import Faker
import sys, os, glob, re

# Faker.seed(1)
fake = Faker()

def generate_text():
    generated = ""
    # file_path = "generated_text.txt"
    for _ in range(10):
        generated+= fake.paragraph(nb_sentences=4) + "\n"
    
    # if os.path.exists(file_path):
    #     os.remove(file_path)
        
    f = open("generated_text.txt", "w")
    f.write(generated)
    f.close()
    print("Generated successfully")
    

def split_file_line():
    with open("generated_text.txt", "r") as file:
        for index,line in enumerate(file):
            f = open(f"split_text_{index}.txt","w")
            line_cap = f"{index}-{line.strip().upper()}"
            f.write(line_cap)
            f.close()
    print("Generated files successfully")

def join_files():
    pattern = r"\d+\.txt"
    regex = re.compile(pattern)
    # list all files in the current directory
    all_files = os.listdir()
    matching_files = [file for file in all_files if regex.search(file)]
    file_contents = ""
    for file_path in sorted(matching_files):
        try:
            with open(file_path,"r") as file:
                file_contents+= f"{file.read()}\n" 
        except FileNotFoundError:
            print(f"File {file_path} not found.\n")
    f = open("joined_text.txt","w")
    f.write(file_contents)
    f.close()

if __name__ == "__main__":
    function_map = {
        "generate_text": generate_text,
        "split_file": split_file_line,
        "join_files": join_files,
    }
    
    func_name = sys.argv[1]
    selected_func = function_map.get(func_name)
    if selected_func:
        selected_func()
    else:
        print("Invalid function name")