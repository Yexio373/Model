temperatures = []
for i in range(6):
    temperature = float(input("Input the tem{}：".format(i+1)))
    temperatures.append(temperature)

max_temperature = max(temperatures)
min_temperature = min(temperatures)
average_temperature = sum(temperatures) / len(temperatures)

print("max：{:.2f}".format(max_temperature))
print("min：{:.2f}".format(min_temperature))
print("ave：{:.2f}".format(average_temperature))