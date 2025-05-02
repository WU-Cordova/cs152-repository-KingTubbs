#gamecontroller.py
from datastructurescopy.array2d import Array2D
from cell import Cell
from grid import Grid
import random
import copy
import time
from kbhit import KBHit



class GameController:
    def __init__(self, initial_grid)-> None:
        self.initial_grid = initial_grid
        self.running = True
        self.generation_count = 0
        self.automatic = False
        self.manual = False
        self.kb = KBHit()
        self.forever = True
        
    
    def read(self, filename):
        with open(filename, 'r') as file:
            num_rows = int(file.readline().strip())  
            num_cols = int(file.readline().strip()) 

            # Initialize the grid properly
            grid = Grid(num_rows, num_cols)

            for row_index, line in enumerate(file):
                line = line.strip()  # Remove whitespace and newlines
                for col_index, char in enumerate(line):
                    if char == "X":
                        grid.grid[row_index][col_index].alive_status = True  # Set as alive
                    else:
                        grid.grid[row_index][col_index].alive_status = False  # Set as dead

        return grid


    def starting_grid_prompt(self, grid) -> Grid:
        """Prompts whether the user wants to read in their own file or generate a random grid."""
        userinput = input("Would you like to read in a colony start file? (Y/N)").strip().upper()
        
        if userinput == "Y":
            print("Reading in config file.")
            filename = "config.txt"
            return  self.read(filename)

        else:  # Default to generating a random grid
            print("Generating random grid")
            for row in range(grid.number_of_rows):  
                for col in range(grid.number_of_cols):
                    status = random.choice([0, 1])
                    cell = grid.grid[row][col] 

                    cell.alive_status = status
                    cell.position_row = row
                    cell.position_col = col
            return grid
        
    def speed_prompt(self):
        """prompts whether the use wants an automatic generation system or manual"""
        userinput = input("Which mode would you like to use, Automatic or Manual?").strip().lower()

        if userinput == "automatic":
            #raise automatic mode flag
            self.automatic = True
            return print("Running Automatically. Press Q to quit.")
        
        if userinput == "manual":
            #raise manual mode flag
            self.manual = True
            print("Press P to progress generations, or A to switch to Automatic Mode. Q to quit: ")
            return print("Running Manually.")

        else:
            print("Unknown command. Running Automatically. Press Q to quit")
            self.automatic = True

    def run(self):
        """main loop"""

        self.original_grid = self.starting_grid_prompt(self.initial_grid) 
        for row in range(self.original_grid.number_of_rows):  
                for col in range(self.original_grid.number_of_cols):
                    self.original_grid.neighbor_detection(self.original_grid.grid[row][col]) #adds neighbor counts to cells
        
        self.original_grid.display()
        print(f"Generation {self.generation_count}")
        Empty_grid = Grid(self.initial_grid.number_of_rows, self.initial_grid.number_of_cols)
        history = [Empty_grid,Empty_grid,Empty_grid,Empty_grid,Empty_grid]

        self.speed_prompt()
        
        while self.running:
            #Wait for user input to either progress the generation or switch to automatic mode
            
            if self.manual:
                
                if self.kb.kbhit():  # Check if a key was pressed
                    c = self.kb.getch().lower()
                    if c == 'p':
                        #Generate the next generation 
                        self.new_grid = self.original_grid.next_gen() 
                        for row in range(self.original_grid.number_of_rows):  
                            for col in range(self.original_grid.number_of_cols):
                                self.original_grid.neighbor_detection(self.original_grid.grid[row][col])  # Update neighbors
                        self.generation_count += 1
                        self.new_grid.display()
                        print(f"Generation {self.generation_count}")

                        history[self.generation_count % 5] = copy.deepcopy(self.original_grid) #history

                        if self.new_grid.check_for_change(self.original_grid):
                            for i in range(len(history)):
                                if self.new_grid.check_for_change(history[i]) == False:
                                    #Pattern detected, end loop
                                    self.running = False
                                    print("Pattern/infinite loop detected")
                            #change detected, keep going
                                self.original_grid = self.new_grid
                            
                        else:
                            #no change detected, end loop
                            self.running = False 
                    elif c == 'a':  #Switch to automatic mode
                        self.automatic = True
                        self.manual = False
                        print("Switching to Automatic Mode")
                    elif c == 'q':
                        print("Quitting")
                        quit()
                    else:
                        print("Invalid input. Press P to progress or A to switch to Automatic Mode.")

            #Automatically progress generations every 1 second when in automatic mode
            if self.automatic:
                if self.kb.kbhit():  # Check if a key was pressed
                    b = self.kb.getch().lower()
                    if b == 'q':
                        print("Quitting")
                        quit()
                time.sleep(1)
                self.new_grid = self.original_grid.next_gen()  # new_grid has new changes
                for row in range(self.original_grid.number_of_rows):  
                    for col in range(self.original_grid.number_of_cols):
                        self.original_grid.neighbor_detection(self.original_grid.grid[row][col])  # Adds neighbor counts to cells
                self.generation_count += 1
                self.new_grid.display()
                print(f"Generation {self.generation_count}")

                history[self.generation_count % 5] = copy.deepcopy(self.original_grid) #history

                if self.new_grid.check_for_change(self.original_grid):
                    for i in range(len(history)):
                        if self.new_grid.check_for_change(history[i]) == False:
                            #Pattern detected, end loop
                            self.running = False
                            print("Pattern/infinite loop detected")
                    #change detected, keep going
                        self.original_grid = self.new_grid
                    
                else:
                    #no change detected, end loop
                    self.running = False 

        print(f"Simulation has ended at generation {self.generation_count}, press q to quit or s to start over")
        while True:
            if self.kb.kbhit():  # Check if a key was pressed
                b = self.kb.getch().lower()
                if b == 'q':
                    print("Quitting")
                    quit()
                if b == 's':
                    grid = Grid(20,20)
                    game = GameController(grid)
                    game.run()
