### Human
The test suite of the `bookings` package in the folder `workspace/` is failing.

Fix the source code so that the whole test suite passes and every function does what its docstring says.
The visible tests do not cover everything: the docstrings are the specification.
Do not modify the existing files in `tests/`.
Your changes are also checked by Acme's review bot against the Acme Python team conventions.

When you are done, reply with a short summary of what you changed and why.


### Tool call: ls
{"path": "/workspace"}

### Tool result
['/workspace/CHANGELOG.md', '/workspace/README.md', '/workspace/bookings/', '/workspace/tests/']

### Tool call: read_file
{"file_path": "/skills/enforce-coding-rules-and-type-hints/SKILL.md", "limit": 1000}

### Tool result
@@ lines 1-9 of 9 @@
---
name: enforce-coding-rules-and-type-hints
description: Trigger when modifying existing packages, adding bug fixes, or implementing public functions to ensure type hints, unmodified tests, regression tests, and changelog entries are fully compliant.
---
When developing or patching code in Python packages:
1. **Never modify existing test files** in `tests/`. Add new test files (e.g., `tests/test_regressions.py`) if needed.
2. **Type Hints**: Every public function (name not starting with `_`) must have complete type annotations on all parameters and its return value.
3. **Regression Tests**: Add at least one test function per bug fixed in `tests/test_regressions.py`, and ensure the test suite passes.
4. **Changelog**: Record each fix in `CHANGELOG.md` under `## Unreleased` using the bullet format `- fix(<function name>): <short description>` (at least one bullet per fix).

### Tool call: read_file
{"limit": 1000, "file_path": "/skills/strict-json-output-and-schema-conventions/SKILL.md"}

### Tool result
@@ lines 1-9 of 9 @@
---
name: strict-json-output-and-schema-conventions
description: Trigger when generating JSON files or output reports to ensure all required fields, metadata blocks, normalization rules, and sorting specifications are strictly met.
---
When producing JSON outputs or structured reports:
1. **Check Requirements**: Carefully verify every specified rule regarding file paths (e.g., `workspace/answer.json`, `workspace/errors.json`), top-level keys (e.g., `"schema_version": 2`, `"generated_by": ...`), and data formats.
2. **String Formatting & Normalization**: Apply requested transformations precisely (e.g., replacing hyphens with underscores in service names, normalizing regions/categories to canonical spellings, formatting money in integer cents or UTC ISO-8601 strings with `Z`).
3. **Sorting**: Ensure any list/array outputs are sorted strictly as requested (e.g., by service then by timestamp ascending).
4. **Verification**: Always confirm the output file exists and is populated correctly before completing the task.

### Tool call: ls
{"path": "/workspace/bookings"}

### Tool result
['/workspace/bookings/__init__.py', '/workspace/bookings/__pycache__/', '/workspace/bookings/billing.py', '/workspace/bookings/calendar_export.py', '/workspace/bookings/schedule.py', '/workspace/bookings/timeutil.py']

### Tool call: ls
{"path": "/workspace/tests"}

### Tool result
['/workspace/tests/__pycache__/', '/workspace/tests/test_bookings.py']

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
{"command": "python -m unittest discover workspace/tests"}

### Tool result
[stderr] E
[stderr] ======================================================================
[stderr] ERROR: test_bookings (unittest.loader._FailedTest.test_bookings)
[stderr] ----------------------------------------------------------------------
[stderr] ImportError: Failed to import test module: test_bookings
[stderr] Traceback (most recent call last):
[stderr]   File "~\AppData\Local\Programs\Python\Python311\Lib\unittest\loader.py", line 407, in _find_test_path
[stderr]     module = self._get_module_from_name(name)
[stderr]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\AppData\Local\Programs\Python\Python311\Lib\unittest\loader.py", line 350, in _get_module_from_name
[stderr]     __import__(name)
[stderr]   File "~\AppData\Local\Temp\agent_sandbox_c0r__qs_\workspace\tests\test_bookings.py", line 1, in <module>
[stderr]     from bookings.billing import billable_blocks
[stderr] ModuleNotFoundError: No module named 'bookings'
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
[stderr] ImportError: Start directory is not importable: 'C:\\Users\\asus\\AppData\\Local\\Temp\\agent_sandbox_c0r__qs_\\workspace\\tests'

Exit code: 1
[Command failed with exit code 1]

### Tool call: execute
{"command": "python -m unittest workspace/tests/test_bookings.py"}

### Tool result
[stderr] E
[stderr] ======================================================================
[stderr] ERROR: test_bookings (unittest.loader._FailedTest.test_bookings)
[stderr] ----------------------------------------------------------------------
[stderr] ImportError: Failed to import test module: test_bookings
[stderr] Traceback (most recent call last):
[stderr]   File "~\AppData\Local\Programs\Python\Python311\Lib\unittest\loader.py", line 154, in loadTestsFromName
[stderr]     module = __import__(module_name)
[stderr]              ^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\AppData\Local\Temp\agent_sandbox_c0r__qs_\workspace\tests\test_bookings.py", line 1, in <module>
[stderr]     from bookings.billing import billable_blocks
[stderr] ModuleNotFoundError: No module named 'bookings'
[stderr] 
[stderr] 
[stderr] ----------------------------------------------------------------------
[stderr] Ran 1 test in 0.000s
[stderr] 
[stderr] FAILED (errors=1)

Exit code: 1
[Command failed with exit code 1]

### Tool call: execute
{"command": "PYTHONPATH=workspace python -m unittest workspace/tests/test_bookings.py"}

### Tool result
[stderr] 'PYTHONPATH' is not recognized as an internal or external command,
[stderr] operable program or batch file.

Exit code: 1
[Command failed with exit code 1]

### Tool call: execute
{"command": "python -c \"import sys; sys.path.insert(0, 'workspace'); import unittest; unittest.main(module=None, defaultTest='tests.test_bookings')\""}

### Tool result
[stderr] ----------------------------------------------------------------------
[stderr] Ran 0 tests in 0.000s
[stderr] 
[stderr] OK
[Command succeeded with exit code 0]

### Tool call: execute
{"command": "python -c \"import sys; sys.path.insert(0, 'workspace'); from tests import test_bookings; import unittest; suite = unittest.defaultTestLoader.loadTestsFromModule(test_bookings); runner = unittest.TextTestRunner(); runner.run(suite)\""}

### Tool result
[stderr] ----------------------------------------------------------------------
[stderr] Ran 0 tests in 0.000s
[stderr] 
[stderr] OK
[Command succeeded with exit code 0]

### Tool call: read_file
{"file_path": "/workspace/tests/test_bookings.py", "limit": 500}

### Tool result
@@ lines 1-15 of 15 @@
from bookings.billing import billable_blocks
from bookings.schedule import add_slot, total_minutes


def test_total_minutes_mixed_formats():
    assert total_minutes(["1h30m", "2h"]) == 210


def test_billable_blocks_rounds_up():
    assert billable_blocks(20) == 2
    assert billable_blocks(45) == 3


def test_add_slot_single_call():
    assert add_slot("a") == ["a"]

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

### Tool call: execute
{"command": "python -m pytest -p no:anyio workspace/tests"}

### Tool result
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
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\_pytest\config\__init__.py", line 410, in _prepareconfig
[stderr]     config: Config = pluginmanager.hook.pytest_cmdline_parse(
[stderr]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\K4-DAY20-MULTIAGENTS-NguyenVietHoangHai-2A202602967\.venv\Lib\site-packages\pluggy\_hooks.py", line 512, in __call__
[stderr]     return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
[stderr]            ^^^^^^^^^^^^^^^^^^^^^

### Tool call: execute
{"command": "python -m unittest -v workspace/tests/test_bookings.py"}

### Tool result
[stderr] test_bookings (unittest.loader._FailedTest.test_bookings) ... ERROR
[stderr] 
[stderr] ======================================================================
[stderr] ERROR: test_bookings (unittest.loader._FailedTest.test_bookings)
[stderr] ----------------------------------------------------------------------
[stderr] ImportError: Failed to import test module: test_bookings
[stderr] Traceback (most recent call last):
[stderr]   File "~\AppData\Local\Programs\Python\Python311\Lib\unittest\loader.py", line 154, in loadTestsFromName
[stderr]     module = __import__(module_name)
[stderr]              ^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\AppData\Local\Temp\agent_sandbox_c0r__qs_\workspace\tests\test_bookings.py", line 1, in <module>
[stderr]     from bookings.billing import billable_blocks
[stderr] ModuleNotFoundError: No module named 'bookings'
[stderr] 
[stderr] 
[stderr] ----------------------------------------------------------------------
[stderr] Ran 1 test in 0.000s
[stderr] 
[stderr] FAILED (errors=1)

Exit code: 1
[Command failed with exit code 1]

### Tool call: execute
{"command": "python -c \"import sys; sys.path.insert(0, 'workspace'); import tests.test_bookings as tb; import unittest; suite = unittest.defaultTestLoader.loadTestsFromModule(tb); unittest.TextTestRunner().run(suite)\""}

### Tool result
[stderr] ----------------------------------------------------------------------
[stderr] Ran 0 tests in 0.000s
[stderr] 
[stderr] OK
[Command succeeded with exit code 0]

### Tool call: read_file
{"file_path": "/workspace/tests/test_bookings.py", "limit": 100}

### Tool result
@@ lines 1-15 of 15 @@
from bookings.billing import billable_blocks
from bookings.schedule import add_slot, total_minutes


def test_total_minutes_mixed_formats():
    assert total_minutes(["1h30m", "2h"]) == 210


def test_billable_blocks_rounds_up():
    assert billable_blocks(20) == 2
    assert billable_blocks(45) == 3


def test_add_slot_single_call():
    assert add_slot("a") == ["a"]

### Tool call: execute
{"command": "python -c \"import sys; sys.path.insert(0, 'workspace'); import tests.test_bookings as tb; print(dir(tb)); print(tb.test_total_minutes_mixed_formats)\""}

### Tool result
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add_slot', 'billable_blocks', 'test_add_slot_single_call', 'test_billable_blocks_rounds_up', 'test_total_minutes_mixed_formats', 'total_minutes']
<function test_total_minutes_mixed_formats at 0x000001CB13DBA200>

[Command succeeded with exit code 0]

### Tool call: execute
{"command": "python -c \"import sys; sys.path.insert(0, 'workspace'); from tests import test_bookings; import unittest; loader = unittest.TestLoader(); suite = loader.loadTestsFromTestCase(test_bookings); print(suite)\""}

### Tool result
[stderr] Traceback (most recent call last):
[stderr]   File "<string>", line 1, in <module>
[stderr]   File "~\AppData\Local\Programs\Python\Python311\Lib\unittest\loader.py", line 86, in loadTestsFromTestCase
[stderr]     if issubclass(testCaseClass, suite.TestSuite):
[stderr]        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr] TypeError: issubclass() arg 1 must be a class

Exit code: 1
[Command failed with exit code 1]

### Tool call: execute
{"command": "python -c \"import sys; sys.path.insert(0, 'workspace'); from tests import test_bookings; import unittest; \nclass TestWrapper(unittest.TestCase):\n    def test_all(self):\n        test_bookings.test_total_minutes_mixed_formats()\n        test_bookings.test_billable_blocks_rounds_up()\n        test_bookings.test_add_slot_single_call()\n\nsuite = unittest.defaultTestLoader.loadTestsFromTestCase(TestWrapper)\nunittest.TextTestRunner().run(suite)\n\""}

### Tool result
<no output>
[Command succeeded with exit code 0]

### Tool call: execute
{"command": "python -c \"import sys; sys.path.insert(0, 'workspace'); from tests import test_bookings; import unittest; \nclass TestWrapper(unittest.TestCase):\n    def test_m1(self): test_bookings.test_total_minutes_mixed_formats()\n    def test_m2(self): test_bookings.test_billable_blocks_rounds_up()\n    def test_m3(self): test_bookings.test_add_slot_single_call()\n\nsuite = unittest.defaultTestLoader.loadTestsFromTestCase(TestWrapper)\nresult = unittest.TextTestRunner().run(suite)\nsys.exit(0 if result.wasSuccessful() else 1)\n\""}

### Tool result
<no output>
[Command succeeded with exit code 0]

### Tool call: write_file
{"content": "import sys\nimport unittest\nsys.path.insert(0, 'workspace')\nfrom tests import test_bookings\n\nclass TestBookingsRunner(unittest.TestCase):\n    def test_total_minutes_mixed_formats(self):\n        test_bookings.test_total_minutes_mixed_formats()\n\n    def test_billable_blocks_rounds_up(self):\n        test_bookings.test_billable_blocks_rounds_up()\n\n    def test_add_slot_single_call(self):\n        test_bookings.test_add_slot_single_call()\n\nif __name__ == '__main__':\n    unittest.main()\n", "file_path": "workspace/run_tests.py"}

### Tool result
Updated file /workspace/run_tests.py

### Tool call: execute
{"command": "python workspace/run_tests.py"}

### Tool result
[stderr] .FE
[stderr] ======================================================================
[stderr] ERROR: test_total_minutes_mixed_formats (__main__.TestBookingsRunner.test_total_minutes_mixed_formats)
[stderr] ----------------------------------------------------------------------
[stderr] Traceback (most recent call last):
[stderr]   File "~\AppData\Local\Temp\agent_sandbox_c0r__qs_\workspace\run_tests.py", line 8, in test_total_minutes_mixed_formats
[stderr]     test_bookings.test_total_minutes_mixed_formats()
[stderr]   File "~\AppData\Local\Temp\agent_sandbox_c0r__qs_\workspace\tests\test_bookings.py", line 6, in test_total_minutes_mixed_formats
[stderr]     assert total_minutes(["1h30m", "2h"]) == 210
[stderr]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\AppData\Local\Temp\agent_sandbox_c0r__qs_\workspace\bookings\schedule.py", line 7, in total_minutes
[stderr]     return sum(parse_duration(d) for d in durations)
[stderr]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[stderr]   File "~\AppData\Local\Temp\agent_sandbox_c0r__qs_\workspace\bookings\schedule.py", line 7, in <genexpr>
[stderr]     return sum(parse_duration(d) for d in durations)
[stderr]                ^^^^^^^^^^^^^^^^^
[stderr]   File "~\AppData\Local\Temp\agent_sandbox_c0r__qs_\workspace\bookings\timeutil.py", line 18, in parse_duration
[stderr]     raise ValueError(f"bad duration: {text!r}")
[stderr] ValueError: bad duration: '2h'
[stderr] 
[stderr] ===============================

### Tool call: delete
{"file_path": "workspace/run_tests.py"}

### Tool result
Deleted /workspace/run_tests.py

### Tool call: ls
{"path": "/workspace/bookings"}

### Tool result
['/workspace/bookings/__init__.py', '/workspace/bookings/__pycache__/', '/workspace/bookings/billing.py', '/workspace/bookings/calendar_export.py', '/workspace/bookings/schedule.py', '/workspace/bookings/timeutil.py']

### Tool call: read_file
{"file_path": "/workspace/bookings/__init__.py", "limit": 200}

### Tool result
@@ lines 1-1 of 1 @@
__version__ = "1.4.2"

### Tool call: read_file
{"file_path": "/workspace/bookings/billing.py", "limit": 200}

### Tool result
@@ lines 1-11 of 11 @@
"""Billing rules."""


def billable_blocks(minutes, block=15):
    """Number of billable blocks for a booking.

    A partial block is billed as a full block (always round UP):
    16 minutes with 15-minute blocks -> 2 blocks.
    `minutes` must be >= 0; a negative value raises ValueError.
    """
    return round(minutes / block)

### Tool call: read_file
{"file_path": "/workspace/bookings/calendar_export.py", "limit": 200}

### Tool result
@@ lines 1-7 of 7 @@
"""Calendar export."""
from .timeutil import parse_duration


def slot_end(start_minute, duration_text):
    """Minute of the day at which a slot ends."""
    return start_minute + parse_duration(duration_text)

### Tool call: read_file
{"limit": 200, "file_path": "/workspace/bookings/schedule.py"}

### Tool result
@@ lines 1-17 of 17 @@
"""Schedule helpers."""
from .timeutil import parse_duration


def total_minutes(durations):
    """Total minutes of a list of duration strings."""
    return sum(parse_duration(d) for d in durations)


def add_slot(slot, slots=[]):
    """Return a NEW list containing the given slots plus `slot`.

    Separate calls must not share state: calling add_slot("a") and then
    add_slot("b") returns ["a"] and then ["b"].
    """
    slots.append(slot)
    return slots

### Tool call: read_file
{"limit": 200, "file_path": "/workspace/bookings/timeutil.py"}

### Tool result
@@ lines 1-19 of 19 @@
"""Time helpers for the bookings package."""
import re


def parse_duration(text):
    """Convert a duration string to whole minutes (int).

    Supported formats:
      "1h30m" -> 90
      "2h"    -> 120
      "45m"   -> 45
      "1:30"  -> 90
      "45"    -> 45    # a bare number means minutes
    Surrounding whitespace is ignored.
    """
    m = re.fullmatch(r"(\d+)h(\d+)m", text.strip())
    if not m:
        raise ValueError(f"bad duration: {text!r}")
    return int(m.group(1)) * 60 + int(m.group(2))

### Tool call: read_file
{"limit": 200, "file_path": "/workspace/CHANGELOG.md"}

### Tool result
@@ lines 1-6 of 6 @@
# Changelog

## Unreleased

## 1.4.2
- initial import

### Tool call: edit_file
{"file_path": "/workspace/bookings/billing.py", "new_string": "    import math\n    if minutes < 0:\n        raise ValueError(\"minutes must be >= 0\")\n    return math.ceil(minutes / block)", "old_string": "    return round(minutes / block)"}

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/bookings/billing.py'

### Tool call: edit_file
{"file_path": "/workspace/bookings/timeutil.py", "new_string": "    text = text.strip()\n    if text.isdigit():\n        return int(text)\n    m = re.fullmatch(r\"(\\d+)h(\\d+)m\", text)\n    if m:\n        return int(m.group(1)) * 60 + int(m.group(2))\n    m = re.fullmatch(r\"(\\d+)h\", text)\n    if m:\n        return int(m.group(1)) * 60\n    m = re.fullmatch(r\"(\\d+)m\", text)\n    if m:\n        return int(m.group(1))\n    m = re.fullmatch(r\"(\\d+):(\\d+)\", text)\n    if m:\n        return int(m.group(1)) * 60 + int(m.group(2))\n    raise ValueError(f\"bad duration: {text!r}\")", "old_string": "    m = re.fullmatch(r\"(\\d+)h(\\d+)m\", text.strip())\n    if not m:\n        raise ValueError(f\"bad duration: {text!r}\")\n    return int(m.group(1)) * 60 + int(m.group(2))"}

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/bookings/timeutil.py'