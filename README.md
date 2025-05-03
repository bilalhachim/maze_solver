# Maze Solver

This project implements a maze generator and solver using a graphical interface. It utilizes a recursive backtracker algorithm to generate mazes and a recursive depth-first search algorithm to solve them.

## Features and Functionality

*   **Maze Generation:** Generates random mazes of specified dimensions using a recursive backtracker algorithm.
*   **Maze Solving:** Solves the generated maze using a recursive depth-first search algorithm.
*   **Graphical Interface:** Visualizes the maze generation and solving process using `tkinter`.
*   **Animation:** Provides animation during maze generation and solving for better visualization.
*   **Customizable Maze Size:** Allows users to define the number of rows and columns for the maze.
*   **Entrance and Exit:** Automatically creates an entrance and exit point in the maze.

## Technology Stack

*   **Python:** The primary programming language.
*   **tkinter:** Used for creating the graphical user interface.

## Prerequisites

Before running the project, ensure you have the following installed:

*   **Python 3.x:**  Download and install from [python.org](https://www.python.org/downloads/).
*   **tkinter:** Usually comes pre-installed with Python.  If not, install via your distribution's package manager (e.g., `apt-get install python3-tk` on Debian/Ubuntu).

## Installation Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/bilalhachim/maze_solver.git
    cd maze_solver
    ```

2.  **(Optional) Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install any missing dependencies (although tkinter is generally pre-installed):**
    ```bash
    # No pip install required based on the code.  tkinter is generally included with Python.
    # If you encounter issues, consult tkinter installation guides for your OS.
    ```

## Usage Guide

1.  **Run the `main.py` script:**

    ```bash
    python3 main.py
    ```

    This will:

    *   Create a window.
    *   Generate a maze.
    *   Solve the maze.
    *   Display the animated solving process.

2.  **Configuration:**

    Modify the parameters in `main.py` to customize the maze:

    ```python
    from Window import *
    from Point import *
    from Line import *
    from Cell import *
    from Maze import *
    from random import *
    win = Window(600, 600)
    maze = Maze(3,3,20,20,40,40,win,23)  # x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed
    maze.solve()
    win.wait_for_close()
    ```

    *   `x1`, `y1`: Top-left coordinates of the maze within the window.  These values affect where the maze is drawn.
    *   `num_rows`: Number of rows in the maze.
    *   `num_cols`: Number of columns in the maze.
    *   `cell_size_x`: Width of each cell in the maze.
    *   `cell_size_y`: Height of each cell in the maze.
    *   `win`: The `Window` object.
    *   `seed`:  An optional seed for the random number generator.  Using the same seed will generate the same maze every time.  Remove the `seed` argument (or set it to `None`) for a truly random maze each time.

## API Documentation

The core classes used in the project are:

*   **`Cell(win=None)`:** Represents a single cell in the maze.

    *   `__init__(self, win=None)`: Initializes a cell with walls on all sides and a `visited` flag set to `False`. `win` is the `Window` object where the cell will be drawn.
    *   `draw(self, top_left_point, bottom_right_point, fill_color)`: Draws the cell on the canvas with the specified color.  `top_left_point` and `bottom_right_point` are `Point` objects defining the cell's boundaries.
    *   `draw_move(self, to_cell, canvas, undo=False)`: Draws a line representing a move from the current cell to the `to_cell`.  The color of the line is red for a move and gray (if `undo=True`) to backtrack.  `canvas` is the tkinter `Canvas` object.
    *   `get_x1(self)`: Returns the x-coordinate of the top-left corner of the cell.
    *   `get_x2(self)`: Returns the x-coordinate of the bottom-right corner of the cell.
    *   `get_y1(self)`: Returns the y-coordinate of the top-left corner of the cell.
    *   `get_y2(self)`: Returns the y-coordinate of the bottom-right corner of the cell.

*   **`Line(point1, point2)`:** Represents a line segment.

    *   `__init__(self, point1, point2)`: Initializes a line with two `Point` objects.
    *   `draw(self, win, fill_color)`: Draws the line on the canvas with the specified color.  `win` is the `Window` object.

*   **`Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None)`:** Represents the maze structure.

    *   `__init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None)`: Initializes the maze with specified dimensions, cell sizes, and window. `seed` is an optional seed for the random number generator.
    *   `solve()`: Solves the maze using recursive backtracking.
    *   `_break_entrance_and_exit()`: Creates the entrance and exit points by removing the top wall of the starting cell and the bottom wall of the ending cell.
    *   `_break_walls_r(self, i, j)`: Recursive function to break walls and generate the maze.
    *   `_draw_cell(self, i, j)`: Draws a single cell at the given row and column.
    *   `_solve_r(self, i, j)`: Recursive function to solve the maze.
    *   `_animate(self)`: Redraws the window to create animation effect using `sleep(0.03)`.
    *   `_reset_cells_visited(self)`: Resets the `visited` flag of all cells to `False`.
    *   Internal attributes like `_cells`, `_num_rows`, `_num_cols`, `_cell_size_x`, `_cell_size_y` store the maze's structure and dimensions.

*   **`Point(x, y)`:** Represents a point in 2D space.

    *   `__init__(self, x, y)`: Initializes a point with x and y coordinates.

*   **`Window(width, height)`:** Represents the application window.

    *   `__init__(self, width, height)`: Initializes the window with the specified width and height.
    *   `redraw()`: Updates the window.
    *   `wait_for_close()`: Keeps the window open until it is closed by the user.
    *   `close()`: Closes the window.
    *   `draw_line(self, line, fill_color)`: Draws a line on the window.

## Contributing Guidelines

Contributions are welcome!  To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Test your changes thoroughly. Run `python tests.py` to execute the unit tests.  Add new tests as needed.
5.  Submit a pull request.

## License Information

This project has not specified a license. All rights are reserved.

## Contact/Support Information

For questions or support, please contact bilalhachim through GitHub.