DEBUG_MODE = False

def debug_print(*args, **kwargs):
    if DEBUG_MODE:
        print(*args, **kwargs)
