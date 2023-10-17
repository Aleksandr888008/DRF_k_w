from datetime import datetime
from celery import shared_task

from habits.models import Habit
from habits.telegram import send_message


@shared_task
def check_habits():
    """ Напоминание о привычки. """
    now_hour = datetime.now().hour
    now_minute = datetime.now().minute

    habits = Habit.objects.filter(
        time__hour=now_hour,
        time__minute=now_minute
    )

    for habit in habits:
        action = habit.action
        place = habit.place
        execution_time = habit.execution_time
        owner = habit.owner

        text = f"Вам нужно выполнить {action} в {place}, за {execution_time} секунд"

        send_message(
            owner, text
        )
