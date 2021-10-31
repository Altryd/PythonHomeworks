import random


class Alphabet:
    def __init__(self, lang, string_of_symbols):
        self.__lang = lang
        self.__string_of_symbols = string_of_symbols

    def print_all_symbols(self):
        for symbol in self.__string_of_symbols:
            print(symbol, end='')
        print(end='\n')

    def get_alphabet_len(self):
        return len(self.__string_of_symbols)

    @property
    def get_language(self):
        return self.__lang

    @property
    def get_string_of_symbols(self):
        return self.__string_of_symbols


class EnglishAlphabet(Alphabet):
    def __init__(self):
        Alphabet.__init__(self, 'ENG', 'abcdefghijklmnopqrstuvwxyz')
        self.__count_symbols = len(self.get_string_of_symbols)

    def is_english_letter(self, symbol):
        return symbol.lower() in self.get_string_of_symbols

    def random_text(self):
        text = ""
        length = random.randint(30, 100)
        for i in range(length+1):
            letter = random.randint(0, self.get_alphabet_len()+3)
            text = text + (self.get_string_of_symbols[letter] if letter < 26 else ' ')
        return text


if __name__ == '__main__':
    print("\t\tРабота с русским алфавитом:")
    Ru_Alphabet = Alphabet('RU', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    print("Все буквы русского алфавита:")
    Ru_Alphabet.print_all_symbols()
    ky = Ru_Alphabet.get_language
    print(f'длина алфавита:{Ru_Alphabet.get_alphabet_len()}', end='\n\n')

    print("\t\tРабота с английским алфавитом:")
    Eng = EnglishAlphabet()
    print("Все буквы английского алфавита:")
    Eng.print_all_symbols()
    print(f'длина алфавита:{Eng.get_alphabet_len()}')
    print("Буква г " + ("является" if Eng.is_english_letter('г') else "не является") + " буквой английского алфавита")
    print("Буква Ц " + ("является" if Eng.is_english_letter('Ц') else "не является") + " буквой английского алфавита")
    print("Буква V " + ("является" if Eng.is_english_letter('V') else "не является") + " буквой английского алфавита")
    print("Буква L " + ("является" if Eng.is_english_letter('L') else "не является") + " буквой английского алфавита")
    rand_text = Eng.random_text()
    print("случайный текст:", rand_text)
