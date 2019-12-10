# py module for generating random numbers
import random
# module that provides an interface for the curses library
# terminal handling for character-cell displays
import curses
# initializes the library, returns a window object which represents the whole screen. short for initialize screen
screen = curses.initscr()
# option for setting cursor visibility, 0 is invisible, 1 is visible (often underline), 2 is very visible (often block cursor)
curses.curs_set(0)
# getmaxyx() returns a tuple of the height and width of the window. destructuring as screen_height and screen_width
screen_height, screen_width = screen.getmaxyx()
# create a new window object with newwin() and give it nlines (height), ncols (width), beginning y, and beginning x values
window = curses.newwin(screen_height, screen_width, 0, 0)
# accept keypad input (might not need this?)
window.keypad(1)
# refresh the screen every 100ms
window.timeout(100)

# snake initial position
snake_x = screen_width / 4
snake_y = screen_height / 2
# coords for initializing snake
snake = [
  [snake_y, snake_x], # head
  [snake_y, snake_x - 1], # body 1 left and 2 left of the head
  [snake_y, snake_x - 2],
]

print(snake)





