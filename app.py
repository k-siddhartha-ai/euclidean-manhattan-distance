# Visualization and Comparison of Euclidean and Manhattan Distance in Machine Learning

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Euclidean vs Manhattan Distance", layout="centered")

st.title("📏 Euclidean vs Manhattan Distance")
st.write("Visual comparison of distance metrics used in Machine Learning")

# Sidebar
st.sidebar.header("Select Points")

p_x = st.sidebar.slider("Point P - X", 0, 10, 2)
p_y = st.sidebar.slider("Point P - Y", 0, 10, 3)

q_x = st.sidebar.slider("Point Q - X", 0, 10, 8)
q_y = st.sidebar.slider("Point Q - Y", 0, 10, 7)

p = np.array([p_x, p_y])
q = np.array([q_x, q_y])

# Distance calculations
euclidean = np.sqrt((q[0] - p[0])**2 + (q[1] - p[1])**2)
manhattan = abs(q[0] - p[0]) + abs(q[1] - p[1])

st.subheader("📐 Distance Values")
st.write(f"**Euclidean Distance:** {euclidean:.3f}")
st.write(f"**Manhattan Distance:** {manhattan:.3f}")

# Distance path plot
st.subheader("🧭 Distance Path Comparison")

fig1, ax1 = plt.subplots()
ax1.scatter(p[0], p[1], s=100, label="Point P")
ax1.scatter(q[0], q[1], s=100, label="Point Q")

ax1.plot([p[0], q[0]], [p[1], q[1]], linewidth=2, label="Euclidean Path")
ax1.plot([p[0], q[0], q[0]], [p[1], p[1], q[1]], linewidth=2, label="Manhattan Path")

ax1.set_aspect("equal")
ax1.set_xlabel("X-axis")
ax1.set_ylabel("Y-axis")
ax1.legend()

st.pyplot(fig1)

# Heatmaps
st.subheader("🌈 Distance Field Heatmaps")

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)

euclidean_grid = np.sqrt((X - p[0])**2 + (Y - p[1])**2)
manhattan_grid = np.abs(X - p[0]) + np.abs(Y - p[1])

fig2, ax2 = plt.subplots(1, 2, figsize=(10, 4))

# Euclidean heatmap
im1 = ax2[0].imshow(
    euclidean_grid,
    cmap="coolwarm",
    extent=[0, 10, 0, 10],
    origin="lower"
)
ax2[0].scatter(p[0], p[1], color="white", marker="*", s=120)
ax2[0].set_title("Euclidean Distance Field")
plt.colorbar(im1, ax=ax2[0])

# Manhattan heatmap
im2 = ax2[1].imshow(
    manhattan_grid,
    cmap="coolwarm",
    extent=[0, 10, 0, 10],
    origin="lower"
)
ax2[1].scatter(p[0], p[1], color="white", marker="*", s=120)
ax2[1].set_title("Manhattan Distance Field")
plt.colorbar(im2, ax=ax2[1])

st.pyplot(fig2)

# Footer
st.markdown("---")
st.markdown("Built with **Streamlit**, **NumPy**, and **Matplotlib**")

