class Territory:
    ALLTERRITORIES = []
    def __init__(self, name, value):
        assert isinstance(name, str)
        self.name = name
        self.value = value
        self.troops = 0
        self.boardering = {}
        self.boardering.setdefault(None)
        
        Territory.ALLTERRITORIES.append(self.name)
    
    def add_troops(self, num):
        self.troops += num

    def set_boarder(self, board):
        self.boardering[board.name] = board
        board.boardering[self.name] = self
    
    def get_boarder(self, board):
        if board == None:
            return None
        elif board.name in self.boardering.keys():
            return self.boardering[board.name]
        return None