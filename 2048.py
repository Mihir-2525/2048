import numpy as np
import random
import keyboard
import os

# Return Check to user get 2048 Number  
def win(arr):
    for i in arr:
        for j in i:
            if j==2048:return True

# Check if the array is empty or not
def check(arr):
    # np.all() returns True if the array doesn't have any 0 value in any element
    return not np.all(arr)

# Horizontally check for duplicates
def check_Horizontal(x):
    for i in x:
        for j in range(len(i)-1):
            if i[j] == i[j+1]:
                return True

# Vertically check for duplicates
def check_Vertical(x):
    for i in range(len(x)-1):
        for j in range(len(x)):
            if x[i,j] == x[i+1,j]:
                return True

# Add a new element to the array
def new_var(arr, size):
    # Check if the array doesn't contain zero, then don't add any new elements
    while check(arr):
        # Set random dimensions
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        if arr[x, y] == 0:
            arr[x, y] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 8])
            break

# <---
def right_to_left(arr, size):
    for i in range(size):
        # shift all non-zero elements to the left
        non_zero_elements = [num for num in arr[i] if num != 0]
        # merge elements if they are the same and next to each other
        merged_elements = []
        skip = False
        for j in range(len(non_zero_elements)):
            if skip:
                skip = False
                continue
            if j < len(non_zero_elements) - 1 and non_zero_elements[j] == non_zero_elements[j + 1]:
                merged_elements.append(non_zero_elements[j] * 2)
                skip = True
            else:
                merged_elements.append(non_zero_elements[j])
        # Fill the remaining spaces with zeros
        merged_elements.extend([0] * (size - len(merged_elements)))
        arr[i] = merged_elements

# --->
def left_to_right(arr, size):
    for i in range(size):
        # shift all non-zero elements to the right
        non_zero_elements = [num for num in arr[i] if num != 0]
        # merge elements if they are the same and next to each other
        merged_elements = []
        skip = False
        for j in range(len(non_zero_elements) - 1, -1, -1):
            if skip:
                skip = False
                continue
            if j > 0 and non_zero_elements[j] == non_zero_elements[j - 1]:
                merged_elements.append(non_zero_elements[j] * 2)
                skip = True
            else:
                merged_elements.append(non_zero_elements[j])
        # Fill the remaining spaces with zeros
        merged_elements = [0] * (size - len(merged_elements)) + merged_elements[::-1]
        arr[i] = merged_elements

# ^
# |
def bottom_to_top(arr, size):
    for j in range(size):
        # shift all non-zero elements upwards
        non_zero_elements = [arr[i][j] for i in range(size) if arr[i][j] != 0]
        # merge elements if they are the same and next to each other
        merged_elements = []
        skip = False
        for i in range(len(non_zero_elements)):
            if skip:
                skip = False
                continue
            if i < len(non_zero_elements) - 1 and non_zero_elements[i] == non_zero_elements[i + 1]:
                merged_elements.append(non_zero_elements[i] * 2)
                skip = True
            else:
                merged_elements.append(non_zero_elements[i])
        # Fill the remaining spaces with zeros
        merged_elements = merged_elements + [0] * (size - len(merged_elements))
        for i in range(size):
            arr[i][j] = merged_elements[i]
    
# |
# V
def top_to_bottom(arr, size):
    for j in range(size):
        # shift all non-zero elements downwards
        non_zero_elements = [arr[i][j] for i in range(size) if arr[i][j] != 0]
        # merge elements if they are the same and next to each other
        merged_elements = []
        skip = False
        for i in range(len(non_zero_elements) - 1, -1, -1):
            if skip:
                skip = False
                continue
            if i > 0 and non_zero_elements[i] == non_zero_elements[i - 1]:
                merged_elements.append(non_zero_elements[i] * 2)
                skip = True
            else:
                merged_elements.append(non_zero_elements[i])
        # Fill the remaining spaces with zeros
        merged_elements = [0] * (size - len(merged_elements)) + merged_elements[::-1]
        for i in range(size):
            arr[i][j] = merged_elements[i]

# Print data on console display
def print_board(array):
    # Print the game board
    # ╔═══════════════╦═══════════════╦═══════════════╦═══════════════╗
    print("╔"+"═"*15,end="")
    for i in range(len(array)-1):
        print("╦"+"═"*15,end="")
    print("╗")
    # Print single line
    for i in range(len(array)):
        # ║               ║               ║               ║               ║
        print("║",end="")
        for j in range(len(array)):
            print("\t\t║",end="")
        print()
        # ║       x       ║       x       ║       x       ║       x       ║
        for j in range(len(array)):print("║\t"+str(array[i][j])+"\t",end="")
        print("║")
        # ║               ║               ║               ║               ║
        print("║",end="")
        for j in range(len(array)):
            print("\t\t║",end="")
        print()
        # ╠═══════════════╬═══════════════╬═══════════════╬═══════════════╣
        if not(i==len(array)-1):
            print("╠"+"═"*15,end="")
            for i in range(len(array)-1):
                print("╬"+"═"*15,end="")
            print("╣")
    # ╚═══════════════╩═══════════════╩═══════════════╩═══════════════╝
    print("╚"+"═"*15,end="")
    for i in range(len(array)-1):
        print("╩"+"═"*15,end="")
    print("╝")
  
def main():
    # x is the size of the array (i.e., if x = 3, then 'a' makes a 3x3 array)
    x = 4
    # Set the array (i.e., if x = 3, then 'a' makes a 3x3 empty (0) array)
    a = np.zeros(x*x, dtype=np.int32).reshape(x, x)
    new_var(a, x)
    print_board(a)
    while True:
        if (check(a) or check_Horizontal(a) or check_Vertical(a)):
            if win(a):
                os.system("cls")
                print_board(a)
                print("╔═══╗╔═══╗╔═╗─╔╗╔═══╗╔═══╗╔═══╗╔════╗╔╗─╔╗╔╗───╔═══╗╔════╗╔══╗╔═══╗╔═╗─╔╗╔═══╗")
                print("║╔═╗║║╔═╗║║║╚╗║║║╔═╗║║╔═╗║║╔═╗║║╔╗╔╗║║║─║║║║───║╔═╗║║╔╗╔╗║╚╣─╝║╔═╗║║║╚╗║║║╔═╗║")
                print("║║─╚╝║║─║║║╔╗╚╝║║║─╚╝║╚═╝║║║─║║╚╝║║╚╝║║─║║║║───║║─║║╚╝║║╚╝─║║─║║─║║║╔╗╚╝║║╚══╗")
                print("║║─╔╗║║─║║║║╚╗║║║║╔═╗║╔╗╔╝║╚═╝║──║║──║║─║║║║─╔╗║╚═╝║──║║───║║─║║─║║║║╚╗║║╚══╗║")
                print("║╚═╝║║╚═╝║║║─║║║║╚╩═║║║║╚╗║╔═╗║──║║──║╚═╝║║╚═╝║║╔═╗║──║║──╔╣─╗║╚═╝║║║─║║║║╚═╝║")
                print("╚═══╝╚═══╝╚╝─╚═╝╚═══╝╚╝╚═╝╚╝─╚╝──╚╝──╚═══╝╚═══╝╚╝─╚╝──╚╝──╚══╝╚═══╝╚╝─╚═╝╚═══╝")
                break
            key = keyboard.read_key()
            if key == "w" or key == "up":
                bottom_to_top(a, x)
            elif key == "s" or key == "down":
                top_to_bottom(a, x)
            elif key == "a" or key == "left":
                right_to_left(a, x)
            elif key == "d" or key == "right":
                left_to_right(a, x)
            elif key == "x":
                break
            else:
                print('Invalid key')
                continue
            new_var(a, x)
            os.system("cls")
            print_board(a)
        else:
            print("╔╗──╔╗╔═══╗╔╗─╔╗   ╔╗───╔═══╗╔═══╗╔═══╗   ╔════╗╔╗─╔╗╔═══╗   ╔═══╗╔═══╗╔═╗╔═╗╔═══╗")
            print("║╚╗╔╝║║╔═╗║║║─║║   ║║───║╔═╗║║╔═╗║║╔══╝   ║╔╗╔╗║║║─║║║╔══╝   ║╔═╗║║╔═╗║║║╚╝║║║╔══╝")
            print("╚╗╚╝╔╝║║─║║║║─║║   ║║───║║─║║║╚══╗║╚══╗   ╚╝║║╚╝║╚═╝║║╚══╗   ║║─╚╝║║─║║║╔╗╔╗║║╚══╗")
            print("─╚╗╔╝─║║─║║║║─║║   ║║─╔╗║║─║║╚══╗║║╔══╝   ──║║──║╔═╗║║╔══╝   ║║╔═╗║╚═╝║║║║║║║║╔══╝")
            print("──║║──║╚═╝║║╚═╝║   ║╚═╝║║╚═╝║║╚═╝║║╚══╗   ──║║──║║─║║║╚══╗   ║╚╩═║║╔═╗║║║║║║║║╚══╗")
            print("──╚╝──╚═══╝╚═══╝   ╚═══╝╚═══╝╚═══╝╚═══╝   ──╚╝──╚╝─╚╝╚═══╝   ╚═══╝╚╝─╚╝╚╝╚╝╚╝╚═══╝")
            break

if __name__ == "__main__":
    main()