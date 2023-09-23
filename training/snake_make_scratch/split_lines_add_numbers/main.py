from faker import Faker
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
    
if __name__ == "__main__":
    function_map = {
        "generate_text": generate_text,
    }
    
    func_name = sys.argv[1]
    selected_func = function_map.get(func_name)
    if selected_func:
        selected_func()
    else:
        print("Invalid function name")