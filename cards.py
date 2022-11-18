# # Write your code here
# import os
# import logging
# import io
# from random import choice
#
#
#
# def out_(msg):
#     print(msg)
#     output.write(msg + '\n')
#
#
# def in_():
#     string = input()
#     print(string, file=output)
#     return string
#
#
# def log():
#     out_('File name:')
#     filename = in_()
#     content = output.getvalue().split('\n')
#     with open(filename, 'w') as file:
#         for line in content:
#             print(line, file=file)
#     out_('The log has been saved')
#
#
# class FlashCard():
#     cards = {}
#
#     def __int__(self, term, description):
#         self.term = term
#         self.description = description
#
#     def add_flash_card(self):
#         print()
#
#     def __str__(self):
#         print('Input the action (add, remove, import, export, ask, exit):')
#
#
# output = io.StringIO()
# cards = {}
# terms = set()
# definitions = set()
# count_cards = dict(sorted(cards.items(), key=lambda x: (x[1][1]), reverse=True))
#
# while True:
#     print('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
#     instruction = in_()
#     if instruction == 'add':
#         out_(f'The card:')
#         term = in_()
#         while term in terms:
#             out_(f'The term "{term}" already exists. Try again:')
#             term = in_()
#         terms.add(term)
#
#         out_(f'The definition of the card:')
#         definition = in_()
#         while definition in definitions:
#             out_(f'The definition "{definition}" already exists. Try again:')
#             definition = in_()
#         definitions.add(definition)
#         mistakes = 0
#         cards[term] = [definition, mistakes]
#         out_(f'The pair ("{term}":"{definition}") has been added')
#
#     elif instruction == 'remove':
#         out_('Which card?')
#         del_card = in_()
#         if cards.get(del_card, 0) == 0:
#             out_(f'Can\'t remove "{del_card}": there is no such card.')
#         else:
#             del cards[del_card]
#             out_('The card has been removed.')
#
#     elif instruction == 'import':
#         print('File name:')
#         file_path = in_()
#         if not os.path.exists(file_path):
#             out_('File not found.')
#         else:
#             f = open(file_path, 'r')
#             f = f.readlines()
#             n = len(f)
#             out_(f'{n} cards have been loaded.')
#
#     elif instruction == 'export':
#         print('File name:')
#         file_name = input()
#         f = open(file_name, 'a')
#         for k, v in cards.items():
#             des, num = v
#             f.write('{0}: {1} {2} \n'.format(k, des, num))
#         f.close()
#         n = len(cards)
#         out_(f'{n} cards have been saved')
#
#     elif instruction == 'ask':
#         out_('How many times to ask?')
#         num = int(in_())
#
#         for i in range(num):
#             selection = choice([k for k in cards])
#             out_(f'Print the definition of "{selection}":')
#             ans = in_()
#             if ans == cards[selection][0]:
#                 out_("Correct!")
#             else:
#                 cards[selection][1] = cards[selection][1] + 1
#                 kys = [val[0] for k, val in cards.items() if val[0] == ans]
#                 if kys:
#                     out_(
#                         f'Wrong. The right answer is "{cards[selection][0]}", but your definition is correct for "{kys[0]}".')
#                 else:
#                     out_(f'Wrong. The right answer is "{cards[selection][0]}"')
#                     continue
#
#     elif instruction == 'log':
#         log()
#         # print('File name:')
#         # file_name = input()
#         # print(file_name, file=output)
#         #
#         # content = output.getvalue().split('\n')
#         # with open(file_name, 'w') as file:
#         #     for line in content:
#         #         print(line, file=file)
#         # print('The log has been saved')
#
#     elif instruction == 'hardest card':
#         errors = [v[1] for k, v in count_cards.items() if v[1] == 0]
#
#         if not errors:
#             out_('There are no cards with errors.')
#
#         else:
#
#             highest_num = max(count_cards.values())
#             hardest_terms = [term for term, count_mistake in count_cards.items()
#                              if count_mistake[1] == highest_num]
#             cards = '", "'.join(hardest_terms)
#             if len(hardest_terms) == 1:
#                 out_(f'The hardest card is "{cards}". You have {highest_num} errors answering it.')
#             else:
#                 out_(f'The hardest cards are "{cards}". You have {highest_num} errors answering them.')
#
#             # check_cards = [k for k, v in count_cards.items() if v[1] == top_errors]
#             # cas = '", "'.join(check_cards)
#             # if len(check_cards) == 1:
#             #     out_(f'The hardest cards are {cas}')
#             #
#             # else:
#             #     out_(f'The hardest card is "{count_cards[0][0]}". You have N errors answering it')
#
#     elif instruction == 'reset stats':
#         for deck in cards.values():
#             deck[1] = 0
#         out_('Card statistics have been reset.')
#
#     elif instruction == 'exit':
#         out_('Bye bye!')
#         break

import argparse
import random
from io import StringIO
import logging

dictionary = {}
mistakes = {}

output = StringIO()

parser = argparse.ArgumentParser(description='This is a Flashcards application!:)')
parser.add_argument('-i', '--import_from',
                    help='Please, enter the name of the txt file from where the flashcards will be imported')
parser.add_argument('-e', '--export_to',
                    help='Please, enter the name of the txt file where the flashcards will be saved')
args = parser.parse_args()


logger = logging.getLogger()

logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')

file_handler = logging.FileHandler('default.txt')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def out_(msg):
    print(msg)
    output.write(msg + '\n')


def in_():
    string = input()
    print(string, file=output)
    return string


def add_card():
    out_('The card:')
    while True:
        term = in_()
        if term in dictionary.keys():
            out_(f'The term "{term}" already exists. Try again:')
            continue
        else:
            break
    out_('The definition of the card:')
    while True:
        definition = in_()
        if definition in dictionary.values():
            out_(f'The definition "{definition}" already exists. Try again:')
            continue
        else:
            break
    dictionary[term] = definition
    out_(f'The pair ("{term}":"{definition}") has been added.')


def remove_card():
    out_('Which card?')
    card = in_()
    if card in dictionary.keys():
        dictionary.pop(card)
        out_('The card has been removed.')
    else:
        out_(f'Can\'t remove "{card}": there is no such card.')


def import_from_file(f):
    try:
        file = open(f)
    except FileNotFoundError:
        out_('File not found.')
    else:
        n = 0
        for line in file:
            term, definition, count_mistake = (line.rstrip(' mistakes\n')).split(':')
            dictionary[term] = definition
            mistakes[term] = int(count_mistake)
            n += 1
        out_(f'{n} cards have been loaded.')
        file.close()


def export_to_file(f):
    if dictionary == {}:
        out_('The dictionary is empty. Fill it in via "add" command or '
             'import from file using "import".')
    else:
        count = 0
        with open(f, 'w') as file:
            for term, definition in dictionary.items():
                if term not in mistakes.keys():
                    mistakes[term] = 0
                file.write(f'{term}:{definition}:{mistakes[term]} mistakes\n')
                count += 1
            out_(f'{count} cards have been saved.')


def get_term(val, d):
    for k, v in d:
        if val == v:
            return k


def ask_card():
    count_mistake = 0
    if dictionary == {}:
        out_('The dictionary is empty. Fill it in via "add" command or '
             'import from file using "import".')
    else:
        out_('How many times to ask?')
        times = int(in_())
        for _ in range(times):
            term = random.choice(list(dictionary))
            out_(f'Print the definition of "{term}":')
            answer = in_()
            if answer == dictionary[term]:
                out_('Correct!')
            else:
                count_mistake += 1
                if term in mistakes.keys():
                    mistakes[term] += count_mistake
                else:
                    mistakes[term] = count_mistake
                result = get_term(answer, dictionary.items())
                if result is None:
                    out_(f'Wrong. The right answer is "{dictionary[term]}".')
                else:
                    out_(f'Wrong. The right answer is "{dictionary[term]}", '
                         f'but your definition is correct for "{result}".')
            count_mistake = 0


def log():
    out_('File name:')
    filename = in_()
    content = output.getvalue().split('\n')
    with open(filename, 'w') as file:
        for line in content:
            print(line, file=file)
    out_('The log has been saved')


def hardest_card():
    if mistakes == {}:
        out_('There are no cards with errors.')
    else:
        highest_num = max(mistakes.values())
        hardest_terms = [term for term, count_mistake in mistakes.items()
                         if count_mistake == highest_num]
        cards = '", "'.join(hardest_terms)
        if len(hardest_terms) == 1:
            out_(f'The hardest card is "{cards}". You have {highest_num} errors answering it.')
        else:
            out_(f'The hardest cards are "{cards}". You have {highest_num} errors answering them.')


def reset_stats():
    mistakes.clear()
    print('Card statistics have been reset.')


def import_file():
    filename = str(input('File:\n'))
    import_from_file(filename)


def export_file():
    filename = str(input('File:\n'))
    export_to_file(filename)


def main():
    if args.import_from:
        import_from_file(args.import_from)

    actions = {'add': add_card,
               'remove': remove_card,
               'import': import_file,
               'export': export_file,
               'ask': ask_card,
               'log': log,
               'hardest card': hardest_card,
               'reset stats': reset_stats}
    action = ''
    while action != 'exit':
        out_('Input the action (add, remove, import, export, ask,'
             ' exit, log, hardest card, reset stats):')
        action = in_()
        if action in actions:
            actions[action]()

    else:
        if args.export_to:
            export_to_file(args.export_to)

        else:
            out_('Bye bye!')
        out_(' ')


if __name__ == '__main__':
    main()

