from program import *


class Algorithm:
    def __init__(self):
        self.result = None
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.', '.', '.'],
                              ['.', '.', '.'],
                              ['.', '.', '.']]

        # Player X always plays first
        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    # Determines if the made move is a legal move
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    # Checks if the game has ended and returns the winner in each case
    def is_end(self):
        # Vertical win
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                    self.current_state[0][i] == self.current_state[1][i] and
                    self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                self.result = 'X'
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                self.result = 'O'
                return 'O'

        # Main diagonal win
        if (self.current_state[0][0] != '.' and
                self.current_state[0][0] == self.current_state[1][1] and
                self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # Second diagonal win
        if (self.current_state[0][2] != '.' and
                self.current_state[0][2] == self.current_state[1][1] and
                self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (self.current_state[i][j] == '.'):
                    return None

        # It's a tie!
        self.result = '.'
        return '.'

    def check_winer(self):
        self.result = self.is_end()
        if self.result != None:
            if self.result == 'X':
                print('The winner is X!')
                pygame.draw.rect(DISPLAYSURF, WHITE, (440, 290, 250, 60))  # Hình chữ nhật
                DISPLAYSURF.blit(FONT.render("NGƯỜI THẮNG", True, RED, WHITE), (460, 300))
            elif self.result == 'O':
                print('The winner is O!')
                pygame.draw.rect(DISPLAYSURF, WHITE, (440, 290, 250, 60))  # Hình chữ nhật
                DISPLAYSURF.blit(FONT.render("  MÁY THẮNG", True, RED, WHITE), (460, 300))
            elif self.result == '.':
                print("It's a tie!")
                pygame.draw.rect(DISPLAYSURF, WHITE, (440, 290, 250, 60))  # Hình chữ nhật
                DISPLAYSURF.blit(FONT.render("     HÒA   ", True, RED, WHITE), (460, 300))
            return
        return False


class MinMax(Algorithm):
    def __init__(self):
        super().__init__()

    def max(self):
        maxv = -2

        px = None
        py = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    # On the empty field player 'O' makes a move and calls Min
                    # That's one branch of the game tree.
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Setting back the field to empty
                    self.current_state[i][j] = '.'
        return (maxv, px, py)

    # Player 'X' is min, in this case human
    def min(self):

        # Possible values for minv are:
        # -1 - win
        # 0  - a tie
        # 1  - loss

        # We're initially setting it to 2 as worse than the worst case:
        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'

        return (minv, qx, qy)

    def play_min_max(self, px=0, py=0, ai_First=False):
        if self.check_winer() == None:
            return

        if ai_First:
            (m, px, py) = self.max()
            self.current_state[px][py] = 'O'
            DISPLAYSURF.blit(ICON_O, (70 + py * 110, 220 + px * 110))
            self.player_turn = 'X'
            self.draw_board()
            return

        # If it's player's turn

        if self.is_valid(px, py):
            self.current_state[px][py] = 'X'
            DISPLAYSURF.blit(ICON_X, (70 + py * 110, 220 + px * 110))
            self.player_turn = 'O'
        else:
            print('The move is not valid! Try again.')
            return

        if self.check_winer() == None:
            return

        # If it's AI's turn
        (m, px, py) = self.max()
        self.current_state[px][py] = 'O'
        DISPLAYSURF.blit(ICON_O, (70 + py * 110, 220 + px * 110))
        self.player_turn = 'X'

        if self.check_winer() == None:
            return


class AlphaBeta(Algorithm):

    def __init__(self):
        super().__init__()

    def max_alpha_beta(self, alpha, beta):
        maxv = -2
        px = None
        py = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'O'
                    (m, min_i, in_j) = self.min_alpha_beta(alpha, beta)
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.current_state[i][j] = '.'

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    if maxv >= beta:
                        return (maxv, px, py)

                    if maxv > alpha:
                        alpha = maxv

        return (maxv, px, py)

    def min_alpha_beta(self, alpha, beta):

        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max_alpha_beta(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'

                    if minv <= alpha:
                        return minv, qx, qy

                    if minv < beta:
                        beta = minv

        return minv, qx, qy

    def play_alpha_beta(self, px=0, py=0, ai_First=False):

        if self.check_winer() == None:
            return

        if ai_First:
            (m, px, py) = self.max_alpha_beta(-2, 2)
            self.current_state[px][py] = 'O'
            DISPLAYSURF.blit(ICON_O, (70 + py * 110, 220 + px * 110))
            self.player_turn = 'X'
            self.draw_board()
            return

        (m, qx, qy) = self.min_alpha_beta(-2, 2)
        print('Recommended move: X = {}, Y = {}'.format(qx, qy))

        if self.is_valid(px, py):
            self.current_state[px][py] = 'X'
            DISPLAYSURF.blit(ICON_X, (70 + py * 110, 220 + px * 110))
            print(px, py)
            self.player_turn = 'O'
        else:
            print('The move is not valid! Try again.')
            return

        if self.check_winer() == None:
            return

        (m, px, py) = self.max_alpha_beta(-2, 2)
        self.current_state[px][py] = 'O'
        DISPLAYSURF.blit(ICON_O, (70 + py * 110, 220 + px * 110))
        self.player_turn = 'X'
        self.draw_board()
        if self.check_winer() == None:
            return
