import board
import keypad
import digitalio

rows = [board.GP26, board.GP27, board.GP28, board.GP28, board.GP29]
cols = [board.GP6, board.GP7, board.GP0]
matrix = keypad.KeyMatrix(rows, cols, columns_to_anodes=False)

while True:
    event = matrix.events.get()
    if event:
        if (event.key_number == 0):
            kbd.send(Keycode.ESC)
        elif (event.key_number == 1):
            kbd.send(Keycode.A)
        elif (event.key_number == 2):
            kbd.send(Keycode.X)
        elif (event.key_number == 3):
            kbd.send(Keycode.CTRL, Keycode.S)
        elif (event.key_number == 4):
            kbd.send(Keycode.W)
        elif (event.key_number == 5):
            kbd.send(Keycode.V)
        elif (event.key_number == 6):
            kbd.send(Keycode.DELETE)
        elif (event.key_number == 7):
            kbd.send(Keycode.CTRL, Keycode.L)
        elif (event.key_number == 8):
            kbd.send(Keycode.F)
        elif (event.key_number == 9):
            kbd.send(Keycode.ENTER)
        elif (event.key_number == 10):
            kbd.send(Keycode.R)
        elif (event.key_number == 11):
            kbd.send(Keycode.B)