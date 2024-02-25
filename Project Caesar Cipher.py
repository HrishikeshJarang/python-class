#Project Caesar Cipher 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift = shift % 26

    
def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabet:  #if any of char is present in alphabet go with this
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = position + shift_amount
            elif cipher_direction == "decode":
                new_position = position - shift_amount
            else:  #if any of text or char not in alphabet then whatever store in char print as a end_text
                end_text += char     
        #or
        # if cipher_direction == "decode":
        #     shift_amount *= -1     #shift_amount 
        # new_position = position + shift_amount        
            end_text += alphabet[new_position]  
                
    print(f"The {cipher_direction} text is {end_text}")  


#caeser(start_text=text, shift_amount=shift, cipher_direction=direction)    
# from art import logo
# print(logo)
    
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)    

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if result == 'no':
        should_continue = False
        print("GoodBye")