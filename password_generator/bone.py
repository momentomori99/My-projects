import numpy as np
import random as rand
import time
class Create_pass:
    def __init__(self):
        self.number = np.array([0,1,2,3,4,5,6,7,8,9])
        with open('random_wordlist.txt') as wordlist:
            line = wordlist.read().split("\n")
            self.line = line[:-1] #somehow last element was always empty

        with open('random_wordlist2.txt') as wordlist2:
            line = wordlist2.read().split("\n")
            self.line2 = line[:-1]
    def random(self):
        print("Creating password...")
        time.sleep(0.2)
        print(".")
        time.sleep(0.2)
        print(".")
        time.sleep(0.2)
        print(".")
        time.sleep(0.2)






        word = str(rand.choice(self.line))
        word2 = str(rand.choice(self.line2))
        numb = str(rand.choice(self.number)) + str(rand.choice(self.number)) + str(rand.choice(self.number))
        result = word2 + word + numb
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

        random_word = str(rand.choice(self.line2))
        numb = str(rand.choice(self.number)) + str(rand.choice(self.number)) + str(rand.choice(self.number))
        result = random_word + str(word) + numb
        return result


if __name__ == '__main__':
    inst = Create_pass()
    result1 = inst.random()
    print(result1)
    # word = input("whats the word:")
    # result2 = inst.own_word(word)
    # print(result2)
