# Random Python Code - pandage

import random
import string

def generate_random_string(length=10):
    """Generate a random string of specified length"""
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))

def generate_random_numbers(count=5, min_val=1, max_val=100):
    """Generate a list of random numbers"""
    return [random.randint(min_val, max_val) for _ in range(count)]

if __name__ == "__main__":
    print("Random String:", generate_random_string(15))
    print("Random Numbers:", generate_random_numbers(10))
