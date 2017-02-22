import apache_log_parser
from pprint import pprint

line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b")
fs = open("files/NASA_access_log_Aug95")
fo = open("results.txt","w" )

res = ""
fo.write("remote_host,request_method,request_url,status,time_received\n")

for line in fs:
	 json = line_parser(line)
	 res = json['remote_host'] + "," + json['request_method'] + "," + json['request_url'] + "," + json['status'] + "," + json['time_received'] + "\n"
	 fo.write(res)

