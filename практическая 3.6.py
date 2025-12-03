def check_lucky_ticket():
    ticket_number_str = input()
    sum_first_three = sum(int(digit) for digit in ticket_number_str[:3])
    sum_last_three = sum(int(digit) for digit in ticket_number_str[3:])
    if sum_first_three == sum_last_three:
        print("Счастливый")
    else:
        print("Обычный")