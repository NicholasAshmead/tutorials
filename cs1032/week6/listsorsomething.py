#Write a function that receives a string as a parameter and returns the text in the string without vowels.withoutVowels(“I do not like vowels!”) →“  d  n t l k  v w ls!”

def withoutVowels(string, vowels=['a','e','i','o','u']):
    for vowel in vowels: string = string.replace(vowel, "")
    return string

print(withoutVowels("I do not like vowels!"))