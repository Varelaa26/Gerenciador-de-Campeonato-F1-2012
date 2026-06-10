from Classes.team import Team

class Driver:
    def __init__(self, num: int, name: str, team_object: Team, points: int = 0, position: int = 0, wins: int = 0):
        self.num = num
        self.name = name
        self.team = team_object
        self.points = points
        self.position = position
        self.wins = wins

    def add_win(self):
        self.wins += 1
        self.points += 25
        self.team.wins += 1
        self.team.wins += 25
