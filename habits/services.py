import json
from datetime import datetime, timedelta

from django_celery_beat.models import IntervalSchedule, PeriodicTask


def get_schedule(*args, **kwargs):
    """Создание расписания по привычки каждую минуту. """
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.MINUTES,
    )

    # Создаем задачу для повторения
    PeriodicTask.objects.create(
        interval=schedule,
        name='check_habits',
        task='habits.tasks.check_habits',
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )
