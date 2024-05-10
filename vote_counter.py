class Candidate:
    def __init__(self, name: str):
        '''Initialize Candidate object with a name and votes count.'''
        self.name = name
        self.votes = 0

    def vote(self):
        '''Increment the vote counr for the Candidate.'''
        self.votes += 1

class VoteSystem:
    def __init__(self):
        '''Initialize VoteSystem with an empty dictionary.'''
        