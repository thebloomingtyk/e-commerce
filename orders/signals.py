from django.dispatch import receiver
from orders.models import Order
from django.db.models.signals import post_save
from django.contrib import messages


from django.core.mail import send_mail
@receiver(post_save, sender=Order)
def send_email(sender , instance, created, **kwargs):
    if created:
        
        subject = f'{instance.first_name} {instance.last_name} made an order'
        recipient = ['tykdbk@gmail.com']
        # message = f'Hello. We have a new message on our blog. Visit our blog to read the post.Post: "The order made {instance}" at https://lifecookies.com/post/{str(instance)}'
        from_email = 'The Afric group'
        # messages = [subject, message, from_email, recipient]
        # send_mail(messages)
        # first_name, last_name, phone_number, address
        #  {instance.product} {instance.quantity}
        message = f'Hello Phone number: {instance.phone_number} Address: {instance.address} made an order'


        import datetime
        now = datetime.datetime.now()
        hour = now.hour
        min = now.minute+1
        import pywhatkit as kit
        kit.sendwhatmsg("+255754661191", f'{instance.first_name} {instance.last_name} made an order. Phone number: {instance.phone_number} Address: {instance.address}', hour, min)

        send_mail(
        subject, message, from_email, recipient,
        fail_silently=False
        )
        if send_email:
            print('mail sent successfully')

