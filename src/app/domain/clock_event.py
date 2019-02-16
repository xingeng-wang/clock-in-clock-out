import MySQLdb
from settings import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_NAME, MYSQL_TABLE_NAME
from datetime import datetime


def creat_clock_event(first_name, last_name, clock_type):
    """
    create a new clock event in the sql database

    :param first_name: first name
    :param last_name: last name
    :param clock_type: one of the clockIn or clockOut
    :param time: clock in/out time
    """
    db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_NAME)
    cursor = db.cursor()
    time = datetime.utcnow()
    sql = 'INSERT INTO %s(FIRST_NAME, LAST_NAME, EVENT_TIME, TIME) VALUES (%s, %s,%s, %s)' \
        .format(MYSQL_TABLE_NAME, first_name, last_name, clock_type, time)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        raise Exception('Failed to Clock In/Out')
    db.close()


def list_clock_event():
    pass
