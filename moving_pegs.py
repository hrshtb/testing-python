# The module tries to achieve the goal of moving pegs which are arranged in a
# triangular structure into an empty space consecutively finishing the
# acquired space in the structure

import io
from collections import OrderedDict


class HiQ:
    def __init__(self, upper_limit):
        self.structure_upper_limit = upper_limit
        self.structure_state = OrderedDict(bool)

    def create_structure(self, empty_peg=None):
        for i in range(self.structure_upper_limit):
            if i != empty_peg:
                self.structure_state[i] = 1
            else:
                self.structure_state[i] = 0

    def calculate(self, *args):
        if self.structure_state[args[0]] and self.structure_state[
            args[1]] and not self.structure_state[args[2]]:
            self.structure_state[args[1]] = 0

    def print_structure(self):
        i = 0
        while i < self.structure_upper_limit:
            print(str(i) + ' : ' + str(self.structure_state[i]), end=' ')
            if i in [0, 2, 5, 9, 14]:
                print('\n')
            i += 1


if __name__ == '__main__':

    peg_empty_no = 0
    while True:
        peg_empty_no = int(
            input('Enter a number between 0 and 14, for the initial '
                  'empty '
                  'peg : '))

        try:
            assert -1 < peg_empty_no < 15
            break
        except AssertionError as ae:
            print('Please enter number in range 0-14. Try again.')

    class_obj = HiQ(15)
    class_obj.create_structure(peg_empty_no)

    with io.open('board_description.txt', buffering=8192) as \
            board_description_data:
        for line in board_description_data:
            class_obj.calculate(tuple(line.split(' ')))

    class_obj.print_structure()
