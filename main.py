string=input("Enter the input")

str=string.split("c")

str1=str[0]
str2=str[1]
str2=list(str2)
print(str2);
for i in range(len(str2)):
    print(str2[i]+str2[i+1])
    i=i+2