import numpy as np
import matplotlib.pyplot as plt

# 4 разных случая
funcs = [
    lambda x: (x-1.5)**2 - 0.5,           
    lambda x: -(x-1.5)**2 + 0.5,           
    lambda x: -np.sqrt(x-1) + 0.5,         
    lambda x: np.sqrt(2.5-x) - 0.5         
]

titles = ["F'>0, F''>0", "F'<0, F''<0", "F'<0, F''>0", "F'>0, F''<0"]
roots = [1.5+np.sqrt(0.5), 1.5-np.sqrt(0.5), 1.25, 2.25]

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for i, (f, title, root) in enumerate(zip(funcs, titles, roots)):
    x = np.linspace(0.5, 2.8, 200)
    y = f(x)
    
    axes[i].plot(x, y, 'b-', linewidth=2)
    axes[i].axhline(0, color='black', linewidth=0.5)
    axes[i].axvline(root, color='g', linestyle='--', alpha=0.7, label='Корень')
    axes[i].set_title(f'Случай {chr(97+i)}: {title}')
    axes[i].grid(True, alpha=0.3)
    axes[i].legend()

plt.tight_layout()
plt.show()