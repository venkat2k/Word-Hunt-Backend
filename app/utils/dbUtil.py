import pymysql
import os

connection = None

dbCredentials = {
    "HOST": os.environ["DB_HOST"],
    "NAME": os.environ["DB_USERNAME"],
    "PASSWORD": os.environ["DB_PASSWORD"],
    "DBNAME": os.environ["DB_NAME"]
}
def getDBConnection():
    global connection
    if connection == None:
        connection = pymysql.connect(host=dbCredentials["HOST"], user=dbCredentials["NAME"], passwd=dbCredentials["PASSWORD"], database=dbCredentials["DBNAME"]);
    return connection

