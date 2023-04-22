#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    n_list = []
    for i in range(list_length):
        try:
            jm = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            jm = 0
        except ZeroDivisionError:
            print("division by 0")
            jm = 0
        except IndexError:
            print("out of range")
            jm = 0
        finally:
            n_list.append(jm)
    return (n_list)
