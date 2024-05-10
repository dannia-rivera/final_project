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
        self.candidates = []

    def vote(self, candidate_name: str):
        '''Increment the vote count for the Candidate by their name'''
        for candidate in self.candidates:
            if candidate.name == candidate_name:
                candidate.votes += 1
                return
    def calculate_winner(self): -> str:
    '''Calculate the winner based on maximum votes, return the winners name'''
    if not self.candidates:
        return 'No candidates'

    max_votes = max(candidate.votes for candidate in self.candidates)
    winners = [candidate.name for candidate in self.candidates if candidate.votes == max_votes]

    if len(winners) == 1:
        return winners[0]
    else:
        return ", ".join(winners)


