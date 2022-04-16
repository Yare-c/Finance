import csv

# todo
# 1) fix shit with main array

with open('WMT.csv') as File:
    reader = csv.reader(File)
    x = list(reader)


    i = 1
    arr_date = []

    while i < len(x):
        date = x[i]
        arr_date.append(date[0])
        i = i + 1 

    gar = [] 
    def good_date():
        h = 0
        while h < len(arr_date):
            k = arr_date[h]
            k_n = list(k.split("-"))
            gar.append(k_n)
            h = h + 1

        
    
        # search
        # u = 0
        # while u < len(gar):
        #     new = gar[u]
        #     if '2015' == new[0]:
        #         print('Found')
        #         print(new)
        #         u = u + 1
        #     else:
        #         u = u + 1

    x.pop(0)
    good_date()
    q = 0
    main_obj = []
    while q < len(x):
        date = gar[q]
        t = x[q]
        main_dict = dict({'Year': date[0], 'Month': date[1],  1:dict({date[2]: t[1]})})
        main_obj.append(main_dict)
        q = q + 1
    

    


# good array


# output of this function are 
# 1) gar - array with date arrayes

# print('\n1)Open price\n 2)Close price\n 3)High price\n 4)Low Price\n 5)Volume')
# u = int(input('What information do you want to see?\n Enter the number --> '))












