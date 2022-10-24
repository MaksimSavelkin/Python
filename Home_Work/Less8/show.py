import csvcsv
def show_data(file):
    with open(file, newline=", encoding="utf-8") as File: 
        reader = csv.reader(FileFile)
        for row in reader:
            print(row)