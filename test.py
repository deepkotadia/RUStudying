import pymongo, json
import pdb
from flask import *
app = Flask(__name__)

client = pymongo.MongoClient()
iterative=0
@app.route('/')
def index():
	return render_template('index.html')


@app.route("/search", methods=['GET', 'POST'])
def display():
	
	meetingDay = request.form["meetingDay"]
	campusName = request.form["campusName"]
	cursor = client.rutgers.classinfo.aggregate([ {"$unwind": "$sections"}, {"$unwind": "$sections.meetingTimes"}, { "$match": { "sections.meetingTimes.campusName": campusName}},{"$match": { "sections.meetingTimes.meetingDay": meetingDay}}])
	final = []
	for i in cursor:
		curr = {}
		meet = i['sections']['meetingTimes']
		curr['buildingCode'] = meet['buildingCode']
		curr['roomNumber'] = meet['roomNumber']
		curr['startTime'] = meet['startTime']
		curr['endTime'] = meet['endTime']
		final.append(curr)
		
	for j in range(0,len(final)-3):
		print final[j] 
		print final[j+1]
		print final[j+2]
		print final[j+3]
		print '\n'
	return json.dumps(final)
		

if __name__=="__main__":
	app.run(debug=True)

