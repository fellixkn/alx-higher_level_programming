#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    args = sys.argv[1:]  # Exclude the script name from the arguments
    count = len(args)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")

    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")
        