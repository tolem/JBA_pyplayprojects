# write your code here
import os
import sys
import re
import ast
base_path = sys.argv[1]



def s001_test(line, li, book, path):
    if len(li) > 79 and "#" != li[0]:
        book[line].append(f"{path}: Line {line}: S001 Too long")


def s004_test(line, li, book, path):
    if "#" in li and '#' != li[0]:
        start = li.index('#') - 4
        end = li.index('#')
        if li[start:end].count(' ') < 2:
            book[line].append(f"{path}: Line {line}: S004 At least two spaces required before inline comments")


def s003_test(line, li, book, path):
    if ';' in li and "#" != li[0]:
        test_case = li.split(';')
        cbody = "".join(li.strip(' '))
        cbody = cbody
        if 'print' in cbody:
            if '(' in cbody and ')' in cbody:
                a, b = cbody.index('('), cbody.index(')')
                if len(test_case) > 0 and (("=" not in test_case[0] and "#" not in test_case[0]) and ";" not in cbody[a:b+1]):
                    book[line].append(f"{path}: Line {line}: S003 Unnecessary semicolon")
        else:
            if len(test_case) > 0 and ("'"  not in test_case[0] and "#" not in test_case[0]) :
                book[line].append(f"{path}: Line {line}: S003 Unnecessary semicolon")


def s002_test(line, li, past, book, path, ):
    if (len(past) - (len(past.lstrip(' ')))) % 4 != 0:
        line = line - 1
        book[line].append(f"{path}: Line {line}: S002 Indentation is not a multiple of four")


def s006_test(line, li,  past, book, path):
    counter = sum([True for check in past if check == '\n'])
    if counter > 2 and li != '\n':
        book[line].append(f"{path}: Line {line}: S006 More than two blank lines used before this line")


def s005_test(line, li, book, path):
    todo = "todo"
    if "#" in li:
        check = li.split("#")
        if todo in check[1].lower():
            book[line].append(f"{path}: Line {line}: S005 TODO found")


def s007_test(line, li, book, path):
    spaces = re.search(r'[ \s]?(class|def)\s{2,}.+:$', li)
    cl, func = 'class', 'def'
    if spaces and (cl in li or func in li):
        name = cl if cl in li else func
        book[line].append(f'{path}: Line {line}: S007 Too many spaces after {name}')


def s008_test(line, li, book, path):
    camel_case = re.search(r'[ \s]?class [a-z]\w+:$', li)
    if camel_case:
        name = li.split(' ', 1)[1].rstrip(':\n')
        book[line].append(f'{path}: Line {line}: S008 Class name \'{name}\' should use CamelCase')


def s009_test(line, li, book, path):
    snake_case = re.search(r'[\s]?def\s+[A-Z]\w+\(\w*\):$', li)
    if snake_case:
        name = li.split()[1].rstrip('():\n')
        book[line].append(f'{path}: Line {line}: S009 Function name \'{name}\' should use snake_case')


def s010_test(line, name, book, path):
    # pattern = r'[\s+]def[\s]' + f'{name}' + r'\((.+[,])*[\s]+(([A-Z])\w+\=\w+)\):'
    # pattern = r'{}'.format(pattern)
    snake_case = re.match(r'^[A-Z]', name)
    if snake_case:
        book.setdefault(line, [])
        book[line].append(f'{path}: Line {line}: S010 Argument name \'{name}\' should be snake_case')


def s011_test(line, li,  book, path):
    if re.match(r'\w+.=', li.strip()):
        variable = re.search(r'\w+ =', li.strip()).group()[:-2]
        if re.fullmatch('[a-z0-9_]+', variable):
            pass
        else:
            name = li.split(" = ")[0].strip()
            book[line].append(f'{path}: Line {line}: S011 Variable \'{name}\' in function should be snake_case')


# def check_s011(local_path, sample: str, i: int):
#     if re.match(r'\w+.=', sample.strip()):
#         variable = re.search(r'\w+ =', sample.strip()).group()[:-2]
#         if re.fullmatch('[a-z0-9_]+', variable):
#             pass
#         else:
#             print(f'{local_path}: Line {i}: S011 Variable \'\' in function should be snake_case')
#

def s012_test(line, book, path):
    book[line].append(f'{path}: Line {line}: S012 Default argument value is mutable' )


def ast_tester(book, filename):
    with open (filename) as file:
        file = file.read()
        tree = ast.parse(file)
        # print(ast.dump(tree))
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # check whether the function's name is written in camel_case
                # fields = node.targets[0]
                # if hasattr(fields, 'id'):
                #     _name = node.targets[0].id
                #     print(_name)
                for argument_name in [a.arg for a in node.args.args]:
                    # print(argument_name)
                    s010_test(node.lineno, argument_name, book, filename)



                for item in node.args.defaults:
                    mutables = { ast.List, ast.Dict, ast.Set}
                    for defaults in mutables:
                        if isinstance(item, defaults):
                            s012_test(item.lineno, book, filename)

            s011_test(node.lineno, file, book, filename)



            # elif isinstance(node, ast.Name):
            #     if isinstance(node.ctx, ast.Store):
            #         variable_name = node.id
            #         s011_test(node.lineno, str(variable_name), book, filename)








def static_analyzer(path, filename):
    static_dict = {}
    for idx, expr in enumerate(path, 1):
        s, e = idx-4, idx
        blank = path[s: e]
        static_dict.setdefault(idx, [])
        back = idx - 2
        s001_test(idx, expr, static_dict, filename)
        s004_test(idx, expr, static_dict, filename)
        s003_test(idx, expr, static_dict, filename)
        s002_test(idx, expr, path[back], static_dict, filename)
        s006_test(idx, expr, blank, static_dict, filename)
        s005_test(idx, expr, static_dict, filename)
        s007_test(idx, expr, static_dict, filename)
        s008_test(idx, expr, static_dict, filename)
        s009_test(idx, expr, static_dict, filename)
        # s011_test(idx, expr, static_dict, filename)
    ast_tester(static_dict, filename)

    return static_dict


def sorted_list(di):
    for item in di:
        if len(di[item]) >= 1:
            di[item].sort()


def display_test(di):
    # print(di)
    for n in di:
        if len(di[n]) == 1:
            print(di[n][0])
        elif len(di[n]) >= 2:
            print(*(di[n]), sep="\n")


def run(dirname):
    with open(dirname, 'r') as file:
        f = file.readlines()
        result = static_analyzer(f, dirname)
        sorted_list(result)
        display_test(result)


def start(basepath):
    if os.path.isdir(basepath):
        for entry in os.listdir(basepath):
            file_path = os.path.join(basepath, entry)
            if os.path.isfile(os.path.join(basepath, entry)):
                py = "py"
                if entry.endswith(py):
                    run(file_path)

    elif os.path.isfile(basepath):
        run(basepath)


if __name__ == '__main__':
    start(base_path)
