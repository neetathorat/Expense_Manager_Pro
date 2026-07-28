for i in range(1,6):
    print("*"*i)

for i in range(5,0,-1):
    print("*"*i)

for i in range(1,6):
    print(" " * (5-i) + "*" * i)

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
        
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
