#Fruits Basket

dirty_dozen = ["Strawberries", "Spinach", "Apples", "Grapes", "Peaches", "Kale", "Nectarines", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
fruits[-1] = "Melons"  #first from last
fruits.append("Lemons") #last value
#Nested List
dirty_dozen = [fruits, vegetables]

print(dirty_dozen)  #fruits + vegetables
print(dirty_dozen[0])  #fruits
print(dirty_dozen[1])  #vegetables


print(dirty_dozen[0][2]) #from [0]- fruits and fruits[2] - Apple