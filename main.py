#Project Number One.
#MORSE PROGRAM

print("Hello Everyone!\n"
      "Welcome in our MORSE program!")
word = input("Please, write a word which one would you like to convert to Morse Code: ").lower()

x = list(word)

new_word = []

for letter in x:
    if letter == "a":
        new_word.append("·−")
    elif letter == "b":
        new_word.append("−···")
    elif letter == "c":
        new_word.append("−·−·")
    elif letter == "d":
        new_word.append("−··")
    elif letter == "e":
        new_word.append("·")
    elif letter == "f":
        new_word.append("··−·")
    elif letter == "g":
        new_word.append("−−·")
    elif letter == "h":
        new_word.append("····")
    elif letter == "i":
        new_word.append("··")
    elif letter == "j":
        new_word.append("·−−−")
    elif letter == "k":
        new_word.append("−·−")
    elif letter == "l":
        new_word.append("·−··")
    elif letter == "m":
        new_word.append("−−")
    elif letter == "n":
        new_word.append("−·")
    elif letter == "o":
        new_word.append("−−−")
    elif letter == "p":
        new_word.append("·−−·")
    elif letter == "q":
        new_word.append("−−·−")
    elif letter == "r":
        new_word.append("·−·")
    elif letter == "s":
        new_word.append("···")
    elif letter == "t":
        new_word.append("−")
    elif letter == "u":
        new_word.append("··−")
    elif letter == "v":
        new_word.append("···−")
    elif letter == "w":
        new_word.append("·−−")
    elif letter == "x":
        new_word.append("−··−")
    elif letter == "y":
        new_word.append("−·−−")
    elif letter == "z":
        new_word.append("−−··")
    else:
        print("So sorry... Program is not printing number's yet!")



print("Letter by letter is like this : ")
print(new_word)



def convert(new_w):
    new = ""

    for x in new_w:
        new += x
    return new

print("But if you want to see in one word it will be like this : ")
print(convert(new_word))