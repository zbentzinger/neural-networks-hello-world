from dataclasses import dataclass, field
import os
import random
from time import sleep


@dataclass
class PointV1:
    x: int
    y: int

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


@dataclass
class CellV1:
    point: PointV1
    state: bool = False
    mutation_rate: float = 0.1

    def __repr__(self) -> str:
        return "#" if self.state else " "

    def evolve(self, neighbor_states: list[bool]) -> None:
        if self.state is True:
            if neighbor_states.count(True) < 2 or neighbor_states.count(True) > 3:
                # It dies
                self.state = False
            else:
                pass  # No change.
        else:
            if neighbor_states.count(True) == 3:
                # It is born
                self.state = True

        mutate = random.random() < self.mutation_rate
        if mutate:
            # flip its state
            self.state = not self.state


@dataclass
class BoardV1:
    columns: int
    rows: int
    entropy: float = 0.05
    grid: list[list] = field(init=False)

    def __post_init__(self) -> None:
        self.grid = []
        self.initialize()
        self.draw()

    def clear_screen(self) -> None:
        os.system("printf '\033c'")

    def initialize(self) -> None:
        self.grid = [[CellV1(PointV1(x, y)) for y in range(self.columns)] for x in range(self.rows)]

        random_rows = int((self.columns * self.rows) * self.entropy)
        for _ in range(0, random_rows + 1):
            random_x = random.randint(0, self.rows - 1)
            random_y = random.randint(0, self.columns - 1)
            self.grid[random_x][random_y].state = True

    def draw(self) -> None:
        self.clear_screen()

        board = ""

        for row in self.grid:
            for cell in row:
                board += f"{cell}"
            board += "\n"

        print(board)

@dataclass
class SimulationV1:
    board: BoardV1
    ticks: int
    tick_rate: float

    def get_cell_neighbor_states(self, x: int, y: int) -> list[bool]:

        offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        possible_neighbors = {(x + x_add, y + y_add) for x_add, y_add in offsets}

        neighbor_states = []

        for neighbor in possible_neighbors:
            try:
                cell = self.board.grid[neighbor[0]][neighbor[1]]
                neighbor_states.append(cell.state)
            except IndexError:
                neighbor_states.append(False)

        return neighbor_states

    def tick(self) -> None:

        for x, row in enumerate(self.board.grid):
            for y, cell in enumerate(row):
                neighbor_states = self.get_cell_neighbor_states(x, y)
                cell.evolve(neighbor_states)


    def run(self) -> None:
        for _ in range(0, self.ticks + 1):
            self.tick()
            self.board.draw()
            sleep(self.tick_rate)
