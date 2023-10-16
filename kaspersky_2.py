def count_letters(word):
    letter_count = {}

    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count

def can_form_kaspersky(word):
    kaspersky = "kaspersky"
    kaspersky_count = count_letters(kaspersky)
    word_count = count_letters(word)

    can_form = True
    for letter in kaspersky_count:
        if letter not in word_count or word_count[letter] < kaspersky_count[letter]:
            can_form = False
            break

    return can_form

def count_kaspersky_words(word):
    kaspersky = "kaspersky"
    kaspersky_count = count_letters(kaspersky)
    word_count = count_letters(word)

    min_count = float('inf')
    for letter in kaspersky_count:
        if letter not in word_count:
            min_count = 0
            break
        min_count = min(min_count, word_count[letter] // kaspersky_count[letter])

    return min_count

word = input()
can_form = can_form_kaspersky(word)
count = count_kaspersky_words(word)

if can_form:
    print(count)
else:
    print(0)
