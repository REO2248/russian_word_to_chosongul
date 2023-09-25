russian_vowels = ["а", "э", "о", "у", "ы", "я", "е", "ё", "ю", "и"]

def vowel_jamoize(word, number:int):
    if word[number] == "а":
        return "ㅏ"
    elif word[number] == "э":
        return "ㅔ"
    elif word[number] == "о":
        return "ㅗ"
    elif word[number] == "у":
        return "ㅜ"
    elif word[number] == "ы":
        return "ㅢ"
    elif word[number] == "я":
        return "ㅑ"
    elif word[number] == "ё":
        return "ㅛ"
    elif word[number] == "ю":
        return "ㅠ"
    elif word[number] == "и":
        return "ㅣ"
    elif word[number] == "е":
        try:
            if (word[number-1] in russian_vowels
                or word[number+1] == "й"
                or word[number+1] == "ь"
                or word[number+1] == "ъ"):
                return "ㅖ"
            else:
                return "ㅔ"
        except IndexError:
            return "ㅔ"
    else:
        return word[number]

def consonant_jamoize(word, number:int):
    pass


def jamoize(word):
    list_for_word = []
    for char in word:
        list_for_word.append(char)

    for i in range(len(word)):
        list_for_word[i] = vowel_jamoize(word, i)

    word = "".join(list_for_word)
    return word



print(jamoize("моя"))
print(jamoize("земля"))