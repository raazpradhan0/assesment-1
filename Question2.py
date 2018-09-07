# Q. The user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

def count_string(input, sub):
    count = 0
    lenX = len(input)
    LenY = len(sub)
    
    for i in range(0, lenX):
        if input[i] == sub[0]:
            if input[i:i + LenY] == sub:
                count += 1
    return count

x = input("Enter a string : ")
y = input("Enter a sub string : ")
print(count_string(x,y))