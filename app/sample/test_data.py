from app.db import db
from app.sample import test_acc, test_cl


# заполнение базы тестовыми данными
def insert_test_data():
    print('test data has been added')
    db.create_db()
    db.insert_test_data('client', test_cl)
    db.insert_test_data('account', test_acc)
    tma = db.select_join()
    for t in tma:
        print(t)
