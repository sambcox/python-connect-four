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
    win_count = 0
    win_count_offset_1 = 0
    win_count_offset_2 = 0
    row = 1
    row_offset_1 = 2
    row_offset_2 = 3
    for column in ['A', 'B', 'C', 'D', 'E', 'F']:
      if self.columns[column][row].piece == 'X':
        win_count += 1
      elif win_count > 3:
        return True
      else:
        win_count = 0
      if row < 5:
        if self.columns[column][row + 2].piece == 'X':
          win_count_offset_2 += 1
        elif win_count_offset_1 > 3:
          return True
        else:
          win_count_offset_2 = 0
      else:
        row += 1
        continue
      if row < 6:
        if self.columns[column][row + 1].piece == 'X':
          win_count_offset_1 += 1
        elif win_count_offset_1 > 3:
          return True
        else:
          win_count_offset_1 = 0
      else:
        row += 1
        continue
      row += 1
    if win_count > 3:
      return True
    else:
      win_count = 0
      row = 1
      for column in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        if row > 6:
          continue
        else:
          if self.columns[column][row].piece == 'O':
            win_count += 1
          elif win_count > 3:
            return True
          else:
            win_count = 0
        row += 1


