class Candidate:
    def __init__(self, name: str):
        '''Initialize Candidate object with a name and votes count.'''
        self.name = name
        self.votes = 0

    def vote(self):
        