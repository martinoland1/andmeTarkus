class File_functions:

    def add_line_to_file(self, file_path, line):
        with open(file_path, "a", encoding='utf-8') as f:
            f.write(line + "\n")
    
    def read_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.readlines()