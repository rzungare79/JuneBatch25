
"""
Result =1
for i in range(5):
    Result = Result*i

print("value of multilication :",Result)
def method1():
    s1 = []
    for i in emp:
        if i in s1:
         return True
        else:
         s1.append(i)
    return False

emp = [1, 2, 3, 4, 5, 1, 3]
print(method1())



def method1():
    s1 = []
    for i in emp:
        if i in s1:
            print("Duplicate found:", i)   # print duplicate immediately
        else:
            s1.append(i)

emp = [1, 2, 3, 4, 5, 1, 3]
method1()



def find_duplicates():
    seen = set()
    duplicates = set()

    for i in emp:
        if i in seen:
            duplicates.add(i)   # collect duplicate
        else:
            seen.add(i)

    print(seen)
    print(duplicates)

emp = [1, 2, 3, 4, 5,1,2]
print(find_duplicates())
"""





