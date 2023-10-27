num=int(input("Enter rows= "))
rows=0
while rows<num:
    space=num-rows-1
    while space>0:
        print(end=" ")
        space=space-1
    pattern=rows+1
    while pattern>0:
        print("o", end=" ")
        pattern=pattern-1
    rows=rows+1
    print()
        