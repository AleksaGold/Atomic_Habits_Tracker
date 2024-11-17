from celery import shared_task

from habit.models import Habit
from habit.services import send_telegram_message

from datetime import timedelta
from django.utils import timezone

CURRENT_TIME = timezone.now()


@shared_task
def send_reminder_to_telegram():
    """Фоновая задача, которая отправляет напоминание в Telegram-чат."""
    habits = Habit.objects.filter(owner__isnull=False)
    for habit in habits:
        tg_chat_id = habit.owner.tg_chat_id
        message = f"Привет, тебе сегодня нужно"
        message += f"\n\nСделать: {habit.name}"
        message += f"\nГде: {habit.condition.place}"
        message += f"\nКогда: {habit.condition.start_time}"
        if habit.next_sending is None:
            send_telegram_message(message, tg_chat_id)
            habit.next_sending = CURRENT_TIME
        elif habit.next_sending < CURRENT_TIME:
            send_telegram_message(message, tg_chat_id)
            habit.next_sending = CURRENT_TIME + timedelta(days=habit.condition.frequency)
        habit.save()
