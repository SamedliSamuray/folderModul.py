import string
vowel=['a','ı','o','u','e','ə','i','ö','ü']
def give_consonant(consonant):
    
    consonants=[h for h in consonant if h.lower() in string.ascii_lowercase and h.lower() not in vowel]
    print(consonants)