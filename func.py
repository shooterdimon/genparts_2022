import config
from openpyxl import load_workbook


def read_token():
    with open(config.TOKEN_FILE_PATH) as file:
        tokens = [token.strip() for token in file.read().split('\n')]
    return tokens


def read_input():
    wb = load_workbook(config.INPUT_FILE_PATH)
    ws = wb.active
    return ws.values


def read_settings():
    with open(config.SETTINGS_FILE_PATH, "r") as file:
        text = file.read()
        settings_list = text.split("\n")
        settings_list = [i.split(" - ") for i in settings_list]
        settings_list = [(int(i[0]), int(i[1])) for i in settings_list]
        print("Settings pre-set")
        for setting in settings_list:
            print(f"Order {setting[0]} - pause {setting[1]} sec")
        print()
        return settings_list


def write_counter(counter):
    try:
        with open(config.TMP, 'w') as file:
            file.write(str(counter))
    except Exception as e:
        print(e)


def read_counter():
    try:
        with open(config.TMP, 'r') as file:
            return int(file.read())+1
    except FileNotFoundError:
        print('There is no saved progress. Starting from the 1st position')
        return 0

