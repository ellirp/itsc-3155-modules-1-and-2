

# taking input
b=input("Enter a string: ")

# Remove space from string
b=b.replace(" ","")

# initialize list
d=[]

for i in range(len(b)):
    # checking string character in lower case, if true then store in list
    if(b[i].islower()==True):
        d.append(b[i])
        
        
for j in range(len(b)):
    # checking string character in upper case, if true then store in list
    if(b[j].isupper()==True):
        d.append(b[j])
        
# print the element present in list d
for x in d:
    print(x,end="")
