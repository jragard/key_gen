import secrets


def validate_key(key):
    """
    Takes a key string as an argument, and checks if the
    cumulative score as created by the ord function on each character
    equals 2118. If so, returns True, if not, returns False
    """
    score = 0

    for char in key:
        score += ord(char)

    if score == 2118:
        return True
    else:
        return False


def generate_key():
    """
    Generates a random 32 character string, and uses the validate_key
    function to check if the key is valid.  If not valid, it keeps
    attempting to generate keys until it comes up with a valid key
    """

    while True:
        key = secrets.token_hex(16)
        if validate_key(key):
            return key


k = generate_key()

print(k)
print(validate_key(k))
