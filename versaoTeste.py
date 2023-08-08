import numpy as np
import matplotlib.pyplot as plt

def projetil(V_inicial, teta, drag = True):
  g = 9.8
  m = 2
  C = 0.45
  r = 0.5
  S = np.pi*pow(r, 2)
  ro_mars = 0.0175
  teta = (teta*np.pi)/180

  time = np.linspace(0, 100, 1000)
  tof = 0.0
  dt = time[1] - time[0]
  gravity = -g * m
  V_ix = V_inicial * np.cos(teta)
  V_iy = V_inicial * np.sin(teta)
  v_x = V_ix
  v_y = V_iy
  r_x = 0.0
  r_y = 0.0
  r_xs = list()
  r_ys = list()
  r_xs.append(r_x)
  r_ys.append((r_y))

  for t in time:
    F_x = 0.0
    F_y = 0.0

    F_y = F_y - 0.5*C*S*ro_mars*pow(v_y, 2)
    F_x = F_x - 0.5*C*S*ro_mars*pow(v_x, 2) * np.sign(v_y)
    F_y = F_y + gravity

    r_x = r_x + v_x * dt + (F_x / (2 * m)) * dt ** 2
    r_y = r_y + v_y * dt + (F_y / (2 * m)) * dt ** 2
    v_x = v_x + (F_x / m) * dt
    v_y = v_y + (F_y / m) * dt

    if (r_y >= 0.0):
      r_xs.append(r_x)
      r_ys.append(r_y)
    else:
      tof = t
      r_xs.append(r_x)
      r_ys.append(r_y)
      break

  return r_xs, r_ys, tof

v = 20
teta =120

fig = plt.figure(figsize=(7,4), dpi=150)
r_xs, r_ys, tof = projetil(v, teta, False)
plt.plot(r_xs, r_ys, label="Gravity")
plt.title("Trajectory", fontsize=10)
plt.xlabel("Displacement in x-direction (m)")
plt.ylabel("Displacement in y-direction (m)")
plt.ylim(bottom=0.0)
plt.legend()
plt.show()
