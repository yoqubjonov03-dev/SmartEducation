import requests
import time
from django.conf import settings
from celery import shared_task


@shared_task()
def send_telegram_notification(payment_id, enrollment_id, amount, payment_method):
    time.sleep(5)
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = 5145991019
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    message_text = (f"New Payment: {payment_id}\nEnrolment: {enrollment_id}\n"
                    f"amount: {amount}\npayment_method: {payment_method}")
    response = requests.post(
        url=url,
        data={'chat_id': chat_id, 'text': message_text}
    )
