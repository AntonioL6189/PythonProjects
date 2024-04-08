import string
import getpass

def check_password_strength(password):
    strength = 0
    remarks = ''

    if len(password) == 0:
        remarks = 'Password cannot be empty.'
        return remarks

    lower_count = sum(1 for char in password if char in string.ascii_lowercase)
    upper_count = sum(1 for char in password if char in string.ascii_uppercase)
    num_count = sum(1 for char in password if char in string.digits)
    wspace_count = sum(1 for char in password if char == ' ')
    special_count = len(password) - (lower_count + upper_count + num_count + wspace_count)

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if len(password) >= 8:
        strength += 1

    if strength == 1:
        remarks = 'That\'s a very bad password. Change it as soon as possible.'
    elif strength == 2:
        remarks = 'That\'s a weak password. You should consider using a tougher password.'
    elif strength == 3:
        remarks = 'Your password is okay, but it can be improved.'
    elif strength == 4:
        remarks = 'Your password is hard to guess. But you could make it even more secure.'
    elif strength == 5:
        remarks = 'Now that\'s one hell of a strong password!!! Hackers don\'t have a chance guessing that password!'

    return remarks

def check_pwd(another_pw=False):
    while True:
        if another_pw:
            choice = input('Do you want to check another password\'s strength (y/n) : ')
        else:
            choice = input('Do you want to check your password\'s strength (y/n) : ')

        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            print('Exiting...')
            return False
        else:
            print('Invalid input...please try again.\n')

if __name__ == '__main__':
    print('==== Welcome to Password Strength Checker ====')
    check_pw = check_pwd()
    while check_pw:
        password = getpass.getpass('Enter the password: ')
        strength_remarks = check_password_strength(password)
        print(strength_remarks)
        check_pw = check_pwd(True)
