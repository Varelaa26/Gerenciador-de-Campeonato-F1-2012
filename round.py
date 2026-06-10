class Round:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.results = []
        self.fast_lap = None