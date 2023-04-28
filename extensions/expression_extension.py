operator = "expression"
required_data = True


def calculate(operand1, operand2, data=None):
    # expression = data.get("expression")
    # variables = data.get("variables", {})
    # result = eval(expression, variables)
    # return {"result": result}
    if data is None:
        return {"error": "Missing data for expression calculation"}

    expression = data.get("expression")
    if expression is None:
        return {"error": "Missing expression in data"}

    variables = {"operand1": operand1, "operand2": operand2}

    try:
        result = eval(expression, variables)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
