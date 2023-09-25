russian_vowels = ["а", "э", "о", "у", "ы", "я", "е", "ё", "ю", "и"]
russian_consonants = ["б", "в", "г", "д", "ж", "з", "к", "л", "м",
                      "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
russian_other_letters = ["й", "ь", "ъ"]

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
            #語頭
            if number == 0:
                return "ㅖ"
            #母音字とй, ь, ъの後ろ
            elif (word[number-1] in russian_vowels
                or word[number+1] == "й"
                or word[number+1] == "ь"
                or word[number+1] == "ъ"):
                return "ㅖ"
            #その他
            else:
                return "ㅔ"
        except IndexError:
            return "ㅔ"
    else:
        raise ValueError("Not a vowel")

def consonant_jamoize(word, number:int):
    #м
    if word[number] == "м":
        try:
            #母音字とьの前
            if (word[number+1] in russian_vowels
            or word[number+1] == "ь"):
                return "ㅁ"#ㅁ-
        except IndexError:
            pass
        try:
            #子音字前の語頭
            if (number == 0
                and word[number+1] in russian_consonants):
                return "ㅁㅡ"#므
        except IndexError:
            pass
        try:
            #лの前
            if word[number+1] == "л":
                return "ㅁㅡ"#므
        except IndexError:
            pass
        try:
            #м後ろの語末
            if (number == len(word)-1
                and word[number-1] == "м"):
                return "" #∅
        except IndexError:
            pass
        #その他
        return "ㅁ"#-ㅁ
    #д
    if word[number] == "д":
        try:
            #а, о, у, ъ, ы, эの前
            if (word[number+1] == "а"
                or word[number+1] == "о"
                or word[number+1] == "у"
                or word[number+1] == "ъ"
                or word[number+1] == "ы"
                or word[number+1] == "э"):
                return "ㄷ"#ㄷ-
            #е, ё, и, ю, я,ьの前
            elif (word[number+1] == "е"
                or word[number+1] == "ё"
                or word[number+1] == "и"
                or word[number+1] == "ю"
                or word[number+1] == "я"
                or word[number+1] == "ь"):
                return "ㅈ"#ㅈ-
            #т, ц, чの前
            elif (word[number+1] == "т"
                or word[number+1] == "ц"
                or word[number+1] == "ч"):
                return ""#∅
        except IndexError:
            pass
        return "ㄷㅡ" #드

    else:
        raise ValueError("Not a consonant")


def jamoize(word):
    list_for_word = []
    for char in word:
        list_for_word.append(char)

    for i in range(len(word)):
        try:
            list_for_word[i] = vowel_jamoize(word, i)
        except ValueError:
            pass
    for i in range(len(word)):
        try:
            list_for_word[i] = consonant_jamoize(word, i)
        except ValueError:
            pass
    word = "".join(list_for_word)
    return word



print(jamoize("моя"))
print(jamoize("будет"))