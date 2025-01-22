from letter_state import LetterSate

class Wordle:
    
    max_attempts = 6
    word_lenght = 5

    def __init__(self, secret: str):
        self.secret: str = secret
        self.attempts = []
        pass

    def attempt(self, word: str):
        self.attempts.append(word)

    def guess(self, word: str):
        result = []

        for i in range(self.word_lenght):
            character = word[i]
            letter = LetterSate(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = character == self.secret[i]
            result.append(letter)

        return result

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret
    
    @property
    def remainning_attempt(self) -> int:
        return self.max_attempts - len(self.attempts)
    
    
    @property
    def can_attempt(self):
        return self.remainning_attempt > 0 and not self.is_solved

