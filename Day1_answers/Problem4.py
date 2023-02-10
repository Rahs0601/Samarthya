def count_vowels_consonants(str):
    vowels = 0
    consonants = 0
    for i in str:
        if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
        i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
            vowels = vowels+1
        else:
            consonants = consonants+1
    return vowels, consonants

str = "Samarthya"
vowels, consonants = count_vowels_consonants(str)
print("The number of vowels:",vowels)
print("\nThe number of consonant:",consonants)
