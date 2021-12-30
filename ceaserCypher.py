alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
             "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
             "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w","x", "y", "z"]


def ceaser():
    finalText = ""
    for letter in text:
        if letter in alphabets:
            position = alphabets.index(letter)
            if direction == "encode":
                newPosition = position + shift
            elif direction == "decode":
                newPosition = position - shift
            else:
                print("invalid direction")
            newLetter = alphabets[newPosition]
            finalText += newLetter
        else:
            finalText += letter
    print(f"Here is the {direction}d text: {finalText}")


Uchoice = "true"
while Uchoice == "true":
    direction = input("Type 'encode' to encrypt the text and 'decode' to decrypt the text: ")
    text = input("enter your message: ").lower()
    shift = int(input("Type the shift number: "))
    while shift > 26:
            shift = shift % 26
    ceaser()
    choice = input("Type 'yes' to continue encoding/decoding or 'no' to stop: ").lower()
    if choice == "yes":
        Uchice = "true"
    elif choice == "no":
        Uchoice = "false"
        print("Thank you for using my code, have a nice day, Good bye")
    else:
        print("invalid input")
        choice = input("Type 'yes' to continue encoding/decoding or 'no' to stop: ").lower()