from collections import defaultdict


def solution(id_list, report, k):

    reported_list = defaultdict(set)
    warned_list = defaultdict(int)
    email_list = []
    res = []

    for each in report:
        reported_user, warned_user = each.split(' ')
        if warned_user in reported_list[reported_user]:
            continue
        reported_list[reported_user].add(warned_user)
        warned_list[warned_user] += 1

    for each in warned_list:
        if warned_list[each] >= k:
            email_list.append(each)

    for each in id_list:
        cnt = 0
        for individual in email_list:
            if individual in reported_list[each]:
                cnt += 1
        res.append(cnt)

    return res
    