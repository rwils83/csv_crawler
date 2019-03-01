import csv
#import collections
fileName = raw_input("Please Enter the File Name: ")
#print fileName
f=open(fileName)
field1 = raw_input("Enter the First Field: ")
field1 = int(field1)
# field2 = raw_input("Enter the second field: ")
# field2 = int(field2)
reader = csv.reader(f)

for row in reader:
    if row[field1] == '':
        print  '{:<30}'.format('null'), #'{:>40}'.format(row[field2])
    elif len(row[field1])>= 25:
        print '{:<30}'.format(row[field1]), #'{:>30}'.format(row[field2])

    else:
        print '{:<30}'.format(row[field1]), #'{:>40}'.format(row[field2])

     #   print len(row[0])

    #thisdict[row[field1]]= row[field2]


#print thisdict2


