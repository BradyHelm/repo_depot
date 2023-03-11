"""Word Finder: finds random words from a dictionary."""


import random


class WordFinder:
    ...


class WordFinder:
    """Finds random words from a dictionary file."""


def __init__(self, filename):
      """Reads words from a file and initializes the instance variables."""
      self.words = []
with open(filename, 'r') as file:
          for line in file:
            word = line.strip()
            if word:
                self.words.append(word)
                print(f"{len(self.words)} words read")

def random(self):
        """Returns a random word from the list of words."""
        return random.choice(self.words)            


