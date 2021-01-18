import requests, json
from datetime import datetime, timedelta
from time import mktime, strptime

date_list = []
acceleration_list = []
altitude_list = []

date_now = datetime.now()
print(date_now)
date_now = (date_now - timedelta(hours=1))
print(date_now)
date_now = date_now.strftime("%Y-%m-%d %H:%M:%S")
print(date_now)

url = "http://210.119.145.22/data/"
d = {"number": 5076905, "date": date_now}
res = requests.post(url, d)
mybytes = res.text
mybytes = json.loads(mybytes)
print(res.status_code)
print(mybytes)

# for i in mybytes:
#     print(i)
#     utc_now = mktime(strptime(str(i['date']), '%Y-%m-%d %H:%M:%S')) * 1000
#     date_list.append(i['date'])
#     acceleration_list.append([utc_now, i['acceleration_z']])
#     altitude_list.append([utc_now, i['current_altitude']])
#
# # print(date_list)
# # print(acceleration_list)
# # print(altitude_list)

# class ElvtAPIVIEW_D(APIView):
# 	authentication_classes = []
# 	permission_classes = []
#
# 	def get(self, request):
# 		date_list = []
# 		acceleration_list = []
# 		altitude_list = []
#
# 		url = "http://210.119.145.22/data/"
# 		d = {"number": number}
# 		res = requests.post(url, d)
# 		mybytes = res.text
# 		mybytes = json.loads(mybytes)
#
# 		for i in mybytes:	# 하루
# 			date_now = datetime.now()
# 			date_now = (date_now - timedelta(days=1))
# 			date_now = date_now.strftime("%Y-%m-%d %H:%M:%S")
# 			date_now = datetime.strptime(date_now, "%Y-%m-%d %H:%M:%S").date()
# 			date_res = datetime.strptime(i['date'], "%Y-%m-%d %H:%M:%S").date()
# 			if date_res > date_now:
# 				utc_now = mktime(strptime(str(i['date']), '%Y-%m-%d %H:%M:%S')) * 1000
# 				date_list.append(i['date'])
# 				acceleration_list.append([utc_now, i['acceleration_z']])
# 				altitude_list.append([utc_now, i['current_altitude']])
# 			else :	# 하루 이후(지난) 데이터
# 				pass
# 		context = {
# 			'acceleration': acceleration_list,
# 			'altitude': altitude_list,
# 			'date': date_list
# 		}
# 		return Response(context)