def send_email(message, recipient, *, sender='university.help@gmail.com'):
    tuple_ = '.com', '.ru', '.net'
    result_1_ = (recipient.endswith(tuple_) == 1 and recipient.count('@') == 1
            and sender.endswith(tuple_) == 1 and sender.count('@') == 1)
    result_2_ = (recipient.endswith(tuple_) == 0 or recipient.count('@') == 0
            or sender.endswith(tuple_) == 0 or sender.count('@') == 0)

    if result_1_ == True and recipient == sender:
        print('Нельзя отправить письмо самому себе')
    elif result_2_ == True:
        print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
    elif result_1_ == True and sender == 'university.help@gmail.com':
        print ('Письмо успешно отправлено с адреса <sender> на адрес <recipient>')
    elif result_1_ == True and sender != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@gmail.com', sender='urban.info@gmail.com')
send_email('Пожалуйста исправьте задание',
           'urban.studen@tmail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')