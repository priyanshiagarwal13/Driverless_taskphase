string_1 = input("Enter your value: ")
string_2 = input("Enter your value: ")
a = list(set(string_1) ^ set(string_2))
print("The letters are:")
for i in a:
    print(i)