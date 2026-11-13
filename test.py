import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

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

# --- PPG signal simulation (sine wave + noise) and peak detection ---
fs = 100            # sampling rate [Hz]
duration = 10       # [sec]
heart_rate = 72     # [bpm]
f_heart = heart_rate / 60  # [Hz]

rng = np.random.default_rng(0)
t = np.arange(0, duration, 1 / fs)
ppg = np.sin(2 * np.pi * f_heart * t) + 0.1 * rng.standard_normal(len(t))

# Peaks must be at least ~0.5 period apart and clearly above the noise
min_distance = int(0.5 * fs / f_heart)
peaks, _ = find_peaks(ppg, distance=min_distance, height=0.5)

print("מספר פיקים:", len(peaks))
if len(peaks) > 1:
    rr = np.diff(t[peaks])
    print("דופק משוער:", round(60 / rr.mean(), 1), "bpm")

plt.figure()
plt.plot(t, ppg, label="PPG (simulated)")
plt.plot(t[peaks], ppg[peaks], "rx", markersize=10, label="Peaks")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.savefig("ppg.png")
plt.show()
