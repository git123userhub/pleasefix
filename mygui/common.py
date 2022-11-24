def is_char(arg):
    return len(arg) == 1 and isinstance(arg, str)

def is_str(arg):
    return len(arg) > 1 and isinstance(arg, str)
