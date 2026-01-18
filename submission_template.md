# AI Code Review Assignment (Python)

## Candidate
- Name: Ian Koech
- Approximate time spent: 1hr 10 minutes 

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
- `ZeroDivisionCrash` , If an empty list [] is passed, count becomes 0, causing the program to crash with a `ZeroDivisionError` on the return statement.
- Mathematical `Dilution Error`,  The count is set to the length of the entire input list, but the total only sums non-null values.
- Unchecked Type Casting, The code calls float(v) without a try/except block. If the list contains a string that cannot be converted, the function will crash with a ValueError

### Edge cases & risks
- Empty or All-None Lists, If the list contains only None values, the code still attempts to divide by the original length, resulting in 0 / len, which might be mathematically misleading or crash if the list is empty.
- Input Type Integrity, The function does not verify if the input is actually a list. Passing a single number or a string will cause an iteration error.

### Code quality / design issues
- Static Denominator, Calculating the count at the start is a rigid design choice that fails to account for the filtering happening inside the loop.
- Lack of Resilience, The function is "brittle", it assumes the data is either a valid number or None, with no middle ground for "dirty" data.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Synchronized Counting, Updated the logic to only increment the counter (or use the length of a filtered list) when a value is successfully processed.
- Error Trapping, Added a try/except block around the float() conversion to gracefully skip non-numeric strings instead of crashing.
- Zero-State Handling, Added guard clauses to return 0.0 if the list is empty or if no valid measurements are found after filtering.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Mixed Data Types, Pass a list like [10, "20", "invalid", None]. This tests if the function can extract the 10 and 20, skip the "invalid" string without crashing, and ignore the None.
- The "All None" Test, Pass [None, None]. This verifies that the function doesn't return 0.0 due to a dilution error, but rather handles it as a "no data" scenario.
- Empty Dataset,  Pass [] to ensure the ZeroDivisionError has been successfully patched.
- Large Floating Point Precision, Test with very small or very large decimals to ensure float() conversion maintains necessary precision.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- False Claim of Accuracy, It claims to "ensure an accurate average," yet the math is fundamentally broken because it divides by the wrong count.
- False Claim of Safety, It claims to "safely handle mixed input types," but it will actually crash if it encounters a non-numeric string or an empty list.
- Misleading Logic, It implies None is the only "invalid" type, ignoring other potential data errors.

### Rewritten explanation
- This function attempts to average a list of measurements but contains a critical calculation flaw: it includes missing values (None) in the divisor while excluding them from the dividend. This results in an artificially deflated average. Additionally, the function is not "safe" for production use, as it lacks error handling for non-numeric strings and will trigger a fatal crash if provided with an empty dataset. A robust version must synchronize the count with the valid entries and implement defensive type-casting to ensure mathematical integrity and application stability.

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
