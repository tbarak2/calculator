def format_result(result):
    color = "red"
    if result % 2 == 0:
        color = "green"
    response = {"result": result, "color": color}
    return response
