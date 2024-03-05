import datetime
import schedule


def job():
    t = datetime.datetime.now().hour
    if not(int(tim[0]) <= t and t <= int(tim[1])):
        print(t * o if t <= 12 else (t-12) * o)

o = str(input())
tim = str(input("Введите время ")).split('-')
schedule.every().hour.at(":59").do(job)

while True:
    schedule.run_pending()
