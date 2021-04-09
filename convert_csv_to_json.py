from csv import DictReader
import json


def convert():
    # open file in read mode
    data={}
    with open('test.csv', 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)
        # iterate over each line as a ordered dictionary
        for row in csv_dict_reader:
            # row variable is a dictionary that represents a row in csv
            print(row)
            data[row['Company']] = row
        print('Data:', data)
        
    with open('iron.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    
convert()