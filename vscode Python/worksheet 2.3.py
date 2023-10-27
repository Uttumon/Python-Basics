# a={'a':100,'b':200,'c':300}
# b={"a":300,"b":200,"c":400}
# print("First dictionary is: ") 
# print(a, "\n")
# print("Second dictionary is: ") 
# print(b,"\n")
# c = b
# for i,j in a.items(): 
#     if i in b:
#         c[i] = j + b[i] 
#     else:
#         c[i] = j
# print("After both the dictionaries") 
# print("The new dict is:", c)


f = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}
print("Entered Dictionary:") 
print(f, "\n")
print("The 3 highest values in the dictionary:") 
print("Keys: Values")

x=list(f.values()) 
d=dict() 
x.sort(reverse=True)

x=x[:3]
for i in x:
    for j in f.keys(): 
        if(f[j]==i):
            print(str(j)+" : "+str(f[j]))
