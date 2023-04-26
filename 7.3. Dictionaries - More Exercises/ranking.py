contests, users = {}, {}
contest_data = input()

while contest_data != "end of contests":
    contest, password = contest_data.split(":")
    contests[contest] = password
    contest_data = input()

submission_data = input()

while submission_data != "end of submissions":
    contest, password, username, points = [int(x) if x.isdigit() else x for x in submission_data.split("=>")]

    if contests.get(contest) == password:
        users[username] = users.get(username, {})
        users[username][contest] = users[username].get(contest, 0)

        if users[username][contest] < points:
            users[username][contest] = points

    submission_data = input()


candidates = {name: sum(users[name].values()) for name in users}
best_candidate = max(candidates, key=candidates.get)
print(f"Best candidate is {best_candidate} with total {candidates[best_candidate]} points."
      f"\nRanking:")

for name in sorted(users):
    print(name)
    for contest, points in sorted(users[name].items(), key=lambda item: -item[1]):
        print(f"#  {contest} -> {points}")