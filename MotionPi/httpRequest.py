#pip install requests
#pip install json

import requests
import json
import logging



urlPost = "http://54.210.23.150:8080/demo/addMotion"
urlLocal = "http://192.168.0.107:8080/demo/addMotion"


def postData(json_Data):
	logging.info("Posting Data")
        try:
		r=requests.post(urlPost, json=json_Data, timeout = 30)
	
		if r.status_code == requests.codes.ok:
			print("ok")
                        print(str(r.status_code))
			return r.status_code
		else: 
			print("not ok")
			print(str(r.status_code))
			return r.status_code
	except:
		logging.warning("error Posting data")
                return 0

def formatJson(piId,sensorId,dateTime, pic):
	try:
                #dateTime = datetime.datetime.fromtimestamp(dateTime).strftime('%Y-%m-%d %H:%M:%S')
		json_data = {"deviceId":piId,"sensorId": sensorId,"event_occurred":dateTime,"img":pic}
		#print json.dumps(json_data)	
		return json_data
	except:
		logging.warning("error converting to json")
		return "0"
