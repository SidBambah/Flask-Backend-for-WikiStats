from flask import Flask, request
import pymongo
import os
app = Flask(__name__)

uri = "mongodb+srv://" + os.environ.get('USERNAME') + ":" + os.environ.get('PASSWORD') + "@" + os.environ.get('HOST') + "/" + os.environ.get('DATABASE') + "?retryWrites=true&w=majority"

mongoClient = pymongo.MongoClient(uri)
db = mongoClient.get_database('wikiStats')
daywise_changes = db.daywise_changes

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/hourlyChangesBarChart')
def hourlyChanges():
    try:
        # Get query parameter
        day = request.args.get('day')

        # Look for record in database and send it back


        return day
    except:
        return "Day not found"

if __name__ == '__main__':
    app.run()