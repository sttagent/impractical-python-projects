

def main():
    key = {}
    print("Enter route cipher key. Press Enter"
          " without answer to quit.")
    while True:
        column = input("Column number: ")
        if not column:
            break
        direction = input("Direction (up/down): ")
        if not direction:
            break

        input_is_valid = validate_input(column, direction)
        if input_is_valid:
            column_int, direction_int = convert_input_to_int(column, direction)
            key[column_int] =  direction_int
        else:
            print("Invalid input!")

    print(f"key: {key}")


def validate_input(column, direction):
    valid_directions = {'up', 'down'}
    if column.isnumeric() and direction in valid_directions:
        is_valid = True
    else:
        is_valid = False

    return is_valid


def convert_input_to_int(column, direction):
    column_int = int(column)
    if direction == "up":
        direction_int = 1
    elif direction == 'down':
        direction_int = -1

    return column_int, direction_int


if __name__ == '__main__':
    main()
