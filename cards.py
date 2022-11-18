
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

