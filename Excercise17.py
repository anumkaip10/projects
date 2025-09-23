def secret_code(sentence):
    words = sentence.split()   
    new_words = []

    for word in words:
        if len(word) >= 3:
            new_word = word[1:] + word[0] + "ay"
        else:
            new_word = word[::-1]
        new_words.append(new_word)

    
    return " ".join(new_words)


msg = input("Enter a sentence: ")
print("Secret Code:", secret_code(msg))
