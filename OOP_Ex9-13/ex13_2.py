from flask import Flask
import mysql.connector

connection = mysql.connector.connect(
    # use own DB name and pass if different
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="password"
)
cursor = connection.cursor()

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def redirect():
    return f'Click the <a href="/airport/">link</a> for further instructions'


@app.route('/airport/')
def icao_search():
    return f'Enter ICAO code in the end of the URL to get information about the airport'


@app.route('/airport/<ICAO>', methods=['GET'])
def request_info(ICAO):
    sql = f'SELECT ident, name, municipality FROM airport WHERE ident = "{ICAO.upper()}"'
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) == 0:
        return {"ICAO": ICAO.upper(), "Name": "Not found", "Location": "Not found"}
    return {"ICAO": results[0][0], "Name": results[0][1], "Location": results[0][2]}


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
