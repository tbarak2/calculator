from flask import Flask, jsonify, request
from core.calculator import Calculator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Load extensions
extensions_dir = "extensions"
calculator = Calculator()
calculator.load_extensions(extensions_dir)


@app.route("/operators", methods=["GET"])
def get_operators():
    operators = []
    for operator, extension in calculator.operations.items():
        is_data_needed = extension.get("is_data_needed", False)
        operators.append({"operator": operator, "is_data_needed": is_data_needed})

    return jsonify(operators)


@app.route("/calculate", methods=["POST"])
def calculate():
    payload = request.get_json()
    data = None
    operator = payload["operator"]
    operand1 = payload["operand1"]
    operand2 = payload["operand2"]
    result_extension = payload.get("result_extension")
    if "data" in payload:
        data = payload["data"]
    result = calculator.calculate(operator, operand1, operand2, data, result_extension)
    return jsonify(result)


if __name__ == "__main__":
    app.run()
