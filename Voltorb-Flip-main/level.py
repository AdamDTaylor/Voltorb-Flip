# class to form levels
class level():
    # init with parameteers for list of(num of 2s, 3s) and voltorb tiles
    def __init__(self, potential_x2: list, potential_x3: list, potential_voltorb: list):
        self.x2s = potential_x2
        self.x3s = potential_x3
        self.voltorb = potential_voltorb

        boards = [
            [],
            [],
            [],
            [],
            []
        ]

        for x in range(len(boards)):
            boards[x].append(self.x2s[x])
            boards[x].append(self.x3s[x])
            boards[x].append(potential_voltorb[x])

        print(boards)
        self.boards = boards
