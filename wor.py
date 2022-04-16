import csv



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
def c_obj():
    q = 0
    main_obj = []
    while q < len(x):
        p = Date[q] # change date
        p2 = x[q] #change data
        main_dict = dict({'Year': p[0], 'Month': p[1],  'Day':dict({p[2]: p2[1]})})
        main_obj.append(main_dict)
        q = q + 1
    print(main_obj[13])

c_obj()

    








# print('\n1)Open price\n 2)Close price\n 3)High price\n 4)Low Price\n 5)Volume')
# u = int(input('What information do you want to see?\n Enter the number --> '))












