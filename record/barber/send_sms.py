from sms import send_sms
import random


def random_code() -> str:

    code_list = []
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(4):
        code_list.append(str(random.choice(number)))

    return ''.join(code_list)


send_sms(
    random_code(),
    '+792195440445',
    ['+79219544045'],
    fail_silently=False
)