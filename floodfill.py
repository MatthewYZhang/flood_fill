from typing import List

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

def visit(board: List[str], x: int, y: int, old: str, new: str):
    """Change the board's old values replaced with new values
    through flood filling starting from the coordinates x, y;
    change is done in place
    Args:
        board (List[str])
        x (int)
        y (int)
    Returns:
        None
    """
    m, n = len(board), len(board[0])
    if x < 0 or y < 0 or x >= m or y >= n:
        return
    if board[x][y] != old:
        return
    board[x] = board[x][:y] + new + board[x][y+1:]
    position_list = [-1, 0, 1, 0, -1]
    for i in range(4):
        visit(board=board, x=x+position_list[i], y=y+position_list[i+1], old=old, new=new)
    return


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    visit(board=input_board, x=x, y=y, old=old, new=new)
    return input_board
    
    # Implement your code here.


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....