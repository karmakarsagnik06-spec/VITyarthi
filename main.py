import csv
import os
from datetime import datetime

file = "attendance.csv"

def readfile():
    data = []
    if os.path.exists(file):
        f = open(file,"r",encoding="utf-8")
        rr = csv.reader(f)
        for r in rr:
            if len(r)==3:
                data.append(r)
        f.close()
    return data


def writefile(name, date, status):
    f = open(file,"a",newline="",encoding="utf-8")
    w = csv.writer(f)
    w.writerow([name,date,status])
    f.close()



def mark():
    n = input("name: ")
    s = input("status (present/absent): ")

    s = s.lower()
    if s=="present":
        s = "Present"
    elif s=="absent":
        s = "Absent"
    else:
        print("wrong input")
        return

    d = datetime.now().strftime("%Y-%m-%d")
    writefile(n, d, s)
    print("saved")



def show():
    d = readfile()
    if d==[]:
        print("no data")
        return

    for i in d:
        print(i[0], i[1], i[2])



def search():
    n = input("enter name: ")
    d = readfile()
    f = 0

    for i in d:
        if i[0].lower()==n.lower():
            print(i[0], i[1], i[2])
            f=1

    if f==0:
        print("not found")



def main():
    while True:
        print("\n1 mark attendance")
        print("2 show all")
        print("3 search")
        print("4 exit")

        c = input("choice: ")

        if c=="1":
            mark()
        elif c=="2":
            show()
        elif c=="3":
            search()
        elif c=="4":
            break
        else:
            print("invalid")

main()
