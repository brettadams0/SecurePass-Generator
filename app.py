import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True, exclude_ambiguous=True):
    # Define character sets
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    special_chars = string.punctuation

    # Exclude ambiguous characters
    if exclude_ambiguous:
        ambiguous_chars = 'l1IO0'
        for char in ambiguous_chars:
            uppercase_chars = uppercase_chars.replace(char, '')
            lowercase_chars = lowercase_chars.replace(char, '')
            digit_chars = digit_chars.replace(char, '')
            special_chars = special_chars.replace(char, '')

    # Initialize the character pool based on user preferences
    char_pool = ''
    if use_uppercase:
        char_pool += uppercase_chars
    if use_lowercase:
        char_pool += lowercase_chars
    if use_digits:
        char_pool += digit_chars
    if use_special:
        char_pool += special_chars

    # Generate the password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

if __name__ == "__main__":
    # Example usage
    password_length = 16
    generated_password = generate_password(length=password_length)
    print(f"Generated password: {generated_password}")
