# calculator

A simple calculator with the ability to add extensions

### Requirements

Using Pip to install
`pip install -r requierments.txt`

- blinker 1.6.2
- click 8.1.3
- colorama 0.4.6
- Flask 2.3.1
- Flask-Cors 3.0.10
- importlib-metadata 6.6.0
- itsdangerous 2.1.2
- Jinja2 3.1.2
- MarkupSafe 2.1.2
- six 1.16.0
- Werkzeug 2.3.1
- zipp 3.15.0

### Using

For simple run the following command:
`python main.py`

### Description

The project build in a simple way.
.
├── main.py
├── client
│ └── index.html
├── core
│ ├── calculator.py
│ ├── operations.py
├── extexnsions
│ ├── power_extesoin.py
│ ├── expression_extension.py
│ ├── complex_expression_extension.py
│ ├── response_extension_color.py
└── ...

### Adding extension

To add extension you need to rember yow things.

1.  Extension for calculation.
2.  Extension for response.

- Calculation extension.
  The format of calculation extension should include one 2 functions.
  `def calculate(operand1, operand2, data=None)` It should return result.
  there is an option to 3 things:

  - Another function: `def is_data_needed():` That return to the client if there is a need for extra data.
  - operator - They oprator that going to be showen if there is any.
  - is_data_required - Not a must.

  2 Examples:

  ```
    operator = "**"
    def calculate(operand1, operand2):
        result = operand1**operand2
        return {"result": result}
  ```

  ```
    operator = "complex_exp"
    is_data_required = True


    def calculate(operand1, operand2, data=None):
        expression = data.get("expression")
        result = eval(expression)
        return {"result": result}


    def is_data_needed():
        return is_data_required
  ```

- Response extension
  This extension is a bit more simple then the calculate extensions, all its do is getting the result from calculation and formating the response.
  It should contain one method: `def format_result(result)` .
  Example:

  ```
  def format_result(result):
      color = "red"
      if result % 2 == 0:
          color = "green"
      response = {"result": result, "color": color}
      return response

  ```

### Client

In this example (the code) the client side is coding in vannila html with js.
It is not ready and not following all functionality.
