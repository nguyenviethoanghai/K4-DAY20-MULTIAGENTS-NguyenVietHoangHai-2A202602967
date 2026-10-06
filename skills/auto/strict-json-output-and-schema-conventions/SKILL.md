---
name: strict-json-output-and-schema-conventions
description: Trigger when generating JSON files or output reports to ensure all required fields, metadata blocks, normalization rules, and sorting specifications are strictly met.
---
When producing JSON outputs or structured reports:
1. **Check Requirements**: Carefully verify every specified rule regarding file paths (e.g., `workspace/answer.json`, `workspace/errors.json`), top-level keys (e.g., `"schema_version": 2`, `"generated_by": ...`), and data formats.
2. **String Formatting & Normalization**: Apply requested transformations precisely (e.g., replacing hyphens with underscores in service names, normalizing regions/categories to canonical spellings, formatting money in integer cents or UTC ISO-8601 strings with `Z`).
3. **Sorting**: Ensure any list/array outputs are sorted strictly as requested (e.g., by service then by timestamp ascending).
4. **Verification**: Always confirm the output file exists and is populated correctly before completing the task.
