import pymysql
import os

dbCredentials = {
    "HOST": os.environ["DB_HOST"],
    "NAME": os.environ["DB_USERNAME"],
    "PASSWORD": os.environ["DB_PASSWORD"],
    "DBNAME": os.environ["DB_NAME"]
}
def getDBConnection():
    connection = pymysql.connect(host=dbCredentials["HOST"], user=dbCredentials["NAME"], passwd=dbCredentials["PASSWORD"], database=dbCredentials["DBNAME"]);
    return connection

