# calculator.py
from core.operations import Operations
import importlib
import os


class Calculator:
    def __init__(self):
        self.operations = {
            "+": {"function": Operations.add, "is_data_needed": False},
            "-": {"function": Operations.subtract, "is_data_needed": False},
            "*": {"function": Operations.multiply, "is_data_needed": False},
            "/": {"function": Operations.divide, "is_data_needed": False},
        }

    def load_extensions(self, extensions_dir):
        extensions = [
            filename.split(".")[0]
            for filename in os.listdir(extensions_dir)
            if filename.endswith(".py")
        ]
        for extension in extensions:
            if extension != "__init__":
                module = importlib.import_module(f"extensions.{extension}")
                if hasattr(module, "calculate"):
                    self.add_extension(extension, module)

    def add_extension(self, extension_name, module):
        if hasattr(module, "operator"):
            operator = module.operator
            if operator not in self.operations:
                self.operations[operator] = {"function": module.calculate}
                if hasattr(module, "is_data_needed"):
                    self.operations[operator][
                        "is_data_needed"
                    ] = module.is_data_needed()

    def calculate(self, operator, operand1, operand2, data=None):
        operation = self.operations.get(operator)
        if operation:
            function = operation["function"]
            if data is None:
                return function(operand1, operand2)
            else:
                return function(operand1, operand2, data)
        else:
            return {"error": "Invalid operator"}
