# Rubik's Cube 3D Simulator

This project is a **3D Rubik's Cube simulator** built using **Python**, **Pygame**, and **OpenGL**. It allows users to interact with, scramble, and solve a virtual Rubik's Cube through animations and algorithmic solutions.

## Features
- **3D Rendering**: Uses OpenGL to provide a realistic visualization of the Rubik's Cube.
- **Mouse Interaction**: Rotate the cube and its faces using mouse gestures.
- **Scrambling System**: A built-in scrambler applies random moves to shuffle the cube.
- **Automated Solver**: Implements a step-by-step solving algorithm.
- **Smooth Animations**: Transitions between cube states are animated for a better user experience.
- **Move Notation**: Displays the solution sequence using standard Rubik's Cube move notation.

---

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed, then install the necessary dependencies:
```bash
pip install pygame PyOpenGL numpy
```

---

## Usage
### Running the Simulator
To launch the Rubik's Cube simulator, run:
```bash
python RubiksCube.py
```

### Controls
- **Left Click & Drag**: Rotate the entire cube.
- **Right Click & Drag**: Rotate an individual face.
- **Escape Key**: Exit the program.

### Scrambling the Cube
To scramble the cube, the `Scrambler` module generates and applies random moves:
```python
scrambler = CubeScrambler(cube_instance)
scramble_sequence = scrambler.scramble(num_moves=20)
```

### Solving the Cube
The `Solver` module attempts to solve the cube using predefined algorithms:
```python
solver = CubeSolver(cube_instance)
solver.solve()
solution_moves = solver.get_move_notation()
print("Solution:", solution_moves)
```

---

## Code Structure
- **`RubiksCube.py`** – Main file for rendering and interacting with the cube.
- **`scrambler.py`** – Handles random scrambling of the cube.
- **`solver.py`** – Implements solving logic based on layer-by-layer methods.

---

## How It Works
1. The cube is represented as a collection of smaller cubies with distinct face colors.
2. **Scrambling** applies a sequence of random moves to mix up the cube.
3. **Solving** follows logical steps:
   - Solve the **white cross**.
   - Position the **white corners**.
   - Solve the **middle layer**.
   - Form the **yellow cross**.
   - Orient and permute the **yellow corners**.
   - Finalize the **yellow edges**.
4. The solution moves are displayed using standard Rubik's Cube notation (R, U, F, etc.).

---

## Future Improvements
- Implement advanced solving techniques (e.g., CFOP method).
- Add keyboard shortcuts for manual cube rotation.
- Improve performance and animation speed.
- Implement a GUI for easier interaction.

---

## License
This project is open-source and available under the **MIT License**.

---

🚀 **Happy Cubing!**

