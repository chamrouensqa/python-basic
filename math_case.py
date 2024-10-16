user_action_list = []
while True:
    print("Add, Show, Exit your To-Do-Task: ")
    user_action = input()

    match user_action:
        case 'Add':
            print("Enter your new task : ")
            new_add_task = input()
            user_action_list.append(new_add_task)

        case 'Show':
            for task in user_action_list:
                print(task)
        case 'Exit':
            break
        case _:
            print("Invalid input")
            break

print(user_action_list)