#  Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)

# Expected Output : 20


from xml.dom.minidom import Element


li = []

Elements = int(input("Enter number of elements to be Stored : "))

for i in range(Elements):
    li.append(int(input(" Enter the Elements :")))

print(li)

def summation(a):
    print(f'sum of all elements of list {sum(a)}')

summation(li)
