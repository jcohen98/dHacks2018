# server.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import pymysql.cursors
import time

app = Flask(__name__, static_folder="../static", template_folder="../static")

conn = pymysql.connect(host='bengis.cjgicbekjjvr.us-east-1.rds.amazonaws.com',
                       user='sight',
                       password='ICantSee',
                       db='sight',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
while(True):
    with conn.cursor() as cur:
        qu = "SELECT @diff := TIMESTAMPDIFF(SECOND, (SELECT date FROM loc ORDER BY date ASC LIMIT 1), date) as time, x, y \
			FROM loc WHERE @diff > %s;"
        cur.execute(qu, 30)
        result = cur.fetchone()
        print(result)
        conn.commit()
    time.sleep(0.5)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
