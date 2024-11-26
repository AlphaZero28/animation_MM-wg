"""
 * author: Ohidul Islam
 * created on 09-10-2024-16h-10m
 * copyright 2024
"""

from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
from numpy import transpose


plt.rcParams.update({"font.family": "Times new Roman", "font.size": 20})

# file_path = "transfer-Hz-6x6.mat"
file_path = "input_probe-Hz-6x6_final.mat"
data = loadmat(file_path)
# print(data.keys())
in_Hz = np.array(data["probe_Hz"])

file_path = "output_probe-Hz-6x6_final.mat"
data = loadmat(file_path)
out_Hz = np.array(data["probe_Hz"])
print(out_Hz)

# print(Hz.shape)

in_amp = np.abs(in_Hz)
out_amp = np.abs(out_Hz)

print(f"input amplitude:\n {in_amp}")
print(f"output amplitude:\n {out_amp}")
# print(out_amp)


# T_amp = out_amp_norm @ np.linalg.inv(in_amp_norm)
T_amp = np.dot(out_amp, np.linalg.inv(in_amp))


fig, ax = plt.subplots(1, 3, figsize=(15, 5))
im = ax[0].imshow(in_amp)
ax[0].set_title("Input Probe (Amp)")
# fig.colorbar(im, ax=ax[0])

im2 = ax[1].imshow(out_amp)
ax[1].set_title("Output Probe (Amp)")
# fig.colorbar(im2, ax=ax[1])

im3 = ax[2].imshow(T_amp)
ax[2].set_title("Transfer Matrix (Amp)")
# fig.colorbar(im3, ax=ax[2])

# in_test = in_amp[:, 0]
# out_test = np.dot(T_amp, in_test)

# print(out_Hz)
# plt.figure()
# plt.imshow(np.angle(out_Hz))
# plt.colorbar()

# print(f"input amplitude (1st column):\n {in_test}")
# print(f"output amplitude (1st column):\n {out_test}")

# fig, ax = plt.subplots(1, 2, figsize=(10, 5))
# ax[0].imshow(in_test.reshape((6, 1)))
# ax[0].set_title("1st column (input)")
# ax[0].axis("off")
# ax[1].imshow(out_test.reshape((6, 1)))
# ax[1].set_title("1st column (output)")
# ax[1].axis("off")

# Save the figure to a file
filename = 'transfer-matrix.png'
plt.tight_layout()
fig.savefig(filename, dpi=300)

print(f"Figure saved as {filename} in the current directory.")
plt.show()
