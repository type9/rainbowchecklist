"""coding=utf-8."""

checklist = list()
checklist.append('Blue')
checklist.append('Orange')


# Create
def create(item):
    checklist.append(item)


# Read
def read(index):
    item = checklist[index]
    print(item)


# Update
def update(index, item):
    checklist[index] = item


# Destroy
def destroy(index):
    checklist.pop(index)


# Mark completed
def completed(index):
    temp = ""
    temp = checklist[index]
    checklist[index] = "√" + temp


# Lists all items
def list_all_items():
    index = 0
    for list_item in checklist:
        print("[" + str(index) + "]" + list_item)
        index = index + 1


def user_input(prompt):
    user_input = input(prompt)
    return user_input


# Multi input select function
def select(code_letter):
    # Create item
    if code_letter == "A":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif code_letter == "R":
        item_index = user_input("Index Number?: ")
        read(int(item_index))

    # Print all items
    elif code_letter == "P":
        list_all_items()

    # Print all items
    elif code_letter == "Q":
        return False

    # Destroy item
    elif code_letter == "D":
        item_index = user_input("Index Number?: ")
        destroy(int(item_index))

    # Change item
    elif code_letter == "U":
        item_index = user_input("Index to change?: ")
        replace_item = user_input("Item to replace with?: ")
        update(int(item_index), replace_item)

    # Marks as completed
    elif code_letter == "C":
        item_index = user_input("Index to mark?: ")
        completed(int(item_index))

    # Incorrect Code
    else:
        print("Uknown Code")
    return True


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1))

    list_all_items()

# MAIN


test()

running = True
while running:
    selection = user_input(
        "A > Add to list\nR > Read item at index\nP > Display list\nD > Remove"
        " item\nU > Change item at index\nC > Mark as completed\nQ > To quit\n"
    )
    running = select(selection)
