def task_solvable(n):
    return (n * 3) % 2 == 0


def fisherman():
    successful_teams = 0
    while True:
        n = int(input())
        if n == 0:
            break
        if n % 2 == 0:
            successful_teams += task_solvable(n)

    print(successful_teams)
fisherman()
