from app.db import db
from app import setting


# проверка на тип данных
def is_float(s):
    if s.count(".") == 0:
        if s.isdigit():
            return True
    elif s.count(".") == 1:
        if s.replace(".", "").isdigit():
            return True
    return False


# функция перевода денег
def transfer_money(value):
    if not value:
        return 'please input command "transfer from xxxxxxxxx to xxxxxxxx sum".\n' +\
                'command must contain 1 space between values'

    elif len(value) < 5:
        return 'please input command "transfer from xxxxxxxxx to xxxxxxxx sum".\n' +\
                'command must contain 1 space between values'
    elif not value[1].isdigit() or not value[3].isdigit():
        answer = 'account must be digits'
        return answer
    elif not is_float(value[4]):
        return 'sum must be digits or float (3434 or 234.1) with separate "."'
    else:
        balance_dst = db.select_balance(value[3])
        balance_src = db.select_balance(value[1])
        if balance_dst and balance_src:
            if float(balance_dst) > float(setting.MAX_BALANCE):
                return 'limit dst balance'
            elif float(balance_src) < float(value[4]):
                return 'there is not enough money in your account'
            else:
                db.update_balance(value[1], value[3], value[4])
                return 'success'
        else:
            return 'one of accounts does not exist'

