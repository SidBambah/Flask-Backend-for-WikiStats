from flask import Flask, request, jsonify
import pymongo
import os
from dotenv import load_dotenv

app = Flask(__name__)

# load dotenv in the base root
dotenv_path = os.path.join('./.env')
load_dotenv(dotenv_path)

# Define mongoDB connection
uri = "mongodb+srv://" + os.getenv('USERNAME') + ":" + os.getenv('PASSWORD') + "@" + os.getenv('HOST') + "/" + os.getenv('DATABASE') + "?retryWrites=true&w=majority"

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
        day = request.args.get("day")

        # Look for record in database
        result = daywise_changes.find_one({"day": day}, projection={"_id": 0, "day": 0})

        # Format record and send it back
        result = {"labels": list(result.keys()), "data": list(result.values())}

        if result is not None:
            return result
        else:
            return "Invalid day"
    except:
        return "Invalid query param"

if __name__ == '__main__':
    app.run()