# #uppercase a string

# input_string1 = input("What is your string ? ")
# upper_string = input_string1.upper()
# print("Your string in upper case is %s " % upper_string)


# #capitalize string

# input_string2 = input("What is your second  string ? ")
# cap_string = input_string2.capitalize()
# print("Your string capitalized is %s " % cap_string)


# #reverse a string

# input_string3 = input("What is your string to reverse? ")

# count = 1
# reverse_string = ""
# for letter in input_string3:
#     reverse_string += input_string3[len(input_string3) - count]
#     count += 1
# print(reverse_string)

# #leetspeak

# input_string4 = input("What is your string to encrypt to leet speak ? ").upper()

# encrypt_message = " "


# for char in input_string4:
#    if char == "A":
#        char = "4"
       
#    if char == "E":
#        char  = "3"
        
#    if char == "G":
#        char  = "6"
#    if char == "I":
#        char  = "1"
#    if char == "O":
#        char  = "0"
#    if char == "S":
#        char  = "5"
#    if char == "T":
#        char  = "7"
#    encrypt_message += char

    

# print(encrypt_message)


# #long-long vowels

# userinput5 = input("Enter a word and I will multiply all the duplicate adjacent vowels ").lower()


# userinput5 = userinput5.replace("oo","ooooo")
# userinput5 = userinput5.replace("aa","aaaaa")
# userinput5 = userinput5.replace("ee","eeeee")
# userinput5 = userinput5.replace("ii","iiiii")
# userinput5 = userinput5.replace("uu","uuuuu")

# print(userinput5)


#ceasar cypher

string_2_encryz = input("Enter the text you want to encrypt")

encrypzified = ""

alphakey = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encryptkey = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
# for alpha in alphakey:
# for char in string_2_encryz:
# for char in string_2_encryz:
for char in string_2_encryz:
    for alpha in alphakey:
        if char == " ":
            encrypzified += " "
            break
        elif char == alpha:
            rep = encryptkey[alphakey.index(alpha)]
            encrypzified += rep
            break
        
            
            
            

print(encrypzified)
#lbh zhfg hayrnea jung lbh unir yrnearq
# for char in string_2_encryz:
#     for encrypz in encryptkey:
#         if char == encrypz:
#             char = alphakey[encryptkey.index(encrypz)]
#     encrypzified += char

# print(encrypzified)


 






    












