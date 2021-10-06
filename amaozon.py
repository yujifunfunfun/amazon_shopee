from googletrans import Translator
from currency_converter import CurrencyConverter

line = "hello"

translator = Translator()
translated = translator.translate(line, dest="ja")
c = CurrencyConverter()

print(c.convert(1, 'JPY', 'USD'))
print(translated.text)