import random
import string

latter = string.ascii_lowercase

msg = input("Enter a Message: ")
words = msg.split(" ")
choice = input("Enter '1' for encoding & '0' for Decoding: ")
coding = True if (choice == '1') else False
if coding:
    nword = []
    for word in words:
        str1 = "".join(random.choice(latter) for i in range(3))
        str2 = "".join(random.choice(latter) for i in range(3))
        if len(word) >= 3:
            r1 = str1
            r2 = str2
            str = r1 + word[1:] + word[0] + r2
            nword.append(str)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))
else:
    nword = []
    for word in words:
        if len(word) >= 3:
            str = word[3:-3]
            str = str[-1] + str[:-1]
            nword.append(str)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))
