import argparse
import math
from collections import Counter


try:
    parser = argparse.ArgumentParser(exit_on_error=False)
    parser.add_argument('-dataType', choices=['long', 'line', 'word'], default='word')
    parser.add_argument('-sortingType', choices=['natural', 'byCount'], default='natural')
    parser.add_argument('-inputFile')
    parser.add_argument('-outputFile')
    args, unknown = parser.parse_known_args()
    # print(unknown)
    if unknown:
        for _ in unknown:
            print(f"\"{_}\" is not a valid parameter. It will be skipped.")
    cmd = args.dataType
    sorted_cmd = args.sortingType
    read_file = args.inputFile
    output_file = args.outputFile



except argparse.ArgumentError as err:
    # print(err, "Hello")
    ex = (err.argument_name.split("Type")[0][1:])
    if ex in ["sorting", "data"]:
        print('No %s type defined!' % ex)
        exit(1)


sports = []
word = []

while read_file is None:
    try:
        data = input()
        sports.append(data.split())
        word.append(data)
        if data == '0':
            break
    except EOFError:
        break

if read_file is not None:
    with open(read_file, encoding='utf-8') as file:
        for n in file.readlines():
            sports.append(n.rstrip('\n').split())
            word.append(n.rstrip('\n'))


def out_file(f, result):
    # print(result)
    with open(f, mode='w', encoding='utf-8') as out:
        for n in result:
            out.writelines(n)


if sorted_cmd == "natural":
    if cmd == "long":
        sporting = []
        # _ = [[sporting.append(val) for val in num] for num in sports]
        for num in sports:
            for val in num:
                if val.isnumeric():
                    sporting.append(val)
                else:
                    if len(val) > 1:
                        if val.split('-')[1].isnumeric():
                            sporting.append(val)
                    else:
                        print(f" \"{val}\" is not a long. It will be skipped.")
        count = len(sporting)
        sorted_list = (sorted(sporting, key=int))
        result = []
        if output_file is not None:
            s = " ".join(map(str, sorted_list))
            result.append(f"Total numbers: {count}.\n")
            result.append(f"Sorted data: {s}")
            out_file(output_file, result)
        else:
            print(f"Total numbers: {count}.")
            print(f"Sorted data:", *sorted_list, end="")

    if cmd == "line":
        line = word
        sort_line = sorted(line, key=str)
        result = []
        if output_file is not None:
            result.append(f"Total lines: {len(line)}\n.")
            # out_file(output_file, f"Total lines: {len(line)}\n.")
            # out_file("Sorted data:\n")
            result.append("Sorted data:\n")
            for l in sort_line:
                result.append(f"{l}\n")
                # out_file(output_file, l)
            out_file(output_file, result)
        else:
            print(f"Total lines: {len(line)}.")
            print("Sorted data:")
            print(*sort_line, sep='\n')

    if cmd == "word":
        sporting = []
        # _ = [[sporting.append(val) for val in num] for num in sports]
        for num in sports:
            for val in num:
                if type(val) == str:
                    sporting.append(val)
                else:
                    print(f" \"{val}\" is not a word. It will be skipped.")
        count = len(sporting)
        sorted_list = (sorted(sporting, key=str))
        result = []
        if output_file is not None:
            result.append(f"Total words: {count}.\n")
            # out_file(output_file, f"Total words: {count}.\n")
            result.append("Sorted data:\n")
            # out_file(output_file, "Sorted data:\n")
            for s in sorted_list:
                result.append(f"{s}\n")
                # out_file(output_file, s)
            out_file(output_file, result)
        else:
            print(f"Total words: {count}.")
            print(f"Sorted data:", *sorted_list, end="")


elif sorted_cmd == "byCount":
    if cmd == "long":
        sporting = []
        # _ = [[sporting.append(val) for val in num] for num in sports]
        for num in sports:
            for val in num:
                if val.isdecimal():
                    sporting.append(val)
                else:
                    if val.startswith("-"):
                        if val.split('-')[1].isnumeric():
                                sporting.append(val)
                    else:
                        print(f" \"{val}\" is not a long. It will be skipped.")

        sporting = [int(val) for val in sporting]
        count = len(sporting)
        result = []
        if output_file is not None:
            result.append(f"Total numbers: {count}.\n")
            # out_file(output_file, f"Total numbers: {count}.")
        else:
            print(f"Total numbers: {count}.")

        counted_list = Counter(sporting)
        sorted_list = sorted(counted_list.items(), key=lambda x: (x[0], x[1]), reverse=True)
        for n in counted_list:
            # print(n)
            count_item = counted_list[n]
            avg = int(math.floor(count_item / int(count) * 100))
            counted_list[n] = [count_item, avg]
            # print(f"Sorted data:", *sorted_list, end="")
        sorted_count = dict(sorted(counted_list.items(), key=lambda x: ((x[1][1]), x[0], x[1][0])))
        for n in sorted_count:
            count_item = sorted_count[n][0]
            avg = sorted_count[n][1]

            if output_file is not None:
                result.append(f"{n}: {count_item} time(s), {avg}%.\n")
                # out_file(output_file, f"{n}: {count_item} time(s), {avg}%.")
            else:
                print(f"{n}: {count_item} time(s), {avg}%.")

            if output_file is not None:
                out_file(output_file, result)

    if cmd == "word":
        sporting = []
        # _ = [[sporting.append(val) for val in num] for num in sports]
        for num in sports:
            for val in num:
                if type(val) == str:
                    sporting.append(val)
                else:
                    print(f" \"{val}\" is not a word. It will be skipped.")
        # sporting = [ int(val) for val in sporting]
        count = len(sporting)
        result = []
        if output_file is not None:
            result.append(f"Total words: {count}.\n")
            # out_file(output_file, f"Total words: {count}.")
        else:
            print(f"Total words: {count}.")
        counted_list = Counter(sporting)
        sorted_list = sorted(counted_list.items(), key=lambda x: (x[0], x[1]), reverse=True)
        for n in counted_list:
            # print(n)
            count_item = counted_list[n]
            avg = int(math.floor(count_item / int(count) * 100))
            counted_list[n] = [count_item, avg]

            # print(f"Sorted data:", *sorted_list, end="")
        sorted_count = dict(sorted(counted_list.items(), key=lambda x: ((x[1][1]), x[0], x[1][0])))
        for n in sorted_count:
            count_item = sorted_count[n][0]
            avg = sorted_count[n][1]
            if output_file is not None:
                result.append(f"{n}: {count_item} time(s), {avg}%.\n")
                # out_file(output_file, f"{n}: {count_item} time(s), {avg}%.")
            else:
                print(f"{n}: {count_item} time(s), {avg}%.")

        if output_file is not None:
            output_file(output_file, result)

    if cmd == "line":
        line = word
        max_line = Counter(sorted(line, key=str))
        result = []
        if output_file is not None:
            result.append(f"Total lines: {len(line)}.")
            # out_file(output_file, f"Total lines: {len(line)}.")
        else:
            print(f"Total lines: {len(line)}.")
        for l in max_line:
            count = max_line[l]
            avg = int(math.floor(count / int(len(line)) * 100))
            if output_file is not None:
                result.append(f"{l}: {count} {avg}\n")
                # out_file(output_file, f"{l}: {count} {avg}")
            else:
                print(f"{l}: {count} {avg}")
        if output_file is not None:
            out_file(output_file, result)

