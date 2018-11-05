import secrets


def generate_key():
    """
    Generates a random 32 character string, and simulates
    storing this string in a database by writing it to db.txt
    """

    key = secrets.token_hex(16)
    f = open('db.txt', 'a')
    f.write(key + '\n')


generate_key()


def validate_key(key):
    """
    Takes a key string as an argument, and checks our
    'database' db.txt to see if the key is stored there.
    If so, returns True, if not, returns False
    """

    keys = open('db.txt', 'r').read()
    if key in keys:
        return True
    else:
        return False


print(validate_key('a5c4ebeddd3f50faf4fb1d7497476e37'))
