import numpy as np
import matplotlib.pyplot as plt

def simulate_projectile(v0=30, angle_deg=60, g=9.8):
    plt.close('all')
    theta = np.radians(angle_deg)
    v0x = v0 * np.cos(theta)
    v0y = v0 * np.sin(theta)
    t_flight = 2 * v0y / g
    t = np.linspace(0, t_flight, 500)
    x = v0x * t
    y = v0y * t - 0.5 * g * t**2
    vx = np.full_like(t, v0x)
    vy = v0y - g * t
    ax = np.zeros_like(t)
    ay = np.full_like(t, -g)
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs[0, 0].plot(x, y)
    axs[0, 0].set_title('Trajectory (x vs y)')
    axs[0, 0].set_xlabel('x (m)')
    axs[0, 0].set_ylabel('y (m)')
    axs[0, 1].plot(t, x, label='x(t)')
    axs[0, 1].plot(t, y, label='y(t)')
    axs[0, 1].legend()
    axs[0, 1].set_title('Position vs Time')
    axs[1, 0].plot(t, vx, label='vx(t)')
    axs[1, 0].plot(t, vy, label='vy(t)')
    axs[1, 0].legend()
    axs[1, 0].set_title('Velocity vs Time')
    axs[1, 1].plot(t, ax, label='ax(t)')
    axs[1, 1].plot(t, ay, label='ay(t)')
    axs[1, 1].legend()
    axs[1, 1].set_title('Acceleration vs Time')
    plt.tight_layout()
    plt.show()