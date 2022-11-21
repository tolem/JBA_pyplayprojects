import requests
from bs4 import BeautifulSoup
import re
import sys


class Translation(object):
    welcome_msg = "Type the number of a language you want to translate to or '0' to translate to all languages:"
    supported_lang = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese','Dutch','Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']

    def __init__(self, lang, target_lang, word):
        self.lang = lang
        self.target_lang = target_lang
        self.word = word

    @staticmethod
    def welcome():
        return 'Type the word you want to translate:'

    def translate(self):
        return f'You chose "{Translation.supported_lang[self.target_lang]}" as a language to translate "{self.word}".'

    def exit_program(self):
        print(f'Sorry, unable to find {self.word}')
        exit(code=1)

    def connect_to_website(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        if self.target_lang.lower() == 'all':
            supported_lang = Translation.supported_lang
            translate = supported_lang
            translate.remove(self.lang.capitalize())

            for k in translate:
                url = f'https://context.reverso.net/translation/{self.lang.lower()}-{k.lower()}/'
                r = requests.get(f'{url}{self.word}', headers=headers)
                if r.status_code != 200:
                    if r.status_code == 404:
                        self.exit_program()
                    else:
                        print('Something wrong with your internet connection')

                self.target_lang = [i for i in supported_lang if i == k][0]
                self.extract_data(r.content)
            return "Pass"

        else:
            lang, target = self.lang.lower(), self.target_lang.lower()
            url = f'https://context.reverso.net/translation/{lang}-{target}/'
            r = requests.get(f'{url}{self.word}', headers=headers)
            if r.status_code != 200:
                if r.status_code == 404:
                    self.exit_program()
                else:
                    print('Something wrong with your internet connection')
                return 'Try again'
        return r.content

    @staticmethod
    def save_to_file(name, data):
        f = open(f'{name}.txt', 'a', encoding='utf-8')
        f.write(f'{data}\n')
        f.close()

    def extract_data(self, data):
        message = f'Sorry, the program doesn\'t support {self.target_lang}'
        try:
            assert self.target_lang in Translation.supported_lang, message
        except AssertionError:
            print(message)
            exit()
        sup_indexs = Translation.supported_lang.index(self.target_lang.capitalize())
        lang = Translation.supported_lang[sup_indexs]
        Translation.save_to_file(self.word, f'{lang} Translations:')
        soup = BeautifulSoup(data, 'html.parser')
        example_words = [term.text for term in soup.find_all('span', class_='display-term')]
        soup2 = [sent.find('div', class_='ltr') for sent in soup.find_all('div', class_='example')]
        soup3 = [sent.find('span', class_='text', attrs={'lang': re.compile(r'...?')}).text for sent in soup.find_all('div', class_='example')]

        for trm in example_words:
            Translation.save_to_file(self.word, trm)
        examples_sentences, translate_sentences = [], []
        Translation.save_to_file(self.word, f'\n{lang} Examples:')
        for sent in soup2:
            li = []
            for trans in sent:
                li.append(trans.text.strip('\n\r '))
            clean_string = "".join(li)
            examples_sentences.append(clean_string)

        for texts in soup3:
            translate_sentences.append('\n' + texts.strip('\n\r '))

        for w in zip(translate_sentences, examples_sentences):
            for i in w:
                Translation.save_to_file(self.word, i)

    def printer(self):
        f = open(self.word + '.txt', encoding='utf-8')
        print(f.read())
        f.close()


def main():
    lang, target, word = sys.argv[1], sys.argv[2], sys.argv[3]
    word_term = Translation(lang, target, word)
    content = word_term.connect_to_website()
    if content == "Try again" or content == 'Pass':
        pass
    else:
        word_term.extract_data(content)
    word_term.printer()


if __name__ == '__main__':
    main()
