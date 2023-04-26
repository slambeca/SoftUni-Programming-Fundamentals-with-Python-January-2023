events = input().split("|")
# ['rest-2', 'order-10', 'eggs-100', 'rest-10']

total_coins = 100
total_energy = 100

factory_is_open = True

for event in events:
    event_items = event.split("-")  # splitting the input for a second time, it looks like this ['order', '10']

    type_of_event = event_items[0]
    event_value = int(event_items[1])    # or [-1] if we do not know the number of elements

    # type_of_event, event_value = event.split("-")    # same as the 3 lines above, returns strings like this - order 10
    # and we should change it to int
    # we use this method only if we are 100% sure that the input will be correct!

    if type_of_event == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100    # this is the maximum energy
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            # if total_energy > 100:    # no need for those lines, because of the check above
            #     total_energy = 100
            print(f"You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            factory_is_open = False
            break

if factory_is_open:
    print(f"Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")

# Variant 2
# total_energy = 100
# initial_coins = 100
#
# day_completed = True
#
# working_day_events = input().split("|")
#
# for event in working_day_events:
#     event_args = event.split("-")
#
#     type_of_event = event_args[0]
#     value_of_event = int(event_args[1])  # or [-1] if we only know that it is the last value, also we convert to int
#
#     if type_of_event == "rest":
#         current_energy = total_energy
#         total_energy += value_of_event
#         if total_energy > 100:
#             total_energy = 100
#         gained_energy = total_energy - current_energy
#         print(f"You gained {gained_energy} energy.")
#         print(f"Current energy: {total_energy}.")
#     elif type_of_event == "order":
#         if total_energy >= 30:
#             total_energy -= 30
#             initial_coins += value_of_event
#             print(f"You earned {value_of_event} coins.")
#         else:
#             total_energy += 50
#             if total_energy > 100:
#                 total_energy = 100
#             print("You had to rest!")
#     else:
#         if initial_coins >= value_of_event:
#             initial_coins -= value_of_event
#             print(f"You bought {type_of_event}.")
#         else:
#             print(f"Closed! Cannot afford {type_of_event}.")
#             day_completed = False
#             break
#
# if day_completed:
#     print("Day completed!")
#     print(f"Coins: {initial_coins}")
#     print(f"Energy: {total_energy}")
