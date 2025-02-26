import numpy as np  # Because reinventing the wheel is for chumps

# Define the coefficients matrix (A)
A = np.array([[2, 3],  # 2x + 3y
              [4, -1]]) # 4x - y

# Define the results matrix (B)
B = np.array([12, 5])  # The numbers on the other side of the equations

# Solve for X (the mythical values of x and y)
solution = np.linalg.solve(A, B)

# Print the results like we did something impressive
print(f"Behold! The solution is: x = {solution[0]:.2f}, y = {solution[1]:.2f}")
