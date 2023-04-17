from lib.board import Board
from lib.turn import Turn

class Game:
  def __init__(self):
    self.board = None
    self.turn = None

  def main_menu(self):
    print('Welcome to Connect Four!')
    print('To play, press p. To quit, press q.')

    want_to_play = input()
    if want_to_play == 'p':
      self.start()
    elif want_to_play == 'q':
      self.quit_game()
    else:
      print('Invalid input, please press p or q.')
      self.main_menu

  def start(self):
    self.board = Board()
    self.turn = Turn(self.board)
    self.board.print_board()
    self.user_take_turn()

  def user_take_turn(self):
    if self.board.win_game():
      self.lose_game()
    elif self.board.draw_game():
      self.draw_game()
    else:
      print('--------------------------------')
      print('Please enter a letter between A and G')
      print('--------------------------------')
      self.turn.user_take_turn()
      self.board.print_board()
      self.computer_take_turn()

  def computer_take_turn(self):
    if self.board.win_game():
      self.win_game()
    elif self.board.draw_game():
      self.draw_game()
    else:
      print('--------------------------------')
      self.turn.computer_take_turn()
      self.board.print_board()
      self.user_take_turn()

  def play_again(self):
    print('--------------------------------')
    print('Would you like to play again? Press Y for yes or N for no')
    user_input = input()
    if user_input.lower() == 'y':
      self.start()
    elif user_input.lower() == 'n':
      self.quit_game()
    else:
      print('That is not a valid input, please press either Y or N.')
      self.play_again()


  def draw_game(self):
    print("It's a draw! Thank you for playing.")
    self.play_again

  def win_game(self):
    print('--------------------------------')
    print('You won! Congratulations')
    self.play_again()

  def lose_game(self):
    print('--------------------------------')
    print('You lost. Better luck next time!')
    self.play_again()

  def quit_game(self):
    print('--------------------------------')
    print('Goodbye!')

