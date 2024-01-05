import random

MAXLINES = 3
MAXBET = 100
MINBET = 1

ROWS = 3
COLS = 3

symbol_count = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8
}

symbol_value = {
  "A": 5,
  "B": 4,
  "C": 3,
  "D": 2
}

def check_winnings(columns, lines, bet, values):
  winnings = 0
  winning_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for col in columns:
      if symbol != col[line]:
        break
    else:
      winning_lines.append(line + 1)
      winnings += values[symbol] * bet
  return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)

  columns = []
  for _ in range(cols):
    column = []
    cur_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(cur_symbols)
      cur_symbols.remove(value)
      column.append(value)

    columns.append(column)

  return columns

def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i, col in enumerate(columns):
      if i != len(columns) - 1:
        print(col[row], end=' | ')
      else:
        print(col[row])

def deposit():
  while True:
    amount = input("What would you like to deposit? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Amount must be greater than 0.")
    else:
      print("Please enter a number.")
  return amount

def get_number_of_lines():
  while True:
    lines = input("Enter the number of lines to bet on (1 - " + str(MAXLINES) + ")? ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAXLINES:
        break
      else:
        print("Enter a valid number of lines")
    else:
      print("Please enter a number.")
  return lines

def get_bet():
  while True:
    amount = input("What would you like to bet on each line? $")
    if amount.isdigit():
      amount = int(amount)
      if MAXBET >= amount >= MINBET:
        break
      else:
        print(f"Amount must be between {MINBET} and {MAXBET}.")
    else:
      print("Please enter a number.")
  return amount

def spin(balance):
  lines = get_number_of_lines()
  while True:
    bet = get_bet()
    total_bet = bet * lines
    if total_bet > balance:
      print(f"You do not have enough money to bet. Balance: ${balance}")
    else:
      break
  print(f"You are betting ${bet} on {lines} lines. The total bet is equal to: ${total_bet}.")
  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
  print(f"You have won ${winnings}.")
  print(f"You won on lines:", *winning_lines)
  return winnings - total_bet

def main():
  balance = deposit()
  while True:
    print(f"Current balance is ${balance}")
    ans = input("Press enter to spin (q to quit). ")
    if ans == "q":
      break
    balance += spin(balance)
  print(f"You are left with ${balance}")
main()