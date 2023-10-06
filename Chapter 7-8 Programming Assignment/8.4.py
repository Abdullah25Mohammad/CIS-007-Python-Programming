#8.4
#Occurrences of a specified character
#Abdullah Mohammad
#1/16/23


def count(string, character):
    numOfCharacter = 0
    for ch in string:
        if ch == character:
            numOfCharacter +=1
        
    return numOfCharacter


def main():
    string = input("Enter a string: ")
    character = input("Enter a character: ")

    print("The character", character, "appears", count(string, character), "time" if count(string, character) == 1 else "times", "in the string", string)

main()