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

    def get_string_of_symbols(self):
        return self.__string_of_symbols


class EnglishAlphabet(Alphabet):
    def __init__(self):
        Alphabet.__init__(self, 'ENG', 'abcdefghijklmnopqrstuvwxyz')
        self.__count_symbols = len(self.get_string_of_symbols())

    def is_english_letter(self, symbol):
        return symbol.lower() in self.get_string_of_symbols()


if __name__ == '__main__':
    Ru_Alphabet = Alphabet('RU', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    Ru_Alphabet.print_all_symbols()
    print(f'длина:{Ru_Alphabet.get_alphabet_len()}', end='\n\n')

    Eng = EnglishAlphabet()
    Eng.print_all_symbols()
    print(f'длина:{Eng.get_alphabet_len()}')
    print(Eng.is_english_letter('г'))
    print(Eng.is_english_letter('Ц'))
    print(Eng.is_english_letter('V'))
    print(Eng.is_english_letter('L'))
