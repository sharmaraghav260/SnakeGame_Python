import random
import curses

# Initialize the screen
s = curses.initscr()

# Hide the cursor
curses.curs_set(0)

# Get screen width and height
sh, sw = s.getmaxyx()

# Create a new window starting top left
w = curses.newwin(sh, sw, 0, 0)

# Accept keypad input
w.keypad(1)

# Refresh every 100 ms
w.timeout(100)

# Snake's initial position
snk_x = sw/4
snk_y = sh/2

# Initial size 3 snake
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# Initial position of the food and add to screen
food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

# Snake goes right initially
key = curses.KEY_RIGHT

# Infinite loop for every movement of the snake
while True:
    # Fetch next key and update accordingly
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Check if person has lost the game
    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    
    # Figure out next head according to the key pressed
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    # Determine if snake eats the food
    if snake[0] == food:
        food = None
        while food is None:
            n_food = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = n_food if n_food not in snake else None

        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], " ")

    # Add the head of the snake to the board
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)