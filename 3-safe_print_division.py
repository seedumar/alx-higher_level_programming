#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        jm = a / b
    except (TypeError, ZeroDivisionError):
        jm = None
    finally:
        print("Inside result: {}".format(jm))
    return jm
