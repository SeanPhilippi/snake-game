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
snake_x = screen_width // 4
snake_y = screen_height // 2
# coords for initializing snake
snake = [
  [snake_y, snake_x], # head
  [snake_y, snake_x - 1], # body 1 left and 2 left of the head
  [snake_y, snake_x - 2],
]
# food position coords
food = [screen_height // 2, screen_width // 2]
# add character a y, x coords
window.addch(food[0], food[1], curses.ACS_PI)
# simulates press of right key with curses
key = curses.KEY_RIGHT
# starting an infinite loop
while True:
  # get character at y,x coords, assign to next_key variable
  next_key = window.getch()
  # do nothing if next_key == -1 else assign to next_key
  key = key if next_key == -1 else next_key
  # if the snake's x position is equal to 0 (at the top) or the height of the screen
  # or if the snake's y position is equal to 0 (at the the left limit) or the width of the screen
  # or if the snake head is found in snake[1] or snake[2] (the body)
  if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
    # kill the window
    curses.endwin()
    # and quit
    quit()

  # initialize a new head at the position of the original head
  new_head = [snake[0][0], snake[0][1]]

  # reassigning the new_head value depending on key value
  if key == curses.KEY_DOWN:
    new_head[0] += 1
  if key == curses.KEY_UP:
    new_head[0] -= 1
  if key == curses.KEY_LEFT:
    new_head[1] -= 1
  if key == curses.KEY_RIGHT:
    new_head[1] += 1

  #insert new head of snake
  snake.insert(0, new_head)

  # if snake head reaches food coords, set food to None
  if snake[0] == food:
    food = None
    while food is None:
      # generate new food at random y and x coords within bounds of screen height and width
      new_food = [
        random.randint(1, screen_height - 1),
        random.randint(1, screen_width - 1)
      ]
      # if the newly generated food coords are not within the snake coords, assign to food, else assign None
      food = new_food if new_food not in snake else None
    # add pi character to window at food coordinates
    window.addch(food[0], food[1], curses.ACS_PI)
  else:
    # remove the last array (tail coords) in the snake array and assign to tail
    tail = snake.pop()
    # replace with ' ' at the tail coords
    window.addch(tail[0], tail[1], ' ')
  # adding the snake to the board at y and x positions with ASC checkerboard character
  window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)