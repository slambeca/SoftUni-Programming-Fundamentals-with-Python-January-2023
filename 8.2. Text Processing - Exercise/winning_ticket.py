def is_winning_ticket(some_ticket):
    if len(some_ticket) != 20:
        return f"invalid ticket"
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_repetitions = match_symbol * uninterrupted_match_length
            if winning_symbol_repetitions in left_part and winning_symbol_repetitions in right_part:
                if uninterrupted_match_length == 10:    # We win the jackpot
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                    # We have just a winning ticket, but not jackpot
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


winning_symbols = ["@", "#", "$", "^"]

tickets = [ticket.strip() for ticket in input().split(", ")]  # ['$$$$$$$$$$$$$$$$$$$$', 'aabb', 'th@@@@@@eemo@@@@@@ey']

for ticket in tickets:
    print(is_winning_ticket(ticket))