from os  


def change_info_file(, id: str, last_name, first_name, diagnosis, chamber : str, size_cp , status):
    '{0};{1};{2};{3};{4};{5};{6} = '='.format (id, last_name, first_name, , chamber, size_cp, status)
    if path.isfile(file_name):
        with open(file_name, 'r', encoding="utf-8") as file1:
            data = file1.readlines()
            for i in range(len(data)):
                lst = data[i].replace("\n", ").split(';')
                if lst[0] == id:
                    data[i] = new_str
                    break
        with open(file_name, 'w', encoding="utf-8") as file2: 
            file2.writelines(data) 
        print ("Data added to", file_name)
    else:
        print("File not found, write the data to a file")
        return [0]


def read_data (file_name):
    if path.isfile(file_name):
        with open(file_name, 'r', encoding="utf-8") as file1:
            data = file1.readlines()
        return data
    else:
        print("File not found, write the data to a file", file_name)
        return [0]