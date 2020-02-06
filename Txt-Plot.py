from matplotlib import pyplot as plt
import re


with open('snippets.txt', 'rt') as myfile:
    text = myfile.read()

matched_lines = [line for line in text.split('\n') if "dev_x" in line]
x = matched_lines[0]

matched_lines = [line for line in text.split('\n') if "dev_y" in line]
y = matched_lines[0]


x = re.findall(r'\d+', x)
y = re.findall(r'\d+', y)

plt.bar(x, y)

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.show()