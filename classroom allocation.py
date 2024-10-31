import random

from tabulate import tabulate


class day1:
    day = [['NULL' for i in range(10)] for j in range(4)]


class day2:
    day = [['NULL' for i in range(10)] for j in range(4)]


class day3:
    day = [['NULL' for i in range(10)] for j in range(4)]


class day4:
    day = [['NULL' for i in range(10)] for j in range(4)]


class day5:
    day = [['NULL' for i in range(10)] for j in range(4)]


day = [0 for i in range(5)]

day[0] = day1
day[1] = day2
day[2] = day3
day[3] = day4
day[4] = day5


class test:
    def _init_(self, k, i, j):
        self.k = k
        self.i = i
        self.j = j


def unassigned():
    for k in range(6):
        for i in range(4):
            for j in range(10):
                if (day[k].day[i][j] == 'NULL'):
                    return test(k, i, j)


def consistant(k, i, j):
    val = day[k].day[i][j]
    val = val[:3]

    if (i == 1):
        if (day[k].day[i + 1][j][:3] != val and day[k].day[i + 2][j][:3] != val):
            return True
    if (i == 2):
        if (day[k].day[i - 1][j][:3] != val and day[k].day[i + 1][j][:3] != val):
            return True
    if (i == 3):
        if (day[k].day[i - 1][j][:3] != val and day[k].day[i - 2][j][:3] != val):
            return True
    else:
        return False


def csp_backtrack(domains):
    if len(domains) == 0:
        return True

    u = unassigned()
    k = u.k
    i = u.i
    j = u.j

    for val in domains:
        day[k].day[i][j] = val
        if consistant(k, i, j):
            domains.remove(val)
            return csp_backtrack(domains)
        else:
            day[k].day[i][j] = 'NULL'
    return False


if _name_ == "_main_":
    # variables= [mon, tue, wed, ths, fri]
    for k in range(5):
        day[k].day[0][0] = "MONDAY"
        day[k].day[0][1] = "9:00AM-9:45AM"
        day[k].day[0][2] = "9:45AM-10:30AM"
        day[k].day[0][3] = "10:30AM-11:15AM"
        day[k].day[0][4] = "11:15AM-12:30PM"
        day[k].day[0][5] = "12:30PM-1:15PM"
        day[k].day[0][6] = "1:15PM-2:00PM"
        day[k].day[0][7] = "2:00PM-2:45PM"
        day[k].day[0][8] = "2:45PM-3:30PM"
        day[k].day[0][9] = "3:30PM-4:15PM"
        day[k].day[1][5] = "BREAK"
        day[k].day[2][5] = "BREAK"
        day[k].day[3][5] = "BREAK"
        day[k].day[1][0] = "ROOM1"
        day[k].day[2][0] = "ROOM2"
        day[k].day[3][0] = "ROOM3"

    day[1].day[0][0] = "TUESDAY"
    day[2].day[0][0] = "WEDNESDAY"
    day[3].day[0][0] = "THURSDAY"
    day[4].day[0][0] = "FRIDAY"

    domains = ["AI_1", "AI_2", "AI_3", "AI_4", "AI_5", "AI_1.", "AI_2.", "AI_3.", "AI_4.", "AI_5.", "AIL_1", "AIL_2",
               "AIL_3", "AIL_4", "AIL_5",
               "CD_1", "CD_2", "CD_3", "CD_4", "CD_5", "CD_1.", "CD_2.", "CD_3.", "CD_4.", "CD_5.", "CDL_1", "CDL_2",
               "CDL_3", "CDL_4", "CDL_5",
               "CN_1", "CN_2", "CN_3", "CN_4", "CN_5", "CN_1.", "CN_2.", "CN_3.", "CN_4.", "CN_5.", "CNL_1", "CNL_2",
               "CNL_3", "CN_4", "CNL_5",
               "DBMS_1", "DBMS_2", "DBMS_3", "DBMS_4", "DBMS_5", "DBMS_1.", "DBMS_2.", "DBMS_3.", "DBMS_4.", "DBMS_5.",
               "DBMSL_1", "DBMSL_2", "DBMSL_3", "DBMSL_4", "DBMSL_5",
               "MAT_1", "MAT_2", "MAT_3", "MAT_4", "MAT_5", "MAT_1.", "MAT_2.", "MAT_3.", "MAT_4.", "MAT_5.",
               "ISCP_1", "ISCP_2", "ISCP_3", "ISCP_4", "ISCP_5", "ISCP_1.", "ISCP_2.", "ISCP_3.", "ISCP_4.", "ISCP_5.",
               "CDC_1", "CDC_2", "CDC_3", "CDC_4", "CDC_5", "CDC_1.", "CDC_2.", "CDC_3.", "CDC_4.", "CDC_5.",
               "AI_6", "AI_6.", "AIL_6", "CD_6", "CD_6.", "CNL_6", "CN_6", "CN_6.", "CNL_6", "DBMS_6", "DBMS_6.",
               "DBMSL_6",
               "MAT_6", "MAT_6.", "ISCP_6", "ISCP_6", "CDC_6", "CDC_6.", "OE_1", "OE_1.", "OE_2", "OE_2.", "OE_3",
               "OE_3.", "OE_4",
               "OE_4.", "OE_5", "OE_5.", "OE_6", "OE_6."
               ]

    random.shuffle(domains)

    if csp_backtrack(domains):
        print("\n")
        print(tabulate(day[0].day, headers="firstrow"))
        print("\n")
        print(tabulate(day[1].day, headers="firstrow"))
        print("\n")
        print(tabulate(day[2].day, headers="firstrow"))
        print("\n")
        print(tabulate(day[3].day, headers="firstrow"))
        print("\n")
        print(tabulate(day[4].day, headers="firstrow"))
        print("\n")
    else:
        print("Solution not found")