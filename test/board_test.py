import sys
import pytest
sys.path.append('/Users/samuelcox/turing_work/python/connect-four')

from lib.board import Board

def test_print_board(capsys):
  new_board = Board()
  new_board.print_board()
  captured = capsys.readouterr()
  assert captured.out == 'A B C D E F G\n. . . . . . .\n. . . . . . .\n. . . . . . .\n. . . . . . .\n. . . . . . .\n. . . . . . .\n'