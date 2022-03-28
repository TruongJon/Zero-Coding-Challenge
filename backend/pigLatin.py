def isVowel(c):
    return (c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U' 
            or c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u');
 
def pigLatin(s):
    if (isVowel(s[-1])):
        return s + "way"
    elif (not(isVowel(s[:1])) and not(isVowel(s[1:2]))):
        return (s[2:] + s[:2] + "ay").lower()
    elif (not(isVowel(s[:1])) and (isVowel(s[1:2]))):
        return (s[1:] + s[:1] + "ay").lower()
    else:
        return s
