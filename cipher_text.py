#the below is about taking an plain text as the input then converts it into an cipher text(not human readable)...
alphabet = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 't' , 's' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 't' , 's' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']

direction = input("Type 'encode' to Encrypt , Type 'decode' to Decrypt \n")
text = str(input("Enter the Plain text: \n")).lower()
shift = int(input("Enter the shift amount: \n"))

def ceaser(start_text , shift_amount , cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift_amount
            end_text = alphabet[new_position]
            cipher_text += end_text
        print(f"The encrypted value is {cipher_text}")

        elif direction == "decode":
            new_position = position - shift_amount
            end_text = alphabet[new_position]
            cipher_text += end_text
        print(f"The encrypted value is {cipher_text}")
            




#     if direction == "encode":


#         def encrypt(plain_text , shift_amount):
#             cipher_text = ""
#             for letter in plain_text:
#                 position = alphabet.index(letter)
#                 new_position = position + shift_amount
#                 new_letter = alphabet[new_position]
#                 cipher_text += new_letter
#             print(f"The encrypted value is {cipher_text}")

#         encrypt(plain_text=text , shift_amount=shift)
#     elif direction == "decode":
#         text = str(input("Enter the Cipher text: \n")).lower()
#         shift = int(input("Enter the shift amount: \n"))
        
#         def decrypt(cipher_text , shift_amount):
#             plain_text = ""
#             for letter in cipher_text:
#                 cipher_position = alphabet.index(letter)
#                 new_position = cipher_position - shift_amount
#                 new_letter = alphabet[new_position]
#                 plain_text += new_letter
#             print(f"The decrypted value is {plain_text}")

#         decrypt(cipher_text=text , shift_amount=shift)

#     else:
#         print("Enter the valid answer...")

# ceaser()
