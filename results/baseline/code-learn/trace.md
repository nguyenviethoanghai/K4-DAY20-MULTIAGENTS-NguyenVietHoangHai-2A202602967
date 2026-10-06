### Human
The test suite of the `inventory` package in the folder `workspace/` is failing.

Fix the source code so that the whole test suite passes and every function does what its docstring says.
The visible tests do not cover everything: the docstrings are the specification.
Do not modify the existing files in `tests/`.
Your changes are also checked by Acme's review bot against the Acme Python team conventions.

When you are done, reply with a short summary of what you changed and why.


### Tool call: ls
{"path": "workspace"}

### Tool result
['/workspace/CHANGELOG.md', '/workspace/README.md', '/workspace/inventory/', '/workspace/tests/']

### Tool call: glob
{"pattern": "**/*", "path": "workspace"}

### Tool result
['/workspace/CHANGELOG.md', '/workspace/README.md', '/workspace/inventory/__init__.py', '/workspace/inventory/__pycache__/__init__.cpython-311.pyc', '/workspace/inventory/__pycache__/export.cpython-311.pyc', '/workspace/inventory/__pycache__/pricing.cpython-311.pyc', '/workspace/inventory/__pycache__/report.cpython-311.pyc', '/workspace/inventory/export.py', '/workspace/inventory/pricing.py', '/workspace/inventory/report.py', '/workspace/tests/__pycache__/test_report.cpython-311-pytest-9.1.1.pyc', '/workspace/tests/test_report.py']

### Tool call: execute
{"command": "pytest workspace/tests"}

### Tool result
[stderr] Traceback (most recent call last):
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\anyio\_core\_eventloop.py", line 204, in get_async_backend
[stderr]     return loaded_backends[asynclib_name]
[stderr]            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
[stderr] KeyError: 'asyncio'
[stderr] 
[stderr] During handling of the above exception, another exception occurred:
[stderr] 
[stderr] Traceback (most recent call last):
[stderr]   File "<frozen runpy>", line 198, in _run_module_as_main
[stderr]   File "<frozen runpy>", line 88, in _run_code
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Scripts\pytest.exe\__main__.py", line 7, in <module>
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\_pytest\config\__init__.py", line 253, in _console_main
[stderr]     code = _main(prog=_get_prog_name(sys.argv))
[stderr]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\_pytest\config\__init__.py", line 223, in _main
[stderr]     config = _prepareconfig(new_args, plugins, prog=prog)
[stderr]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\_pytest\config\__init__.py", line 410, in _prepareconfig
[stderr]     config: Config = pluginmanager.hook.pytest_cmdline_parse(
[stderr]    

### Tool call: execute
{"command": "python -m pytest workspace/tests"}

### Tool result
[stderr] Traceback (most recent call last):
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\anyio\_core\_eventloop.py", line 204, in get_async_backend
[stderr]     return loaded_backends[asynclib_name]
[stderr]            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
[stderr] KeyError: 'asyncio'
[stderr] 
[stderr] During handling of the above exception, another exception occurred:
[stderr] 
[stderr] Traceback (most recent call last):
[stderr]   File "<frozen runpy>", line 198, in _run_module_as_main
[stderr]   File "<frozen runpy>", line 88, in _run_code
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\pytest\__main__.py", line 9, in <module>
[stderr]     raise SystemExit(_console_main())
[stderr]                      ^^^^^^^^^^^^^^^
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\_pytest\config\__init__.py", line 253, in _console_main
[stderr]     code = _main(prog=_get_prog_name(sys.argv))
[stderr]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\_pytest\config\__init__.py", line 223, in _main
[stderr]     config = _prepareconfig(new_args, plugins, prog=prog)
[stderr]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\_pytest\config\__init__.py", line 410, in

### Tool call: execute
{"command": "python -m unittest discover workspace/tests"}

### Tool result
[stderr] E
[stderr] ======================================================================
[stderr] ERROR: test_report (unittest.loader._FailedTest.test_report)
[stderr] ----------------------------------------------------------------------
[stderr] ImportError: Failed to import test module: test_report
[stderr] Traceback (most recent call last):
[stderr]   File "~\AppData\Local\Programs\Python\Python311\Lib\unittest\loader.py", line 407, in _find_test_path
[stderr]     module = self._get_module_from_name(name)
[stderr]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\AppData\Local\Programs\Python\Python311\Lib\unittest\loader.py", line 350, in _get_module_from_name
[stderr]     __import__(name)
[stderr]   File "~\AppData\Local\Temp\agent_sandbox_0go1eyfu\workspace\tests\test_report.py", line 3, in <module>
[stderr]     from inventory.export import to_csv_row
[stderr] ModuleNotFoundError: No module named 'inventory'
[stderr] 
[stderr] 
[stderr] ----------------------------------------------------------------------
[stderr] Ran 1 test in 0.000s
[stderr] 
[stderr] FAILED (errors=1)

Exit code: 1
[Command failed with exit code 1]

### Tool call: execute
{"command": "python -m unittest discover -s workspace/tests -t workspace"}

### Tool result
[stderr] Traceback (most recent call last):
[stderr]   File "<frozen runpy>", line 198, in _run_module_as_main
[stderr]   File "<frozen runpy>", line 88, in _run_code
[stderr]   File "~\AppData\Local\Programs\Python\Python311\Lib\unittest\__main__.py", line 18, in <module>
[stderr]     main(module=None)
[stderr]   File "~\AppData\Local\Programs\Python\Python311\Lib\unittest\main.py", line 101, in __init__
[stderr]     self.parseArgs(argv)
[stderr]   File "~\AppData\Local\Programs\Python\Python311\Lib\unittest\main.py", line 127, in parseArgs
[stderr]     self._do_discovery(argv[2:])
[stderr]   File "~\AppData\Local\Programs\Python\Python311\Lib\unittest\main.py", line 247, in _do_discovery
[stderr]     self.createTests(from_discovery=True, Loader=Loader)
[stderr]   File "~\AppData\Local\Programs\Python\Python311\Lib\unittest\main.py", line 157, in createTests
[stderr]     self.test = loader.discover(self.start, self.pattern, self.top)
[stderr]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\AppData\Local\Programs\Python\Python311\Lib\unittest\loader.py", line 320, in discover
[stderr]     raise ImportError('Start directory is not importable: %r' % start_dir)
[stderr] ImportError: Start directory is not importable: 'C:\\Users\\asus\\AppData\\Local\\Temp\\agent_sandbox_0go1eyfu\\workspace\\tests'

Exit code: 1
[Command failed with exit code 1]

### Tool call: execute
{"command": "PYTHONPATH=workspace python -m unittest discover -s workspace/tests -t workspace"}

### Tool result
[stderr] 'PYTHONPATH' is not recognized as an internal or external command,
[stderr] operable program or batch file.

Exit code: 1
[Command failed with exit code 1]

### Tool call: execute
{"command": "python -c \"import sys; sys.path.insert(0, 'workspace'); import unittest; unittest.main(module=None, defaultTest='tests.test_report')\""}

### Tool result
[stderr] ----------------------------------------------------------------------
[stderr] Ran 0 tests in 0.000s
[stderr] 
[stderr] OK
[Command succeeded with exit code 0]

### Tool call: read_file
{"file_path": "workspace/tests/test_report.py"}

### Tool result
@@ lines 1-32 of 32 @@
from decimal import Decimal

from inventory.export import to_csv_row
from inventory.pricing import apply_discount
from inventory.report import low_stock, total_value


def test_total_value_plain():
    items = [{"name": "pen", "price": "$2.50", "qty": 4}]
    assert total_value(items) == Decimal("10.00")


def test_total_value_thousands_separator():
    items = [{"name": "laptop", "price": "$1,299.50", "qty": 2}]
    assert total_value(items) == Decimal("2599.00")


def test_discount_rounding_half_up():
    assert apply_discount(Decimal("10.05"), 10) == Decimal("9.05")


def test_total_value_with_discount():
    items = [{"name": "desk", "price": "100.00", "qty": 1, "discount": 15}]
    assert total_value(items) == Decimal("85.00")


def test_low_stock_basic():
    assert low_stock([{"name": "pen", "qty": 2}, {"name": "ink", "qty": 9}]) == ["pen"]


def test_csv_row_plain_name():
    assert to_csv_row({"name": "pen", "price": "2.5", "qty": 4}) == "pen,2.50,4"

### Tool call: read_file
{"file_path": "workspace/inventory/__init__.py"}

### Tool result
@@ lines 1-1 @@
System reminder: File exists but has empty contents

### Tool call: read_file
{"file_path": "workspace/inventory/export.py"}

### Tool result
@@ lines 1-12 of 12 @@
"""Export helpers."""
from .pricing import parse_price


def to_csv_row(item):
    """Format one item as a CSV row: name,price,qty (price with 2 decimals).

    A name that contains a comma or a double quote is wrapped in double quotes,
    and every double quote inside it is doubled (RFC 4180).
    """
    price = parse_price(item["price"])
    return f'{item["name"]},{price:.2f},{item["qty"]}'

### Tool call: read_file
{"file_path": "workspace/inventory/pricing.py"}

### Tool result
@@ lines 1-25 of 25 @@
"""Price utilities for the inventory package."""
from decimal import Decimal


def parse_price(text):
    """Convert a price string to a Decimal.

    Supported formats:
      "$1,299.50" -> Decimal("1299.50")
      "  12 "     -> Decimal("12")
      "1299.5"    -> Decimal("1299.5")
      "(12.00)"   -> Decimal("-12.00")   # accounting style: parentheses mean negative
    """
    cleaned = text.strip().replace("$", "")
    return Decimal(cleaned)


def apply_discount(price, percent):
    """Return `price` after a percentage discount.

    The result is a Decimal rounded to 2 decimal places using the
    commercial rule "round half up" (0.005 -> 0.01).
    """
    discounted = price * (100 - percent) / 100
    return discounted.quantize(Decimal("0.01"))

### Tool call: read_file
{"file_path": "workspace/inventory/report.py"}

### Tool result
@@ lines 1-25 of 25 @@
"""Inventory reports."""
from decimal import Decimal

from .pricing import apply_discount, parse_price


def total_value(items):
    """Total value of `items` after per-item discounts.

    Each item is a dict: {"name": str, "price": str, "qty": int, "discount": percent (optional)}.
    """
    total = Decimal("0")
    for item in items:
        price = parse_price(item["price"])
        price = apply_discount(price, item.get("discount", 0))
        total += price * item["qty"]
    return total


def low_stock(items, threshold=5):
    """Names of the items whose quantity is strictly below `threshold`.

    The names are sorted alphabetically, ignoring case.
    """
    return [item["name"] for item in items if item["qty"] <= threshold]

### Tool call: write_file
{"file_path": "run_tests.py", "content": "import sys\nfrom decimal import Decimal\nsys.path.insert(0, \"workspace\")\n\nfrom inventory.pricing import parse_price, apply_discount\nfrom inventory.report import total_value, low_stock\nfrom inventory.export import to_csv_row\n\nprint(\"Testing parse_price...\")\ntry:\n    assert parse_price(\"$1,299.50\") == Decimal(\"1299.50\")\n    assert parse_price(\"  12 \") == Decimal(\"12\")\n    assert parse_price(\"1299.5\") == Decimal(\"1299.5\")\n    assert parse_price(\"(12.00)\") == Decimal(\"-12.00\")\n    print(\"parse_price passed.\")\nexcept AssertionError as e:\n    print(\"parse_price failed:\", e)\n\nprint(\"Testing apply_discount rounding half up...\")\ntry:\n    # 10.05 - 10% = 9.045 -> round half up -> 9.05\n    assert apply_discount(Decimal(\"10.05\"), 10) == Decimal(\"9.05\")\n    # What about decimal quantization mode? Decimal rounding defaults to ROUND_HALF_EVEN in python Decimal if not specified.\n    print(\"apply_discount passed.\")\nexcept AssertionError as e:\n    print(\"apply_discount failed:\", e)\n\nprint(\"Testing low_stock sorting...\")\ntry:\n    items = [{\"name\": \"Zebra\", \"qty\": 2}, {\"name\": \"apple\", \"qty\": 1}, {\"name\": \"Banana\", \"qty\": 10}]\n    # threshold default is 5. Strictly below 5: Zebra (2), apple (1). Sorted case-insensitive: apple, Zebra.\n    assert low_stock(items) == [\"apple\", \"Zebra\"]\n    print(\"low_stock passed.\")\nexcept AssertionError as e:\n    print(\"low_stock f

### Tool result
Updated file /run_tests.py

### Tool call: execute
{"command": "python run_tests.py"}

### Tool result
Testing parse_price...

[stderr] Traceback (most recent call last):
[stderr]   File "~\AppData\Local\Temp\agent_sandbox_0go1eyfu\run_tests.py", line 11, in <module>
[stderr]     assert parse_price("$1,299.50") == Decimal("1299.50")
[stderr]            ^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\AppData\Local\Temp\agent_sandbox_0go1eyfu\workspace\inventory\pricing.py", line 15, in parse_price
[stderr]     return Decimal(cleaned)
[stderr]            ^^^^^^^^^^^^^^^^
[stderr] decimal.InvalidOperation: [<class 'decimal.ConversionSyntax'>]

Exit code: 1
[Command failed with exit code 1]

### Tool call: delete
{"file_path": "run_tests.py"}

### Tool result
Deleted /run_tests.py

### Tool call: edit_file
{"old_string": "def parse_price(text):\n    \"\"\"Convert a price string to a Decimal.\n\n    Supported formats:\n      \"$1,299.50\" -> Decimal(\"1299.50\")\n      \"  12 \"     -> Decimal(\"12\")\n      \"1299.5\"    -> Decimal(\"1299.5\")\n      \"(12.00)\"   -> Decimal(\"-12.00\")   # accounting style: parentheses mean negative\n    \"\"\"\n    cleaned = text.strip().replace(\"$\", \"\")\n    return Decimal(cleaned)\n\n\ndef apply_discount(price, percent):\n    \"\"\"Return `price` after a percentage discount.\n\n    The result is a Decimal rounded to 2 decimal places using the\n    commercial rule \"round half up\" (0.005 -> 0.01).\n    \"\"\"\n    discounted = price * (100 - percent) / 100\n    return discounted.quantize(Decimal(\"0.01\"))", "new_string": "def parse_price(text):\n    \"\"\"Convert a price string to a Decimal.\n\n    Supported formats:\n      \"$1,299.50\" -> Decimal(\"1299.50\")\n      \"  12 \"     -> Decimal(\"12\")\n      \"1299.5\"    -> Decimal(\"1299.5\")\n      \"(12.00)\"   -> Decimal(\"-12.00\")   # accounting style: parentheses mean negative\n    \"\"\"\n    cleaned = text.strip()\n    negative = False\n    if cleaned.startswith(\"(\") and cleaned.endswith(\")\") :\n        negative = True\n        cleaned = cleaned[1:-1].strip()\n    cleaned = cleaned.replace(\"$\", \"\").replace(\",\", \"\")\n    val = Decimal(cleaned)\n    return -val if negative else val\n\n\ndef apply_discount(price, percent):\n    \"\"\"Return `price` after a percentage 

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/inventory/pricing.py'

### Tool call: edit_file
{"file_path": "workspace/inventory/report.py", "new_string": "def low_stock(items, threshold=5):\n    \"\"\"Names of the items whose quantity is strictly below `threshold`.\n\n    The names are sorted alphabetically, ignoring case.\n    \"\"\"\n    names = [item[\"name\"] for item in items if item[\"qty\"] < threshold]\n    return sorted(names, key=str.lower)", "old_string": "def low_stock(items, threshold=5):\n    \"\"\"Names of the items whose quantity is strictly below `threshold`.\n\n    The names are sorted alphabetically, ignoring case.\n    \"\"\"\n    return [item[\"name\"] for item in items if item[\"qty\"] <= threshold]"}

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/inventory/report.py'

### Tool call: edit_file
{"file_path": "workspace/inventory/export.py", "new_string": "def to_csv_row(item):\n    \"\"\"Format one item as a CSV row: name,price,qty (price with 2 decimals).\n\n    A name that contains a comma or a double quote is wrapped in double quotes,\n    and every double quote inside it is doubled (RFC 4180).\n    \"\"\"\n    name = item[\"name\"]\n    if \",\" in name or '\"' in name:\n        name = '\"' + name.replace('\"', '\"\"') + '\"'\n    price = parse_price(item[\"price\"])\n    return f'{name},{price:.2f},{item[\"qty\"]}'", "old_string": "def to_csv_row(item):\n    \"\"\"Format one item as a CSV row: name,price,qty (price with 2 decimals).\n\n    A name that contains a comma or a double quote is wrapped in double quotes,\n    and every double quote inside it is doubled (RFC 4180).\n    \"\"\"\n    price = parse_price(item[\"price\"])\n    return f'{item[\"name\"]},{price:.2f},{item[\"qty\"]}'"}

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/inventory/export.py'

### Tool call: write_file
{"file_path": "run_tests.py", "content": "import sys\nfrom decimal import Decimal\nsys.path.insert(0, \"workspace\")\n\nfrom inventory.pricing import parse_price, apply_discount\nfrom inventory.report import total_value, low_stock\nfrom inventory.export import to_csv_row\n\nprint(\"Testing parse_price...\")\nassert parse_price(\"$1,299.50\") == Decimal(\"1299.50\")\nassert parse_price(\"  12 \") == Decimal(\"12\")\nassert parse_price(\"1299.5\") == Decimal(\"1299.5\")\nassert parse_price(\"(12.00)\") == Decimal(\"-12.00\")\nprint(\"parse_price passed.\")\n\nprint(\"Testing apply_discount rounding half up...\")\nassert apply_discount(Decimal(\"10.05\"), 10) == Decimal(\"9.05\")\nprint(\"apply_discount passed.\")\n\nprint(\"Testing low_stock sorting and strict threshold...\")\nitems = [{\"name\": \"Zebra\", \"qty\": 5}, {\"name\": \"apple\", \"qty\": 1}, {\"name\": \"Banana\", \"qty\": 10}]\nassert low_stock(items, threshold=5) == [\"apple\"]\nitems2 = [{\"name\": \"Zebra\", \"qty\": 2}, {\"name\": \"apple\", \"qty\": 1}]\nassert low_stock(items2) == [\"apple\", \"Zebra\"]\nprint(\"low_stock passed.\")\n\nprint(\"Testing to_csv_row...\")\nassert to_csv_row({\"name\": \"pen, red\", \"price\": \"2.5\", \"qty\": 4}) == '\"pen, red\",2.50,4'\nassert to_csv_row({\"name\": 'my \"special\" pen', \"price\": \"2.5\", \"qty\": 4}) == '\"my \"\"special\"\" pen\",2.50,4'\nassert to_csv_row({\"name\": 'normal', \"price\": \"2.5\", \"qty\": 4}) == 'normal,2.50,4'\nprint(\"to_csv_row passed.\

### Tool result
Updated file /run_tests.py

### Tool call: execute
{"command": "python run_tests.py"}

### Tool result
Testing parse_price...
parse_price passed.
Testing apply_discount rounding half up...
apply_discount passed.
Testing low_stock sorting and strict threshold...
low_stock passed.
Testing to_csv_row...
to_csv_row passed.
All custom tests passed successfully!

[Command succeeded with exit code 0]

### Tool call: delete
{"file_path": "run_tests.py"}

### Tool result
Deleted /run_tests.py

### Tool call: execute
{"command": "python -c \"import sys; sys.path.insert(0, 'workspace'); import pytest; sys.exit(pytest.main(['workspace/tests']))\""}

### Tool result
[stderr] Traceback (most recent call last):
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\anyio\_core\_eventloop.py", line 204, in get_async_backend
[stderr]     return loaded_backends[asynclib_name]
[stderr]            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
[stderr] KeyError: 'asyncio'
[stderr] 
[stderr] During handling of the above exception, another exception occurred:
[stderr] 
[stderr] Traceback (most recent call last):
[stderr]   File "<string>", line 1, in <module>
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\_pytest\config\__init__.py", line 201, in main
[stderr]     return _main(args=args, plugins=plugins, prog="pytest.main()")
[stderr]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\_pytest\config\__init__.py", line 223, in _main
[stderr]     config = _prepareconfig(new_args, plugins, prog=prog)
[stderr]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\_pytest\config\__init__.py", line 410, in _prepareconfig
[stderr]     config: Config = pluginmanager.hook.pytest_cmdline_parse(
[stderr]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\pluggy\_hooks.py", lin

### Tool call: write_file
{"content": "import sys\nsys.path.insert(0, \"workspace\")\nimport unittest\nfrom tests.test_report import *\n\nif __name__ == \"__main__\":\n    unittest.main()\n", "file_path": "run_tests.py"}

### Tool result
Updated file /run_tests.py

### Tool call: execute
{"command": "python run_tests.py"}

### Tool result
[stderr] ----------------------------------------------------------------------
[stderr] Ran 0 tests in 0.000s
[stderr] 
[stderr] OK
[Command succeeded with exit code 0]

### Tool call: delete
{"file_path": "run_tests.py"}

### Tool result
Deleted /run_tests.py

### Tool call: read_file
{"file_path": "workspace/tests/test_report.py"}

### Tool result
@@ lines 1-32 of 32 @@
from decimal import Decimal

from inventory.export import to_csv_row
from inventory.pricing import apply_discount
from inventory.report import low_stock, total_value


def test_total_value_plain():
    items = [{"name": "pen", "price": "$2.50", "qty": 4}]
    assert total_value(items) == Decimal("10.00")


def test_total_value_thousands_separator():
    items = [{"name": "laptop", "price": "$1,299.50", "qty": 2}]
    assert total_value(items) == Decimal("2599.00")


def test_discount_rounding_half_up():
    assert apply_discount(Decimal("10.05"), 10) == Decimal("9.05")


def test_total_value_with_discount():
    items = [{"name": "desk", "price": "100.00", "qty": 1, "discount": 15}]
    assert total_value(items) == Decimal("85.00")


def test_low_stock_basic():
    assert low_stock([{"name": "pen", "qty": 2}, {"name": "ink", "qty": 9}]) == ["pen"]


def test_csv_row_plain_name():
    assert to_csv_row({"name": "pen", "price": "2.5", "qty": 4}) == "pen,2.50,4"

### Tool call: write_file
{"file_path": "run_tests.py", "content": "import sys\nsys.path.insert(0, \"workspace\")\nfrom decimal import Decimal\nfrom inventory.export import to_csv_row\nfrom inventory.pricing import apply_discount, parse_price\nfrom inventory.report import low_stock, total_value\n\ndef test_total_value_plain():\n    items = [{\"name\": \"pen\", \"price\": \"$2.50\", \"qty\": 4}]\n    assert total_value(items) == Decimal(\"10.00\")\n\ndef test_total_value_thousands_separator():\n    items = [{\"name\": \"laptop\", \"price\": \"$1,299.50\", \"qty\": 2}]\n    assert total_value(items) == Decimal(\"2599.00\")\n\ndef test_discount_rounding_half_up():\n    assert apply_discount(Decimal(\"10.05\"), 10) == Decimal(\"9.05\")\n\ndef test_total_value_with_discount():\n    items = [{\"name\": \"desk\", \"price\": \"100.00\", \"qty\": 1, \"discount\": 15}]\n    assert total_value(items) == Decimal(\"85.00\")\n\ndef test_low_stock_basic():\n    assert low_stock([{\"name\": \"pen\", \"qty\": 2}, {\"name\": \"ink\", \"qty\": 9}]) == [\"pen\"]\n\ndef test_csv_row_plain_name():\n    assert to_csv_row({\"name\": \"pen\", \"price\": \"2.5\", \"qty\": 4}) == \"pen,2.50,4\"\n\nif __name__ == \"__main__\":\n    test_total_value_plain()\n    test_total_value_thousands_separator()\n    test_discount_rounding_half_up()\n    test_total_value_with_discount()\n    test_low_stock_basic()\n    test_csv_row_plain_name()\n    print(\"All tests passed successfully via standalone runner!\")\n"}

### Tool result
Updated file /run_tests.py

### Tool call: execute
{"command": "python run_tests.py"}

### Tool result
All tests passed successfully via standalone runner!

[Command succeeded with exit code 0]

### Tool call: delete
{"file_path": "run_tests.py"}