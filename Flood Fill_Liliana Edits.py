#ib = input_board

def flood_fill(ib, x, y, old, new):
    if x < 0 or x >= len(ib) or y < 0 or y >= len(ib[0]) or ib[x][y] != old:
        return

    ib[x] = ib[x][:y] + new + ib[x][y+1:]

    flood_fill(ib, x+1, y, old, new)
    flood_fill(ib, x-1, y, old, new)
    flood_fill(ib, x, y+1, old, new)
    flood_fill(ib, x, y-1, old, new)


board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]



# I changed a board to test it !

modified_board = flood_fill(ib=board, old=".", new="~", x=5, y=15)

for i in board:
    print(i)
