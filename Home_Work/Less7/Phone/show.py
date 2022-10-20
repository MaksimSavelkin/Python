import csv
def show_data():
    with open('Telefon.csv', newline=", encoding="utf-8") as File: 
        reader = csv.reader(File)
        for row in reader:
            print (row)

show_data()