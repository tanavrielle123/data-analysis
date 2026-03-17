import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Hour": [6,7,8,9,10,11,12,17,18,19,20],
    "Passengers": [2000, 5000, 9000, 7000, 3000, 2500, 2800, 8000, 9500, 6000, 3500]
}

df = pd.DataFrame(data)

plt.plot(df["Hour"], df["Passengers"])
plt.title("Peak Hour Pattern")
plt.xlabel("Hour")
plt.ylabel("Passenger Volume")
plt.show()

print(df.loc[df["Passengers"].idxmax()])
