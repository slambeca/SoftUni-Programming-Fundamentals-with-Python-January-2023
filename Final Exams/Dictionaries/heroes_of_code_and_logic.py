number_of_heroes = int(input())
heroes = {}

for hero in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    if int(hp) <= 100 and int(mp) <= 200:
        heroes[hero_name] = [int(hp), int(mp)]

while True:
    command = input()

    if command == 'End':
        break

    command = command.split(' - ')
    action = command[0]

    if action == 'CastSpell':
        hero = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]

        if heroes[hero][1] < mp_needed:
            print(f'{hero} does not have enough MP to cast {spell_name}!')
        else:
            heroes[hero][1] -= mp_needed
            print(f'{hero} has successfully cast {spell_name} and now has {heroes[hero][1]} MP!')

    elif action == 'TakeDamage':
        hero = command[1]
        damage = int(command[2])
        attacker = command[3]

        heroes[hero][0] -= damage

        if heroes[hero][0] > 0:
            print(f'{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!')
        else:
            del heroes[hero]
            print(f'{hero} has been killed by {attacker}!')

    elif action == 'Recharge':
        hero = command[1]
        amount = int(command[2])

        if heroes[hero][1] + amount > 200:
            amount = 200 - heroes[hero][1]
            heroes[hero][1] += amount
        else:
            heroes[hero][1] += amount

        print(f'{hero} recharged for {amount} MP!')

    elif action == 'Heal':
        hero = command[1]
        amount = int(command[2])

        if heroes[hero][0] + amount > 100:
            amount = 100 - heroes[hero][0]
            heroes[hero][0] += amount
        else:
            heroes[hero][0] += amount

        print(f'{hero} healed for {amount} HP!')

ordered_heroes = sorted(heroes.items(), key=lambda data: (-data[1][0], data[0]))

for hero, stats in ordered_heroes:
    print(hero)
    print(f'  HP: {stats[0]}')
    print(f'  MP: {stats[1]}')

# # Variant 2
# number_of_heroes = int(input())
# heroes_data = {}
#
#
# def cast_spell(name, mana, spell, mana_availability):
#     if mana <= mana_availability:
#         mana_availability -= mana
#         print(f"{name} has successfully cast {spell} and now has {mana_availability} MP!")
#     else:
#         print(f"{name} does not have enough MP to cast {spell}!")
#     return mana_availability
#
#
# def take_dmg(name, dmg, attacker, health_availability):
#     health_availability[name]["HP"] -= dmg
#     if health_availability[name]["HP"] > 0:
#         print(f"{name} was hit for {dmg} HP by {attacker} and now has {health_availability[name]['HP']} HP left!")
#         return health_availability
#     else:
#         del health_availability[name]
#         print(f"{name} has been killed by {attacker}!")
#         return health_availability
#
#
# def recharge(name, mana, mana_availability):
#     needed_mana = 200-mana_availability
#     mana_availability += mana
#     if mana_availability >= 200:
#         mana_availability = 200
#         print(f"{name} recharged for {needed_mana} MP!")
#         return mana_availability
#     else:
#         print(f"{name} recharged for {mana} MP!")
#         return mana_availability
#
#
# def heal(name, health, health_availability):
#     needed_health = 100-health_availability
#     health_availability += health
#     if health_availability >= 100:
#         health_availability = 100
#         print(f"{name} healed for {needed_health} HP!")
#         return health_availability
#     else:
#         print(f"{name} healed for {health} HP!")
#         return health_availability
#
#
# for _ in range(number_of_heroes):
#     [hero_name, hp_points, mana_points] = input().split(" ")
#     hp_points = int(hp_points)
#     mana_points = int(mana_points)
#     heroes_data[hero_name] = {"HP": hp_points, "MP": mana_points}
#
# while True:
#     command = input()
#     if command == "End":
#         break
#
#     action = command.split(" - ")
#     current_action = action[0]
#     current_name = action[1]
#     current_value = int(action[2])
#     if current_action == "CastSpell":
#         current_spell = action[3]
#         heroes_data[current_name]["MP"] = \
#             cast_spell(current_name, current_value, current_spell, heroes_data[current_name]["MP"])
#     elif current_action == "TakeDamage":
#         current_attacker = action[3]
#         heroes_data = \
#             take_dmg(current_name, current_value, current_attacker, heroes_data)
#     elif current_action == "Recharge":
#         heroes_data[current_name]["MP"] = \
#             recharge(current_name, current_value, heroes_data[current_name]["MP"])
#     elif current_action == "Heal":
#         heroes_data[current_name]["HP"] = \
#             heal(current_name, current_value, heroes_data[current_name]["HP"])
#
# filtered_heroes = sorted(heroes_data.items(), key=lambda x: (-x[1]["HP"], x[0]))
#
# for hero, data in filtered_heroes:
#     print(hero)
#     print(f"HP: {data['HP']}")
#     print(f"MP: {data['MP']}")
#
# # Variant 3
# number_of_heroes = int(input())
#
# dictionary = {}    # {'Solmyr': [85, 120], 'Kyrre': [99, 50]}
#
# MAX_HEALTH = 100
# MAX_MANA = 200
#
# for _ in range(number_of_heroes):
#     hero = input().split()
#
#     name = hero[0]
#     health = int(hero[1])
#     mana = int(hero[2])
#
#     dictionary[name] = [health, mana]
#
# while True:
#     command = input()
#
#     if command == "End":
#         break
#
#     actions = command.split(" - ")
#
#     type_of_action = actions[0]
#     name = actions[1]
#
#     if type_of_action == "CastSpell":
#         mana_needed = int(actions[2])
#         spell_name = actions[3]
#         if dictionary[name][1] - mana_needed >= 0:
#             dictionary[name][1] -= mana_needed
#             print(f"{name} has successfully cast {spell_name} and now has {dictionary[name][1]} MP!")
#         else:
#             print(f"{name} does not have enough MP to cast {spell_name}!")
#
#     elif type_of_action == "TakeDamage":
#         damage = int(actions[2])
#         attacker = actions[3]
#         if dictionary[name][0] - damage > 0:
#             dictionary[name][0] -= damage
#             print(f"{name} was hit for {damage} HP by {attacker} and now has {dictionary[name][0]} HP left!")
#         else:
#             del dictionary[name]
#             print(f"{name} has been killed by {attacker}!")
#
#     elif type_of_action == "Recharge":
#         amount = int(actions[2])
#         current_mana = dictionary[name][1]
#         if dictionary[name][1] + amount <= MAX_MANA:
#             dictionary[name][1] += amount
#             print(f"{name} recharged for {amount} MP!")
#         else:
#             dictionary[name][1] = MAX_MANA
#             print(f"{name} recharged for {MAX_MANA - current_mana} MP!")
#
#     elif type_of_action == "Heal":
#         amount = int(actions[2])
#         current_health = dictionary[name][0]
#         if dictionary[name][0] + amount <= MAX_HEALTH:
#             dictionary[name][0] += amount
#             print(f"{name} healed for {amount} HP!")
#         else:
#             dictionary[name][0] = MAX_HEALTH
#             print(f"{name} healed for {MAX_HEALTH - current_health} HP!")
#
# for hero, stats in dictionary.items():
#     print(f"{hero}\n  HP: {stats[0]}\n  MP: {stats[1]}")