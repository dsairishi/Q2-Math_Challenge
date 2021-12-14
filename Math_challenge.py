# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


# :param string_array: the array of string to be printed
# :param delimiter: the delimiter that needs to be appended for above array of strings
# print_in_console prints the array of strings with delimiter
def print_in_console(string_array, delimiter="\n"):
    for string in string_array:
        print(string, end=delimiter)


# :param result_set the final result set that needs to be evaluated
# evaluate_result prints the evaluated result from result_set
def evaluvate_result(result_set):
    correct_answers = 0
    print("Your results are as follows :")
    for question_no in result_set.keys():
        if result_set[question_no]['user_result'] == result_set[question_no]['system_result']:
            correct_answers += 1
            print_in_console([question_no, ". (✓) "], "")
        else:
            print_in_console([question_no, ". (x) "], "")
    print()
    print_in_console(["You have answered ", correct_answers, " out of ", len(result_set.keys()), " correctly."], "")
    print()


# param:operation the operation that user has chosen
# param:question_no the question number
# returns: result of randomly generated operands with operation
# generate_equation generates operands for given operation randomly and returns result
def generate_equation(operation, question_no):
    result = 0
    if operation == "1":  # addition
        operand1 = random.randint(0, 1000)
        operand2 = random.randint(0, 1000)
        print_in_console([question_no, ". ", operand1, " + ", operand2, " = "], "")
        result = operand1 + operand2
    elif operation == "2":  # substation
        operand1 = random.randint(500, 1000)
        operand2 = random.randint(0, operand1)
        print_in_console([question_no, ". ", operand1, " - ", operand2, " = "], "")
        result = operand1 - operand2
    elif operation == "3":  # multiplication
        operand1 = random.randint(0, 1000)
        operand2 = random.randint(0, 1000)
        print_in_console([question_no, ". ", operand1, " * ", operand2, " = "], "")
        result = operand1 * operand2
    elif operation == "4":  # division
        operand2 = random.randint(0, 1000)
        operand1 = operand2 * random.randint(1, 100)
        print_in_console([question_no, ". ", operand1, " / ", operand2, " = "], "")
        result = int(operand1 / operand2)

    return result


# :param no_of_questions: the no of question to answer
# Start_math_challenge will loop for no_of_questions and stores
# answers in result_set
def start_math_challenge(no_of_questions=10):
    print_in_console(["###  welcome to the math challenge ###"])  # Press Ctrl+F8 to toggle the breakpoint.
    is_valid_selection = False
    while not is_valid_selection:
        print_menu()
        operation = input()
        if operation in ["1", "2", "3", "4"]:
            question_no = 1
            is_valid_selection = True
            result_set = {}
            while question_no <= no_of_questions:
                system_result = generate_equation(operation, question_no)
                user_result = input()
                result_set[question_no] = {"user_result": user_result, "system_result": str(system_result)}
                question_no += 1
            evaluvate_result(result_set)
        else:
            print("Please select a valid operation.")


# print_menu prints menu
def print_menu():
    print_in_console(
        [
            "Select one of the following operation",
            "1. Addition",
            "2. Subtraction",
            "3. Multiplication",
            "4. Division"
        ]
    )


if __name__ == '__main__':
    replay = True
    while replay:
        start_math_challenge()
        print_in_console(["Do you want to replay ? press y to continue or any other key to exit"])
        if input() == "y":
            replay = True
        else:
            replay = False
