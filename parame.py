# import matplotlib
# matplotlib.use("TkAgg")  # Needed for live animation in PyCharm
#
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# from matplotlib.widgets import Button
#
# # -----------------------------
# # Path on sphere
# # -----------------------------
# def r(t):
#     """
#     A curve constrained to the unit sphere.
#     """
#     return np.array([
#         np.cos(t) * np.sin(2*t),
#         np.sin(t) * np.sin(2*t),
#         np.cos(2*t)
#     ])
#
# def tangent(t):
#     """
#     Derivative r'(t), tangent to the sphere surface.
#     """
#     return np.array([
#         -np.sin(t)*np.sin(2*t) + 2*np.cos(t)*np.cos(2*t),
#          np.cos(t)*np.sin(2*t) + 2*np.sin(t)*np.cos(2*t),
#         -2*np.sin(2*t)
#     ])
#
# # -----------------------------
# # Setup figure
# # -----------------------------
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(111, projection="3d")
# plt.subplots_adjust(bottom=0.15)
#
# # Sphere surface
# u = np.linspace(0, 2*np.pi, 60)
# v = np.linspace(0, np.pi, 30)
#
# X = np.outer(np.cos(u), np.sin(v))
# Y = np.outer(np.sin(u), np.sin(v))
# Z = np.outer(np.ones_like(u), np.cos(v))
#
# ax.plot_surface(X, Y, Z, alpha=0.18, linewidth=0)
#
# # Initial point
# t0 = 0.2
# p0 = r(t0)
# T0 = tangent(t0)
# T0 = T0 / np.linalg.norm(T0)
#
# # Point moving on sphere
# point, = ax.plot([p0[0]], [p0[1]], [p0[2]], "o", markersize=8)
#
# # Radius vector from origin to point
# radius_vec = ax.quiver(
#     0, 0, 0,
#     p0[0], p0[1], p0[2],
#     length=1,
#     normalize=False
# )
#
# # Tangent vector at point
# tangent_vec = ax.quiver(
#     p0[0], p0[1], p0[2],
#     0.35*T0[0], 0.35*T0[1], 0.35*T0[2],
#     length=1,
#     normalize=False
# )
#
# # Trace curve
# trace_x, trace_y, trace_z = [], [], []
# trace_line, = ax.plot([], [], [], linewidth=2)
#
# # Text
# info_text = ax.text2D(
#     0.03, 0.95,
#     "",
#     transform=ax.transAxes,
#     fontsize=11
# )
#
# # Axes settings
# ax.set_xlim(-1.4, 1.4)
# ax.set_ylim(-1.4, 1.4)
# ax.set_zlim(-1.4, 1.4)
#
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")
#
# ax.set_title("Moving Vector on the Surface of a Sphere")
#
# # Make axes visually equal
# ax.set_box_aspect([1, 1, 1])
#
# # -----------------------------
# # Animation
# # -----------------------------
# t_vals = np.linspace(0.2, 8*np.pi, 500)
# is_paused = False
#
# def update(frame):
#     global radius_vec, tangent_vec
#
#     t = t_vals[frame]
#
#     p = r(t)
#     T = tangent(t)
#     T_hat = T / np.linalg.norm(T)
#
#     # Update point
#     point.set_data([p[0]], [p[1]])
#     point.set_3d_properties([p[2]])
#
#     # Remove old vectors
#     radius_vec.remove()
#     tangent_vec.remove()
#
#     # Radius vector from origin to point
#     radius_vec = ax.quiver(
#         0, 0, 0,
#         p[0], p[1], p[2],
#         length=1,
#         normalize=False
#     )
#
#     # Tangent vector sitting on surface
#     tangent_vec = ax.quiver(
#         p[0], p[1], p[2],
#         0.35*T_hat[0], 0.35*T_hat[1], 0.35*T_hat[2],
#         length=1,
#         normalize=False
#     )
#
#     # Update trace
#     trace_x.append(p[0])
#     trace_y.append(p[1])
#     trace_z.append(p[2])
#
#     trace_line.set_data(trace_x, trace_y)
#     trace_line.set_3d_properties(trace_z)
#
#     info_text.set_text(
#         rf"$t = {t:.2f}$" "\n"
#         rf"$r(t)=({p[0]:.2f}, {p[1]:.2f}, {p[2]:.2f})$" "\n"
#         rf"$\hat{{T}}=({T_hat[0]:.2f}, {T_hat[1]:.2f}, {T_hat[2]:.2f})$"
#     )
#
#     return point, trace_line, info_text
#
# ani = FuncAnimation(
#     fig,
#     update,
#     frames=len(t_vals),
#     interval=40,
#     blit=False,
#     repeat=True
# )
#
# # -----------------------------
# # Play/Pause Button
# # -----------------------------
# button_ax = plt.axes([0.42, 0.04, 0.16, 0.06])
# button = Button(button_ax, "Pause")
#
# def toggle_animation(event):
#     global is_paused
#
#     if is_paused:
#         ani.event_source.start()
#         button.label.set_text("Pause")
#         is_paused = False
#     else:
#         ani.event_source.stop()
#         button.label.set_text("Play")
#         is_paused = True
#
# button.on_clicked(toggle_animation)
#
# plt.show()
#

import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

# --------------------------------------------------
# Scalar function f(x, y)
# --------------------------------------------------
def f(x, y):
    return x**2 + y


# Gradient of f(x, y) = x^2 + y
# grad f = <2x, 1>
def grad_f(x, y):
    return np.array([2*x, 1])


# --------------------------------------------------
# Set up time values
# --------------------------------------------------
t_vals = np.linspace(0, 2*np.pi, 300)

# Circle points
theta = np.linspace(0, 2*np.pi, 400)
circle_x = np.cos(theta)
circle_y = np.sin(theta)


# --------------------------------------------------
# Create figure
# --------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 7))
plt.subplots_adjust(bottom=0.2)

ax.plot(circle_x, circle_y, label=r"$r(t)=\langle \cos t,\sin t\rangle$")

ax.axhline(0)
ax.axvline(0)
ax.grid(True)
ax.set_aspect("equal")
ax.set_xlim(-1.7, 1.7)
ax.set_ylim(-1.7, 1.7)
ax.set_title("Moving Vector on Unit Circle with Tangent Directional Derivative")

# Initial values
t0 = t_vals[0]
x0 = np.cos(t0)
y0 = np.sin(t0)

# Moving point
point, = ax.plot(x0, y0, "o", markersize=8)

# Radius vector r(t)
radius_vec = ax.quiver(
    0, 0, x0, y0,
    angles="xy",
    scale_units="xy",
    scale=1,
    label=r"$r(t)$"
)

# Tangent vector r'(t)
tangent_vec = ax.quiver(
    x0, y0, 0, 0,
    angles="xy",
    scale_units="xy",
    scale=1,
    label=r"$\hat{T}$"
)

# Text box
info_text = ax.text(
    -1.55, 1.35,
    "",
    fontsize=11,
    bbox=dict(facecolor="white", alpha=0.8)
)

ax.legend(loc="lower left")


# --------------------------------------------------
# Animation state
# --------------------------------------------------
is_paused = False


# --------------------------------------------------
# Update function
# --------------------------------------------------
def update(frame):
    global radius_vec, tangent_vec

    t = t_vals[frame]

    # Position vector r(t) = <cos(t), sin(t)>
    x = np.cos(t)
    y = np.sin(t)

    # Tangent vector r'(t) = <-sin(t), cos(t)>
    tangent = np.array([-np.sin(t), np.cos(t)])
    unit_tangent = tangent / np.linalg.norm(tangent)

    # Gradient of f at the point
    grad = grad_f(x, y)

    # Directional derivative in tangent direction
    D_tangent = np.dot(grad, unit_tangent)

    # Update moving point
    point.set_data([x], [y])

    # Remove old arrows
    radius_vec.remove()
    tangent_vec.remove()

    # Draw updated radius vector
    radius_vec = ax.quiver(
        0, 0, x, y,
        angles="xy",
        scale_units="xy",
        scale=1
    )

    # Draw updated tangent vector
    tangent_vec = ax.quiver(
        x, y,
        0.5 * unit_tangent[0],
        0.5 * unit_tangent[1],
        angles="xy",
        scale_units="xy",
        scale=1
    )

    # Update text
    info_text.set_text(
        rf"$t = {t:.2f}$" "\n"
        rf"$r(t) = ({x:.2f}, {y:.2f})$" "\n"
        rf"$\hat{{T}} = ({unit_tangent[0]:.2f}, {unit_tangent[1]:.2f})$" "\n"
        rf"$\nabla f = ({grad[0]:.2f}, {grad[1]:.2f})$" "\n"
        rf"$D_{{\hat{{T}}}} f = {D_tangent:.2f}$"
    )

    return point, radius_vec, tangent_vec, info_text


# --------------------------------------------------
# Create animation
# --------------------------------------------------
ani = FuncAnimation(
    fig,
    update,
    frames=len(t_vals),
    interval=40,
    blit=False,
    repeat=True
)


# --------------------------------------------------
# Play / Pause button
# --------------------------------------------------
button_ax = plt.axes([0.42, 0.05, 0.16, 0.07])
button = Button(button_ax, "Pause")


def toggle_animation(event):
    global is_paused

    if is_paused:
        ani.event_source.start()
        button.label.set_text("Pause")
        is_paused = False
    else:
        ani.event_source.stop()
        button.label.set_text("Play")
        is_paused = True


button.on_clicked(toggle_animation)


# --------------------------------------------------
# Show plot
# --------------------------------------------------
plt.show()