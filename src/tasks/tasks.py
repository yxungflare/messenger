import smtplib
from email.message import EmailMessage

from celery import Celery
from config import SMTP_USER, SMTP_PASSWORD

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465

# Редис - для исполнения задач
celery = Celery('tasks', broker='redis://localhost:6379')


def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = 'Натрейдил Отчет Дашборд'
    email['From'] = SMTP_USER # наша почта
    email['To'] = SMTP_USER # почта получателя

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчет. Зацените 😊</h1>'
        '<img src="https://static.vecteezy.com/system/resources/previews/008/295/031/original/custom-relationship'
        '-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app'
        '-mobile-free-vector.jpg" width="600">'
        '</div>',
        subtype='html'
    )
    return email


# Для запуска celery:           | можно bit - каждый день выполнение
# celery -A tasks.tasks:celery worker --loglevel=INFO --pool=solo(Для винды)
# celery -A tasks.tasks:celery flower
@celery.task
def send_email_report_dashboard(username:str):
    # Генерация шаблона
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        # Авторизация и отправка
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)