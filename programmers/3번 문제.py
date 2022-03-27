


num_teams	=2
remote_tasks =	["design"]
office_tasks=	["building","supervise"]
employees= ["2 design","1 supervise building design","1 design","2 design"]

def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    team = [[] for _ in range(num_teams+1)]
    for j in range(1, num_teams+1):
        for i in range(len(employees)):
            if str(j) in employees[i]:
                team[j].append([i+1, employees[i]])

    team_cnt = [[] for _ in range(num_teams+1)]
    for i in range(1,num_teams+1):
        team_cnt[i].append(len(team[i]))

    poplist = [[] for _ in range(num_teams+1)]
    for k in range(1, num_teams+1):
        for i in range(len(team[k])):
            for j in office_tasks:
                if j in team[k][i][1]:
                    poplist[k].append(i)
                    break

    for i in range(1, num_teams+1):
        for j in poplist[i]:
            team[i].pop(j)
    for i in range(1, num_teams+1):
        if len(team[i]) == team_cnt[i][0]:
            team[i].pop(0)
    for i in range(1, num_teams+1):
        for j in team[i]:
            answer.append(j[0])

    return answer


print(solution(num_teams, remote_tasks, office_tasks, employees))
