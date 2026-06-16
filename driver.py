from Classes.team import Team

class Driver:
    def __init__(self, num: int, name: str, team_object: Team, points: int = 0, position: int = 0, wins: int = 0):
        self.num = num
        self.name = name
        self.team = team_object
        self.points = points
        self.position = position
        self.wins = wins

    def add_result(self, pos_ended: int):
        if pos_ended == 1:
            self.points += 25
            self.team.points += 25
            self.wins += 1
            self.team.wins += 1
        elif pos_ended == 2:
            self.points += 18
            self.team.points += 18
        elif pos_ended == 3:
            self.points += 15
            self.team.points += 15
        elif pos_ended == 4:
            self.points += 12
            self.team.points += 12
        elif pos_ended == 5:
            self.points += 10
            self.team.points += 10
        elif pos_ended == 6:
            self.points += 8
            self.team.points += 8
        elif pos_ended == 7:
            self.points += 6
            self.team.points += 6
        elif pos_ended == 8:
            self.points += 4
            self.team.points += 4
        elif pos_ended == 9:
            self.points += 2
            self.team.points += 2
        elif pos_ended == 10:
            self.points += 1
            self.team.points += 1