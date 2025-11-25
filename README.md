# Deadline Countdown Microservice 
This microservice calculates how many days are left until a user-specified deadline. It runs locally and uses standard input/output to return the number of remaining days.
How It Works

The program prompts the user to enter a date in the format:
```
MM-DD-YYYY
```

### The microservice checks:
- whether the date is valid
- whether the date is in the future
### It prints either:
- the number of days remaining, or
- an error message for invalid or past dates
#### Example
Input:
```
Enter deadline date (MM-DD-YYYY): 12-25-2025
```
Output:
```
There are 423 days left until 12-25-2025
```

If the date is invalid or already passed:
```
Invalid deadline date. Please enter a future date.
```
Files Included
- ```countdown_service.py — main microservice logic```
- ```test_countdown.py — simple test file```
- ```README.md — documentation```
- 
How to Run
In a terminal, run:
```
python3 countdown_service.py
```
Enter a date when prompted.

How to Run the Tests
```
python3 test_countdown.py
```
