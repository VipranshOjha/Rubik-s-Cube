# Rubik's Cube 3D Simulation

This repository contains a 3D simulation of a Rubik's Cube using Pygame and OpenGL. The program allows you to rotate and interact with a virtual Rubik's Cube in a graphical environment.

## How to Use

To run the Rubik's Cube simulation, follow these steps:

1. **Installation**
   - Clone this repository:
     ```bash
     git clone https://github.com/VipranshOjha/rubiks-cube-3d.git
     ```
   - Install Python and required libraries (`pygame` and `PyOpenGL`).
     ```bash
     pip install pygame PyOpenGL
     ```

2. **Run the Simulation**
   - Navigate to the project directory.
   - Execute the Python script:
     ```bash
     python rubiks_cube_3d.py
     ```

3. **Controls**
   - Use the arrow keys (`←`, `→`, `↑`, `↓`) to rotate the entire Rubik's Cube in different directions.
   - Additional controls (placeholders for layer rotation):
     - `W`: Rotate a specific layer clockwise (e.g., white layer).
     - `A`: Rotate a specific layer counter-clockwise (e.g., white layer).
     - `S`: Rotate a different layer clockwise (e.g., yellow layer).
     - `D`: Rotate a different layer counter-clockwise (e.g., yellow layer).

## Features

- **Interactive 3D Visualization**
  - Utilizes Pygame and OpenGL for rendering a 3D Rubik's Cube.
  - Implements basic rotation functionalities for the entire cube and specific layers (placeholders for advanced functionality).

- **Color-Coded Cube**
  - Each face of the cube is colored using defined RGB values, representing the standard Rubik's Cube color scheme.

## Repository Structure

- `rubiks_cube_3d.py`: Main Python script containing the Rubik's Cube simulation logic.
- `README.md`: This document explaining the simulation and its usage.

## Dependencies

- Python 3.x
- `pygame` library for game development.
- `PyOpenGL` library for OpenGL integration with Python.

## Acknowledgments

This Rubik's Cube 3D simulation was developed by Vipransh Ojha as a learning project to explore 3D graphics programming with Pygame and OpenGL.

Feel free to explore and modify the code to enhance the Rubik's Cube simulation further!

Enjoy simulating the Rubik's Cube in 3D! If you have any feedback or suggestions, please reach out.
