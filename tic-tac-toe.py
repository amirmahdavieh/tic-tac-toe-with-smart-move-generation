import tkinter as tk
import random
from itertools import permutations, combinations

def check_condition(s, valid_combinations):
    extracted_digits = s[1::2]  # Check subsets of extracted odd index digits against valid combinations
    for length in range(1, len(extracted_digits) + 1):
        for subset in combinations(extracted_digits, length):
            if ''.join(sorted(subset)) in valid_combinations:
                return True
    return False

def generate_strings(base):
    list_of_results = []
    valid_combinations = {'012', '345', '678', '036', '147', '258', '048', '246'}
    remaining_digits = ''.join([str(digit) for digit in range(10) if str(digit) not in base])

    for n in range(1, len(remaining_digits) + 1):
        for p in permutations(remaining_digits, n):
            extended_string = base + ''.join(p)
            if len(extended_string) >= 5 and check_condition(extended_string, valid_combinations):
                list_of_results.append(extended_string)

    if list_of_results:
        min_length = min(len(result) for result in list_of_results)
        min_length_strings = [result for result in list_of_results if len(result) == min_length]
        while min_length_strings:
            chosen_string = random.choice(min_length_strings)
            min_length_strings.remove(chosen_string)
            even_index_digits = chosen_string[::2]
            if not any(''.join(sorted(subset)) in valid_combinations for length in range(1, len(even_index_digits) + 1) for subset in combinations(even_index_digits, length)):
                return chosen_string
        return random.choice(list_of_results)
    return None

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")
        self.turn = True  # True if human's turn, False for computer's turn
        self.board = [''] * 9
        self.played_str = ''
        self.buttons = [tk.Button(master, text='', height=3, width=6, font=("Helvetica", 24),
                                  command=lambda index=i: self.make_move(index)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)

    def make_move(self, index):
        if self.board[index] == '' and self.turn:
            self.board[index] = 'X'
            self.buttons[index].config(text='X', state='disabled')
            self.played_str += str(index)
            self.turn = not self.turn
            self.master.after(500, self.computer_move)  # Wait 500ms and then computer makes a move

    def computer_move(self):
        if not self.check_win('X'):
            # Check for blocking moves
            for a, b, c in self.get_win_conditions():
                if self.is_threat(a, b, c):
                    self.board[c] = 'O'
                    self.buttons[c].config(text='O', state='disabled')
                    self.played_str += str(c)
                    self.turn = True
                    return

            # No immediate threats, choose move based on generate_strings
            s = generate_strings(self.played_str)
            if s and len(s) > len(self.played_str):
                comp_move = int(s[len(self.played_str)])
                if self.board[comp_move] == '':
                    self.board[comp_move] = 'O'
                    self.buttons[comp_move].config(text='O', state='disabled')
                    self.played_str += str(comp_move)
                    self.turn = True
                    if self.check_win('O'):
                        self.end_game("Computer wins!")
            else:
                self.end_game("Draw!")

    def is_threat(self, a, b, c):
        # Check if two 'X's and one empty space form a winning threat
        return self.board[a] == self.board[b] == 'X' and self.board[c] == ''

    def get_win_conditions(self):
        return [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    def check_win(self, player):
        for a, b, c in self.get_win_conditions():
            if self.board[a] == self.board[b] == self.board[c] == player:
                self.end_game(f"{player} wins!")
                return True
        return False

    def end_game(self, message):
        for button in self.buttons:
            button.config(state='disabled')
        win_label = tk.Label(self.master, text=message, font=("Helvetica", 16))
        win_label.grid(row=3, column=0, columnspan=3)

root = tk.Tk()
game_gui = TicTacToeGUI(root)
root.mainloop()
