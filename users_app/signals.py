
from django.db.models.signals import post_save
from django.dispatch import receiver
from billing.models import Payments
from .tasks import send_telegram_notification
from users_app.models import Enrollments

@receiver(post_save, sender=Payments)
def notify_admin(sender, instance, created, **kwargs):
    if created:
        send_telegram_notification.delay(
            payment_id=instance.id,
            enrollment_id=instance.enrollment_id.id,
            amount=instance.amount,
            payment_method=instance.payment_method
        )

@receiver(post_save, sender=Payments)
def update_enrollment_is_paid(sender, instance, created, **kwargs):
    if created and instance.enrollment_id:
        enrollment = instance.enrollment_id
        enrollment.is_paid = True
        enrollment.save(update_fields=["is_paid"])

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



