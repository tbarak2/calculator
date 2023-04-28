operator = "complex_exp"
is_data_required = True


def calculate(operand1, operand2, data=None):
    expression = data.get("expression")
    result = eval(expression)
    return {"result": result}


def is_data_needed():
    return is_data_required
