
dictionary ={
 "e": ".",
 "t": "-",
 "i": "..",
 "s": "...",
 "h":"....",
 "v": "...-",
 "u": "..-",
 "f": "..-.",
 "a": ".-",
 "r": ".-.",
 "l": ".-..",
 "w": ".--",
 "p": ".--.",
 "j": ".---",
 "t": "-",
 "n": "-.",
 "d": "-..",
 "b": "-...",
 "x": "-..-",
 "k": "-.-",
 "c": "-.-.",
 "y": "-.--",
 "m": "--",
 "g": "--.",
 "z": "--..",
 "q": "--.-",
 "o": "---",
 "": " ",
 " ": "/"
 }

def morse2text(s):
    mrs = list()
    for word in s.split(" / "):
        word = ("".join(map(str,word)))
        for letter in word.split(" "):
            mrs.append(list(dictionary.keys())[list(dictionary.values()).index(letter)])
        mrs.append(" ")
    print("\n"+"".join(map(str,mrs[:-1]))+ "\n")


def text2morse(s):
    mrs = list()
    for l in s:
        
        mrs.append(dictionary[l] + " ")
    print("\n"+"".join(map(str,mrs))+ "\n")








i = input("0-Text to Morse\n1-Morse to Text\n>")
if (i.isnumeric()):
    s = input("Insert the message\n>").lower()
    if (int(i)):
        #morse2text:
        morse2text(s)
    else:
        print("text 2 morse")
        text2morse(s)
    



