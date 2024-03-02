class RubiksCube:

# Initialize a solved Rubik's Cube           
    def __init__(self):
        
        self.state = [
            [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # Top layer
            [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # Front layer
            [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],  # Right layer
            [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],  # Back layer
            [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # Left layer
            [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],  # Bottom layer
        ]

    def __str__(self):
        output = ""
        for face in self.state:
            output += " ".join(face[0]) + "\n"
            output += " ".join(face[1]) + "\n"
            output += " ".join(face[2]) + "\n\n"
        return output
    
# Rotate a face clockwise
    def rotate_face_clockwise(self, face):
        
        face_copy = [row[:] for row in self.state[face]]
        for i in range(3):
            for j in range(3):
                self.state[face][i][j] = face_copy[2 - j][i]

# Rotate a face anti-clockwise
    def rotate_face_anti_clockwise(self, face):
        
        face_copy = [row[:] for row in self.state[face]]
        for i in range(3):
            for j in range(3):
                self.state[face][i][j] = face_copy[j][2 - i]

# Rotate Right
    # Clockwise 
    def rotate_right_clockwise(self):
        # Rotate the right face clockwise
        self.rotate_face_clockwise(2)
        # Rotate the adjacent edges
        temp = [self.state[0][i][2] for i in range(3)]
        for i in range(3):
            self.state[i][2][2] = self.state[4][2 - i][0]
        for i in range(3):
            self.state[4][i][0] = self.state[5][2 - i][2]
        for i in range(3):
            self.state[5][i][2] = self.state[1][i][2]
        for i in range(3):
            self.state[1][i][2] = temp[i]
    # Anti-clockwise
    def rotate_right_anti_clockwise(self):
        # Rotate the right face anti-clockwise
        self.rotate_face_anti_clockwise(2)
        # Rotate the adjacent edges
        temp = [self.state[0][i][2] for i in range(3)]
        for i in range(3):
            self.state[i][2][2] = self.state[1][i][2]
        for i in range(3):
            self.state[1][i][2] = self.state[5][2 - i][2]
        for i in range(3):
            self.state[5][i][2] = self.state[4][i][0]
        for i in range(3):
            self.state[4][i][0] = temp[i]

# Rotate Left
    # Clockwise
    def rotate_left_clockwise(self):
        # Rotate the left face clockwise
        self.rotate_face_clockwise(4)
        # Rotate the adjacent edges
        temp = [self.state[0][i][0] for i in range(3)]
        for i in range(3):
            self.state[i][0][0] = self.state[1][i][0]
        for i in range(3):
            self.state[1][i][0] = self.state[5][2 - i][0]
        for i in range(3):
            self.state[5][i][0] = self.state[4][i][2]
        for i in range(3):
            self.state[4][i][2] = temp[i]
    # Anti-clockwise
    def rotate_left_anti_clockwise(self):
        # Rotate the left face anti-clockwise
        self.rotate_face_anti_clockwise(4)
        # Rotate the adjacent edges
        temp = [self.state[0][i][0] for i in range(3)]
        for i in range(3):
            self.state[i][0][0] = self.state[4][2 - i][2]
        for i in range(3):
            self.state[4][i][2] = self.state[5][i][0]
        for i in range(3):
            self.state[5][i][0] = self.state[1][i][0]
        for i in range(3):
            self.state[1][i][0] = temp[i]

# Rotate Up
    # Clockwise
    def rotate_up_clockwise(self):
        # Rotate the up face clockwise
        self.rotate_face_clockwise(2)
        # Rotate the adjacent edges
        temp = [self.state[0][i][2] for i in range(3)]
        for i in range(3):
            self.state[i][2][2] = self.state[4][2 - i][0]
        for i in range(3):
            self.state[4][i][0] = self.state[5][2 - i][2]
        for i in range(3):
            self.state[5][i][2] = self.state[1][i][2]
        for i in range(3):
            self.state[1][i][2] = temp[i]
    # Anti-clockwise
    def rotate_up_anti_clockwise(self):
        # Rotate the up face anti-clockwise
        self.rotate_face_anti_clockwise(2)
        # Rotate the adjacent edges
        temp = [self.state[0][i][2] for i in range(3)]
        for i in range(3):
            self.state[i][2][2] = self.state[1][i][2]
        for i in range(3):
            self.state[1][i][2] = self.state[5][2 - i][2]
        for i in range(3):
            self.state[5][i][2] = self.state[4][i][0]
        for i in range(3):
            self.state[4][i][0] = temp[i]

# Rotate Down
    # Clockwise
    def rotate_down_clockwise(self):
        # Rotate the down face clockwise
        self.rotate_face_clockwise(2)
        # Rotate the adjacent edges
        temp = [self.state[0][i][2] for i in range(3)]
        for i in range(3):
            self.state[i][2][2] = self.state[4][2 - i][0]
        for i in range(3):
            self.state[4][i][0] = self.state[5][2 - i][2]
        for i in range(3):
            self.state[5][i][2] = self.state[1][i][2]
        for i in range(3):
            self.state[1][i][2] = temp[i]
    # Anti-clockwise
    def rotate_down_anti_clockwise(self):
        # Rotate the down face anti-clockwise
        self.rotate_face_anti_clockwise(2)
        # Rotate the adjacent edges
        temp = [self.state[0][i][2] for i in range(3)]
        for i in range(3):
            self.state[i][2][2] = self.state[1][i][2]
        for i in range(3):
            self.state[1][i][2] = self.state[5][2 - i][2]
        for i in range(3):
            self.state[5][i][2] = self.state[4][i][0]
        for i in range(3):
            self.state[4][i][0] = temp[i]

# Rotate Front
    # Clockwise
    def rotate_up_clockwise(self):
        # Rotate the front face clockwise
        self.rotate_face_clockwise(2)
        # Rotate the adjacent edges
        temp = [self.state[0][i][2] for i in range(3)]
        for i in range(3):
            self.state[i][2][2] = self.state[4][2 - i][0]
        for i in range(3):
            self.state[4][i][0] = self.state[5][2 - i][2]
        for i in range(3):
            self.state[5][i][2] = self.state[1][i][2]
        for i in range(3):
            self.state[1][i][2] = temp[i]
    # Anti-clockwise
    def rotate_front_anti_clockwise(self):
        # Rotate the front face anti-clockwise
        self.rotate_face_anti_clockwise(2)
        # Rotate the adjacent edges
        temp = [self.state[0][i][2] for i in range(3)]
        for i in range(3):
            self.state[i][2][2] = self.state[1][i][2]
        for i in range(3):
            self.state[1][i][2] = self.state[5][2 - i][2]
        for i in range(3):
            self.state[5][i][2] = self.state[4][i][0]
        for i in range(3):
            self.state[4][i][0] = temp[i]

# Rotate Back 
    # Clockwise
    def rotate_back_clockwise(self):
        # Rotate the back face clockwise
        self.rotate_face_clockwise(2)
        # Rotate the adjacent edges
        temp = [self.state[0][i][2] for i in range(3)]
        for i in range(3):
            self.state[i][2][2] = self.state[4][2 - i][0]
        for i in range(3):
            self.state[4][i][0] = self.state[5][2 - i][2]
        for i in range(3):
            self.state[5][i][2] = self.state[1][i][2]
        for i in range(3):
            self.state[1][i][2] = temp[i]
    # Anti-clockwise
    def rotate_back_anti_clockwise(self):
        # Rotate the back face anti-clockwise
        self.rotate_face_anti_clockwise(2)
        # Rotate the adjacent edges
        temp = [self.state[0][i][2] for i in range(3)]
        for i in range(3):
            self.state[i][2][2] = self.state[1][i][2]
        for i in range(3):
            self.state[1][i][2] = self.state[5][2 - i][2]
        for i in range(3):
            self.state[5][i][2] = self.state[4][i][0]
        for i in range(3):
            self.state[4][i][0] = temp[i]

# Moves to Make 
    def rotate(self):
        # Prompt the user for rotation input
        print("Which face do you want to rotate?")
        print("Options: 'R' (Right), 'L' (Left), 'U' (Up), 'D' (Down), 'F' (Front), 'B' (Back)")
        face = input("Enter your choice: ").upper()

        # Check the input and call the corresponding rotation method
        if face == 'R':
            direction = input("Rotate 'C' (clockwise) or 'AC' (anti-clockwise)? ").upper()
            if direction == 'C':
                self.rotate_up_clockwise()
            elif direction == 'AC':
                self.rotate_up_anti_clockwise()
        elif face == 'L':
            direction = input("Rotate 'C' (clockwise) or 'AC' (anti-clockwise)? ").upper()
            if direction == 'C':
                self.rotate_down_clockwise()
            elif direction == 'AC':
                self.rotate_down_anti_clockwise()
        elif face == 'U':
            direction = input("Rotate 'C' (clockwise) or 'AC' (anti-clockwise)? ").upper()
            if direction == 'C':
                self.rotate_front_clockwise()
            elif direction == 'AC':
                self.rotate_front_anti_clockwise()
        elif face == 'D':
            direction = input("Rotate 'C' (clockwise) or 'AC' (anti-clockwise)? ").upper()
            if direction == 'C':
                self.rotate_back_clockwise()
            elif direction == 'AC':
                self.rotate_back_anti_clockwise()
        elif face == 'F':
            direction = input("Rotate 'C' (clockwise) or 'AC' (anti-clockwise)? ").upper()
            if direction == 'C':
                self.rotate_left_clockwise()
            elif direction == 'AC':
                self.rotate_left_anti_clockwise()
        elif face == 'B':
            direction = input("Rotate 'C' (clockwise) or 'AC' (anti-clockwise)? ").upper()
            if direction == 'C':
                self.rotate_right_clockwise()
            elif direction == 'AC':
                self.rotate_right_anti_clockwise()
        else:
            print("Invalid input. Please choose from the provided options.")

# Check if Cube is Solved
    def is_solved(self):
        # Check if each face has the same color on each tile
        for face in self.state:
            color = face[0][0]  # Get the color of the first tile
            for row in face:
                for tile in row:
                    if tile != color:
                        return False
        return True
    
    
# Create an instance of the RubiksCube class
cube = RubiksCube()

# Loop until the cube is solved
while True:
    # Prompt the user for rotation input
    cube.rotate()
    
    # Print the current state of the cube
    print(cube)
    
    # Check if the cube is solved
    if cube.is_solved():  # You need to implement the is_solved() method in the RubiksCube class
        print("Congratulations! The cube is solved!")
        break