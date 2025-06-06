import random
import string
import argparse

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument('--length', type=int, default=12, help='Length of the password')
    args = parser.parse_args()

    password = generate_password(args.length)
    print(f"Generated password: {password}")
