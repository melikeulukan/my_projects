from plyer import notification
import time
import random
import glob
path="C:\\Users\melik\PycharmProjects\pythonotificationapp\photos\\"
icons=glob.glob(path+"*.ico")
my_icon=random.choice(icons)
my_title="Time For a Little Break!"
my_message="This notification is to remind you to rest a bit"

if __name__=='__main__':
    while True:
        my_icon = random.choice(icons)
        notification.notify(title=my_title,
                            message=my_message,
                            timeout=3,
                            app_icon= my_icon)
        time.sleep(20*60)


