import apache_log_parser
from pprint import pprint

line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b")
fs = open("files/NASA_access_log_Aug95")
fo = open("results.txt","w" )

res = ""
fo.write("remote_host,request_method,request_url,status,time_received\n")

for line in fs:
	 json = line_parser(line)
	 time = json['time_received_utc_isoformat'].split('T')[0].split('-')[2]
	 res = json['remote_host'] + "," + json['request_method'] + "," + json['request_url'] + "," + json['status'] + "," + time + "\n"
	 fo.write(res)

