import app.utils.dbUtil as dbUtil
import random

def chooseWord():
    connection = dbUtil.getDBConnection()
    cursor = connection.cursor()
    index = random.randint(0, 2030)
    query = "SELECT word FROM words  LIMIT 1 OFFSET {0}".format(index)
    cursor.execute(query)
    word = cursor.fetchone()[0]
    return word

def updateScore(name, score):
    connection = dbUtil.getDBConnection()
    cursor = connection.cursor()
    query = """INSERT INTO scores(name, score) VALUES("{0}", {1})""".format(name, score)
    cursor.execute(query)
    connection.commit()

def getTopScores():
    connection = dbUtil.getDBConnection()
    cursor = connection.cursor()
    query = """SELECT score, name FROM scores ORDER BY score DESC LIMIT 10"""
    cursor.execute(query)
    data = cursor.fetchall()
    result = []
    for row in data:
        result.append({
            "score": row[0],
            "name": row[1]
        })
    return result