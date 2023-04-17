from lib.cell import Cell
import re

class Board:
  def __init__(self):
    self.columns = {
      "A": {
        1: Cell(),
        2: Cell(),
        3: Cell(),
        4: Cell(),
        5: Cell(),
        6: Cell()
      },
      "B": {
        1: Cell(),
        2: Cell(),
        3: Cell(),
        4: Cell(),
        5: Cell(),
        6: Cell()
      },
      "C": {
        1: Cell(),
        2: Cell(),
        3: Cell(),
        4: Cell(),
        5: Cell(),
        6: Cell()
      },
      "D": {
        1: Cell(),
        2: Cell(),
        3: Cell(),
        4: Cell(),
        5: Cell(),
        6: Cell()
      },
      "E": {
        1: Cell(),
        2: Cell(),
        3: Cell(),
        4: Cell(),
        5: Cell(),
        6: Cell()
      },
      "F": {
        1: Cell(),
        2: Cell(),
        3: Cell(),
        4: Cell(),
        5: Cell(),
        6: Cell()
      },
      "G": {
        1: Cell(),
        2: Cell(),
        3: Cell(),
        4: Cell(),
        5: Cell(),
        6: Cell()
      }
    }

  def print_board(self):
    raw_keys = str(self.columns.keys())
    stripped = re.sub("[^A-Za-z]","",raw_keys)[8:]
    key_list = [*stripped]
    keys = ' '.join(key_list)
    print(keys)
    for row_number in reversed(range(1, 7)):
      print(self.row(row_number))

  def row(self, row_number):
    raw_row = []
    for column in self.columns.values():
      piece = column[row_number].piece
      raw_row.append(piece)
    row = ' '.join(raw_row)
    return row

  def draw_game(self):
    for column in self.columns.values():
      if column[6].piece == '.':
        return False
      else:
        continue
    return True

  def win_game(self):
    if self.vertical_win():
      return True
    elif self.horizontal_win():
      return True
    elif self.diagonal_win():
      return True
    else:
      return False

  def vertical_win(self):
    for column in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
      win_count = 0
      for row in range(1, 7):
        if self.columns[column][row].piece == 'X':
          win_count += 1
        elif win_count > 3:
          return True
        else:
          win_count = 0
      if win_count > 3:
        return True
      else:
        win_count = 0
        for row in range(1, 7):
          if self.columns[column][row].piece == 'O':
            win_count += 1
          elif win_count > 3:
            return True
          else:
            win_count = 0
      if win_count > 3:
        return True
      else:
        continue
    return False

  def horizontal_win(self):
    for row in range(1, 7):
      win_count = 0
      for column in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        if self.columns[column][row].piece == 'X':
          win_count += 1
        elif win_count > 3:
          return True
        else:
          win_count = 0
      if win_count > 3:
        return True
      else:
        win_count = 0
        for column in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
          if self.columns[column][row].piece == 'O':
            win_count += 1
          elif win_count > 3:
            return True
          else:
            win_count = 0
      if win_count > 3:
        return True
      else:
        continue
    return False

  def diagonal_win(self):
    # Check for diagonal wins starting from the top-left corner
    for row in range(3):
      for col in range(4):
        if self.columns["A"][row + 1].piece == self.columns["B"][row + 2].piece == self.columns["C"][row + 3].piece == self.columns["D"][row + 4].piece and self.columns["A"][row + 1].piece != ".":
            return True
        elif self.columns["B"][row + 1].piece == self.columns["C"][row + 2].piece == self.columns["D"][row + 3].piece == self.columns["E"][row + 4].piece and self.columns["B"][row + 1].piece != ".":
            return True
        elif self.columns["C"][row + 1].piece == self.columns["D"][row + 2].piece == self.columns["E"][row + 3].piece == self.columns["F"][row + 4].piece and self.columns["C"][row + 1].piece != ".":
            return True
        elif self.columns["D"][row + 1].piece == self.columns["E"][row + 2].piece == self.columns["F"][row + 3].piece == self.columns["G"][row + 4].piece and self.columns["D"][row + 1].piece != ".":
            return True

    # Check for diagonal wins starting from the top-right corner
    for row in range(3):
      for col in range(3, 7):
        if self.columns["G"][row + 1].piece == self.columns["F"][row + 2].piece == self.columns["E"][row + 3].piece == self.columns["D"][row + 4].piece and self.columns["G"][row + 1].piece != ".":
            return True
        elif self.columns["F"][row + 1].piece == self.columns["E"][row + 2].piece == self.columns["D"][row + 3].piece == self.columns["C"][row + 4].piece and self.columns["F"][row + 1].piece != ".":
            return True
        elif self.columns["E"][row + 1].piece == self.columns["D"][row + 2].piece == self.columns["C"][row + 3].piece == self.columns["B"][row + 4].piece and self.columns["E"][row + 1].piece != ".":
            return True
        elif self.columns["D"][row + 1].piece == self.columns["C"][row + 2].piece == self.columns["B"][row + 3].piece == self.columns["A"][row + 4].piece and self.columns["D"][row + 1].piece != ".":
            return True

    return False


