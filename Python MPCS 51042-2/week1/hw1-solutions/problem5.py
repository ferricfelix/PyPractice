import csv
import sys


N = int(sys.argv[1])

with open('employees.csv', 'r', newline='') as csv_file:
    data = []
    for employee in csv.DictReader(csv_file):
        # Skip hourly employees
        if employee['Salary or Hourly'] == 'Hourly':
            continue

        # Get name and salary (as a float)
        name = employee['Name']
        salary = float(employee['Annual Salary'][1:])

        # Add salary and name to list we will sort later
        data.append((salary, name))

# Sort the data relying on the fact that salary is first in the tuple
data.sort(reverse=True)

# Show the N highest paid employees
for employee in data[:N]:
    salary, name = employee
    print(f'{name}: {salary}')
