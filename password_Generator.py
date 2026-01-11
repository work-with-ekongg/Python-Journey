import random

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
min_length = 6
max_length = 12

def generate_password():
    desired_length = input(f"Enter desired password length ({min_length}-{max_length}): ")
    if not desired_length.isdigit():
        print("Please enter a valid number.")
        return
    
    desired_length = int(desired_length)
    while desired_length < min_length or desired_length > max_length:
        print(f"Password length must be between {min_length} and {max_length}.")
        desired_length = int(input(f"Enter desired password length ({min_length}-{max_length}): "))
    
    password = random.choices(alphabets + numbers + special_characters, k=desired_length)
    random.shuffle(password)
    password_str = ''.join(password)    
    print(f"Generated password: {password_str}")

if __name__ == "__main__":
    generate_password()