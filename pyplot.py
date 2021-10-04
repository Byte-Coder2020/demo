import pygal

from die import Die

# 创建一个六面的骰子
die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

