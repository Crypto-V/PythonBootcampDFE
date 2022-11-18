import numpy as np
import matplotlib.pyplot as plt

cw = np.array([54, 67, 40, 82, 72, 43, 33, 73, 53, 80, 42, 63, 88, 29, 55, 60])
ex = np.array([59, 61, 37, 78, 67, 36, 40, 68, 48, 59, 36, 60, 91, 25, 54, 64])

overall = np.ceil((cw + ex) / 2)
print(overall)
counter = 0
counterD = 0
counterP = 0
counterF = 0

for i in overall:
    counter+=1
    if i >= 70:
        print(f"Student {counter} got grade D", i)
        counterD += 1
    elif i >= 40:
        print(f"Student {counter} got grade P", i)
        counterP += 1
    else:
        print(f"Student {counter} got grade F", i)
        counterF += 1

print(f"D: {counterD} , P: {counterP} , F: {counterF}")

plt.plot(cw, ex)
plt.xlabel("coursework")
plt.ylabel("exam")
plt.show()