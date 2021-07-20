import numpy as np
import random as rand
import time
class Create_pass:
    def __init__(self):
        self.number = np.array([0,1,2,3,4,5,6,7,8,9])
        with open('random_wordlist.txt') as wordlist:
            self.line = wordlist.read().split("\n")
    def random(self):
        print("Creating password...")
        time.sleep(0.3)
        print(".")
        time.sleep(0.3)
        print(".")
        time.sleep(0.3)
        print(".")
        time.sleep(0.3)

        word = str(rand.choice(self.line))
        numb = str(rand.choice(self.number)) + str(rand.choice(self.number)) + str(rand.choice(self.number))
        result = word + numb
        return result

    def own_word(self, word):
        print("Creating password...")
        time.sleep(0.3)
        print(".")
        time.sleep(0.3)
        print(".")
        time.sleep(0.3)
        print(".")
        time.sleep(0.3)

        numb = str(rand.choice(self.number)) + str(rand.choice(self.number)) + str(rand.choice(self.number))
        result = str(word) + numb
        return result


if __name__ == '__main__':
    inst = Create_pass()
    result1 = inst.random()

    word = input("whats the word:")
    result2 = inst.own_word(word)
    print(result2)
