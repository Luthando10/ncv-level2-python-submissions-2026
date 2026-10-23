mark =int(input("Please enter the mark: "))
if mark >= 0 and mark <= 100:
    if mark >= 75 and mark < 75:
        print("Pass")
    elif mark >= 75:
        print("Distinction")
    elif mark < 50:
        print("Fail")
        
else:
    print("Enter a number between 0 and 100")