
from core.models import Session 

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files import File 

import qrcode 
from io import BytesIO


#generating a qrcode for session ,
#applicants can this qrcode for attendance

@receiver(post_save, sender=Session, dispatch_uid="generate_qrcode")
def genereate_qrcode(sender, instance, created, **kwargs):
    print('signal fired!!!'.upper())

    if created:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,

        )

        qrcode_data = instance.qr_token

        qr.add_data(qrcode_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, 'png')
        buffer.seek(0)

        filename = f"qr_code_{str(instance.qr_token)[:8]}.png"

        instance.qrcode.save(filename, File(buffer), save=False)
        instance.save(update_fields=['qrcode'])

        print(f"✅ QRCode save for {instance.qr_token}")

