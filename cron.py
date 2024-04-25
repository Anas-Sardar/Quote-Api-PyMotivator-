from datetime import time
from apscheduler.schedulers.background import BackgroundScheduler
from Motivator import send_whatsapp_text,client,quote,author

scheduler = BackgroundScheduler(timezone="Asia/Karachi")
scheduler.start()

job = scheduler.add_job(send_whatsapp_text,'corn',[client,quote,author],hour="13",minute="52")
print(job)

while True:
 time.sleep(1)