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
    time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    sql = "INSERT INTO %s(FIRST_NAME, LAST_NAME, CLOCK_TYPE, EVENT_TIME) VALUES ('%s','%s','%s','%s')" % \
          (MYSQL_TABLE_NAME, first_name, last_name, clock_type, time)
    print sql
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()


def list_clock_event():
    # prepare a cursor object using cursor() method
    db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_NAME)
    cursor = db.cursor()

    sql = "SELECT * FROM %s" % MYSQL_TABLE_NAME
    cursor.execute(sql)
    sql_results = cursor.fetchall()
    results = []
    for row in sql_results:
        event_time = row[3]
        if isinstance(event_time, datetime):
            event_time = unicode(event_time.replace(microsecond=0))
        results.append({'firstName': row[0], 'lastName': row[1], 'clockType': row[2], 'eventTime': event_time})
    db.close()
    return results
