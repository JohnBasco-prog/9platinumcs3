# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
Changed Food Schedule(String) to Is_available(Boolean)
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
|food_name |string |Private |There are individual food names for different kinds of food |
|food_price |int |Private |There are individual food prices for different kinds of food |
|food_description |string |Private |There are individual food descripitons for different kinds of food |
|is_available |boolean |Public |True and False determine if a food is on stock or not, this can be shared among different food |
## Updated UML Class Diagram
<img width="1067" height="611" alt="Screenshot 2026-09-09 213653" src="https://github.com/user-attachments/assets/183feebc-eb35-4050-9659-24190d45b75f" />

## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
