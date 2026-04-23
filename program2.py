from urllib.parse import unquote
import pyperclip

url = input("Встав URL: ")

decoded = unquote(url)

print("Результат:")
print(decoded)

pyperclip.copy(decoded)