#pip install requests
#pip install json

import requests
import json
from datetime import datetime


urlPost =  "" 


def postData(json_Data):
	r=requests.post(urlPostjsonData, json_Data)
	if r.status_code == requests.codes.ok:
		print("ok")
		print(str(r.status_code))
		return r.status_code
	else: 
		print("not ok")
		print(str(r.status_code))
		return r.status_code


def formatJson(piId,sensorId, pic,  dateTime):
	print("In JSON")
	pic =1
	
	print("piid" + piId)
	print("date " + dateTime)
	json_data = {"deviceId":piId,"sensorId": sensorId,"datetime":dateTime,"img":pic}

	print(json_data)
	return json_data


formatJson("1","2",9, str(datetime.time(datetime.now())))
