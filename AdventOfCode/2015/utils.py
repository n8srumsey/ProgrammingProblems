import contextlib
import os
import urllib.request
import datetime
import shutil
import warnings
import numpy as np

INPUT_FILENAME = "input.txt"
TEST_INPUT_FILENAME = "test.txt"
TESTING = False

def get_input_filename():
    if TESTING:
        warnings.warn("Test mode active, loading " + TEST_INPUT_FILENAME)
        return TEST_INPUT_FILENAME
    return INPUT_FILENAME


def setup_directory(day: int):
    this_dir = os.path.dirname(__file__)
    new_dir = os.path.join(this_dir, 'Day' + str(day))
    with contextlib.suppress(FileExistsError):
        os.mkdir(new_dir)
    new_file_name = os.path.join(new_dir, 'day' + str(day) + '.py')
    template_file_name = os.path.join(this_dir, 'template.py')
    if not(os.path.exists(new_file_name)):
        shutil.copy(template_file_name, new_file_name)
    test_file_name = os.path.join(new_dir, TEST_INPUT_FILENAME)
    open(test_file_name, 'a').close()   
    return new_dir


def download_input_data(day: int, new_dir: str):
    with open('login_cookie.txt') as cookie:
        session_cookie = cookie.read()
    url = f'https://adventofcode.com/2021/day/{day}/input'
    opener = urllib.request.build_opener()
    opener.addheaders = [('cookie', 'session=' + session_cookie)]
    urllib.request.install_opener(opener)
    input_file = os.path.join(new_dir, INPUT_FILENAME)
    urllib.request.urlretrieve(url, input_file)


def start_coding(day):
    new_dir = setup_directory(day)
    download_input_data(day, new_dir)


def start_coding_today():
    day_of_month = datetime.datetime.today().day + 1
    start_coding(day_of_month)


def readlines():
    with open(get_input_filename()) as f:
        data = [l.rstrip('\n') for l in f.readlines()]
    return data


def readlines_no_strip():
    with open(get_input_filename()) as f:
        data = f.readlines()
    return data


def read_whole_input():
    with open(get_input_filename()) as f:
        data = f.read.strip()
    return data


def read_grid_2darray():
    with open(get_input_filename()) as f:
        data = [[int(c) for c in l.rstrip('\n')] for l in f.readlines()]
    return data


def read_dict_input(sep=' => ', key='left'):
    result = {}
    lines = readlines()
    for line in lines:
        left, right = line.split(sep)
        if key.lower() == 'left':
            result[left.strip()] = right.strip()
        else:
            result[right.strip()] = left.strip()
    return result


def read_nparray_from_digits():
    data = readlines()
    result = np.zeros((len(data), len(data[0])), dtype=int)
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            result[i, j] = int(char)
    return result


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other):
        return self.data == other.data


class CircularLinkedList:
    def __init__(self, first_node=0):
        self.head = LinkedListNode(first_node)
        self.head.next = self.head
        self.head.previous = self.head
        self.current = self.head
        self.node_locs = {first_node: self.head}

    def get_current(self):
        return self.current.data

    def add_node_after_current(self, data):
        new_node = LinkedListNode(data)
        new_node.next = self.current.next
        new_node.previous = self.current
        self.current.next.previous = new_node
        self.current.next = new_node
        self.current = new_node
        self.node_locs[data] = new_node

    def remove_current_node(self):
        if self.current == self.head:
            self.head = self.current.previous
        self.current.previous.next = self.current.next
        self.current.next.previous = self.current.previous
        self.current = self.current.next

    def move_clockwise(self, steps):
        for _ in range(steps):
            self.current = self.current.next

    def move_counterclockwise(self, steps):
        for _ in range(steps):
            self.current = self.current.previous

    def set_current_to_data(self, data):
        self.current = self.node_locs[data]

    def __str__(self):
        result = str(self.head) + ' '
        place = self.head.next
        n = 100
        count = 0
        while place != self.head:
            count+=1
            if count > n:
                raise RuntimeError('lost head')
            if place == self.current:
                result = result + '(' + str(place) + ') '
            else:
                result = result + str(place) + ' '
            place = place.next
        return result


if __name__ == '__main__':
    start_coding_today()