from typing import List, Dict

def checking_logic(problems:List) -> Dict:
    # If there are too many problems supplied to the function. The limit is five, anything more will return:
    error = False

    if len(problems) > 5:
        error = "Error: Too many problems."

    # Using dictionary to get a new data structure suitable for operations:
    splitted_problems = {}
    for index, problem in enumerate(problems):
        splitted_problems[index] = problem.split()

    # The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
    # Error: Operator must be '+' or '-'.
    for key, splitted_problem in splitted_problems.items():

        # Each number (operand) should only contain digits. Otherwise, the function will return:
        # Error: Numbers must only contain digits.
        try:
            int(splitted_problem[0])
            int(splitted_problem[2])
        except ValueError:
            error = "Error: Numbers must only contain digits."


        if splitted_problem[1] != '+' and splitted_problem[1] != '-':
            error = "Error: Operator must be '+' or '-'."


        # Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
        # Error: Numbers cannot be more than four digits.
        len(splitted_problem[0])
        len(splitted_problem[2])
        if len(splitted_problem[0]) > 4 or len(splitted_problem[2]) > 4:
            error = "Error: Numbers cannot be more than four digits."

        if isinstance(error, str):
            return error
        else:
            return splitted_problems


def formatting_output(splitted_problems:Dict, output_flag:bool) -> Dict:


    formatted_operations = {}
    # Compose first line:
    for index, splitted_problem in splitted_problems.items():
        # Check max length of the splitted_problems:
        numbers = [int(splitted_problem[0]), int(splitted_problem[2])]
        max_length = len(str(max(numbers)))
        # Number of dashes that will be created:
        number_of_dashes = max_length + 2

        first_line_whitespace = (number_of_dashes - len(splitted_problem[0])) * " "

        formatted_first_line = first_line_whitespace + splitted_problem[0]

        operand = splitted_problem[1]
        whitespace = (number_of_dashes - len(splitted_problem[2]) - 1) * " "
        formatted_second_line = operand + whitespace + splitted_problem[2]

        formatted_third_line = "-" * number_of_dashes

        temp_dict = {"first_line": formatted_first_line, "second_line": formatted_second_line, "third_line": formatted_third_line}

        if output_flag:

            if operand == "+":
                fourth_line_result = int(splitted_problem[0]) + int(splitted_problem[2])
                fourth_line_len = len(str(fourth_line_result))
                fourth_line_whitespace = (number_of_dashes - fourth_line_len) * " "
                formatted_fourth_line = fourth_line_whitespace + str(fourth_line_result)

            if operand == "-":
                fourth_line_result = int(splitted_problem[0]) - int(splitted_problem[2])
                fourth_line_len = len(str(fourth_line_result))
                fourth_line_whitespace = (number_of_dashes - fourth_line_len) * " "
                formatted_fourth_line = fourth_line_whitespace + str(fourth_line_result)

            temp_dict = {"first_line": formatted_first_line, "second_line": formatted_second_line, "third_line": formatted_third_line, "fourth_line": formatted_fourth_line}

        formatted_operations[index] = temp_dict


    # Final formatting:
    arranged_problems_dict = {}
    list_of_strings_first_line = []
    for index, formatted_operation in formatted_operations.items():
        list_of_strings_first_line.append(formatted_operation["first_line"] + 4 * " ")
    arranged_problems_dict["formatted_first_line"] = list_of_strings_first_line

    list_of_strings_second_line = []
    for index, formatted_operation in formatted_operations.items():
        list_of_strings_second_line.append(formatted_operation["second_line"] + 4 * " ")
    arranged_problems_dict["formatted_second_line"] = list_of_strings_second_line


    list_of_strings_third_line = []
    for index, formatted_operation in formatted_operations.items():
        list_of_strings_third_line.append(formatted_operation["third_line"] + 4 * " ")
    arranged_problems_dict["formatted_third_line"] = list_of_strings_third_line
      
    if output_flag:
        list_of_strings_fourth_line = []
        for index, formatted_operation in formatted_operations.items():
            list_of_strings_fourth_line.append(formatted_operation["fourth_line"] + 4 * " ")
        arranged_problems_dict["formatted_fourth_line"] = list_of_strings_fourth_line

    return arranged_problems_dict


def arithmetic_arranger(problems:List, output_flag:bool=False):

    # Checking if the problems that were supplied are correct:
    splitted_problems = checking_logic(problems)


    if isinstance(splitted_problems, dict): 
        arranged_problems_dict = formatting_output(splitted_problems, output_flag)

        if output_flag:
            arranged_problems = ''.join(arranged_problems_dict["formatted_first_line"]).rstrip() + "\n"\
                              + ''.join(arranged_problems_dict["formatted_second_line"]).rstrip() + "\n"\
                              + ''.join(arranged_problems_dict["formatted_third_line"]).rstrip() + "\n"\
                              + ''.join(arranged_problems_dict["formatted_fourth_line"]).rstrip()
            return arranged_problems
        else:
            arranged_problems = ''.join(arranged_problems_dict["formatted_first_line"]).rstrip() + "\n"\
                              + ''.join(arranged_problems_dict["formatted_second_line"]).rstrip() + "\n"\
                              + ''.join(arranged_problems_dict["formatted_third_line"]).rstrip()
            return arranged_problems
    else:
        return splitted_problems


