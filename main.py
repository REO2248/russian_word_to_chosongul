russian_vowels = ["а", "э", "о", "у", "ы", "я", "е", "ё", "ю", "и"]
russian_consonants = ["б", "в", "г", "д", "ж", "з", "к", "л", "м",
                      "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
russian_other_letters = ["й", "ь", "ъ"]

russian_voiceless_consonants = ["п", "ф", "к", "т", "ш", "с", "х", "ц", "ч", "щ"]

korean_consonants = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ',
    'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
    'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ',
    'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]
korean_vowel = [
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ',
    'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
    'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ',
    'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
    'ㅣ'
]
korean_patchim = [
    '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ',
    'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ',
    'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ',
    'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
    'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ',
    'ㅌ', 'ㅍ', 'ㅎ'
]

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
                return "므"#므
        except IndexError:
            pass
        try:
            #лの前
            if word[number+1] == "л":
                return "므"#므
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
    elif word[number] == "д":
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
                return "" #∅
        except IndexError:
            pass
        return "드" #드
    #б
    elif word[number] == "б":
        try:
            #母音字(ъ, ь含む)の前
            if (word[number+1] in russian_vowels
                or word[number+1] == "ъ"
                or word[number+1] == "ь"):
                return "ㅂ"#ㅂ-
        except IndexError:
            pass
        try:
            #母音字と無声音の字の間
            if (word[number+1] in russian_vowels
                and word[number+2] in russian_voiceless_consonants):
                return "ㅂ"#-ㅂ
        except IndexError:
            pass
        #その他
        return "브"#브
    #т
    elif word[number] == "т":
        try:
            #а, о, у, ъ, ы, эの前
            if (word[number+1] == "а"
                or word[number+1] == "о"
                or word[number+1] == "у"
                or word[number+1] == "ъ"
                or word[number+1] == "ы"
                or word[number+1] == "э"):
                return "ㄸ"#ㄸ-
            #е, ё, и, ю, я, ьの前
            elif (word[number+1] == "е"
                or word[number+1] == "ё"
                or word[number+1] == "и"
                or word[number+1] == "ю"
                or word[number+1] == "я"
                or word[number+1] == "ь"):
                return "ㅉ"#ㅉ-
            #ц, чの前
            elif (word[number+1] == "ц"
                or word[number+1] == "ч"):
                return "" #∅
        except IndexError:
            pass
        #その他
        return "뜨" #뜨
    #л
    elif word[number] == "л":
        try:
            #語頭
            if number == 0:
                return "ㄹ" #ㄹ-
            #нと母音字の間
            elif (word[number-1] == "н"
                and word[number+1] in russian_vowels):
                return "ㄹ" #ㄹ-
        except IndexError:
            pass
        try:
            #母音字の間
            if (word[number-1] in russian_vowels
                and word[number+1] in russian_vowels):
                return "ㄹㄹ" #-ㄹㄹ-
        except IndexError:
            pass
        try:
            #母音字と母音字前のьの間
            if (word[number-1] in russian_vowels
                and word[number+1] == "ь"
                and word[number+2] in russian_vowels):
                return "ㄹㄹ" #-ㄹㄹ-
        except IndexError:
            pass
        try:
            #子音字(н以外)と母音の間
            if (word[number-1] in russian_consonants
                and word[number-1] != "н"
                and word[number+1] in russian_vowels):
                return "ㄹㄹ" #-ㄹㄹ-
        except IndexError:
            pass
        try:
            #母音字と子音字前のм, нの間
            if (word[number-1] in russian_vowels
                and (word[number+1] == "м" or word[number-2] == "н")
                and word[number+2] in russian_consonants):
                return "ㄹ르" #-ㄹ르
        except IndexError:
            pass
        try:
            #語末のм, нの前
            if (number+1 == len(word)-1
                and (word[number+1] == "м" or word[number+1] == "н")):
                return "ㄹ르"#-ㄹ르
            #語末のьм, ьнの前
            if (number+2 == len(word)-1
                and word[number+1] == "ь"
                and (word[number+2] == "м" or word[number+2] == "н")):
                return "ㄹ르"#-ㄹ르
        except IndexError:
            pass
        #その他
        return "ㄹ"
    #н
    elif word[number] == "н":
        try:
            #子音字の前の語頭
            if (number == 0
                and word[number+1] in russian_consonants):
                return "느" #느
        except IndexError:
            pass
        try:
            #母音字の前
            if word[number+1] in russian_vowels:
                return "ㄴ" #ㄴ-
        except IndexError:
            pass
        try:
            #母音字と母音字前のьの間
            if (word[number-1] in russian_vowels
                and word[number+1] == "ь"
                and word[number+2] in russian_vowels):
                return "ㄴ" #ㄴ-
        except IndexError:
            pass
        try:
            #нの後の語末
            if (number == len(word)-1
                and word[number-1] == "н"):
                return "" #∅
        except IndexError:
            pass
        #その他
        return "ㄴ" #-ㄴ
    #р
    elif word[number] == "р":
        try:
            #母音字とъ, ьの前
            if (word[number+1] in russian_vowels
                or word[number+1] == "ъ"
                or word[number+1] == "ь"):
                return "ㄹ" #ㄹ-
        except IndexError:
            pass
        try:
            #子音字の前
            if word[number+1] in russian_consonants:
                return "르"#르
        except IndexError:
            pass
        try:
            #語末
            if number == len(word)-1:
                return "르"#르
        except IndexError:
            pass
        #その他
        return "르"#르 一応
    #с
    elif word[number] == "с":
        try:
            #母音字とъ, ьの前
            if (word[number+1] in russian_vowels
                or word[number+1] == "ъ"
                or word[number+1] == "ь"):
                return "ㅆ" #ㅆ-
        except IndexError:
            pass
        #その他
        return "쓰" #쓰
    #к
    elif word[number] == "к":
        try:
            #母音字の前
            if word[number+1] in russian_vowels:
                return "ㄲ" #ㄲ-
        except IndexError:
            pass
        try:
            #母音字と無声音の間
            if (word[number-1] in russian_vowels
            and word[number+1] in russian_voiceless_consonants):
                return "ㄱ"#-ㄱ
        except IndexError:
            pass
        #その他
        return "크" #크
    #г
    elif word[number] == "г":
        try:
            #母音字の直前
            if word[number+1] in russian_vowels:
                return "ㄱ" #ㄱ-
        except IndexError:
            pass
        try:
            #子音字の前
            if word[number+1] in russian_consonants:
                return "그"#그
        except IndexError:
            pass
        try:
            #語末
            if number == len(word)-1:
                return "그"#그
        except IndexError:
            pass
        #その他 一応
        return "그"#그
    #п
    elif word[number] == "п":
        try:
            #母音字とьの前
            if (word[number+1] in russian_vowels
            or word[number+1] == "ь"):
                return "ㅃ"#ㅃ-
        except IndexError:
            pass
        try:
            #母音字と無声音の間
            if (word[number-1] in russian_vowels
            and word[number+1] in russian_voiceless_consonants):
                return "ㅂ"#-ㅂ
        except IndexError:
            pass
        #その他 一応
        return "쁘"#쁘
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

def jamo_to_text(text):
    for i in range(len(text)):
        try:
            if text[i] in korean_vowel:
                if i==0:
                    text= "ㅇ"+text
                if text[i-1] in korean_vowel:
                    text = text[:i]+"ㅇ"+text[i:]
        except ValueError:
            pass
    for i in range(len(korean_consonants)):
        for j in range(len(korean_vowel)):
            text = text.replace(
                korean_consonants[i]+korean_vowel[j],
                chr(i * 21 * 28 + j * 28 + 0xAC00)
            )
    for i in range(len(korean_consonants)):
        for j in range(len(korean_vowel)):
            for k in range(len(korean_patchim)):
                text = text.replace(
                    chr(i * 21 * 28 + j * 28 + 0xAC00)+korean_patchim[k],
                    chr(i * 21 * 28 + j * 28 + k + 0xAC00)
                )
    return text

def chosongulize(text):
    return jamo_to_text(jamoize(text))

if __name__ == "__main__":
    while True:
        print(chosongulize(input("> ")))