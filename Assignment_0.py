#!/usr/bin/env python
# coding: utf-8

# In[ ]:


################################################Q.1#######################################################



print("Q.1. Even Numbers in Given List\n")
list_1= [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 
         237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 
         767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]

for x in list_1:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)
print("_"*50)



#################################################Q.2######################################################



print("Q.2. print out a set containing all the colours from color_list_1 which are not present in color_list_2.\n")
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

print("_"*50)



##################################################Q.3#####################################################



print("Q.3. Pangram String\n")
s = input('Enter string for checking Pangram : ')
c = {i for i in s if i.isalpha()}
if(len(c) == 26):
    print("Your string is a pangram")
else :
    print('Your String is not a Pangram')

print("_"*50)


    
##################################################Q.4######################################################



print("Q.4. Computes the value of n+nn+nnn.\n")
num = int(input("Enter Your Number: "))
n= (num + ((num*10)+num) + ((num*100)+(num*10)+num))
print(n)
print("_"*50)



##################################################Q.5######################################################



print("Q.5. Generate Two List having integer inside.\n")
i= input('Enter the string in required fashion : ')
n = i.split('#')
l_1 = n[0].split()
l_2 = n[1].split()
l_1 = [int(i) for i in l_1]
l_2 = [int(i) for i in l_2]
print('list 1 : ',l_1)
print('list 2 : ',l_2)

print("_"*50)



##################################################Q.6######################################################



print("Q.6. Print the words in a comma-separated sequence after sorting them Alphabetically.\n")
sequence=[x for x in input("Enter The Sequence: ").split(',')]
sequence.sort()
print (','.join(sequence))
print("_"*50)



#################################################Q.7#######################################################



print("Q.7.  Python function to find the name of person obtained highest marks in exam from given dictionary.\n")
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]} 
highest_marks=d['Marks'].index(max(d['Marks']))
print(d['Student'][highest_marks])

print("_"*50)



#################################################Q.8######################################################



print("Q.8. Write a program that accepts a sentence and calculate the number of letters and digits.\n")
st = input("Enter string:\n")
d= {"DIGITS":0, "LETTERS":0}
for c in st:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("LETTERS: ", d["LETTERS"])
print ("DIGITS: ", d["DIGITS"])
print("_"*50)



#################################################Q.9#######################################################



print("Q.9. Create New Dictionary of Students.\n")
d = {'name':['akash','rahul','vishakha','akshay','soniya','vikas'],
     'subjects':['python','java','python','c','python','java'],
     'ratings':['8.4','8.2','8','9','7.8','5.6']}
ND = {'name':[],'ratings':[]}
index = 0
for sub in d['subjects']:
    if(sub == 'python'):
        ND['name'].append(d['name'][index])
        ND['ratings'].append(d['ratings'][index])
        index += 1

print('New dictionary of students :',ND)
print("_"*50)



#################################################Q.10######################################################


print("Q.10. Define a Class with a Generator.\n")
n = int(input())
div = [i for i in range(0, n) if (i % 7 == 0)]
print(div)
def DC(n):
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False
        print(i, value)

DC(n)
print("_"*50)


#################################################Q.11#######################################################


print("Q.11. Robot Tracing.\n")
a = int(input("UP: "))
b = int(input("Down: "))
c = int(input("Left: "))
d = int(input("Right: "))
    
    
            
l1= abs(a - b)
l2= abs(d-c)
Td = (l1**2 + l2**2)**0.5

print('Distance: ',round(Td))

print("_"*50)


# In[ ]:




