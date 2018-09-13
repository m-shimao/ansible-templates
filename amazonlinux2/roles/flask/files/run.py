from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'test'
app.config['MYSQL_DATABASE_PASSWORD'] = 'test'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql.init_app(app)

def ExecuteQuery(sql):
  cur = mysql.connect().cursor()
  cur.execute(sql)
  results = [dict((cur.description[i][0], value)
    for i, value in enumerate(row)) for row in cur.fetchall()]
  return results

@app.route('/')
def index():
  results = ExecuteQuery('select unix_timestamp();')
  return jsonify(results)

if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.jinja_env.auto_reload = True
  app.run(debug=True, host='0.0.0.0')
