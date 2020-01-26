import re
import getpass


def get_point_on_lower_case(password):
    if re.search(r'[a-z]', password):
        return 1
    return 0


def get_point_on_upper_case(password):
    if re.search(r'[A-Z]', password):
        return 1
    return 0


def get_point_on_numbers(password):
    if re.search(r'[0-9]', password):
        return 1
    return 0


def get_point_on_special_symbols(password):
    if re.search(r'[^a-zA-Z0-9]', password):
        return 1
    return 0


def get_point_on_len_password(password):
    return len(password) // 3 % 6


def get_point_on_no_date_format(password):
    if not re.search(r'(19\d{2})|(20\d{2})', password):
        return 1
    return 0


def get_point_password_notin_blacklist(password):
    blacklist = [
        '123456',
        'password',
        '12345678,'
        'qwerty',
        '123456789',
        '12345',
        '1234',
        '111111',
        '1234567',
        'dragon',
        '123123',
        'baseball',
        'abc123',
        'football',
        'monkey',
        'letmein',
        '696969',
        'shadow',
        'master',
        '666666',
    ]
    for word in blacklist:
        if word in password:
            return 0
    return 1


def get_password_strength(password):
    strength = 0
    strength += get_point_on_lower_case(password)
    strength += get_point_on_upper_case(password)
    strength += get_point_on_numbers(password)
    strength += get_point_on_special_symbols(password)
    strength += get_point_on_len_password(password)
    strength += get_point_on_no_date_format(password)
    strength += get_point_password_notin_blacklist(password)
    return strength


if __name__ == '__main__':
    user_password = getpass.getpass('Enter your password >')
    print('The strength is', get_password_strength(user_password))
