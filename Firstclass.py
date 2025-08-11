


"""
def calculate(a,b,c):
    x=a+b+c

    print("addition of all value :", x)
calculate(5,6,7)
calculate(10.5,10.6,10.5)


#datatypes

name ="Rakesh"
age =18
salary =10000.56
print("type of name datatype :",type(salary))


markInPhy = "60"
markINMarth ="90"

markTotal = int(markINMarth) + int(markInPhy)



print("type of total marks :",type(markTotal) ,"sum of marks :",markTotal)



age =17
if (age >18):
     print("your are elligible")

else:
 print("your are not eligible")

print("control came out of loop")

90
marks = int(input("Enter your Marks :"))

if  (marks >= 80):
    print("your are brilliant")

elif (marks >=60 and marks <80):
    print ("your are average")

elif (marks>=35 and marks <60):
    print("you are below average")

else:
    print("you are fail")


for x in range(10):
    print(x)
print(emplist1[1])
print(emptupple[1])
emplist1 = ["Rakesh","Ketan","Amol"]
emptupple   = ("Rakesh","Ketan","Amol")


print(emplist1)
emplist1.append("ramesh")
print(emplist1)

names=[]

while True:
  name = input("Enter name or enter q for quit :")
  if  name == 'q':
      break
  names.append(name)

print(names)

data = []

for i in range(5):
    if(i < 3):
        data.append(i)
    else:
        print("control came out of if loop")
print(data)


emp_list1 =[1,2,3,4,5,6,2,4,4,5]
print(emp_list1)

emp_list1.insert(0,20)
print(emp_list1)

emp_list1.remove(20)
print(emp_list1)

print(emp_list1.pop(0))
print(emp_list1)


emp_list1.clear()

print(emp_list1.count(4))
emp_list1.sort()
print(emp_list1)
emp_list1.reverse()
print(emp_list1)


emp_tuple =[1,2,3,4,5,6,2,4,4,5]
print(emp_tuple)
print(emp_tuple.index(3))

emp_set ={1,2,3,4,5,6,2,4,4,5}
print(emp_set)
emp_set.add(50)
print(emp_set)

emp_set.update([77,78,79])
print(emp_set)


set1 = {1,2,3,4,5}
set2 ={3,4,5,6}
print(set1)
print(set2)

set_result = set1 | set2
print(set_result)

#common
set_result = set1 & set2
print(set_result)

#minus
set_result = set1 - set2
print(set_result)

emp_dist = {1:"a",2:"b",3:"c"}
print(type(emp_dist))

print(emp_dist[2])


emp_dist = {1:"a",2:"b",3:"c"}


print(emp_dist.keys())

print(emp_dist.values())

emp_dist[7]="y"
print(emp_dist)

emp_dist.pop(1)
print(emp_dist)


emp_dist.popitem()

print(emp_dist)

emp_dist = {1:"a",2:"b",3:"c"}

for key,value in emp_dist.items():
    print(key,":",value)


    emp_dist = {1:"a",2:"b",3:"c"}

for keys in emp_dist.keys():
        print(keys+100)


marks_list.reverse()
print(marks_list)
# highest number form the list

marks_list =[20,30,89,29,50]

marks_list.sort()
n = len(marks_list)


print(marks_list(n-1))
City = "ETLqalabs"
reverse1 = ''

for i in City:
    reverse1 = i + reverse1

print(reverse1)

city = "ETLqalabs"

print(city[3:8:1])

list1 =[1,2,3,4,3]

Non_duplicae_List =[]
duplicate_list = []

def Duplicat_check():
 for i in list1:
    if i in Non_duplicae_List:
        duplicate_list.append(i)

    else:
      Non_duplicae_List.append(i)

 if duplicate_list:
     print("duplicate found", duplicate_list)
     return "Yes"

 else:
     print("No duplicate Found")
     return False
print(Duplicat_check())

list_1 = [1, 4, 3, 19, 5]
def getmaxi():
    maxi_num = 0
    for i in list_1:
        if i > maxi_num:
         maxi_num =i
    print(maxi_num)


getmaxi()



list1= [1,2,3,4,5,6,1,2,3,4,1,2,3,]

list2= [1,2,3,4,1,2,3]

def numer_duplicate(list):
    dict1 ={}

    for i in list:
        if i in dict1:
            dict1[i] = dict1[i]+1
        else:
          dict1[i]=1

    print(dict1)
numer_duplicate(list2)

    """

#python day 3


# Databas Connectivity
from sqlalchemy import create_engine
import pandas as pd



mysql_connection = create_engine("mysql+pymysql://root:Rakesh%4012345@localhost:3306/collage")
sqlquery = """ select * from student"""
df = pd.read_sql(sqlquery, mysql_connection)
print(df)




























































