import numpy
import re


def get_unique(data: list, value: str) -> list:
    try:
        return list(set(data))[:int(value)]
    except ValueError:
        return list(set(data))


def get_filter(data: list, text: str) -> list:
    if type(text) is str:
        return list(filter(lambda x: text in x, data))
    return []


def get_sorted(data: list, val: bool) -> list:
    try:
        if val == "desc":
            return sorted(data, reverse=False)
        return sorted(data, reverse=True)
    except IndexError:
        return sorted(data, reverse=True)


def get_map(data: list, value: int) -> list:
    try:
        return list(map(lambda x: x.split(" ")[int(value)], data))
    except (IndexError, ValueError):
        return []


def get_regex(data: list, value: str) -> list:
    filter_list: list = []
    try:
        for i in data:
            r = re.compile(value)
            if r.match(i):
                filter_list.append(i)
        return filter_list
    except:
        return filter_list


dict_cmd: dict = {
    "regex": get_regex,
    "sorted": get_sorted,
    "filter": get_filter,
    "unique": get_unique,
    "map": get_map
}