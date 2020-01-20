import re


def get_password_strength(password):
    strength = 0

    if re.search(r'[a-z]', password):
        strength += 1
    
    if re.search(r'[A-Z]', password):
        strength += 1
    
    if re.search(r'[0-9]', password):
        strength += 1
    
    #match special characters
    if re.search(r'[^a-zA-Z0-9]', password):
        strength += 1
    
    strength += len(password) // 3 % 6

    return strength



if __name__ == '__main__':
    user_password = input('Enter your password >')
    print("The strength is", get_password_strength(user_password))
