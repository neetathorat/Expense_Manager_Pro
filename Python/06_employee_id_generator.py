employee_name = input("Enter User Name : ")
no_of_id = int(input("How many employee ID you want to generate? "))
print(f"\n Employee Name : {employee_name}\n")
for i in range(1,no_of_id+1):
     print(f"EMP-{i:03d}")
