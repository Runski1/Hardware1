import numpy as np

array = np.random.randint(0, 100, size=5)
print(array, type(array))

u = np.array([2, 3])
v = np.array([4, -7])
uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])

u_norm = np.linalg.norm(u)
v_norm = np.linalg.norm(v)
uu_norm = np.linalg.norm(uu)
vv_norm = np.linalg.norm(vv)

print("--Norms--")
print(f"u: {u_norm.round(2)}")
print(f"v: {v_norm.round(2)}")
print(f"uu: {uu_norm.round(2)}")
print(f"vv: {vv_norm.round(2)}")