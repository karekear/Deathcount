from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import deathcount

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=1)
#@twische.scheduled_job('cron',minutes=0) #毎時00分に実行
def timed_job():
    deathcount.job()

if __name__ == "__main__":
    twische.start()

#deathcount.job()