import csv
import matplotlib.pyplot as plt
import matplotlib 
import numpy as np
import os 




with open('WMT.csv') as File:
    reader = csv.reader(File)
    x = list(reader)


    # the loop, which create a main array Date
    i = 1
    Date = []
    while i < len(x):
        dat = x[i]
        dat_n = list(dat[0].split("-"))
        Date.append(dat_n)
        i = i + 1 
    # Date[] - example: ['2022', '12', '15'] - p[0]
    x.pop(0)
b = True
while b:

    print('What type of data you want? \n 1)Open price\n 2)High price\n 3)Low price\n 4)Close Price\n 5)Adj Close\n 6)Volume')
    type_information = int(input('What information do you want to see? \n Enter the number --> '))
    type_view = int(input('What period of time you want to see?\n 1)By month\n 2)By year\n --> '))
    if type_view == 1:
        year = int(input('Enter the year --> '))
        month = int(input('Enter the month --> '))
    if type_view == 2:
        year = int(input('Enter the year --> '))
    if year > 2022 or year < 1972:
        print('Error: Uncorrect date')
        break

    if month > 12 or month < 0:
        print('Error: Uncorrect date')
        break



    def c_obj(index):
        global labels, data
        q = 0
        main_obj = []
        while q < len(x):
            p = Date[q] # change date
            p2 = x[q] #change data
            main_dict = dict({'Year': int(p[0]), 'Month': int(p[1]),  'Day':dict({int(p[2]): float(p2[index])})})
            main_obj.append(main_dict)
            q = q + 1

        count = 0
        labels = []
        data = []
        test = []
        while count < len(main_obj):
            if year == main_obj[count].get('Year'):
                print('Found!')
                print(main_obj[count])
                for key, val in main_obj[count].get('Day').items(): 
                    test.append([key, val])
                count = count + 1
            else:
                count = count + 1
        
        k = 0 
        while k < len(test):
            ag = test[k]
            data.append(ag[1])
            labels.append(ag[0])   
            k = k + 1
        
        print(data)
        print(labels)
        plt.style.use('ggplot')
        fig, ax = plt.subplots()
        ax.plot(data)
        ax.set_ylabel('Walmart stock prices in $')
        ax.set_xlabel('Date in days')
        plt.title(f'Walmart stock prices in {year}')
        plt.savefig(f'Walmart stock prices in {year}.png')
        
        plt.show()


    if type_information == 1:
        c_obj(1)
    if type_information == 2:
        c_obj(2)
    if type_information == 3:
        c_obj(3)
    if type_information == 4:
        c_obj(4)
    if type_information == 5:
        c_obj(5)
    if type_information == 6:
        c_obj(6)
    else:
        print('Error: Uncorrect number')
        break












