class DataManager:
    def __init__(self, filename: str):
        '''Initializes the data manager with filename'''
        self.filename = filename

    def save_results(self,candidates: list):
        '''Saves the candidate results to the file'''
        with open(self.filename,'w') as file:
            for candidate in candidates:
                file.write(f'{candidate.name}, {candidate.votes}\n')

    def load_results(self) -> list:
        '''Loads the candidate results from the file'''
        candidates = []