# Returns true if the given character is a vowel
def isVowel(c):
    return (c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U' 
            or c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u');

# Translates a string into PigLatin.
def pigLatin(s):
    # If a word starts with a vowel, add "way" to the end
    if (isVowel(s[-1])):
        return s + "way"
    # If a word starts with two consonants, move the two consonants and add "ay" to the end
    elif (not(isVowel(s[:1])) and not(isVowel(s[1:2]))):
        return (s[2:] + s[:2] + "ay").lower()
    # If a word starts with a consonant and a vowel, move the first letter and add "ay to the end
    elif (not(isVowel(s[:1])) and (isVowel(s[1:2]))):
        return (s[1:] + s[:1] + "ay").lower()
    else:
        return s
