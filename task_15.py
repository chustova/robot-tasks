#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if not wall_is_beneath():
        if not wall_is_on_the_right():
            move_right(n=9)
            move_down(n=9)
        else:
            move_left(n=9)
            move_down(n=9)
    else:
        if not wall_is_on_the_right():
            move_right(n=9)
            move_up(n=9)
        else:
            move_left(n=9)
            move_up(n=9)




if __name__ == '__main__':
    run_tasks()
