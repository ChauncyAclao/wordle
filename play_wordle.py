
#original code by pixegami

from wordle import Wordle 
from letter_state import LetterSate
from colorama import Fore
import random

def main():

    word_set = load_word_set("wordle_words.txt")
    secret = random.choice(list(word_set))

    print('\nWELCOME TO WORDLE')
    print("┌"  + "─" * 11 + "┐")
    print("│" + " _" + " _ " + "_" + " _ " + "_ " + "│")
    print("│" + " _" + " _ " + "_" + " _ " + "_ " + "│")
    print("│" + " _" + " _ " + "_" + " _ " + "_ " + "│")
    print("│" + " _" + " _ " + "_" + " _ " + "_ " + "│")
    print("│" + " _" + " _ " + "_" + " _ " + "_ " + "│")
    print("│" + " _" + " _ " + "_" + " _ " + "_ " + "│")
    print("└"  + "─" * 11 + "┘")

    wordle = Wordle(secret)
    
    while wordle.can_attempt:
        answer = input("\nType out your guess:").strip().upper()

        if len(answer) != wordle.word_lenght:
            print(Fore.RED + f"\nWORD MUST BE {wordle.word_lenght} CHARACTERS LONG" + Fore.RESET)
            continue

        if not answer in word_set:
            print(Fore.RED + f"{answer} NOT A VALID WORD" + Fore.RESET)
            continue
            
        wordle.attempt(answer)
        display_results(wordle)
       
    if wordle.is_solved:
        print(Fore.GREEN + "SOLVED" + Fore.RESET)
    else:
        print(Fore.RED + "FAILED" + Fore.RESET)
        print(f"WORD WAS:{wordle.secret}")

def display_results(wordle: Wordle):
    print(f"\nRemaing Attempts:{wordle.remainning_attempt}")

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    
    for _ in range(wordle.remainning_attempt):
        lines.append(" ".join(["_"] * wordle.word_lenght))

    draw_border_araound(lines)

def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set

def convert_result_to_color(result: list[LetterSate]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.LIGHTBLACK_EX
        colored_letter =  color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)

def draw_border_araound(lines: list[str], size: int=9, pad: int=1):
    content_lenght = size + pad * 2
    top_border = "┌"  + "─" * content_lenght + "┐"
    bottom_border = "└"  + "─" * content_lenght + "┘"
    space = " " * pad

    print(top_border)

    for line in lines:
        print("│" + space + line + space + "│")

    print(bottom_border)

if __name__ == "__main__":
    main()