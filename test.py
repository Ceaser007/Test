s=[]
x=int(input("Enter the number of values")) #inputing the number of inputs
for i in range(0,x):
    y=int(input("Enter the number")) #getting each input
    s.append(y)
odd=[]
even=[]
for i in range(0,x-1):
    c=s[i]
    for j in range(i+1,x):
        if((c*s[j])%2==0):
            print("Even Pair")
            if((c,s[j]) not in even and (s[j],c) not in even): #to prevent duplicate entry if the numbers in the list are repeated
                even.append((c, s[j]))


        if((c+s[j])%2!=0):
            print("Odd Pair")
            if ((c, s[j]) not in odd and (s[j], c) not in odd):#to prevent duplicate entry if the numbers in the list are repeated
                odd.append((c, s[j]))
print("The pairs whose product is even are: ")
print(even)
print("The pairs whose sum is odd are: ")
print(odd)