temperatures = []
for i in range(6):
    temperature = float(input("请输入第{}个温度值：".format(i+1)))
    temperatures.append(temperature)

max_temperature = max(temperatures)
min_temperature = min(temperatures)
average_temperature = sum(temperatures) / len(temperatures)

print("最大值：{:.2f}".format(max_temperature))
print("最小值：{:.2f}".format(min_temperature))
print("平均值：{:.2f}".format(average_temperature))