import os

class Corpus:
    def __init__(self):
        path = "~/python_experiments/regdata/scripts/stop_words"
        with open(os.path.expanduser(path)) as file:
            self.stop_words = [word.strip() for word in file.readlines()]

    @property
    def stop_words(self):
        return self.stop_words