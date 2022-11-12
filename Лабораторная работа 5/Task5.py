import string
from random import sample


def get_random_password(n: int = 8) -> str:
    return str(sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, n))


print(get_random_password())
