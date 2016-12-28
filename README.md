Old school Pong game

- Written in Python 3.4.3
- Using pygame 1.9.2b1

To instal pygame: From the Terminal of Command Prompt, run the following:

- python -m pip install --upgrade pip
- python -m pip install pygame

The player moves his or her paddle up and down by moving the mouse. The computer moves its paddle by following the ball.

The computer is given a random speed each time it moves its paddle.

Every third ball to paddle collision speeds up the ball and the computer's paddle slightly.

The game is not perfect. There is a bug once in a while where the ball gets stuck to a paddle or follows the top or bottom of the screen. Also, collision is not always detected.


