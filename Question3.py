# Q. You are given a string and your task is remove all Upper case letters. 

x="This is mE 123"
y=[]
for i in x:
    if not i.isupper():  
        y.append(i)
        
result = ""
for j in y:
    result = result + j + ""

print (result)
