def solution(logs):
    answer = -1
    cnt = 0
    loglist = [[] for _ in range(len(logs))]
    loglist2 = [[] for _ in range(len(logs))]
    for i in range(len(logs)):
        loglist[i] += (logs[i].split(" : "))

    for i in range(len(loglist)):
        for j in loglist[i]:
            loglist2[i] += (j.split(" "))

    for i in loglist2:
        str_len = 0
        for j in i:
            str_len += len(j)
        if 'team_name' not in i:
            cnt += 1
        elif 'application_name' not in i:
            cnt += 1
        elif 'error_level' not in i:
            cnt += 1
        elif 'message' not in i:
            cnt += 1
        elif len(i) != 8:
            cnt += 1
        elif str_len > 100:
            cnt += 1
        for j in i:
            if any(x in j for x in '!@#$%^&*') == True:
                cnt += 1
            elif any(str(x) in j for x in range(10)) == True:
                cnt += 1
    answer = cnt
    return answer



logs =["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]

print(solution(logs))

