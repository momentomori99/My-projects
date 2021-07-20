from bone import Create_pass

"""
inst = Create_pass()
result1 = inst.random()

word = input("whats the word:")
result2 = inst.own_word(word)
print(result2)

"""

inst = Create_pass()
random = input("Do you want to use your own word in your password? [y/n]:")

if random == "y":
    word = input("please tell me the word then:")
    result = inst.own_word(word)

if random == "n":
    result = inst.random()


print("your password is", '\33[45m' + result + '\x1b[0m')
