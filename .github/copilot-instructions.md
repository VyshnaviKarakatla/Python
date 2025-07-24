# Copilot Instructions for AI Agents

## Project Overview
This workspace is a collection of Python scripts for learning and demonstrating basic programming concepts. Each numbered folder covers a specific topic, such as variables, data types, and operators. There is no complex architecture or cross-file data flow—each script is self-contained.

## Directory Structure
- `01_variables_data_types/01_variables_data_types.py`: Demonstrates variable declarations and data types.
- `02_operators/operators.py`: Shows usage of arithmetic, assignment, and relational operators.

## Key Patterns & Conventions
- Each topic is in its own folder, with a single script per topic.
- Scripts are written for clarity and educational value, not for production use.
- Code is procedural and top-down; no classes or functions unless the topic requires it.
- Comments are used to explain code sections and operator usage.
- Variable names are short and descriptive (e.g., `a`, `b`, `x`, `p`, `q`).

## Developer Workflows
- No build or test system is present; run scripts directly with Python:
  ```powershell
  python 01_variables_data_types/01_variables_data_types.py
  python 02_operators/operators.py
  ```
- No external dependencies or requirements files.
- No integration with external services or APIs.

## Guidance for AI Agents
- When adding new topics, create a new numbered folder and script (e.g., `03_control_flow/control_flow.py`).
- Follow the existing commenting and naming conventions for consistency.
- Keep code simple and focused on illustrating the topic.
- Do not introduce unnecessary complexity or dependencies.

## Example: Adding a New Topic
1. Create a new folder: `03_control_flow/`
2. Add a script: `03_control_flow/control_flow.py`
3. Write code and comments to demonstrate control flow statements (if, for, while, etc.)

---
For questions, see the `README.md` or follow the patterns in existing scripts.
