INCREMENT_NUMBER = 2


def print_tree(tree_level):
    current_level = 1
    lever_leaves_number = 1
    white_sapce_number = tree_level - 1
    while current_level <= tree_level:
        print(" " * white_sapce_number, end="")
        for x in range(lever_leaves_number):
            print("*", end="")
        print()
        white_sapce_number -= 1
        lever_leaves_number += INCREMENT_NUMBER
        current_level += 1


def print_opposite_tree(tree_level):
    current_level = 1
    lever_leaves_number = 1
    white_sapce_number = tree_level - 1
    while current_level <= tree_level:
        print(" " * white_sapce_number, end="")
        for x in range(lever_leaves_number):
            print("*", end="")
        print()
        white_sapce_number -= 1
        lever_leaves_number += INCREMENT_NUMBER
        current_level += 1


print_tree(10)
