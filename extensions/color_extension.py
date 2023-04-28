operator = "color="


def calculate(operand1, operand2):
    result = operand1 + operand2
    color = "green" if result % 2 == 0 else "red"
    return {"result": result, "color": color}
