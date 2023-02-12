import csv, operator
with open('names.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)
data = csv.reader(open('names.csv'),delimiter=',')
data = sorted(data, key=operator.itemgetter(0))    
print('After sorting:')
print(data)
with open("names.csv") as f:
    for i, line in enumerate(f):
        if i%2 == 0:
            print(line)

import csv
filename = open('names.csv', 'r')

file = csv.DictReader(filename)
name = []
for col in file:
	name.append(col['name'])
print('Names:', name)
def listToString(name):
    str1 = " "
    return (str1.join(name))
print(listToString(name))
def remove(string):
    return "".join(string.split())
string = listToString(name)
print(remove(string))

str_ = ""
min_diff = 10 ** 6 
for i in range(len(name)):
    str_ += name[i]
str_ = str_.replace(" ", "")
print(str_)
for i in range(len(str_) - 1):
    diff = abs(ord(str_[i + 1]) - ord(str_[i]))
    if (diff < min_diff) and (diff != 0):
        min_diff = diff
print(min_diff)
