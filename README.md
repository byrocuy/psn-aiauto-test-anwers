# PSN Code Answer

This is solution for PSN Code Test. There are two files that contain the same solution:
- [`assignment.ipynb`](./assignment.ipynb) is the Jupyter Notebook file. It contains the solution and detailed explanation step by step how I approach the problem.
- [`assignment.py`](./assignment.py) is the Python file that can be run in terminal. See the [instruction](#how-to-run-the-python-file) below.

## How to run the Python file
Clone the repository and run the following command in terminal:

```bash
python assignment.py --file_path <path_to_csv_file>
```
example: 
```bash
python assignment.py --file_path ./device_network_data.csv
```

Sample output:
```
Total Downtime: 58310 seconds
```
## General Overview
_You can refer to the [`assignment.ipynb`](assignment.ipynb) file for detailed step-by-step explanation with the code._

For a general overview, here are the steps I took to solve the problem:
- After reading the CSV file, inspect the general data information and check if there are any missing values.
- If there are missing values, fill them with the appropriate value, in this case we fill with the non-null previous value.
- Convert column type to appropriate data type if necessary. Add any additional columns if needed.
- Calculate the downtime by iterating through the dataset before the last one**. 
    - If the current `Value` is 1, calculate the downtime by subtracting the current timestamp with the next timestamp. Take only the seconds part and add it to the total downtime.
    - Return the total downtime after the iteration is finished.

** we only iterate before the last, i.e. `len(data) - 1`, because we need to compare the current value with the next value. If we iterate through the last data point, we will get an error because there is no next data point to compare with, we can handle this by using `try-except` though, but we will avoid it for simplicity.