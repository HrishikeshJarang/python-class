#Prime Number Checker

def prime_checkers(number):  #define function name
    is_prime = True   #if "is_prime = True - it's prime number"
    for i in range(2, number): 

        #Statement or Formula to check prime number
        if number % i == 0:  #number = 13, 13%2 ==0 so is_prime = False
            is_prime = False

    #Conditions to check if the number is prime number or not        
    if is_prime: #if "is_prime = True - it's prime number"
        print(f"{number} is a prime number")
    else: #number = 13, 13%2 !=0 so is_prime = False
        print(f"{number} is not a Prime Number")    

n = int(input())        

prime_checkers(number=n)  #calling function with variable "number" having value "n"