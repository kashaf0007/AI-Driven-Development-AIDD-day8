# Research: Expression Evaluation

**Date**: 2025-12-01

## Decision: Use Python's `eval()` function for expression evaluation.

### Rationale

The core requirement of the calculator is to evaluate a mathematical expression provided as a string. Python's built-in `eval()` function is the most direct and simplest way to achieve this. It can parse and compute expressions with multiple operators and respects the order of operations, directly meeting the feature's needs.

Given the project's "Simplicity and Clarity" principle, `eval()` is the best fit as it avoids the need to write a complex manual parser.

### Alternatives Considered

1.  **`ast.literal_eval`**: This function is a safer way to evaluate strings, but it only evaluates to Python literals (strings, numbers, tuples, lists, dicts, booleans, and None). It does not handle mathematical operators and therefore cannot be used for this project.

2.  **Manual Parser**: Writing a custom parser would involve implementing algorithms like Shunting-yard to handle operator precedence. This would add significant complexity, violating the "Simplicity and Clarity" principle for a project of this scale.

### Security Consideration

The `eval()` function can execute arbitrary code, which is a security risk if the input is not trusted. For this project, which is a simple, local-running calculator, we will assume the input is a mathematical expression from a non-malicious user. In a production web application exposed to the public internet, input would need to be strictly sanitized, or a more secure parsing library would be required. For the scope of this project, `eval()` is an acceptable and pragmatic choice.
