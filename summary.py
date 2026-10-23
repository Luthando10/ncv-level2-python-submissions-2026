#raw = "  1234 DLAMINI Kyle Stone apple card "
#name = raw.strip().title()
#parts = name.split()
#print("Name:   ", parts[2])
#print("Surname:", parts[-1].upper())

#if parts[0].isdigit():
#   print("Accepted")
#else:
#    print("Rejected")

#salary = 23400.56
#print(f"R__{salary:.2f}")
#print(f"R__{salary:.<60}")
#print(f"R__{salary:.>60}")

full_name = input("Please Enter your full name: ")
staff_number = input("Please enter your staff number: ")
level = input("Please enter your level: ")

if full_name.isalpha():
    print("Accepted")
elif staff_number.isdigit():
    print("Perfect")
else:
    print("Invalid")

#if is accepted
print(full_name)
print(staff_number)
print(level)

print("The name of the employee is,", full_name, "the staff number is:", staff_number, "and the employee  post level is:", level)

   
    