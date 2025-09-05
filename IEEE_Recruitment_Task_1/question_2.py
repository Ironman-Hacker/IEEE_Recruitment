import string
paragraph = input("Enter a paragraph (max 100 words): ").split()
palindromes = []
for word in paragraph:
    # Remove punctuation and make lowercase
    clean_word = word.strip(string.punctuation).lower()
    if clean_word and clean_word == clean_word[::-1]:
        palindromes.append(word.strip(string.punctuation))
if palindromes:
    print(palindromes)
else:
    print(0)
