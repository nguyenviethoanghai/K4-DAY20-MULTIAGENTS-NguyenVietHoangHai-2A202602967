---
name: enforce-coding-rules-and-type-hints
description: Trigger when modifying existing packages, adding bug fixes, or implementing public functions to ensure type hints, unmodified tests, regression tests, and changelog entries are fully compliant.
---
When developing or patching code in Python packages:
1. **Never modify existing test files** in `tests/`. Add new test files (e.g., `tests/test_regressions.py`) if needed.
2. **Type Hints**: Every public function (name not starting with `_`) must have complete type annotations on all parameters and its return value.
3. **Regression Tests**: Add at least one test function per bug fixed in `tests/test_regressions.py`, and ensure the test suite passes.
4. **Changelog**: Record each fix in `CHANGELOG.md` under `## Unreleased` using the bullet format `- fix(<function name>): <short description>` (at least one bullet per fix).
