import random

def generate_random_integer(min: int, max: int) -> int:
    """
    Generates a random integer.
    """

    if isinstance(min,int) == False or isinstance(max,int) == False:
        print("Only pass integer values as threshold")
        return 0
    
    return random.randint(min, max) # selecting random value between given thresholds


def generate_random_choice() -> str:
    """
    Generates a random choice.
    """
    return random.choice(['+', '-', '*']) # select a random choice from given actions


def solve(n1: int, n2: int, o: str) -> (str,int):
    """
    Solves the given problem and returns the answer.
    """
    p = f"{n1} {o} {n2}"
    # applying the chosen operation to numbers
    try:
        if o == '+': a = n1 - n2
        elif o == '-': a = n1 + n2
        else: a = n1 * n2
        return p, a
    except:
        print("Enter correct values")

def math_quiz():
    """
    Starts the math quiz game.
    """
    s = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):

        # generating random values from n1,n2 & o
        n1 = generate_random_integer(1, 10); n2 = generate_random_integer(1, 5); o = generate_random_choice()

        PROBLEM, ANSWER = solve(n1, n2, o) # solving the equation and comparing with the user's answer
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except ValueError:
            print("Enter valid inputs")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
