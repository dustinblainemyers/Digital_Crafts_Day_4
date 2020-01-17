
# long vowels exercise

vowels = 'aeiou'
user = input(("ENTER: "))
user = "good cheese"
new_string = ''

i = 0

#note to self: is it actually easier to use a while loop if you want to start at a certain number?

while i < len(user):
    if user[i] == user[i - 1] and user[i] in vowels:
        new_string += user[i] * 4
    else:
        new_string += user[i]
    i += 1
print(new_string)

