import random


def generate_activate_code(code_len: int) -> str:
    """
        Generate random activate code for user
    """
    digits = '0123456789'
    alfabet = 'abcdefghijklmnopqrstvwuxyz'
    symbols = digits + alfabet.upper() + alfabet
    code = [
        symbols[random.randrange(0, len(symbols))] for _ in range(code_len)
    ]
    return "".join(code)
