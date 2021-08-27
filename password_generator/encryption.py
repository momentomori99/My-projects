import numpy as np


# for i in range(len(list)):
#     exp = list[i]
#     index = alphabet.index(str(exp))
#     new_index = index + 2
#     if new_index > (len(alphabet)-1):
#         new_index = (new_index - len(alphabet)) + 1
#     encrypted_input[i] = alphabet[new_index]
# encrypt = encrypted_input[0] + encrypted_input[2]

class Encryption:
    def __init__(self, input):
        self.input = input
        with open('symbols.txt') as wordlist:
            self.line = wordlist.read().split("\n")

        split_input = list(self.input)

        encrypted_input = np.zeros(len(self.input))
        for i in range(len(split_input)):
            




if __name__ == '__main__':
    Encryption("abc123")
