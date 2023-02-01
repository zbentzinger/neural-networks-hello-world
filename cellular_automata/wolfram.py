import copy
import random


def apply_ruleset(ruleset_id: str, neighborhood_state: list[int]) -> int:
    
    rules = {
        "222": [0,1,1,1,1,0,1,1],
        "190": [0,1,1,1,1,1,0,1]
    }

    a = neighborhood_state[0]
    b = neighborhood_state[1]
    c = neighborhood_state[-1]

    match neighborhood_state:
        case [1,1,1]:
            return rules[ruleset_id][0]
        case [1,1,0]:
            return rules[ruleset_id][1]
        case [1,0,1]:
            return rules[ruleset_id][2]
        case [1,0,0]:
            return rules[ruleset_id][3]
        case [0,1,1]:
            return rules[ruleset_id][4]
        case [0,1,0]:
            return rules[ruleset_id][5]
        case [0,0,1]:
            return rules[ruleset_id][6]
        case [0,0,0]:
            return rules[ruleset_id][7]

    return 0

def main() -> None:

    size: int = 400
    seed: int = random.randint(0, size)

    init_cell_grid: list[int] = [0] * size
    init_cell_grid[seed] = 1

    # First gen is the seed array.
    cells: list[int] = init_cell_grid
    generations: int = 10000
    next_generation_cells: list[int] = cells

    for _ in range(0, generations):
        print(cells)
        for i, _ in enumerate(cells):

            left_neighbor = cells[(i - 1) - 1]
            me = cells[i]
            right_neighbor = cells[(i + 1) - 1]

            neighborhood = [left_neighbor, me, right_neighbor]

            next_generation_cells[i] = apply_ruleset("222", neighborhood)
        
        cells = copy.deepcopy(next_generation_cells)


if __name__ == "__main__":
    main()
