def translate(Phrase):
    translation = "gg"
    for letter in Phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
                translation = translation + letter
    return translation

print(translate(input("Enter a Phrase:  ")))
