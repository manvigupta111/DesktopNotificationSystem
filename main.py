import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
                title = "Please drink water now",
                message = "Science shows that drinking water at the correct times of day can help to prevent common problems such as stomach pain, IBS, bloating, fatigue, overeating, high blood pressure, constipation, and even heart attack and stroke.",
                app_icon="C:\\Users\Manvi Gupta\\Desktop\\python projects\\desktopnotification\\icon.ico.ico",
                timeout = 2
            )
        time.sleep(60*60*60)


