ukrainian_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"


def starts_with_ukrainian(word):
    first = word[0].lower() if word else ""
    return first in ukrainian_alphabet


def ukrainian_sort_key(word):
    result = []
    for ch in word.lower():
        if ch in ukrainian_alphabet:
            result.append(ukrainian_alphabet.index(ch))
        else:
            result.append(ord(ch))
    return result


def sort_words(words):
    def sort_key(word):
        is_latin = not starts_with_ukrainian(word)
        return (is_latin, ukrainian_sort_key(word))

    return sorted(words, key=sort_key)


with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Вхідний текст:")
print(text)

words = text.split()
print("\nВхідний список слів:")
print(words)

sorted_words = sort_words(words)

print("\nВідсортований список:")
print(sorted_words)