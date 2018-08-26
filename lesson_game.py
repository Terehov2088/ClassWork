import random

GREETING = """
Enter data
    0 - rock
    1 - papper
    2 - scissors
    \'q\' for exit:
"""

ROCK = 0
PAPPER = 1
SCISSOR = 2

def from_code2_text(code):
    if code == ROCK:
        return 'ROCK'
    elif code == PAPPER:
        return 'PAPPER'
    elif code == SCISSOR:
        return 'SCISSOR'


def who_is_winner(pc_choice, user_choice):
    if pc_choice == ROCK and user_choice == SCISSOR:
        return False
    if pc_choice == PAPPER and user_choice == ROCK:
        return False
    if pc_choice == SCISSOR and user_choice == PAPPER:
        return False
    return True



def game():
    while True:
        input_data = input(GREETING)
        if input_data == 'q':
            break

        if not input_data.isnumeric():
            print('Invalid data')
            continue

        if not ROCK <= int(input_data) <= SCISSOR:
            print('Invalid data')
            continue

        pc_choise = random.randint(ROCK, SCISSOR)
        user_choice = int(input_data)
        print('PC choice: %s ' % from_code2_text(pc_choise))

        if pc_choise == user_choice:
            print('Tie')
        else:
            if who_is_winner(pc_choise, user_choice):
                print('User is winner: %s vs %s' %
                      (from_code2_text(pc_choise),
                       from_code2_text(user_choice)))
            else:
                print('PC is winner: %s vs %s' %
                      (from_code2_text(pc_choise),
                       from_code2_text(user_choice)))


game()