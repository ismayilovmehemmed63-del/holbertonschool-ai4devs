# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability and performance
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Optimized code + explanation

- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting
  - **Input**: Code block
  - **Output**: Rewritten code with consistent style

- **Code Review**
  - **Goal**: Identify potential issues and improvements
  - **Input**: Pull request or code snippet
  - **Output**: Detailed review with suggestions

## Debugging
- **Error Diagnosis**
  - **Goal**: Identify root cause of an error or exception
  - **Input**: Buggy code + error message or stack trace
  - **Output**: Explanation of bug + suggested fix

- **Logic Error Detection**
  - **Goal**: Find logical flaws that produce wrong results
  - **Input**: Function with incorrect output
  - **Output**: Corrected logic + explanation

- **Performance Debugging**
  - **Goal**: Detect slow or inefficient code sections
  - **Input**: Code with performance issues
  - **Output**: Optimized version + profiling notes

## Documentation
- **Function Documentation**
  - **Goal**: Generate docstrings for undocumented functions
  - **Input**: Function signature and body in [LANGUAGE]
  - **Output**: Docstring with parameters, return values, and examples

- **README Generation**
  - **Goal**: Create a project README from codebase description
  - **Input**: Project name, purpose, and main features
  - **Output**: Structured README.md with setup and usage sections

- **API Documentation**
  - **Goal**: Document REST API endpoints clearly
  - **Input**: Endpoint definitions and parameters
  - **Output**: Formatted API reference with examples

## Testing
- **Unit Test Generation**
  - **Goal**: Create unit tests for a given function
  - **Input**: Function in [LANGUAGE] with expected behavior
  - **Output**: Test file with multiple test cases including edge cases

- **Test Case Design**
  - **Goal**: Design test scenarios for complex features
  - **Input**: Feature description and acceptance criteria
  - **Output**: List of test cases covering normal and edge cases

- **Test Coverage Analysis**
  - **Goal**: Identify untested code paths
  - **Input**: Source code + existing test file
  - **Output**: List of missing test cases + suggested additions
