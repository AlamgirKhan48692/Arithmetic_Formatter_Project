
def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        operand1, operator, operand2 = parts

        # Check for valid operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check that operands contain only digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check operand length
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the width of the problem (max length of operands + 2)
        width = max(len(operand1), len(operand2)) + 2

        # Prepare each line
        first_line.append(operand1.rjust(width))
        second_line.append(operator + operand2.rjust(width - 1))
        dash_line.append("-" * width)

        # Optional answer line
        if display_answers:
            result = str(eval(operand1 + operator + operand2))
            answer_line.append(result.rjust(width))

    # Join all parts with four spaces
    arranged_problems = (
        "    ".join(first_line) + "\n" +
        "    ".join(second_line) + "\n" +
        "    ".join(dash_line)
    )

    if display_answers:
        arranged_problems += "\n" + "    ".join(answer_line)

    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43",
                            "123 + 49"], True))

print('------------------------------------------------------')

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999",
                            "523 - 49"], True))