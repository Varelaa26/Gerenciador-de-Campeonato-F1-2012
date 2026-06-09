class Driver:
    def __init__(self, num, name, team, points = 0, position = 0, wins = 0):
        self.num = num
        self.name = name
        self.team = team
        self.points = points
        self.position = position
        self.wins = wins

    def add_win(self):
        self.wins +=1