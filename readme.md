# PSN Code Test 
By : PSN team

## Requirement 

- Programming language: python / golang / php (choose one)
- 24 Hours, (counted from the question is sent).
- create new repo in your github account which name (psn-aiauto-test-anwers)
- add github account [@tripang1702] to your repository answer.
- add readme.md for detail answer is a plus.

## Question
Given the following csv data :

| Epoch Time | Value |
| --- | --- |
1704042000000|1
1704042026000|1
1704042035000|1
1704042037000|1
1704042059000|Null
1704042060000|1
1704042070000|1
1704042086000|0
1704042097000|0
1704042098000|0
1704042119000|0
1704042120000|0
1704042134000|0
1704042146000|0
1704042156000|Null
1704042157000|
1704042179000|0
1704042180000|0

which means this is a historical data from some device network. Value = 1 that means device was down, and Value = 0 that means device was up. Please calculate how long the device was down referred by csv data (in second).

Note :
- If you find Null or "" value in some row, convert that value to the last non-null value before it self.  
- for calculation, please use `device_network_data.csv` in this repository.

Example :
- example 1 

```python 
data_test_1 = [
    (1704042000000, 0),
    (1704042026000, 1),
    (1704042035000, 1),
    (1704042037000, 0),
    (1704042059000, 1),
    (1704042060000, 1)
]
```

Expected Output:
Total Downtime: 12 seconds

- example 2 
```python
data_test_2 = [
    (1704042000000, 1),
    (1704042026000, 1),
    (1704042035000, 1),
    (1704042037000, 1),
    (1704042059000, 1),
]
```

Expected Output:
Total Downtime: 59 seconds