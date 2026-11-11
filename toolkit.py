import random


# Tool 1: Simple Calculator
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Choose an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("You cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: To-Do List Manager
def todo_list_manager():
    tasks = []

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter your task: ")
            tasks.append(task)
            print(f"Task added: {task}")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your task list is empty.")
            else:
                print("\nYour Tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Removed: {removed_task}")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


# Tool 3: Number Guessing Game
def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    print("Guess a number between 1 and 10.")

    secret_number = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 10:
                print("Please choose a number between 1 and 10.")
            elif guess < secret_number:
                print("Too low. Try again!")
            elif guess > secret_number:
                print("Too high. Try again!")
            else:
                print("Congratulations! You guessed correctly.")
                break

        except ValueError:
            print("Please enter a valid whole number.")


# Main Menu
def main():
    while True:
        print("\nWelcome to My Personal Mini-Toolkit!")
        print("\nPlease choose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List Manager")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            calculator()

        elif choice == "2":
            todo_list_manager()

        elif choice == "3":
            number_guessing_game()

        elif choice == "4":
            print("Thank you for using My Personal Mini-Toolkit. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()