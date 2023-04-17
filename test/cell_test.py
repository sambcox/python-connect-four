import sys
sys.path.append('/Users/samuelcox/turing_work/python/connect-four')

from lib.cell import Cell

def test_cell_exists():
  new_cell = Cell()
  assert new_cell.piece == '.'

def test_cell_add_piece():
  new_cell = Cell()
  new_cell.add_piece()
  assert new_cell.piece == 'X'

def test_cell_add_computer_piece():
  new_cell = Cell()
  new_cell.computer_add_piece()
  assert new_cell.piece == 'O'