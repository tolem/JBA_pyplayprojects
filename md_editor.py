import os
full_text = ''


def help():
    print('Available formatters:', *formatters)
    print('Special commands: !help !done')


def done():
    global full_text
    with open("output.md", "w") as file:
        file.write(full_text)
    exit()


def plain():
    text = input('Text: ')
    return text


def bold():
    text = input('Text: ')
    return f'**{text}**'


def italic():
    text = input('Text: ')
    return f'*{text}*'


def header():
    while True:
        lvl = int(input('Level: '))
        if 0 < lvl < 7:
            break
        print('The level should be within the range of 1 to 6')
    text = input('Text: ')
    output = f'{"#" * 4} {text}\n'
    return output


def link():
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def inline_code():
    text = input('Text: ')
    return f'`{text}`'


def new_line():
    return '\n'


def list_txt(txt):
    output = ""
    rows = int(input("Number of rows:"))
    while rows < 1:
        print("The number of rows should be greater than zero")
        rows = int(input("Number of rows:"))

    for row in range(1,rows+1):
        r = input(f"Row #{row} ")

        if txt == "ordered-list":
            output += f"{row}. {r}\n"
        elif txt == "unordered-list":
            output += f"* {r}\n"
        else:
            pass
    return output


formatters = {'plain': plain, 'bold': bold, 'italic': italic, 'header': header,
              'link': link, 'inline-code': inline_code, 'new-line': new_line, "ordered-list": list_txt, "unordered-list": list_txt}


while True:
    action = input('Choose a formatter: ')

    if action in formatters.keys():
        if action in ["unordered-list", "ordered-list"]:
            formatted_text = formatters[action](action)
        else:
            formatted_text = formatters[action]()
        if formatted_text:
            full_text += formatted_text
            print(full_text)
    elif action == '!help':
        help()
    elif action == '!done':
        done()
    else:
        print('Unknown formatting type or command')
