from pathlib import Path

import inspect
import ast

from app.main import calculate_profit

from app import main

BASE_DIR = Path(__file__).resolve().parent.parent


def test_should_be_declared():
    assert (
        hasattr(main, "calculate_profit") is True
    ), "Function 'calculate_profit' should be declared."


def test_function_should_return_none():
    assert (
        calculate_profit(f"{BASE_DIR}/app/trades.json") is None
    ), "Function 'calculate_profit' should return None"


def test_float_should_not_use():
    code = inspect.getsource(calculate_profit)
    parsed_code = ast.parse(code)
    assert "float" not in ast.dump(parsed_code), (
        "You should not use 'float()' inside 'calculate_profit', "
        "because accuracy will be lost."
    )


def test_what_function_should_use():
    code = inspect.getsource(calculate_profit)
    parsed_code = ast.parse(code)

    assert "Decimal" in ast.dump(
        parsed_code
    ), "You should use 'Decimal()' inside 'calculate_profit'"
    assert "open" in ast.dump(
        parsed_code
    ), "You should use 'open()' inside 'calculate_profit'"
    assert "dump" in ast.dump(
        parsed_code
    ), "You should use 'dump()' inside 'calculate_profit'"
    assert "load" in ast.dump(
        parsed_code
    ), "You should use 'load()' inside 'calculate_profit'"
    assert "json" in ast.dump(
        parsed_code
    ), "You should use 'json' module inside 'calculate_profit'"


def test_create_profit_file():
    expected = '{\n  "earned_money": "49.8176904",\n  "matecoin_account": "0.00007"\n}'

    with open(f"{BASE_DIR}/profit.json") as actual:
        assert actual.read() == expected
