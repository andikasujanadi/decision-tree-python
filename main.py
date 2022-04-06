import os
import csv
from attr import attributes
from texttable import Texttable

class DrawTable:
    def draw(self,array,header=True):
        self.table = Texttable()
        if(not header):
            array.insert(0,["-" for i in range(len(array[0]))])
        self.table.add_rows(array)
        print(self.table.draw())

class Dataset:
    def __init__(self,filename):
        self.filename = filename
        self.dataset_array = [["Data not available"],["Check file name"]]
        self.targets = self.trim_target_attribute()
        self.table = DrawTable()
    
    def open_csv(self):
        self.dataset_array = []
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                self.dataset_array.append(row)
                line_count += 1
    
    def transpose(self,l):
        return [list(i) for i in zip(*l)]
    
    def get_sample(self):
        dataset_sample = []
        for index in range(1,len(self.dataset_array)):
            dataset_sample.append(self.dataset_array[index][0])
        return dataset_sample

    def get_attribute(self):
        dataset_attribute = []
        for index in range(1,len(self.dataset_array)):
            dataset_attribute.append(self.dataset_array[index][1:-1])
        return dataset_attribute
    
    def trim_attribute(self):
        attributes = self.transpose(self.get_attribute())
        res = []
        for i in range(len(attributes)):
            res.append(list(set(attributes[i])))
        return res
    
    def get_target_attribute(self):
        target_attribute = []
        for index in range(1,len(self.dataset_array)):
            target_attribute.append(self.dataset_array[index][-1])
        return target_attribute

    def trim_target_attribute(self):
        return list(set(self.get_target_attribute()))
    
    def calculate_entropy():
        pass
        
    def testing(self):
        self.open_csv()
        print("testing ground")
        # print("CSV")
        # self.table.draw(self.dataset_array)
        # print("Attributes")
        # self.table.draw(self.get_attribute(),header=False)
        # print("target")
        print(self.trim_attribute())
        # print(self.trim_target_attribute())
                
def main():
    #clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    dataset = Dataset("data.csv")
    dataset.testing()

if __name__ == '__main__':
   main()