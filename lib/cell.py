class Cell:
  def __init__(self):
    self.piece = '.'

  def add_piece(self):
    self.piece = 'X'

  def computer_add_piece(self):
    self.piece = 'O'