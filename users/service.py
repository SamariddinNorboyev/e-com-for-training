from threading import Thread
from django.core.mail import send_mail
from .models import CustomUserModel, Code
from .utils import code_generate
def send_email_letter(to):
    code = code_generate()
    user = CustomUserModel.objects.filter(email=to).first()
    code_save = Code.objects.create(code = code, user = user)
    send_mail(
        subject='Test subject',
        message='test messege',
        from_email='samariddin.grex@gmail.com',
        recipient_list=[to],
        html_message=f"""
            <main>
                <h1>Salom, {user.email}!</h1>
                <h2>{code_save.code} </h2>
                <i><h4>Bu kodni restore passwordga kiriting!</h4></i>
                <b><h3>Agar parolni o'zgartirmoqchi bo'lmasangiz, hech narsa qilmang!</h3></b>
            </main>
        """
    )


def send_email_async(to):
    thread1 = Thread(target=send_email_letter, args=(to,))
    thread1.start()