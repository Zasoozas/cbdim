from googletrans import Translator

def translate_word(word):
    return Translator().translate(word, src="ru", dest="en").text

if __name__ == "__main__":
    print(translate_word("Камера наружного наблюдения"))