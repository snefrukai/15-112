#################################################
# hw6a.py
#
# name:
# andrew id:
#################################################

import cs112_s21_week6_linter
import math, copy, string
import operator
from icecream import ic

#################################################
# Helper functions
#################################################


def almostEqual(d1, d2, epsilon=10**-7):  #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)


import decimal


def roundHalfUp(d):  #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


# ============================================================================ #
#* Part 2: Case Studies
# ============================================================================ #

# ============================================================================ #
#* Example: Grids

from cmu_112_graphics import *

# def appStarted(app):  # set margin, row, col, selection
#     app.margin = 50
#     app.cols = 8
#     app.rows = 4
#     app.selection = (-1, -1)

#     app.grid_w = int((app.width - app.margin * 2) / app.cols)
#     app.grid_h = int((app.height - app.margin * 2) / app.rows)

# def mousePressed(app, event):  # select this (row, col) unless it is selected
#     select_row = int((event.y - app.margin) / app.grid_h)
#     select_col = int((event.x - app.margin) / app.grid_w)
#     app.selection = (select_row, select_col)
#     print(app.selection)

# def redrawAll(app, canvas):  # draw grid of cells
#     for row in range(app.rows):
#         for col in range(app.cols):
#             x0 = app.margin + app.grid_w * col
#             y0 = app.margin + +app.grid_h * row
#             x1 = x0 + app.grid_w
#             y1 = y0 + app.grid_h
#             fill = "orange" if app.selection == (row, col) else "cyan"
#             canvas.create_rectangle(x0, y0, x1, y1, fill=fill)

# runApp(width=400, height=400)

# ============================================================================ #
#* Optional Example: Pong!

# 112_pong.py

# This is a simplified version of Pong, one of the earliest
# arcade games.  We have kept it simple for learning purposes.

# def appStarted(app):
#     # This is a Controller
#     app.waitingForKeyPress = True
#     resetApp(app)

# def resetApp(app):
#     # This is a helper function for Controllers
#     # This initializes most of our model (stored in app.xyz)
#     # This is called when they start the app, and also after
#     # the game is over when we restart the app.
#     app.timerDelay = 50  # milliseconds
#     app.dotsLeft = 2
#     app.score = 0
#     app.paddleX0 = 20
#     app.paddleX1 = 40
#     app.paddleY0 = 20
#     app.paddleY1 = 80
#     app.margin = 5
#     app.paddleSpeed = 10
#     app.dotR = 15
#     app.gameOver = False
#     app.paused = False
#     resetDot(app)

# def resetDot(app):
#     # This is a helper function for Controllers
#     # Get the dot ready for the next round.  Move the dot to
#     # the center of the screen and give it an initial velocity.
#     app.dotCx = app.width // 2
#     app.dotCy = app.height // 2
#     app.dotDx = -10
#     app.dotDy = -3

# def movePaddle(app, direction):
#     # This is a helper function for Controllers
#     # Move the paddle up while keeping it inside the play area
#     if direction == 'Up':
#         dy = min(app.paddleSpeed, app.paddleY0 - app.margin)
#         dy = -dy
#     elif direction == 'Down':
#         dy = min(app.paddleSpeed, app.height - app.margin - app.paddleY1)
#     app.paddleY0 += dy
#     app.paddleY1 += dy

# def keyPressed(app, event):
#     # This is a Controller
#     if app.gameOver:
#         resetApp(app)
#     elif app.waitingForKeyPress:
#         app.waitingForKeyPress = False
#         app.dotsLeft -= 1
#     elif (event.key == 'Down' or event.key == 'Up'):
#         movePaddle(app, event.key)
#     elif (event.key == 'p'):
#         app.paused = not app.paused
#     elif (event.key == 's') and app.paused:
#         doStep(app)

# def timerFired(app):
#     # This is a Controller
#     if (not app.paused): doStep(app)

# def doStep(app):
#     # This is a helper function for Controllers
#     # The dot should move only when we are not waiting for
#     # a key press or in the game-over state
#     if not app.waitingForKeyPress and not app.gameOver:
#         moveDot(app)

# def dotWentOffLeftSide(app):
#     # This is a helper function for Controllers
#     # Called when the dot went off the left side of the screen,
#     # so the round is over.  If there are no dots left, then
#     # the game is over.
#     if app.dotsLeft == 0:
#         app.gameOver = True
#     else:
#         app.waitingForKeyPress = True
#         resetDot(app)

# def dotIntersectsPaddle(app):
#     # This is a helper function for Controllers
#     # Check if the dot intersects the paddle.  To keep this
#     # simple here, we will only test that the center of the dot
#     # is inside the paddle.  We could be more precise here
#     # (that's an interesting exercise!).
#     return ((app.paddleX0 <= app.dotCx <= app.paddleX1)
#             and (app.paddleY0 <= app.dotCy <= app.paddleY1))

# def moveDot(app):
#     # This is a helper function for Controllers
#     # Move the dot by the current velocity (dotDx and dotDy).
#     # Then handle all the special cases:
#     #  * bounce the dot if it went off the top, right, or bottom
#     #  * bounce the dot if it went off the paddle
#     #  * lose the round (or the game) if it went off the left side
#     app.dotCx += app.dotDx
#     app.dotCy += app.dotDy
#     if (app.dotCy + app.dotR >= app.height):
#         # The dot went off the bottom!
#         app.dotCy = app.height - app.dotR
#         app.dotDy = -app.dotDy
#     elif (app.dotCy - app.dotR <= 0):
#         # The dot went off the top!
#         app.dotCy = app.dotR
#         app.dotDy = -app.dotDy
#     if (app.dotCx + app.dotR >= app.width):
#         # The dot went off the right!
#         app.dotCx = app.width - app.dotR
#         app.dotDx = -app.dotDx
#     elif dotIntersectsPaddle(app):
#         # The dot hit the paddle!
#         app.score += 1  # hurray!
#         app.dotDx = -app.dotDx
#         app.dotCx = app.paddleX1
#         dToMiddleY = app.dotCy - (app.paddleY0 + app.paddleY1) / 2
#         dampeningFactor = 3  # smaller = more extreme bounces
#         app.dotDy = dToMiddleY / dampeningFactor
#     elif (app.dotCx - app.dotR <= 0):
#         # The dot went off the left side
#         dotWentOffLeftSide(app)

# def drawAppInfo(app, canvas):
#     # This is a helper function for the View
#     # This draws the title, the score, and the dots left
#     font = 'Arial 18 bold'
#     title = '112 Pong!'
#     canvas.create_text(app.width / 2, 20, text=title, font=font)
#     canvas.create_text(app.width - 70,
#                        20,
#                        text=f'Score: {app.score}',
#                        font=font)
#     canvas.create_text(app.width - 70,
#                        app.height - 20,
#                        text=f'Dots Left: {app.dotsLeft}',
#                        font=font)

# def drawPaddle(app, canvas):
#     # This is a helper function for the View
#     canvas.create_rectangle(app.paddleX0,
#                             app.paddleY0,
#                             app.paddleX1,
#                             app.paddleY1,
#                             fill='black')

# def drawDot(app, canvas):
#     # This is a helper function for the View
#     cx, cy, r = app.dotCx, app.dotCy, app.dotR
#     canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill='black')

# def drawGameOver(app, canvas):
#     # This is a helper function for the View
#     canvas.create_text(app.width / 2,
#                        app.height / 2,
#                        text='Game Over!',
#                        font='Arial 18 bold')
# canvas.create_text(app.width / 2,
#                        app.height / 2 + 50,
#                        text='Press any key to restart',
#                        font='Arial 16 bold')

# def drawPressAnyKey(app, canvas):
#     # This is a helper function for the View
#     canvas.create_text(app.width / 2,
#                        app.height / 2,
#                        text='Press any key to start!',
#                        font='Arial 18 bold')

# def redrawAll(app, canvas):
#     # This is the View
#     drawAppInfo(app, canvas)
#     drawPaddle(app, canvas)
#     if app.gameOver: drawGameOver(app, canvas)
#     elif app.waitingForKeyPress: drawPressAnyKey(app, canvas)
#     else: drawDot(app, canvas)

# runApp(width=400, height=300)

# ============================================================================ #
#* Example: Snake

# import random

# def appStarted(app):
#     app.rows = 10
#     app.cols = 10
#     app.margin = 5  # margin around grid
#     initSnakeAndFood(app)
#     app.waitingForFirstKeyPress = True

# def initSnakeAndFood(app):
#     app.timerDelay = 250
#     app.snake = [(0, 0)]
#     app.direction = (0, +1)  # (drow, dcol)
#     placeFood(app)
#     app.gameOver = False

# # getCellBounds from grid-demo.py
# def getCellBounds(app, row, col):
#     # aka 'modelToView'
#     # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
#     gridWidth = app.width - 2 * app.margin
#     gridHeight = app.height - 2 * app.margin
#     x0 = app.margin + gridWidth * col / app.cols
#     x1 = app.margin + gridWidth * (col + 1) / app.cols
#     y0 = app.margin + gridHeight * row / app.rows
#     y1 = app.margin + gridHeight * (row + 1) / app.rows
#     return (x0, y0, x1, y1)

# def direction_change(app, key):
#     up, down = (-1, 0), (1, 0)
#     left, right = (0, -1), (0, 1)

#     #! need to restrain direction of 1 for 1 step
#     #! delay of app.timerDelay
#     if (key == 'Up' and app.direction != down):  #* stored as hash table?
#         app.direction = up
#     elif (key == 'Down' and app.direction != up):
#         app.direction = down
#     elif (key == 'Left' and app.direction != right):
#         app.direction = left
#     elif (key == 'Right' and app.direction != left):
#         app.direction = right

# def keyPressed(app, event):
#     if (app.waitingForFirstKeyPress):
#         app.waitingForFirstKeyPress = False
#     elif (event.key == 'r'):
#         initSnakeAndFood(app)
#     elif app.gameOver:
#         return
#     elif (event.key in ['Up', 'Down', 'Left', 'Right']):
#         direction_change(app, event.key)
#     # elif (event.key == 's'):
#     # this was only here for debugging, before we turned on the timer
#     # takeStep(app)

# def timerFired(app):
#     if app.gameOver or app.waitingForFirstKeyPress: return
#     takeStep(app)

# def takeStep(app):
#     (drow, dcol) = app.direction
#     (headRow, headCol) = app.snake[0]
#     (newRow, newCol) = (headRow + drow, headCol + dcol)
#     if ((newRow < 0) or (newRow >= app.rows) or (newCol < 0)
#             or (newCol >= app.cols) \
#             or ((newRow, newCol) in app.snake[:-1])): #* can go to poped tail
#         app.gameOver = True
#     else:
#         app.snake.insert(0, (newRow, newCol))
#         if (app.foodPosition == (newRow, newCol)):
#             placeFood(app)
#             app.timerDelay -= 10  #* add speed
#         else:
#             # didn't eat, so remove old tail (slither forward)
#             app.snake.pop()

# def placeFood(app):
#     # Keep trying random positions until we find one that is not in
#     # the snake. Note: there are more sophisticated ways to do this.
#     while True:
#         row = random.randint(0, app.rows - 1)
#         col = random.randint(0, app.cols - 1)
#         if (row, col) not in app.snake:
#             app.foodPosition = (row, col)
#             return

# def drawBoard(app, canvas):
#     for row in range(app.rows):
#         for col in range(app.cols):
#             (x0, y0, x1, y1) = getCellBounds(app, row, col)
#             canvas.create_rectangle(x0, y0, x1, y1, fill='white')

# def drawSnake(app, canvas):
#     for (row, col) in app.snake:
#         (x0, y0, x1, y1) = getCellBounds(app, row, col)
#         fill = 'red' if (row, col) == app.snake[0] else 'blue'
#         canvas.create_oval(x0, y0, x1, y1, fill=fill)

# def drawFood(app, canvas):
#     if (app.foodPosition != None):
#         (row, col) = app.foodPosition
#         (x0, y0, x1, y1) = getCellBounds(app, row, col)
#         canvas.create_oval(x0, y0, x1, y1, fill='green')

# def drawGameOver(app, canvas):
#     if (app.gameOver):
#         canvas.create_text(app.width / 2,
#                            app.height / 2,
#                            text='Game over!',
#                            font='Arial 26 bold')
#         canvas.create_text(app.width / 2,
#                            app.height / 2 + 40,
#                            text='Press r to restart!',
#                            font='Arial 26 bold')

# def redrawAll(app, canvas):
#     if (app.waitingForFirstKeyPress):
#         canvas.create_text(app.width / 2,
#                            app.height / 2,
#                            text='Press any key to start!',
#                            font='Arial 26 bold')
#     else:
#         drawBoard(app, canvas)
#         drawSnake(app, canvas)
#         drawFood(app, canvas)
#         drawGameOver(app, canvas)

# runApp(width=400, height=400)

# ============================================================================ #
#* OPP: Adding and Deleting Shapes
# ============================================================================ #

# import random
# from dataclasses import make_dataclass

# Dot = make_dataclass('Dot', ['cx', 'cy', 'r', 'counter', 'color'])

# def appStarted(app):
#     app.dots = []

# def pointIsInDot(x, y, dot):
#     return ((x - dot.cx)**2 + (y - dot.cy)**2)**0.5 <= dot.r

# def getRandomColor():
#     colors = [
#         'red', 'orange', 'yellow', 'green', 'blue', 'pink', 'lightGreen',
#         'gold', 'magenta', 'maroon', 'salmon', 'cyan', 'brown', 'orchid',
#         'purple'
#     ]
#     return random.choice(colors)

# def mousePressed(app, event):
#     # go through dots in reverse order so that
#     # we find the topmost dot that intersects

#     for d in reversed(app.dots):
#         if pointIsInDot(event.x, event.y, d):
#             d.counter += 1
#             d.color = getRandomColor()
#             return

#     # mouse click was not in any dot, so create a new dot
#     dot_new = Dot(cx=event.x, cy=event.y, r=20, counter=0, color='cyan')
#     app.dots.append(dot_new)
#     # app.dots += dot_new  # 'Dot' object is not iterable

# def keyPressed(app, event):
#     if (event.key == 'd'):
#         if (len(app.dots) > 0): app.dots.pop(0)
#         else: print('No more dots to delete!')

# def redrawAll(app, canvas):
#     # draw the dots and their counters
#     for d in app.dots:
#         x, y, r = d.cx, d.cy, d.r
#         canvas.create_oval(x - r,
#                            y - r,
#                            x + r,
#                            y + r,
#                            fill='white',
#                            outline=d.color,
#                            width=15)
#         canvas.create_text(x, y, text=str(d.counter))

#     # draw the text
#     canvas.create_text(app.width / 2,
#                        20,
#                        text='Example: Adding and Deleting Shapes')
#     canvas.create_text(app.width / 2,
#                        40,
#                        text='Mouse clicks outside dots create new dots')
#     canvas.create_text(app.width / 2,
#                        60,
#                        text='Mouse clicks inside dots increase their counter')
#     canvas.create_text(app.width / 2, 70, text='and randomize their color.')
#     canvas.create_text(app.width / 2, 90, text='Pressing "d" deletes circles')

# runApp(width=400, height=400)

#################################################
#* hw6-standard functions
#################################################


def destructiveRemoveEvens(L):
    i = 0
    while i < len(L):
        if L[i] % 2 == 0:
            L.remove(L[i])
        else:
            i += 1


def nondestructiveRemoveEvens(L):
    l_new = [d for d in L if d % 2 != 0]
    return l_new


# ============================================================================ #
#


def areaOfPolygon(L):
    # l_dif = []  # new list
    area = 0  # no new list
    for i in range(len(L)):
        i_next = (i + 1) % len(L)
        area += L[i][0] * L[i_next][1] - L[i][1] * L[i_next][0]
        # l_dif += L[i][0] * L[i_next][1] - L[i][1] * L[i_next][0],
    area = abs(area / 2)
    # area = abs(sum(l_dif) / 2)
    return area


# ============================================================================ #
#


def evalPolynomial(l, x):
    # n = 0 #* number
    # for i in range(len(l)):
    #     if l[i] != 0:
    #         n += l[i] * x**(len(l) - 1 - i)
    # return n

    l_new = [l[i] * x**(len(l) - 1 - i) for i in range(len(l)) if l[i] != 0]
    return sum(l_new)


# ============================================================================ #
#


def multiplyPolynomials(p1, p2):
    l = [0] * (len(p1) + len(p2) - 1)
    for k in range(len(p2)):
        for i in range(len(p1)):
            l[k + i] += p2[k] * p1[i]
    return l


# ============================================================================ #
#


def solvesCryptarithm(puzzle, solution):
    # def get_part(s):
    #     # s_new = '' #* old school str
    #     # k = 0
    #     # while k < nth:
    #     #     if '+' not in s and '=' not in 's':
    #     #         s_new = s
    #     #     for i in range(len(s)):
    #     #         if s[i] == '+' or s[i] == '=':
    #     #             s_new = s[:i]
    #     #             s = s[i + 1:]
    #     #             break
    #     #     k += 1
    #     # s_new = s_new.strip()

    #     l = s.split(" ")
    #     for c in ['+', '=']:
    #         l.remove(c)
    #     return l

    def get_n(val, solution):
        s = ''
        for c in val:
            if c not in solution: return False
            s += str(solution.find(c))
        return int(s)

    l_s = puzzle.split(" ")
    for c in ['+', '=']:
        l_s.remove(c)

    l_n = []
    for val in l_s:
        n = get_n(val, solution)
        if n == False: return False
        l_n += [n]
    return l_n[0] + l_n[1] == l_n[2]


# ============================================================================ #
#


def bestScrabbleScore(dictionary, letterScores, hand):
    def check_hit(word, hand):
        s = ''.join(sorted(word))
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:  # aaab
                continue
            elif s.count(s[i]) > hand.count(s[i]):
                return False
        return True

    def get_score(word):
        # n = 0
        # for c in word:
        #     n += letterScores[string.ascii_lowercase.find(c)]
        # return n

        l = [letterScores[string.ascii_lowercase.find(c)] for c in word]
        return sum(l)

    l_hit = [word for word in dictionary if check_hit(word, hand)]
    if l_hit == []: return None
    l_score = [get_score(v) for v in l_hit]
    l_max = [l_hit[i] for i in range(len(l_hit)) if l_score[i] == max(l_score)]
    # for i in range(len(l_score)):
    #     if l_score[i] == max(l_score):
    #         l_max += [l_hit[i]]

    if len(l_max) == 1: l_max = "".join(l_max)  # list to str
    return (l_max, max(l_score))


#################################################
#* hw6-bonus functions
#################################################


def runSimpleProgram_str_translate(l_arg, l_var, val):
    if val[0].isdigit():
        return int(val)
    else:
        i = int(val[1:])
        return l_arg[i] if val[0] == 'A' else l_var[i]


def runSimpleProgram_var_expr(l_arg, l_var, l):
    i = int(l[0][1:])
    if len(l) == 2:
        l_var[i] = int(l[-1])  # easy to forgot format
    elif l[1] in ['+', '-']:
        n1 = runSimpleProgram_str_translate(l_arg, l_var, l[-2])
        n2 = runSimpleProgram_str_translate(l_arg, l_var, l[-1])
        if l[1] == '-': n2 = -n2
        l_var[i] = n1 + n2
    return l_var


def runSimpleProgram_jump(l_arg, l_var, l):
    if l[0] == 'JMP':
        bool = True
    else:  # conditional jump, ????????????????????????????????????
        n = runSimpleProgram_str_translate(l_arg, l_var, l[1])
        # op = l[0][-1] #? del
        # if op == '+': bool = n > 0
        # elif op == '0': bool = n == 0
        bool = (n > 0) if l[0][-1] == '+' else (n == 0)  # '0'
    return bool, l[-1]  # cond, target


def runSimpleProgram(program, args):
    len_var_name = 0
    l = program.split("\n")
    for i in range(len(l)):
        if l[i][0] != '!':  # split sub list of expr
            l[i] = l[i].strip().split(" ")
            for v in l[i]:
                if v[0] == 'L':
                    len_var_name = max(int(v[1:]), len_var_name)
    l_var = [0] * (len_var_name + 1)
    l_arg = [v for v in args]
    # ic(l)

    k = 0
    jump_bool, jump_to = False, ''
    while k != len(l):
        expr = l[k]
        k += 1  # beware of the continue
        if expr[0] == '!': continue
        elif jump_bool:
            if jump_to not in expr[0]: continue  # skip to jump target
            else: jump_bool = False
        elif expr[0][0] == 'L':
            l_var = runSimpleProgram_var_expr(l_arg, l_var, expr)
        elif expr[0][:3] == 'JMP':
            jump_bool, jump_to = runSimpleProgram_jump(l_arg, l_var, expr)
            if jump_bool: k = 0  #* reset to find target
        elif expr[0][:3] == 'RTN':
            return runSimpleProgram_str_translate(l_arg, l_var, expr[-1])
    # ic(l_var)


# ============================================================================ #
#


def getKthBinaryDigit(n, kth):
    len_bin = int(math.log2(n)) + 1 if n != 0 else 1
    if not kth <= len_bin - 1: return None
    l_bin = [0] * len_bin

    for i in range(len(l_bin)):  # n to binary
        n_power = 2**(len(l_bin) - 1 - i)
        # ic(n_power)
        if n >= n_power:
            l_bin[i] = 1
            n -= n_power
    # ic(l_bin, len_bin)
    return l_bin[len(l_bin) - 1 - kth]


def allSublists(L):
    N = len(L)
    for k in range(2**N):
        l_temp = []
        for kth in range(N):
            if getKthBinaryDigit(k, kth) == 1:  # kth result in binary
                l_temp.insert(0, L[-1 - kth])  # from right to left
        # ic(k, l_temp)
        yield l_temp


def solveSubsetSum(L):
    for l in allSublists(L):
        if l != [] and sum(l) == 0:
            return l
    return None


def heapsAlgorithmForPermutations(L):
    n = len(L)
    c = [0] * n
    yield copy.copy(L)

    i = 0
    while i < n:
        if c[i] < i:
            k = 0 if i % 2 == 0 else c[i]
            L[k], L[i] = L[i], L[k]
            yield copy.copy(L)
            # ic(A)
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
        # ic(c)


# ============================================================================ #
#
def solveCryptarithm_get_test(puzzle, maxDigit):
    s = ''
    for c in puzzle:
        if c.isalpha() and c not in s:
            s += c

    n_dif = (maxDigit + 1) - len(s)
    if n_dif > 0:
        s += '-' * n_dif
    else:
        s = s[:maxDigit + 1]
    # s = s[:maxDigit + 1] + '-' * (10 - (maxDigit + 1))
    return s


def formatCryptarithmSolution(puzzle, solution):
    s = puzzle + '\n'
    for c in puzzle:  # format 2nd line
        s += str(solution.find(c)) if c in solution else c  # skip '=' etc
    return s


def solveCryptarithmWithMaxDigit(puzzle, maxDigit):
    l_target = list(solveCryptarithm_get_test(puzzle, maxDigit))
    l_permutation = heapsAlgorithmForPermutations(l_target)

    for l in l_permutation:
        s_test = "".join(l)  # list to s
        # ic(s_test)
        if solvesCryptarithm(puzzle, s_test):
            return formatCryptarithmSolution(puzzle, s_test)
    return None


def countCryptarithmsWithMaxDigit(puzzle, maxDigit):
    count = 0
    hit = ''

    #? only return 1 result
    # if solveCryptarithmWithMaxDigit(puzzle, maxDigit) != None:
    #     s_hit += solveCryptarithmWithMaxDigit(puzzle, maxDigit)
    #     count += 1

    l_target = list(solveCryptarithm_get_test(puzzle, maxDigit))
    l_permutation = heapsAlgorithmForPermutations(l_target)
    for l in l_permutation:
        s_test = "".join(l)
        if solvesCryptarithm(puzzle, s_test):
            count += 1
            hit += formatCryptarithmSolution(puzzle, s_test)
    return count, hit


# ============================================================================ #
#
def get_puzzle(l_left, s_right):
    l_left.sort()
    s = l_left[0] + ' + ' + l_left[1] + ' = ' + s_right
    return s


def getAllSingletonCryptarithmsWithMaxDigit(words, maxDigit):
    l = []
    for i in range(len(words)):  # each comb baesd on each word
        l_temp = words[:]
        l_temp.pop(i)
        l_sub_all = allSublists(l_temp)  # generator
        for l_sub in l_sub_all:
            if len(l_sub) == 2:  # a + b
                puzzle = get_puzzle(l_sub, words[i])
                count, hit = countCryptarithmsWithMaxDigit(puzzle, maxDigit)
                if count == 1:
                    l += [hit]
    s = "\n".join(sorted(l))
    return s


#################################################
#* Test Functions
#################################################


def _destructiveRemoveEvens(L):
    destructiveRemoveEvens(L)
    return L


def testDestructiveRemoveEvens():
    print("Testing destructiveRemoveEvens()...", end="")
    assert (_destructiveRemoveEvens([1, 2, 3, 4]) == [1, 3])
    assert (_destructiveRemoveEvens([1, 3, 5, 7, 3]) == [1, 3, 5, 7, 3])
    assert (_destructiveRemoveEvens([2, 4, 2, 4, 6]) == [])
    assert (_destructiveRemoveEvens([2, 4, 1, 2, 4, 6]) == [1])
    print("Passed!")


def _verifyRemoveEvensIsNondestructive():
    a = [1, 2, 3]
    b = copy.copy(a)
    nondestructiveRemoveEvens(a)  # ignore result, just check if destructive
    return (a == b)


def testNondestructiveRemoveEvens():
    print("Testing nondestructiveRemoveEvens()...", end='')
    assert (_verifyRemoveEvensIsNondestructive())
    assert (nondestructiveRemoveEvens([1, 2, 3, 4]) == [1, 3])
    assert (nondestructiveRemoveEvens([1, 3, 5, 7, 3]) == [1, 3, 5, 7, 3])
    assert (nondestructiveRemoveEvens([2, 4, 2, 4, 6]) == [])
    assert (nondestructiveRemoveEvens([2, 4, 1, 2, 4, 6]) == [1])
    print("Passed!")


def _verifyAreaOfPolygonIsNondestructive():
    a = [(4, 10), (9, 7), (11, 2), (2, 2)]
    b = copy.deepcopy(a)
    # ignore result, just checking for destructiveness here
    areaOfPolygon(a)
    return (a == b)


def testAreaOfPolygon():
    print("Testing areaOfPolygon()...", end="")
    # assert (_verifyAreaOfPolygonIsNondestructive())
    # ic(areaOfPolygon([(4, 10), (9, 7), (11, 2), (2, 2)]))
    assert (almostEqual(areaOfPolygon([(4, 10), (9, 7), (11, 2), (2, 2)]),
                        45.5))
    assert (almostEqual(areaOfPolygon([(9, 7), (11, 2), (2, 2), (4, 10)]),
                        45.5))
    assert (almostEqual(areaOfPolygon([(0, 0), (0.5, 1), (1, 0)]), 0.5))
    assert (almostEqual(areaOfPolygon([(0, 10), (0.5, 11), (1, 10)]), 0.5))
    assert (almostEqual(areaOfPolygon([(-0.5, 10), (0, -11), (0.5, 10)]),
                        10.5))
    print("Passed!")


def _verifyEvalPolynomialIsNondestructive():
    a = [2, 3, 0, 4]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    evalPolynomial(a, 4)
    return (a == b)


def testEvalPolynomial():
    print("Testing evalPolynomial()...", end="")
    assert (_verifyEvalPolynomialIsNondestructive())
    # ic(evalPolynomial([2, -3, 0, 4], 4))
    # ic(evalPolynomial([2, 3, 0, 4], 4))
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    assert (evalPolynomial([2, 3, 0, 4], 4) == 180)
    # # f(x) = 6, f(42) = 6
    assert (evalPolynomial([6], 42) == 6)
    # # f(x) = 6x^2 -2x - 20, f(-1) = -12
    assert (evalPolynomial([6, -2, -20], -1) == -12)
    # # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
    assert (evalPolynomial([6, 0, -8, 0, -8, 0], 2) == 112)
    assert (evalPolynomial([6, 0, -8, 0, -8, 0], 1) == -10)
    assert (evalPolynomial([6, 0, -8, 0, -8, 0], 0) == 0)
    print("Passed.")


def _verifyMultiplyPolynomialsIsNondestructive():
    a, b = [2], [3]
    c, d = copy.copy(a), copy.copy(b)
    # ignore result, just checking for destructiveness here
    multiplyPolynomials(a, b)
    return (a == c) and (b == d)


def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    # _verifyMultiplyPolynomialsIsNondestructive()
    # ic(multiplyPolynomials([1, 2, 3], [1, 2, 3]))
    # ic(multiplyPolynomials([2, -4], [3, 5]))
    # ic(multiplyPolynomials([2, 0, 3], [4, 5]))
    # # (2)*(3) == 6
    assert (multiplyPolynomials([2], [3]) == [6])
    # # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert (multiplyPolynomials([2, -4], [3, 5]) == [6, -2, -20])
    # # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert (multiplyPolynomials([2, 0, -4],
                                [3, 0, 2, 0]) == [6, 0, -8, 0, -8, 0])
    print("Passed!")


def testSolvesCryptarithm():
    print("Testing solvesCryptarithm()...", end="")
    # ic(solvesCryptarithm_part("SEND + MORE = MONEY", 1))
    # ic(solvesCryptarithm_part("SEND + MORE = MONEY", 2))
    # ic(solvesCryptarithm_part("SEND + MORE = MONEY", 3))
    # ic(solvesCryptarithm_val("SEND", "OMY--ENDRS"))
    # ic(solvesCryptarithm_val("SEND", "OMY--"))
    # ic(solvesCryptarithm("SEND + MORE = MONEY", "OMY--ENDRS"))
    # ic(solvesCryptarithm("NUMBER + NUMBER = PUZZLE", "UMNZP-BLER"))  #== True

    assert (solvesCryptarithm("SEND + MORE = MONEY", "OMY--ENDRS") == True)
    assert (solvesCryptarithm("RAM + RAT = ANT", "MRATN-----") == True)
    # from http://www.cryptarithms.com/default.asp?pg=1
    assert (solvesCryptarithm("NUMBER + NUMBER = PUZZLE",
                              "UMNZP-BLER") == True)
    assert (solvesCryptarithm("TILES + PUZZLES = PICTURE",
                              "UISPELCZRT") == True)
    assert (solvesCryptarithm("COCA + COLA = OASIS", "LOS---A-CI") == True)
    assert (solvesCryptarithm("CROSS + ROADS = DANGER", "-DOSEARGNC") == True)

    assert (solvesCryptarithm("SEND + MORE = MONEY", "OMY--ENDR-") == False)
    assert (solvesCryptarithm("SEND + MORE = MONEY", "OMY-ENDRS") == False)
    assert (solvesCryptarithm("SEND + MORE = MONY", "OMY--ENDRS") == False)
    assert (solvesCryptarithm("SEND + MORE = MONEY", "MOY--ENDRS") == False)
    print("Passed!")


def _verifyBestScrabbleScoresIsNondestructive():
    a = ["a", "b", "c"]
    b = [1] * 26
    c = ['b']
    d, e, f = copy.copy(a), copy.copy(b), copy.copy(c)
    bestScrabbleScore(a, b, c)
    return (a == d) and (b == e) and (c == f)


def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")

    # _verifyBestScrabbleScoresIsNondestructive()

    def dictionary1():
        return ["a", "b", "c"]

    def letterScores1():
        return [1] * 26

    def dictionary2():
        return ["xyz", "zxy", "zzy", "yy", "yx", "wow"]

    def letterScores2():
        return [1 + (i % 5) for i in range(26)]

    # ic(bestScrabbleScore_hit(dictionary2(), list("xyzy")))
    # ic(bestScrabbleScore_val(letterScores2(), 'yy')) # 10
    # ic(bestScrabbleScore_val(letterScores2(), 'zxy'))  # 10
    # ic(bestScrabbleScore_val(letterScores2(), 'yx'))  # 9
    # ic(bestScrabbleScore(dictionary2(), letterScores2(),
    #                      list("xyzy")))  # (["xyz", "zxy", "yy"], 10)
    # ic(bestScrabbleScore(dictionary2(), letterScores2(),
    #                      list("xyq")))  # ("yx", 9))

    assert (bestScrabbleScore(dictionary1(), letterScores1(),
                              list("b")) == ("b", 1))
    assert (bestScrabbleScore(dictionary1(), letterScores1(),
                              list("ace")) == (["a", "c"], 1))
    assert (bestScrabbleScore(dictionary1(), letterScores1(),
                              list("b")) == ("b", 1))
    assert (bestScrabbleScore(dictionary1(), letterScores1(),
                              list("z")) == None)
    # # x = 4, y = 5, z = 1
    # # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    # #    10     10     7     10    9      -
    # assert (bestScrabbleScore(dictionary2(), letterScores2(),
    #                           list("xyz")) == (["xyz", "zxy"], 10))
    # assert (bestScrabbleScore(dictionary2(), letterScores2(),
    #                           list("xyzy")) == (["xyz", "zxy", "yy"], 10))
    # assert (bestScrabbleScore(dictionary2(), letterScores2(),
    #                           list("xyq")) == ("yx", 9))
    # assert (bestScrabbleScore(dictionary2(), letterScores2(),
    #                           list("yzz")) == ("zzy", 7))
    # assert (bestScrabbleScore(dictionary2(), letterScores2(),
    #                           list("wxz")) == None)
    print("Passed!")


def test_runSimpleProgram_int_from_list(l_arg, l_var):
    assert (runSimpleProgram_str_translate(l_arg, l_var, 'A0') == 5)
    assert (runSimpleProgram_str_translate(l_arg, [0, 2, 0, 0], 'L1') == 2)
    assert (runSimpleProgram_str_translate(l_arg, [0, 2, 0, 0], '6') == 6)


def test_runSimpleProgram_type_var(l_arg, l_var):
    # L10 - A0 A1
    assert (runSimpleProgram_var_expr(
        l_arg, [0] * 11, ['L10', '+', 'A0', 'A1']) == [0] * 10 + [11])
    assert (runSimpleProgram_var_expr(
        l_arg, [0] * 5, ['L0', '-', 'A0', 'A1']) == [-1] + [0] * 4)
    assert (runSimpleProgram_var_expr(
        l_arg, [0] * 5, ['L2', '-', 'A0', 'A1']) == [0] * 2 + [-1] + [0] * 2)
    # L1 0
    assert (runSimpleProgram_var_expr(l_arg, [0] * 3, ['L1', 3]) == [0, 3, 0])
    # L0 + L0 1
    assert (runSimpleProgram_var_expr(l_arg, [0] * 3,
                                      ['L0', '+', 'L0', '2']) == [2, 0, 0])


def test_runSimpleProgram_type_jump(l_arg, l_var):
    assert (runSimpleProgram_jump(l_arg, [1, 1, 0],
                                  ['JMP', 'loop']) == (True, 'loop'))
    assert (runSimpleProgram_jump(l_arg, [1, 2, 3],
                                  ['JMP+', 'L0', 'a0']) == (True, 'a0'))
    assert (runSimpleProgram_jump(l_arg, [0, 2, 3],
                                  ['JMP+', 'L0', 'a0']) == (False, 'a0'))


def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    l_var = [0] * 10
    l_arg = [5, 6, 0, 0]
    test_runSimpleProgram_int_from_list(l_arg, l_var)
    test_runSimpleProgram_type_var(l_arg, l_var)
    test_runSimpleProgram_type_jump(l_arg, l_var)

    largest = """! largest: Returns max(A0, A1)
                   L10 - A0 A1
                   JMP+ L10 a0
                   RTN A1
                   a0:
                   ! test comment
                   RTN A0"""
    # ic(runSimpleProgram(largest, [6, 5]))
    assert (runSimpleProgram(largest, [5, 6]) == 6)
    assert (runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    # ic(runSimpleProgram(sumToN, [5]))
    assert (runSimpleProgram(sumToN, [5]) == 1 + 2 + 3 + 4 + 5)
    assert (runSimpleProgram(sumToN, [10]) == 10 * 11 // 2)
    print("Passed!")


# ============================================================================ #
#


def test_getKthBinaryDigit():
    assert (getKthBinaryDigit(0, 0)) == 0  # 0
    # ic(getKthBinaryDigit(0, 0))  # 0
    assert (getKthBinaryDigit(1, 0)) == 1  # 1
    assert (getKthBinaryDigit(2, 0)) == 0  # 10
    assert (getKthBinaryDigit(2, 1)) == 1  # 10
    assert (getKthBinaryDigit(2, 2)) == None  # 10


def testAllSublists():
    test_getKthBinaryDigit()

    # ic(allSublists([3, 5]))

    def f():
        yield 42

    assert (type(allSublists([1, 2, 3])) == type(f()))  # generator
    assert (sorted(allSublists([1])) == [[], [1]])
    assert (sorted(allSublists([3, 5])) == [[], [3], [3, 5], [5]])
    assert (sorted(allSublists([6, 7, 8])) == [[], [6], [6, 7], [6, 7, 8],
                                               [6, 8], [7], [7, 8], [8]])


def testSolveSubsetSum():
    # ic(solveSubsetSum([5, 2, 3, -4]))
    # ic(solveSubsetSum([-1, 5, 2, 3, -4]))

    def checkSubsetSum(L):
        solution = solveSubsetSum(L)
        for v in solution:
            assert (solution.count(v) <= L.count(v))
        assert (sum(solution) == 0)

    assert (solveSubsetSum([5, 2, 3, -4]) == None)
    checkSubsetSum([-1, 5, 2, 3, -4])
    checkSubsetSum([8, 19, 31, 27, 52, -70, 4])


def testHeapsAlgorithmForPermutations():
    # ic((heapsAlgorithmForPermutations([3, 1, 2])))
    # ic((heapsAlgorithmForPermutations([1, 2])))
    # ic((heapsAlgorithmForPermutations(['A', 'B', '-'])))

    def f():
        yield 42

    assert (type(heapsAlgorithmForPermutations([1])) == type(f()))  # gen
    assert (sorted(heapsAlgorithmForPermutations([1])) == [[1]])
    assert (sorted(heapsAlgorithmForPermutations([1, 2])) == [[1, 2], [2, 1]])
    assert (sorted(heapsAlgorithmForPermutations([3, 1, 2])) == [[1, 2, 3],
                                                                 [1, 3, 2],
                                                                 [2, 1, 3],
                                                                 [2, 3, 1],
                                                                 [3, 1, 2],
                                                                 [3, 2, 1]])


def testSolveCryptarithmWithMaxDigit():
    # ic(solveCryptarithmWithMaxDigit('RAM + RAT = ANT', 4))

    assert (solveCryptarithmWithMaxDigit('RAM + RAT = ANT', 4) == '''\
RAM + RAT = ANT
120 + 123 = 243''')
    assert (solveCryptarithmWithMaxDigit('ANT + CAT = EEL', 4) == None)
    assert (solveCryptarithmWithMaxDigit('ANT + CAT = EEL', 5) == '''\
ANT + CAT = EEL
125 + 315 = 440''')


def testGetAllSingletonCryptarithmsWithMaxDigit():
    words = ['EEL', 'RAM', 'CAT', 'BEE', 'FLY', 'HEN', 'RAT', 'DOG', 'ANT']

    # ic(countCryptarithmsWithMaxDigit('ANT + CAT = EEL', 6))  # 1
    assert (get_puzzle(['RAT', 'ANT'], 'EEL') == 'ANT + RAT = EEL')

    # ic(getAllSingletonCryptarithmsWithMaxDigit(words, 4))
    # ic(getAllSingletonCryptarithmsWithMaxDigit(words, 5))

    assert (getAllSingletonCryptarithmsWithMaxDigit(words, 3) == '')
    assert (getAllSingletonCryptarithmsWithMaxDigit(words, 4) == '''\
RAM + RAT = ANT
120 + 123 = 243''')
    assert (getAllSingletonCryptarithmsWithMaxDigit(words, 5) == '''\
ANT + CAT = EEL
125 + 315 = 440
ANT + CAT = HEN
105 + 315 = 420
ANT + RAT = EEL
125 + 315 = 440
ANT + RAT = HEN
105 + 315 = 420
BEE + EEL = FLY
411 + 112 = 523''')

    words = [
        'DEER', 'BEAR', 'GOAT', 'MULE', 'PUMA', 'COLT', 'ORCA', 'IBEX', 'LION',
        'WOLF'
    ]

    assert (getAllSingletonCryptarithmsWithMaxDigit(words, 5) == '')
    assert (getAllSingletonCryptarithmsWithMaxDigit(words, 6) == '''\
BEAR + DEER = IBEX
4203 + 1223 = 5426
COLT + GOAT = ORCA
4635 + 1605 = 6240''')


def testBonusCombinatoricsProblems():
    print('Testing bonus combinatorics problems...')

    testAllSublists()
    testSolveSubsetSum()
    testHeapsAlgorithmForPermutations()
    testSolveCryptarithmWithMaxDigit()
    testGetAllSingletonCryptarithmsWithMaxDigit()
    print('Passed!')


#################################################
# testAll and main
#################################################


def testAll():
    # comment out the tests you do not wish to run!
    testDestructiveRemoveEvens()
    testNondestructiveRemoveEvens()
    testAreaOfPolygon()
    testEvalPolynomial()
    testMultiplyPolynomials()
    testSolvesCryptarithm()
    testBestScrabbleScore()

    # bonus
    testRunSimpleProgram()
    testBonusCombinatoricsProblems()


def main():
    cs112_s21_week6_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
