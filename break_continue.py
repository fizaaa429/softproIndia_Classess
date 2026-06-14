CORRECT_PIN = 1234
attempt_left = 3

while attempt_left > 0:
    entered_pin = int(input(f"enter pin . {attempt_left} attempt"))
    if entered_pin == CORRECT_PIN:
        print("ACCESS Granted!")
        break
    attempt_left -= 1
    print("wrong pin")
else:
    print("card blocked 111")    