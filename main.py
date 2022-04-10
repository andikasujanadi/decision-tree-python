import os
import csv
import math
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

    def sum_list(self, list):
        return sum(list[0:len(list)])
    
    def get_sample(self):
        dataset_sample = []
        for i in range(1,len(self.dataset_array)):
            dataset_sample.append(self.dataset_array[i][0])
        return dataset_sample

    def get_data_attribute(self):
        dataset_attribute = []
        for i in range(1,len(self.dataset_array)):
            dataset_attribute.append(self.dataset_array[i][1:-1])
        return dataset_attribute
    
    def get_attribute_header(self):
        return self.dataset_array[0][1:-1]
    
    def trim_attribute(self):
        attributes = self.transpose(self.get_data_attribute())
        res = []
        for i in range(len(attributes)):
            res.append(list(set(attributes[i])))
        return res
    
    def get_target_attribute(self):
        target_attribute = []
        for i in range(1,len(self.dataset_array)):
            target_attribute.append(self.dataset_array[i][-1])
        return target_attribute

    def get_target_header(self):
        return self.dataset_array[0][-1]

    def trim_target_attribute(self):
        return list(set(self.get_target_attribute()))
    
    def calculate_entropy(self):
        target_attribute = self.get_target_attribute()
        target_header    = self.get_target_header()
        target_trim      = self.trim_target_attribute()
        target_value     = []
        data_attribute   = self.get_data_attribute()
        data_header      = self.get_attribute_header()
        data_trim        = self.trim_attribute()
        
        for i in range(len(target_trim)):
            target_value.append(0)
            for j in range(len(target_attribute)):
                if(target_trim[i]==target_attribute[j]):
                    target_value[i]+=1

        for i in range(len(data_header)):
            table = []
            table.append([data_header[i],target_header,'sum'])
            q = []
            entropy = 0
            data_sum = []
            for j in range(len(data_trim[i])):
                sub_data_sum = []
                for k in range(len(target_trim)):
                    sub_data_sum.append(0)
                    # sub_data_sum = 0
                    for l in range(len(data_attribute)):
                        same_data_attribute = data_attribute[l][i] == data_trim[i][j]
                        same_target_attribute = target_attribute[l] == target_trim[k]
                        if same_data_attribute and same_target_attribute:
                            sub_data_sum[k] += 1
                    table.append([data_trim[i][j],target_trim[k],sub_data_sum[k]])
                data_sum.append(self.sum_list(sub_data_sum))
                sub_q = []
                for k in range(len(sub_data_sum)):
                    divided = sub_data_sum[k]/self.sum_list(sub_data_sum)
                    try:
                        temp = -(divided*math.log(divided,2))
                        sub_q.append(temp)
                    except:
                        sub_q.append(10000000)
                q.append(self.sum_list(sub_q))
                print(f'q{j+1} = {q[j]}') if q[j]<=1 else print(f'q{j+1} = ~')
            for j in range(len(data_trim[i])):
                entropy += data_sum[j]/self.sum_list(data_sum)*q[j]
            entropy = 1 if entropy>1 else entropy
            print(f'E  = {entropy}')
            self.table.draw(table)
            print('\n\n')

    def testing(self):
        self.open_csv()
        print("testing ground")
        print()
        self.calculate_entropy()
                
def main():
    #clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    dataset = Dataset("data.csv")
    dataset.testing()

if __name__ == '__main__':
   main()