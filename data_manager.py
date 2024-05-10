class DataManager:
    def __init__(self, filename: str):
        '''Initializes the data manager with filename'''
        self.filename = filename

    def save_results(self,candidates: list):
        '''Saves the candidate results to the file'''
        