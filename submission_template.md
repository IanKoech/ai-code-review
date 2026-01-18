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
- Type error vulnerability. The function assumes every item in the list is a string. If the list contains None, an integer, or a dictionary, the program will crash with a TypeError because it cannot perform an in check on non-string types.
- Extreme False Positives. The logic "is there an @ symbol" is not a validation check. Strings like "@@@", "admin@", or "me@localhost" are counted as "valid," which will lead to database corruption or failed mail deliveries later.

### Edge cases & risks
- Missing Domain Suffix: The code treats user@domain as valid. In real-world scenarios, a valid email almost always requires a Top-Level Domain (e.g., .com, .net).
- Whitespace Issues: An email like " test@example.com " might be considered valid here but fail in a login or mailing system because the code doesn't strip() leading or trailing spaces.
- Empty/Malformed Strings: An empty string "" passes the loop but a single "@" would be counted as a valid email address.

### Code quality / design issues
- Over-Simplified Logic: Using a simple membership test (in) for complex data like an email address violates the principle of "Least Astonishment"—a user expects "Valid" to mean "Usable."
- Performance: For extremely large datasets, a manual for loop is less efficient than Python’s built-in generator expressions.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Regex Integration: Replaced the simple @ check with a Regular Expression to ensure the email follows a username@domain.tld structure.
- Type Guarding: Added a check to ensure each element is a string before processing, preventing runtime crashes on "dirty" data.
- Whitespace Sanitization: Included .strip() to handle emails that accidentally include spaces.
- Input Validation: Added a guard clause to handle cases where the input emails might not be a list.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Non-String Elements: Pass a list like ["a@b.com", None, 123]. The original code would crash; the test ensures the new code skips them safely.
- No-Dot Scenarios: Pass "user@domain". This should be marked invalid to ensure the regex is correctly identifying the lack of a TLD.
- Special Characters: Test strings like "user name@example.com" (with a space) or "user@@example.com". These should fail validation to ensure data cleanliness.
- Empty List: Verify that an empty input returns 0 without errors.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- False Claim of Safety: It claims to "safely ignore invalid entries," but it actually crashes if an entry is not a string.
- Inaccurate Definition of "Valid": It implies a level of validation (checking for a real email) that the code does not actually perform.
- Logical Oversight: It doesn't mention that the function will accept nonsensical strings like "@@@@" as valid.

### Rewritten explanation
- This function performs a superficial check for the presence of the "@" symbol to identify email addresses, but it lacks the logic required to verify actual email validity. It is highly susceptible to TypeErrors if the input contains non-string data and fails to filter out malformed entries that lack a proper domain or suffix. The original logic provides a false sense of data integrity by counting any string containing an "@" as a valid, usable email address.

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
