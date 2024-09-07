''' Missionaries and Cannibals program.'''

lb_M = 3
init_lb_M = 3
lb_M_temp = 3
lb_C = 3
init_lb_C = 3
lb_C_temp = 3
rb_M = 0
init_rb_M = 0
rb_M_temp = 0
rb_C = 0
init_rb_C = 0
rb_C_temp = 0
boat_location = "lb"
progress = False
violates_constraints = False


def move_l_to_r(m, c):
    print("14 move_l_to_r ", m, c)
    boat_location = "lb"
    global lb_M
    global lb_M_temp
    global lb_C
    global lb_C_temp
    global rb_M
    global rb_M_temp
    global rb_C
    global rb_C_temp
    if m > 0:
        lb_M_temp = lb_M - m
    else:
        lb_M_temp = lb_M
    if c > 0:
        lb_C_temp = lb_C - c
    else:
        lb_C_temp = lb_C

    # if lb_C_temp < lb_M_temp :
    #     lb_M = lb_M_temp
    #     lb_C = lb_C_temp

    if lb_C_temp > lb_M_temp and lb_M_temp > 0:
        lb_M_temp = lb_M
        lb_C_temp = lb_C
        print("34 Invalid move, Cannibals may not exceed Missinaries on any bank!")
    elif lb_C_temp <= lb_M_temp or lb_M_temp == 0:
        lb_M = lb_M_temp
        lb_C = lb_C_temp
        if rb_M <= 3:
            rb_M += m
        if rb_C <= 3:
            rb_C += c
        print(f"32 Left bank has {lb_M} missionaries and {lb_C} cannibals")
        print(f"33 Right bank has {rb_M} missionaries and {rb_C} cannibals")

    # elif rb_C_temp > rb_M_temp:
    #     print("36 Invalid move, Cannibals may not exceed Missinaries on any bank!")
    # else:
    #     lb_M = lb_M_temp
    #     lb_C = lb_C_temp
    #     if rb_M <= 3:
    #         rb_M += m
    #     if rb_C <= 3:
    #         rb_C += c
    #     print(f"32 Left bank has {lb_M} missionaries and {lb_C} cannibals")
    #     print(f"33 Right bank has {rb_M} missionaries and {rb_C} cannibals")
        # boat_location == "rb"


def move_r_to_l(m, c):
    print("39 move_r_to_l ", m, c)
    boat_location = "rb"
    global lb_M
    global lb_M_temp
    global lb_C
    global lb_C_temp
    global rb_M
    global rb_M_temp
    global rb_C
    global rb_C_temp
    if m == 0 and c > 0:
        pass
        # print("51 pass")
    elif m > 0 and rb_M == 0:
        print("53 Invalid move, there are no Missinaries on the right bank!")
    elif (m > 0) and ((rb_M - m == 0) or not (rb_C > (rb_M - m))):
        if rb_M > 0:
            rb_M -= m
        if lb_M < 3:
            lb_M += m
        print(f"56 Left bank has {lb_M} missionaries and {lb_C} cannibals")
        print(f"57 Right bank has {rb_M} missionaries and {rb_C} cannibals")
    if c == 0 and m > 0:
        pass
        # print("62 pass")
        # print("51 Invalid move, there are no Cannibals on the right bank!")
    elif c > 0 and rb_C == 0:
        print("56 Invalid move, there are no Cannibals on the right bank!")
    # elif c > 0 and rb_M > 0 and rb_C > rb_M:
    #     print("55 Invalid move, Cannibals may not exceed Missinaries on any bank!")
    elif c > 0:  # and rb_C <= rb_M
        if rb_M > 0:
            rb_M -= m
        if rb_C > 0:
            rb_C -= c
        if lb_M < 3:
            lb_M += m
        if lb_C < 3:
            lb_C += c
        print(f"79 Left bank has {lb_M} missionaries and {lb_C} cannibals")
        print(f"80 Right bank has {rb_M} missionaries and {rb_C} cannibals")
        boat_location = "lb"


''' Make lists of left_bank actions and right_bank actions. Write a function that
switches between left and right bank functions.'''
''' Write a function that checks violated_constraints and replace similar code with it.'''
''' Write a function that recognizes progress. For example， if the number of missionaries or cannibals on the right bank is greater than the initial value. 
Also, set an intermediate value to measure current progress.'''
''' Write a function that removes left_bank functions if they make no progress. Right_bank functions can often be useful even if the left_bank ones aren't. '''
''' Re-write the functions so they can iterate through 0 - 2 in a generic manner.
These are not valid options for Missionaries, but they are for cannibals.'''


def move_actions():
    # if boat_location == "lb":
    # move_l_to_r(1, 0)
    # move_r_to_l(1, 0)
    move_l_to_r(1, 1)
    move_r_to_l(1, 0)
    # or for the same effect use
    # move_l_to_r(0, 2)
    # move_r_to_l(0, 1)

    move_l_to_r(0, 2)
    move_r_to_l(0, 1)
    move_l_to_r(2, 0)
    move_r_to_l(1, 1)
    move_l_to_r(2, 0)
    move_r_to_l(0, 1)
    move_l_to_r(0, 2)
    move_r_to_l(0, 1)
    move_l_to_r(0, 2)
# elif boat_location == "rb":


if __name__ == '__main__':
    move_actions()
