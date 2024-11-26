"""
 * author: Ohidul Islam
 * created on 11-10-2024-12h-07m
 * copyright 2024
"""

from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
from numpy import transpose


plt.rcParams.update({"font.family": "Times new Roman", "font.size": 20})

# file_path = "transfer-Hz-6x6.mat"
file_path = "input_probe-Hz-1x3.mat"
data = loadmat(file_path)
# print(data.keys())
in_Hz = np.array(data["probe_Hz"])

file_path = "output_probe-Hz-1x3.mat"
data = loadmat(file_path)
out_Hz = np.array(data["probe_Hz"])

# print(Hz.shape)

in_amp = np.abs(in_Hz)
in_phase = np.angle(in_Hz)
out_amp = np.abs(out_Hz)
out_phase = np.angle(out_Hz)

print(f"input amplitude:\n {in_amp}")
print(f"input phase:\n {in_phase}")
print(f"output amplitude:\n {out_amp}")
print(f"output phase:\n {out_phase}")
# print(out_amp)


# T_amp = out_amp_norm @ np.linalg.inv(in_amp_norm)
# T_amp = np.dot(out_amp, np.linalg.inv(in_amp))


fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(in_amp)
ax[0].set_title("Input Probe (Amp)")

ax[1].imshow(out_amp)
ax[1].set_title("Output Probe (Amp)")

# ax[2].imshow(T_amp)
# ax[2].set_title("Transfer Matrix (Amp)")

# in_test = in_amp[:, 0]
# out_test = np.dot(T_amp, in_test)

# print(f"input amplitude (1st column):\n {in_test}")
# print(f"output amplitude (1st column):\n {out_test}")

# fig, ax = plt.subplots(1, 2, figsize=(10, 5))
# ax[0].imshow(in_test.reshape((6, 1)))
# ax[0].set_title("1st column (input)")
# ax[0].axis("off")
# ax[1].imshow(out_test.reshape((6, 1)))
# ax[1].set_title("1st column (output)")
# ax[1].axis("off")

plt.show()
