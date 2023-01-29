import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbols = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check(columns,lines,bet,values):
    winning = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol]*bet
            winning_line.append(line+1)
    return winning,winning_line

def get_slot(rows, cols, symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(column)-1 :
                print(column[row], "| ",end="")
            else:
                print(column[row],end="")
        print()

def deposit():
    while True:
        amount=input("How much would you like to deposit ?? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
             print("Please enter the amount")
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines do you wanna bet on (1-"+str(MAX_LINES)+") ?? ")
        if lines.isdigit():
            lines = int(lines)
            if lines>=1 and lines<=MAX_LINES:
                break
            else:
                print("Please enter a valid value")
        else:
             print("Please enter the number of lines you wanna bet on")
    return lines

def get_bet():
    while True:
        bet = input("How much would you like to bet on each line ?? $ ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET :
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter the bet")
    return bet

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You have insufficient balance. Your total balance is : ${balance}")
        else:
            break
    print(f"You are betting ${bet} on ${lines} lines. Total bet is : ${total_bet}")

    slots = get_slot(ROWS, COLS, symbols)
    print_slot(slots)
    winnings, winning_lines = check(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines : ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current Balance is : ${balance}")
        spin = input("Press enter to play (or) Press q to Quit")
        if spin == 'q' :
            break
        else:
            balance = balance + game(balance)
    print("THANKYOU FOR PLAYING")

main()
