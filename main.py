import os
import csv
from texttable import Texttable

class DrawTable:
    def draw(self,array,header=True):
        self.table = Texttable()
        if(not header):
            array.insert(0,["-" for i in range(len(array[0]))])
            # self.table.header([1 for i in range(len(array[0]))])
        self.table.add_rows(array)
        print(self.table.draw())

class Dataset:
    def __init__(self,filename):
        self.filename = filename
        self.dataset_array = [["Data not available"],["Check file name"]]
        self.table = DrawTable()
        
    
    def open_csv(self):
        self.dataset_array = []
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                self.dataset_array.append(row)
                line_count += 1
    
    def get_dataset_sample(self):
        dataset_sample = []
        for index in range(1,len(self.dataset_array)):
            dataset_sample.append(self.dataset_array[index][0])
        return dataset_sample

    def get_dataset_attribute(self):
        dataset_attribute = []
        for index in range(1,len(self.dataset_array)):
            dataset_attribute.append(self.dataset_array[index][1:-1])
        return dataset_attribute
    
    def get_dataset_target_attribute(self):
        dataset_target_attribute = []
        for index in range(1,len(self.dataset_array)):
            dataset_target_attribute.append(self.dataset_array[index][-1])
        return dataset_target_attribute
        
    def testing(self):
        print("testing ground")
        self.open_csv()
        print("CSV")
        self.table.draw(self.dataset_array)
        print("Attribute")
        self.table.draw(self.get_dataset_attribute(),header=False)
                
def main():
    #clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    dataset = Dataset("data.csv")
    dataset.testing()

if __name__ == '__main__':
   main()