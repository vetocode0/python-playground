age = int(input("How old are you?\n"))
decades = age//10
remainingYears = int(age)%10
print("You are " + str(decades) + 
      " decades and " + str(remainingYears) + " year(s) old.")