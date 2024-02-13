print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? ")) #cm
bill = 0 #dollar

if height > 120:
   print("You can ride the rollar coaster!")
   age = int(input("What is your age? "))
   if age < 12:
       bill = 5
       print("Please pay $5. ")
   elif age <= 18:
      bill = 7
      print("Please pay $7. ")
   else:
      bill = 12
      print("Please pay $12. ")
      want_photo = input("Do you want a photo Y or N ")
      if want_photo == "Y":
          bill = bill + 3
          print(f"Your final bill will be ${bill}")
      else:
          bill
          print(f"Your final bill will be ${bill}")
else:
   print("Sorry, you can't ride the rollarcoaster!")  