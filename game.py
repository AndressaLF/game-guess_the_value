from models.calculate import Calculate

def main() -> None:
    score: int = 0
    play(score)

def play(score: int) -> None:
    difficulty: int = int(input('Choose the level of difficulty by setting the number between 1 and 4: '))

    calc: Calculate = Calculate(difficulty)
    print('Write the result for the operation below: ')
    calc.show_operation()

    result: int = int(input('Result = '))

    if calc.check_result(result):
        score += 1
        print(f'You have {score} points.')
    else:
        print('You missed!')

    keep_going: int = int(input('Do you want to continue? 1-Yes or 2-No: '))
    if keep_going == 1:
        play(score)
    else:
        print(f'You finished the game with {score} point(s).')
        print('Bye Bye!')


if __name__ == '__main__':
    main()
