import random
import string

def generate_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
