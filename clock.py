from apscheduler.schedulers.blocking import BlockingScheduler
import deathcount

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=60)
def timed_job():
    deathcount.job()

if __name__ == "__main__":
    twische.start()
