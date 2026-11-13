import matplotlib.pyplot as plt

numbers = [72, 75, 71, 78, 74]
average = sum(numbers) / len(numbers)
print("הממוצע:", average)

plt.plot(range(1, len(numbers) + 1), numbers, marker="o", label="Numbers")
plt.axhline(y=average, color="red", linestyle="--", label=f"Average = {average}")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.savefig("graph.png")
plt.show()
