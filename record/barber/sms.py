from sms import send_sms


send_sms(
    'Here is the message',
    '+792195440445',
    ['+79219544045'],
    fail_silently=False
)