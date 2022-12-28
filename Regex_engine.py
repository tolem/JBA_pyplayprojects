# Regex Engine
def match(exp, text):
    if not exp:
        return True
    if not text:
        return exp == "$"
    
    if exp[0] == '\\':
        exp = exp[1:]
        
    if exp[0] != text[0] and exp[0] != ".":
        if exp[1:2] in ["?", "*"]:
            return match(exp[2:], text)
        return False

    if exp[1:2] == "?":
        return match(exp[2:], text[1:])
    if exp[1:2] == "*":
        return match(exp, text[1:]) or match(exp[2:], text)
    if exp[1:2] == "+":
        return match(exp, text[1:]) or match(exp[2:], text[1:])

    return match(exp[1:], text[1:])


def regexp(pattern, string):
    if not pattern:
        return True
    if pattern[0] == "^":
        return match(pattern[1:], string)
    if match(pattern, string):
        return True
    if not string:
        return pattern == "$"

    return regexp(pattern, string[1:])


print(regexp(*input().split("|")))
