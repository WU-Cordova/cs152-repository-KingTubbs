#cell.py
class Cell:
    def __init__(self) -> None:
        self.position_row = int
        self.position_col = int
        self.neighbor_count = int
        self.alive_status = bool

    def __str__(self) -> str:
        if self.alive_status == True:
            return "O"
        elif self.alive_status == False:
            return "X"
    
        
