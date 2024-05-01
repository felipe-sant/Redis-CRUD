def print_decode(text: str):
    try:
        print(text.decode())
    except AttributeError:
        print(text)
