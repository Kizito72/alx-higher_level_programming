#!/usr/bin/python3


def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(a, b))
if __name__ == "__main__":
    # You can include test cases or additional code that should
    # only run when the script is executed directly.
    pass
