import random

class Turn:
  def __init__(self, board):
    self.board = board

  def user_take_turn(self):
    user_input = input()
    if user_input.upper() in 'ABCDEFG':
      self.place_piece(user_input)
    else:
      print("That is an invalid input! Please select a letter between A and G.")
      self.user_take_turn()

  def computer_take_turn(self):
    computer_input = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    self.computer_place_piece(computer_input)

  def place_piece(self, column):
    if self.board.columns[column.upper()][6].piece != '.':
      print('That column is full! Please select another.')
      self.place_piece(input())
    else:
      for slot in self.board.columns[column.upper()].values():
        if slot.piece == '.':
          slot.add_piece()
          break
        else:
          continue

  def computer_place_piece(self, column):
    if self.board.columns[column.upper()][6].piece != '.':
      self.computer_take_turn()
    else:
      for slot in self.board.columns[column.upper()].values():
        if slot.piece == '.':
          slot.computer_add_piece()
          break
        else:
          continue