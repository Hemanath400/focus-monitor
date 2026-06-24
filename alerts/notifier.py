from plyer import notification


def send_break_alert():

    notification.notify(
        title="Break Reminder",
        message="You've been coding for too long. Take a short break!",
        timeout=10
    )