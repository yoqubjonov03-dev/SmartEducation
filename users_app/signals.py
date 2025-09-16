import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from billing.models import Payments
from django.conf import settings

# @receiver(post_save, sender=Payments)
# def notify_admin(sender, instance, created, **kwargs):
#     if created:
#         token = settings.TELEGRAM_BOT_TOKEN
#         chat_id = 5145991019  # admin ID
#         url = f'https://api.telegram.org/bot{token}/sendMessage'
#
#         message_text = (
#             f"💳 New Payment!\n\n"
#             f"Payment ID: {instance.id}\n"
#             f"Enrolment ID: {instance.enrollment_id.id}\n"
#             f"Amount: {instance.amount}\n"
#             f"Method: {instance.payment_method}"
#         )
#
#         try:
#             response = requests.post(url, data={'chat_id': chat_id, 'text': message_text})
#             print("Telegram response:", response.json())  # debug uchun
#         except Exception as e:
#             print("Telegramga habar yuborishda xato:", e)

@receiver(post_save, sender=Payments)
def notify_admin(sender, instance, created, **kwargs):
    if created:
        token = settings.TELEGRAM_BOT_TOKEN
        chat_id = 5145991019
        url = f'https://api.telegram.org/bot{token}/sendMessage'

        message_text = (f"New Payment: {instance.id}\nEnrolment: {instance.enrollment_id.id}\n"
                        f"amount: {instance.amount}\npayment_method: {instance.payment_method}")
        response=requests.post(
            url=url,
            data={'chat_id':chat_id, 'text':message_text}
        )



