import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Euclidean vs Manhattan Distance")

st.title("📏 Euclidean vs Manhattan Distance")

# Sidebar inputs
p_x = st.sidebar.slider("Point P - X", 0, 10, 2)
p_y = st.sidebar.slider("Point P - Y", 0, 10, 3)

q_x = st.sidebar.slider("Point Q - X", 0, 10, 8)
q_y = st.sidebar.slider("Point Q - Y", 0, 10, 7)

p = np.array([p_x, p_y])
q = np.array([q_x, q_y])

# Distance calculations
euclidean = np.sqrt((q[0]-p[0])**2 + (q[1]-p[1])**2)
manhattan = abs(q[0]-p[0]) + abs(q[1]-p[1])

st.subheader("Distance Values")
st.write(f"Euclidean Distance: {euclidean:.3f}")
st.write(f"Manhattan Distance: {manhattan:.3f}")

# Plot
fig, ax = plt.subplots()
ax.scatter(p[0], p[1], s=100, label="Point P")
ax.scatter(q[0], q[1], s=100, label="Point Q")
ax.plot([p[0], q[0]], [p[1], q[1]], linewidth=2, label="Euclidean")
ax.plot([p[0], q[0], q[0]], [p[1], p[1], q[1]], linewidth=2, label="Manhattan")
ax.set_aspect("equal")
ax.legend()
st.pyplot(fig)
