import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. Machine Learning & AI Algorithms
# Here we perform a simple linear regression using numpy's polyfit.
# This basic ML concept is further explored in the B.S. in Software Engineering.
# =============================================================================
# Generate some data: y = 2x + 1 with a bit of noise
x = np.array([1, 2, 3, 4, 5])
y = 2 * x + 1 + np.random.randn(5) * 0.5  # random noise added for fun
# Fit a line to the data
coeffs = np.polyfit(x, y, 1)
print(f"[ML] Fitted line: y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}")

# =============================================================================
# 2. Analyzing Forces in Equilibrium
# Solve for unknown forces when the net force is zero.
# In our example, we set up equations based on the equilibrium condition.
# This topic is further explored in the B.S. in Mechanical Engineering.
# =============================================================================
# For an object in equilibrium: Sum of forces in x and y directions equals zero.
# We set up the system:
#   2F1 + 3F2 = 10   (force balance in the x-direction)
#   4F1 -  F2 = 2    (force balance in the y-direction)
A = np.array([[2, 3],
              [4, -1]])
B = np.array([10, 2])
F = np.linalg.solve(A, B)
print(f"[Equilibrium] Calculated forces: F1 = {F[0]:.2f} N, F2 = {F[1]:.2f} N")

# =============================================================================
# 3. Calculating Electrical Circuits
# Analyze a circuit with two voltage sources and resistors using Kirchhoff's laws.
# This exercise is typical in the B.S. in Electrical Engineering.
# =============================================================================
# Consider a simple circuit with two loops:
# Loop 1: 10V - (R1 * I1) - (R3 * (I1 - I2)) = 0, where R1 = 2 ohm, R3 = 1 ohm.
# Loop 2:  5V - (R2 * I2) - (R3 * (I2 - I1)) = 0, where R2 = 3 ohm.
# Rearranging the equations:
#   3I1 -  I2 = 10
#   -I1 + 4I2 =  5
A_circuit = np.array([[3, -1],
                      [-1, 4]])
B_circuit = np.array([10, 5])
I = np.linalg.solve(A_circuit, B_circuit)
print(f"[Circuits] Loop currents: I1 = {I[0]:.2f} A, I2 = {I[1]:.2f} A")

# =============================================================================
# 4. Projectile Trajectory with Air Resistance
# Simulate the flight of a projectile taking into account gravity and a simple drag force.
# For an in-depth look at this topic, see courses in the B.S. in Aerospace Engineering.
# =============================================================================
# Initial conditions for the projectile
v0 = 50  # initial speed in m/s
theta = np.deg2rad(45)  # launch angle in radians (45° for max range)
vx = v0 * np.cos(theta)
vy = v0 * np.sin(theta)
g = 9.81  # gravitational acceleration (m/s^2)
k = 0.1   # drag coefficient (simplified linear air resistance)
dt = 0.01  # time step for simulation

# Initialize lists to store the trajectory data
x_pos = [0]
y_pos = [0]
t = 0
x, y = 0, 0

# Simulate until the projectile lands (y < 0)
while y >= 0:
    # Calculate accelerations: drag acts opposite to velocity
    ax = -k * vx
    ay = -g - k * vy
    # Update velocity and position using Euler's method
    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt
    x_pos.append(x)
    y_pos.append(y)
    t += dt

# Plot the trajectory
plt.figure(figsize=(8, 4))
plt.plot(x_pos, y_pos, label="Trajectory")
plt.title("Projectile Motion with Air Resistance")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.legend()
plt.show()

