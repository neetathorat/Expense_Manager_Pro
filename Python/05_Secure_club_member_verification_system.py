member_name = input("Enter User Name : ")
age = int(input("Enter age : "))
city = input("Enter city : ")
membership_fee_paid = input("Did you pay the membership fee? (yes/no)")
id_verified = input("is your ID verified? (yes/no)")

if age >= 18 and membership_fee_paid.lower() == "yes" and id_verified.lower() == "yes":
    print("Membership Approved")
    print("=" * 5 + "MEMBER CARD" + "=" * 5 )
    print(f"Name  : {member_name}")
    print(f"City  : {city}")
    print("Status : Active") 
else:
    print("Membership Rejected")
    if age < 18:
        print("Reason : Age below 18")
    elif membership_fee_paid.lower() != "yes":
        print("Reason : Fee not paid")
    else:
        print("Reason : ID not verified")