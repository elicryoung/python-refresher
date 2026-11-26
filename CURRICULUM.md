# Curriculum Design

## Learning Dependency Rule

Every lesson may only require knowledge introduced in
previous lessons or explicitly taught in the current lesson.

This rule applies to:

- Syntax
- Operators
- Data structures
- Methods
- Built-in functions
- Standard library modules
- Programming techniques
- Worked examples
- Exercises

Never introduce an unexplained programming technique
inside an exercise.

## Learning Order

| Module | Prerequisites |
| --- | --- |
| 01 Fundamentals | None |
| 02 Conditions | 01 |
| 03 Lists | 01–02 |
| 04 Loops | 01–03 |
| 05 Functions | 01–04 |
| 06 Strings | 01–05 |
| 07 Dictionaries | 01–06 |
| 08 Sets and Tuples | 01–07 |
| 09 Built-in Functions | 01–08 |
| 10 Testing and Debugging | 01–09 |
| 11 Practical Patterns | 01–10 |
| 12 Problem Solving | 01–11 |

## Lesson Structure

Each lesson must include:

1. Prerequisites
2. Purpose
3. When to use the concept
4. Syntax
5. Worked example
6. Line-by-line explanation
7. Expected output
8. Important rules
9. Common mistakes
10. Exercises

## Exercises

Provide between one and five exercises per concept.

### Difficulty Levels

1. Basic syntax
2. Understanding and application
3. Independent implementation
4. Combined knowledge
5. Practical problem-solving

Exercises must increase in difficulty gradually.

A learner should be able to complete every exercise using
only concepts taught up to that point.

## Exercise File Format

Use the following layout for active exercises:

```python
# ============================================================
# EXERCISE 03.01 — EXERCISE TITLE
# ============================================================

# QUESTION
"""
Problem description.

# REQUIREMENTS

1. First requirement.
2. Second requirement.
"""

# INPUT
# Executable input goes here.

# SOLUTION


# EXPECTED OUTPUT
"""
Expected output.
"""
```

Keep completed reference solutions inactive inside
triple-quoted blocks.

Include explanations after completed solutions.

Only activate the exercise currently being attempted.

## Completion Criteria

Before progressing, learners should be able to:

- Explain the current concept.
- Recognise when to use it.
- Write its syntax independently.
- Solve an unfamiliar variation.
- Combine it with previously introduced concepts.

## Final Objective

Develop the ability to independently understand
programming problems, select appropriate techniques,
implement solutions and verify their correctness.

Prioritise correctness, readability and then optimisation.
