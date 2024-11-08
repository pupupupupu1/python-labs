# TODO решите задачу
# def task() -> float:
#    ...


# print(task())

def task() -> float:

    a = 0
    sch = 0
    summa = 0
    p1 = 0
    p2 = 0
    f = open("input.json", "r")
    a = f.readlines()

    for i in range(len(a)):
        if a[i].find("score") != -1:
            p1 = float(a[i][((a[i].find("score"))+8):len(a[i])-2])
        elif (a[i].find("weight")) != -1:
            p2 = float(a[i][((a[i].find("weight"))+9):len(a[i])-1])
        if(p1 != 0) and (p2 != 0):
            summa += p1*p2
            p1, p2 = 0, 0
    f.close()

    return round(summa, 3)

print(task())