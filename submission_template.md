# AI Code Review Assignment (Python)

## Candidate
- Name: Ian Koech
- Approximate time spent:  

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Zero Division Crash. If [] is passed as a param to the function, count becomes 0. The division on the return statement  wil trigger a `ZeroDivisonError` breaking the program.

- Logic Error (Incorrect calculation). The count includes cancelled orders while the total excludes them.

### Edge cases & risks
- Missing Dataset - We fail to account for scenarios where an empty array is passed as a param to the function.
- Missing keys, program assumes every dictionary has a `status` as well as an `amount` property. A single object in the array without either key will result in a `KeyError`
- All orders in the param passed cancelled, it currently returns $0 as the order value if all orders passed have $0  in amount. Logic could explicitly dictate what the intended value returned for a user with no succesful orders is

### Code quality / design issues
- Manual Iteration. Using a for loop coupled with a manual total count could be subject to some "off" errors although unlikely.
- Lack of type safety checks. The code would need a way to ensure that the type of the value in `order[amount]` is a number and never a string .
- Hardcoded statuses, a better code principle would be  to have an enum of the order status saved.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added guard clauses to immediately check for empty input and avoid a `ZeroDivisonError`
- Added a filter logic that ensures the `count` used for average calculation only includes the orders that have been summed(excluding the cancelled orders)
- Readability improved.  Now includes a list comprehension or the sum() function that  makes it more concise.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Empty List, there's a need to verify this before it becomes production ready to verify that no `ZeroDivisonErrors`occur. Some users may not have a transaction history and some users might be new to the system.
- A dilution logic with some cancelled and completed orders to verify mathematical correctness.
- Data integrity, Passing some objects in the  param without either keys in place, as well as passing some object with string values in place of integer values


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- False claim of correctness, the cliaim of exclusion of cancelled orders isn't correct as its excluded from the numerator(total) and not the denominator(count)
- Failure to mention code crashes when input is an empty list

### Rewritten explanation
- This function attempts to calculate the Average Order Value (AOV) by summing the revenue from successful orders, but it introduces a calculation error by dividing that sum by the total count of all orders, including cancelled ones. This approach results in a mathematically deflated average and leaves the system vulnerable to a fatal ZeroDivisionError if the input list is empty. Furthermore, the function lacks defensive checks for missing data keys and is strictly case-sensitive, meaning any status other than the exact lowercase string "cancelled" will be erroneously included in the financial totals.

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
