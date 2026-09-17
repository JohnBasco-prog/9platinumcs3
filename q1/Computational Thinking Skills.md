# Computational Thinking Exercise
## [Smart School Canteen Queue]
**John Nathan R. Basco**
**9 - Platinum:**
**Basco:**
**8/21/26:**
## Step 1: Identify the Big Problem
### Main problem
The School canteen’s service is slow.
## Step 2: Identify the Sub-Problems
### Sub-problem
Some students take too long to order.
Manual calculation of totals and give change.
No system to track food
Only 2 cashiers max to take orders
## Step 3: Apply Computational Thinking Skills
|Some students take too long to order.|Pattern recognition|Introduce an online app that takes
their order|
|Manual calculation of totals and give change.|Algorithms|make automatic calculation on the
app|
|No system to track food|Algorithms|create an online inventory that deducts products that are
bought|
|Only 2 cashiers max to take orders|abstraction|introduce an online app that takes orders to
reduce work on the cashiers|

## Step 4: Algorithmic Solution
### Selected Sub-Problem
Some students take too long to order.
### Pseudocode
START
DISPLAY menu items
TAKE ORDER of the user
STORE the selected menu items
SUM = total of stored order prices
TAKE PAYMENT let the user enter their amount of money
CHECK if the user has sufficient money
IF MONEY => SUM
DISPLAY “please proceed to the cashier to claim receipt”
ELSE:
“Insufficient funds, re enter again”

END

## Step 4: Algorithmic Solution
### Selected Sub-Problem
Manual calculation of totals and give change.
### Pseudocode
START
DISPLAY menu items
TAKE ORDER of the user
STORE the selected menu items
SUM = total of stored order prices
IF user money => SUM:
User money - SUM = change
Else:
Insufficient funds
DISPLAY
“SUM, CHANGE”
END

## Step 4: Algorithmic Solution
### Selected Sub-Problem
No system to track food
### Pseudocode
START
LIST products for sale
DISPLAY products for sale using the app
DEDUCT product selected by user
DISPLAY remaining products
IF num of remaining products > user purchased:
DEDUCT product selected by user
DISPLAY “thank you for purchasing”
Elif:
num of remaining products < user purchased
DISPLAY “ less products than user selected”
Else:
Insufficient products

END

## Step 4: Algorithmic Solution
### Selected Sub-Problem
Only 2 cashiers max to take orders
### Pseudocode
START
DISPLAY menu items
TAKE ORDER of the user

STORE the selected menu items
SUM = total of stored order prices
TAKE PAYMENT let the user enter their amount of money
CHECK if the user has sufficient money
IF MONEY => SUM
DISPLAY “please proceed to the cashier to claim receipt”

END
