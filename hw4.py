#################################################
# hw4.py
#
# Your name:
# Your andrew id:
#################################################

from typing import Tuple
import cs112_s21_week4_linter
from cmu_112_graphics import *
import random, string, math, time

# ============================================================================ #
# course case rewrite

# def appStarted(app):
#     app.cx = app.width / 2
#     app.cy = app.height / 2
#     app.r = 40
#     app.paused = False

# def timerFired(app):
#     if app.paused: doStep(app)

# def doStep(app):
#     app.cx -= 10
#     if app.cx + app.r < 0: app.cx = app.width

# def keyPressed(app, event):
#     if event.key == 'Left': app.cx -= 10
#     elif event.key == 'Right': app.cx += 10

#     if event.key == 'p':
#         app.paused = not app.paused  # why cant use True? cuz it's toggle
#     elif not app.paused and event.key == 's':  # stepping
#         doStep(app)

# def mousePressed(app, event):
#     app.cx = event.x
#     app.cy = event.y

# def redrawAll(app, canvas):
#     canvas.create_oval(app.cx - app.r, app.cy - app.r, app.cx + app.r,
#                        app.cy + app.r)

# runApp(width=400, height=400)

# From here: https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO

# Note: Tkinter uses event.keysym for some keys, and event.char
# for others, and it can be confusing how to use these properly.
# Instead, cmu_112_graphics replaces both of these with event.key,
# which simply works as expected in all cases.

# This version moves in both x and y dimensions.

# ============================================================================ #
# model
# ============================================================================ #


def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def restart(app):
    app.word = random.choice(app.word_list.splitlines())
    # app.word = 'occur'
    s_temp = ''
    app.guess = ''
    for i in range(len(app.word)):
        s_temp += app.word[i] + ' '
        app.guess += '_ '
    app.word = s_temp.upper().strip()
    app.guess = app.guess.strip()

    app.guess_count = 0
    app.guess_feedback = None
    app.guess_wrong = ''
    app.info = 'Guess a letter...'
    app.choices_temp = app.choices

    app.bonus_mode = False
    app.display_answer = False
    app.stop = False
    app.elapsed = '0s'
    app.rnd += 1
    app.time_start = time.time()


def appStarted(app):
    # app.cx = app.width / 2
    # app.y_dist = app.height / 4

    app.word_list = readFile('common-words.txt')
    app.choices = string.ascii_letters

    app.rnd = 0
    app.win_count = 0

    restart(app)
    sizeChanged(app)


# ============================================================================ #
# controller
# ============================================================================ #


def mousePressed(app, event):
    if app.stop: restart(app)
    else: app.display_answer = not app.display_answer


def keyPressed(app, event):
    app.input = event.key.upper()
    c = app.input

    if c == 'F5': restart(app)
    elif not app.stop and c in app.choices:
        app.guess_wrong += c
        app.guess_count += 1
        s_temp = app.word

        if c not in app.choices_temp:
            app.info = 'You already guessed ' + c + '. Guess again.'
        elif c in s_temp:
            while s_temp.find(c) != -1:
                i = s_temp.find(c)
                app.guess = app.guess[:i] + c + app.guess[i + 1:]
                s_temp = s_temp.replace(c, '_', 1)
            app.info = 'Good job! Keep guessing...'
            if app.guess == app.word:
                app.stop = True
                app.win_count += 1
                app.info = 'You got it! (press the mouse to restart)'

        app.choices_temp = app.choices_temp.replace(c, '')
    elif c == '!':
        app.bonus_mode = not app.bonus_mode
        if app.bonus_mode:
            # app.elapsed = app.elapsed_2
            print('''[1] you've entered the bonus mode:
- tracks how many rounds played and won
- changed time format to minutes and seconds
        ''')
        else:
            # app.elapsed = app.elapsed_2
            print('''[0] you've changed back to the standard mode
            ''')
    else:
        app.info = f'{c} is not a letter!'


def timerFired(app):
    if not app.stop:
        time.sleep(1)
        foo = int(time.time() - app.time_start)
        if app.bonus_mode:
            app.elapsed = str(foo // 60) + 'min ' + str(foo % 60) + 's'
        elif not app.bonus_mode:
            app.elapsed = str(foo) + 's'


def sizeChanged(app):
    app.cx = app.width / 2
    app.y_dist = app.height / 4
    app.font_1 = f'Arial {app.width // 20} bold'
    app.font_2 = f'Arial {app.width // 30} bold'
    app.font_3 = f'Arial {app.width // 40} '
    app.font_5 = f'Arial {app.width // 50}'


# ============================================================================ #
# redrawAll and drawing helper functions:
# ============================================================================ #


def drawTitle(app, canvas):
    canvas.create_text(app.cx,
                       app.y_dist / 2,
                       text="Word Guessing Game",
                       font=app.font_1)

    for i in range(1, 4):
        canvas.create_line(0,
                           i * app.y_dist,
                           app.width,
                           i * app.y_dist,
                           width=2)


# ============================================================================ #
#


def drawDisplayWord(app, canvas):
    if app.stop:
        fill = '#62F07E'
        width = 1
    else:
        fill = ''
        width = 0
    width_rec = len(app.word) * (app.width // 20) * .76  #? 开始乱起来和挖坑了
    canvas.create_rectangle(app.cx - width_rec / 2,
                            app.y_dist * 1.2,
                            app.cx + width_rec / 2,
                            app.y_dist * 1.8,
                            fill=fill,
                            width=width)

    if app.display_answer: text = app.word
    elif not app.display_answer: text = app.guess
    canvas.create_text(app.cx, app.y_dist * 1.5, text=text, font=app.font_1)


def bonus_drawCount(app, canvas):  # bonus
    if app.bonus_mode:
        text = f'round {app.rnd}\n wins {app.win_count}'
    else:
        text = ''

    canvas.create_text(
        app.width * 1 / 8,
        app.y_dist * 1.5,
        text=text,
        # anchor='s',
        font=app.font_5)


# ============================================================================ #
#


def drawGuesses_row(app, canvas, r, rows, row, y):
    chars_per_line = int(26 / rows)
    dist = app.width / chars_per_line
    y = app.y_dist * y

    for i in range(chars_per_line):
        x = dist * i + dist / 2
        text = app.choices[26 + chars_per_line * (row - 1) + i]
        if text in app.guess:
            fill = 'lightGreen'
            width = 1
        elif text in app.guess_wrong:
            fill = 'pink'
            width = 1
        else:
            fill = ''
            width = 0
        canvas.create_oval(x - r, y, x + r, y + r * 2, fill=fill, width=width)
        canvas.create_text(x, y + r, text=text, font=app.font_5)


def drawGuesses(app, canvas):
    r = app.width // 50
    rows = 2

    drawGuesses_row(app, canvas, r, rows, 1, 2.2)
    drawGuesses_row(app, canvas, r, rows, 2, 2.6)


# ============================================================================ #
#


def drawGuessCount(app, canvas):
    canvas.create_text(app.width * 1 / 3,
                       app.y_dist * 3.25,
                       text=f'Guesses: {app.guess_count}',
                       font=app.font_3)


def drawElapsedTime(app, canvas):
    canvas.create_text(app.width * 2 / 3,
                       app.y_dist * 3.25,
                       text=f'Time: {app.elapsed}',
                       font=app.font_3)


def drawMessage(app, canvas):
    canvas.create_text(app.cx,
                       app.y_dist * 3.65,
                       text=f'{app.info}',
                       font=app.font_2)


# ============================================================================ #
#


def redrawAll(app, canvas):
    drawTitle(app, canvas)
    bonus_drawCount(app, canvas)  # bonus
    drawDisplayWord(app, canvas)
    drawGuesses(app, canvas)
    drawGuessCount(app, canvas)
    drawElapsedTime(app, canvas)
    drawMessage(app, canvas)


def main():
    cs112_s21_week4_linter.lint()
    runApp(width=600, height=400)


if __name__ == '__main__':
    main()