# Write your code here
import re
import itertools
import json
from collections import defaultdict
data_to_test = input()
x = json.loads(data_to_test)

def data_valididity(data):

    errors_found = {
        "bus_id": 0,
        "stop_id": 0,
        "stop_name": 0,
        "next_stop": 0,
        "stop_type": 0,
        "a_time": 0
    }
    format_a_time = r"(([0-1][0-9])|2[0-3]):[0-5][0-9]$"

    for i in data:

        if not isinstance(i["bus_id"], int):
            errors_found["bus_id"] += 1
        if not isinstance(i["stop_id"], int):
            errors_found["stop_id"] += 1
        if isinstance(i["stop_name"], str) and len(i["stop_name"]) == 0:
            errors_found["stop_name"] += 1
        if isinstance(i["stop_name"], str) and (i["stop_name"].split()) == 2:
            road = i["stop_name"].split()
            if not road[0][0].isupper() or not road[1][0].isupper():
                errors_found["stop_name"] += 1
        if isinstance(i["stop_name"], int) or isinstance(i["stop_name"], float):
            errors_found["stop_name"] += 1
        if not isinstance(i["next_stop"], int):
            errors_found["next_stop"] += 1
        if i["stop_type"] not in {"O", "F", "S", ""}:
            errors_found["stop_type"] += 1
        if not re.fullmatch(format_a_time, str(i["a_time"])):
            errors_found["a_time"] += 1

    return errors_found

def format_validity(data):
    errors_found = {
        "stop_name": 0,
        "stop_type": 0,
        "a_time": 0
    }
    format_stop_name = r"^[A-Z][a-z]+( [A-Z][a-z]+)? (Road|Avenue|Boulevard|Street){1}$"
    format_stop_type = r"^(O|F|S)$"
    format_a_time = r"(([0-1][0-9])|2[0-3]):[0-5][0-9]$"
    for i in data:
        match_stop_name = re.match(format_stop_name, i["stop_name"])
        match_stop_type = re.match(format_stop_type, i["stop_type"])
        match_a_time = re.match(format_a_time, i["a_time"])
        if match_stop_name is None:
            errors_found["stop_name"] += 1
        if match_stop_type is None and len(i["stop_type"]) > 0:
            errors_found["stop_type"] += 1
        if match_a_time is None:
            errors_found["a_time"] += 1
    return errors_found

def bus_info(data):
    counter = defaultdict(int)
    for i in data:
        counter[i["bus_id"]] += 1
    x = list(zip(counter.keys(), counter.values()))
    y = "\n".join([f"bus_id: {i}, stops: {j}" for i, j in x])
    return y


def check_end(data, problematic_on_demand=False):
    counter = defaultdict(list)
    problematic_line = None
    start = []
    transfer = defaultdict(int)
    finish = []
    problematic_transfers = []
    for i in data:
        if counter[i["bus_id"]].count("S") > 1 or counter[i["bus_id"]].count("F") > 1:
            problematic_line = i["bus_id"]
            return f'There is no start or end stop for the line: {problematic_line}.'
        counter[i["bus_id"]].append(i["stop_type"])
        if i["stop_type"] == "S":
            if i["stop_name"] not in start:
                start.append(i["stop_name"])
        elif i["stop_type"] == "F":
            if i["stop_name"] not in finish:
                finish.append(i["stop_name"])
        if i["stop_type"] != "O":
            transfer[tuple([i["stop_id"], i["stop_name"]])] += 1
    for d in data:
        if d["stop_type"] == "O" and tuple([d["stop_id"], d["stop_name"]]) in transfer.keys():
            problematic_transfers.append(d["stop_name"])
    for j in counter:
        if counter[j].count("S") != 1 or counter[j].count("F") != 1:
            problematic_line = j
            return f'There is no start or end stop for the line: {problematic_line}.'
    final_transfers = sorted([i[1] for i, j in transfer.items() if int(j) > 1])

    total_start = f"Start stops: {len(start)} {sorted(start)}"
    total_transfer = f"Transfer stops: {len(final_transfers)} {final_transfers}"
    total_finish = f"Finish stops: {len(finish)} {sorted(finish)}"
    formatted_value = f'{total_start}\n{total_transfer}\n{total_finish}'
    if problematic_on_demand:
        if problematic_transfers:
            return f'On demand stops test:\nWrong stop type: {sorted(problematic_transfers)}'
        else:
            return 'On demand stops test:\nOK'
    return formatted_value

def check_arrival(data):
    wrong_times = defaultdict(str)
    next_line = False
    skip_line = None
    for i, j in enumerate(data):
        try:
            current_bus = data[i]["bus_id"]
            next_bus = data[i + 1]["bus_id"]
            current_time = data[i]["a_time"].split(":")
            next_time = data[i + 1]["a_time"].split(":")
            if current_bus == next_bus and next_bus != skip_line:
                differential_time = int(next_time[0]+next_time[1]) - int(current_time[0]+current_time[1])
                if differential_time <= 0:
                    wrong_times[next_bus] = data[i + 1]["stop_name"]
                    skip_line = current_bus

        except IndexError:
            break
    return wrong_times

def check_arrival_printer(data):
    if len(data.values()) == 0:
        return 'Arrival time test:\nOK'

    else:

        return "Arrival time test:\n" + "\n".join([f'bus_id line {i}: wrong time on station {j}' for i, j in data.items()])



# arrivals = check_end(x)
print(check_end(x, problematic_on_demand=True))
# validation = format_validity(x)
# print(f"Type and required field validation: {sum(validation.values())} errors")
# for i,j in validation.items():
#     print(f'{i}: {j}')

