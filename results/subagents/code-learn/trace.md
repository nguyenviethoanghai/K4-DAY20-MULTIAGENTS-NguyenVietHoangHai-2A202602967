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

### Tool call: task
{"subagent_type": "explorer", "description": "Explore the workspace inventory package, run pytest using execute, examine source files in workspace/inventory/ and test files in workspace/tests/, and report the failing tests and code structure. Note that paths are relative to sandbox root (e.g., workspace/inventory)."}

### Tool result
I have explored the workspace inventory package structure and analyzed the source and test files.

### Code Structure

The package is located under `workspace/inventory/` with the following source files:
1. **`workspace/inventory/__init__.py`**: Empty package initialization file.
2. **`workspace/inventory/pricing.py`**: Contains pricing utilities:
   - `parse_price(text)`: Cleans a price string (removes `$` and `.strip()`) and converts it to a `Decimal`.
   - `apply_discount(price, percent)`: Calculates the discounted price using `price * (100 - percent) / 100` and rounds using `.quantize(Decimal("0.01"))`.
3. **`workspace/inventory/report.py`**: Contains report functions:
   - `total_value(items)`: Iterates over inventory items, parses their prices, applies any per-item discounts, and calculates the total inventory value (`price * qty`).
   - `low_stock(items, threshold=5)`: Returns names of items whose quantity is less than or equal to `threshold`.
4. **`workspace/inventory/export.py`**: Contains export helpers:
   - `to_csv_row(item)`: Formats an item dictionary into a CSV string (`name,price,qty`).

The tests are located in **`workspace/tests/test_report.py`**.

---

### Failing Tests & Root-Cause Analysis

When running the unit test suite (`workspace/tests/test_report.py`), two tests fail / raise errors:

1. **`test_total_value_thousands_separator`** (`decimal.InvalidOperation`):
   - **Test case:** `items = [{"name": "laptop", "price": "$1,299.50", "qty": 2}]`
   - **Ro

### Tool call: task
{"subagent_type": "explorer", "description": "Examine all files in workspace/inventory/ and workspace/tests/ to ensure we understand all docstrings, functions, edge cases, and test requirements. Read workspace/inventory/pricing.py, workspace/inventory/report.py, workspace/inventory/export.py, and workspace/tests/test_report.py using read_file."}