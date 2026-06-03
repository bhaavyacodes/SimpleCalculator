# Simple Calculator

A minimal Python calculator that evaluates arithmetic expressions entered by the user.

## Description

This simple script prompts the user for a mathematical expression and prints the evaluated result. It supports Python arithmetic syntax and handles common errors such as division by zero and invalid expressions.

## Features

- Accepts arithmetic expressions from standard input
- Evaluates expressions using Python's built-in `eval`
- Handles division by zero gracefully
- Reports invalid expressions with a friendly error message

## Usage

1. Run the script:

```bash
python SimpleCalculator.py
```
2. Enter an expression when prompted, for example:

```text
Enter expression: 2 + 3 * (4 - 1)
```

3. The result will be printed immediately.

## Error handling

- `Invalid Expression: Division by Zero` when the expression contains division by zero
- `Invalid Expression` for malformed input or unsupported expressions

