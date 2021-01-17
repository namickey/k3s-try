from flask import Flask, jsonify, request
import time
import psycopg2.pool

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
#conn = psycopg2.connect("host=192.168.1.30 dbname=postgres user=postgres password=postgres")
pool = psycopg2.pool.ThreadedConnectionPool(minconn=5, maxconn=35, host="192.168.1.30", dbname="postgres", user="postgres", password="postgres")

@app.route('/')
def index():
  conn = pool.getconn()
  cur = conn.cursor()
  cur.execute('INSERT INTO task (name, date) VALUES (%s, now());', ('aa',))
  conn.commit()
  cur.execute("SELECT max(id) from task")

  try:
    tasks = cur.fetchall()
    max = ''
    for row in tasks:
      if row:
        max = str(row[0])
    pool.putconn(conn)
    return jsonify({
      "message": "max id is " + max
    })
  except psycopg2.ProgrammingError:
    pool.putconn(conn)
    return jsonify({
      "message": "error"
    })

if __name__ == '__main__':
  app.run(threaded=true)
