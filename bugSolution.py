def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
            data = f.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    return data