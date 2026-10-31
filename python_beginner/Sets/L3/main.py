def count_vowels(text):
    vowel_counter = 0
    unique_vowels = set()
    vowels = {'a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O'}

    for char in text :
        if char in vowels: 
            vowel_counter += 1
            unique_vowels.add(char)

    return vowel_counter, unique_vowels