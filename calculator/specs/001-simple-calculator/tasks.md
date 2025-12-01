---
description: "Task list for Simple Expression Calculator"
---

# Tasks: Simple Expression Calculator

**Input**: Design documents from `specs/001-simple-calculator/`
**Prerequisites**: plan.md, spec.md

**Tests**: The constitution requires a Test-Driven Development (TDD) approach, so test tasks are included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `app.py`, `tests/` at repository root

---

## Phase 1: Setup

**Purpose**: Project initialization and basic structure.

- [x] T001 Create project file structure: `app.py`, `requirements.txt`, `README.md`, and `tests/test_calculator.py`.
- [x] T002 Add `streamlit` and `pytest` to `requirements.txt`.

---

## Phase 2: User Story 1 - Basic Expression Calculation (🎯 MVP)

**Goal**: Implement the core functionality for evaluating a valid mathematical expression.

**Independent Test**: A user can enter a simple expression (e.g., "2 + 3"), click "Calculate", and see the correct result (5).

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T003 [US1] In `tests/test_calculator.py`, write a failing test for a simple addition expression.
- [ ] T004 [US1] In `tests/test_calculator.py`, write failing tests for subtraction, multiplication, and division.

### Implementation for User Story 1

- [ ] T005 [US1] In `app.py`, create the basic Streamlit UI with a text input field and a "Calculate" button.
- [ ] T006 [US1] In `app.py`, implement the initial calculation logic to evaluate the expression from the input field and display the result. This should make the tests from T003 and T004 pass.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 3: User Story 2 - Invalid Expression and Error Handling

**Goal**: Add robust error handling for invalid inputs and division by zero.

**Independent Test**: A user can enter "5 / 0" and see a "Cannot divide by zero" error. A user can enter "abc" and see an "Invalid expression" error.

### Tests for User Story 2 ⚠️

- [ ] T007 [P] [US2] In `tests/test_calculator.py`, write a failing test for division by zero.
- [ ] T008 [P] [US2] In `tests/test_calculator.py`, write a failing test for a malformed expression (e.g., "5 + * 3").

### Implementation for User Story 2

- [ ] T009 [US2] In `app.py`, update the calculation logic to handle `ZeroDivisionError` and display the specific error message. This should make the test from T007 pass.
- [ ] T010 [US2] In `app.py`, add a general `try...except` block to the calculation logic to catch any other exceptions during evaluation and display a generic "Invalid expression" error. This should make the test from T008 pass.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Final cleanup and documentation.

- [ ] T011 [P] Populate `README.md` with a project description, features, and usage instructions from `quickstart.md`.
- [ ] T012 Run a final check on the UI and code for formatting, clarity, and adherence to principles.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Must be completed first.
- **User Story 1 (Phase 2)**: Depends on Setup. This is the MVP.
- **User Story 2 (Phase 3)**: Depends on User Story 1.
- **Polish (Phase 4)**: Depends on all user stories being complete.

### Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: User Story 1
3. **STOP and VALIDATE**: Test User Story 1 independently. The app should correctly calculate valid expressions.
4. Demo or deploy the MVP.

### Incremental Delivery

1. Complete MVP → A working (but fragile) calculator is ready.
2. Add User Story 2 → The calculator is now robust with error handling.
3. Complete Polish phase → The project is fully documented and ready for handoff.