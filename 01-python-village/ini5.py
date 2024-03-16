from os import path

script_dir = path.dirname(__file__) #<-- absolute dir the script is in
rel_path = 'ini5.txt'
abs_file_path = path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    i = 1
    for line in f.readlines():
        if i % 2 == 0 :
            print(line)
        i += 1