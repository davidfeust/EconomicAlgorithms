def apportionment(elections, f):
    division = [[i[1] for i in elections]]

    total = it = 0
    n = len(elections)
    seats = [[0] * n]
    num_of_seats = 120

    while it < num_of_seats:
        division.append([division[0][i] / f(seats[it][i])
                         if f(seats[it][i]) != float('inf') else float('inf') for i in range(n)])
        max_div = max(division[it + 1])

        t = []
        for i in range(n):
            if division[it + 1][i] == float('inf') or max_div == division[it + 1][i]:
                t.append(seats[it][i] + 1)
                total += 1

            else:
                t.append(seats[it][i])
        seats.append(t)
        it += 1
        if total == num_of_seats:
            break

    # print all the iterations:
    # for i in range(it + 1):
    #     max_div_index = max(division[i])
    #     for j in range(n):
    #         if division[i][j] == max_div_index:
    #             print('**{0: <25}'.format(division[i][j]), end='|')
    #         else:
    #             print('  {0: <25}'.format(division[i][j]), end='|')
    #     print()
    #     for j in range(n):
    #         print('  {0: <25}'.format(seats[i][j]), end='|')
    #     print()
    #
    # print the final results:
    for i, v in enumerate(elections):
        print('{0: <5}\t{1: <3}'.format(v[0], seats[it][i]))


def threshold(result, percent):
    """
    return the result after threshold.
    """
    s = sum([i[1] for i in result])
    return [i for i in result if ((i[1] / s) * 100) > percent]


if __name__ == '__main__':
    res = [['אמת', 268767], ['ב', 273836], ['ג', 248391], ['ודעם', 212583],
           ['ז', 395], ['זץ', 663], ['ט', 225641], ['י', 811], ['יז', 34883],
           ['ינ', 408], ['יף', 196], ['יק', 429], ['יר', 256], ['כ', 443],
           ['כך', 1291], ['כן', 292257], ['ל', 248370], ['מחל', 1066892],
           ['מרצ', 202218], ['נ', 486], ['ני', 429], ['נר', 220], ['עם', 167064],
           ['פה', 614112], ['ףז', 1309], ['צי', 441], ['צכ', 253], ['צף', 226],
           ['ץ', 385], ['ק', 463], ['קי', 395], ['קך', 514], ['קץ', 729], ['ר', 17346],
           ['רנ', 1189], ['רף', 592], ['רק', 0], ['שס', 316008], ['ת', 209161]]

    threshold_res = threshold(res, 3.25)

    adams = lambda s: s if s != 0 else float('inf')
    webster = lambda s: s + 0.5
    jefferson = lambda s: s + 1

    print('adams:')
    apportionment(res, adams)
    print('adams after threshold:')
    apportionment(threshold_res, adams)

    print('\nwebster:')
    apportionment(res, webster)
    print('webster after threshold:')
    apportionment(threshold_res, webster)

    print('\njefferson:')
    apportionment(res, jefferson)
    print('jefferson after threshold:')
    apportionment(threshold_res, jefferson)
