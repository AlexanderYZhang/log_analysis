import apache_log_parser
from pprint import pprint

line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b")
fs = open("NASA_access_log_Aug95")
fo = open("results.txt","w" )

res = ""

for line in fs:
	 json = line_parser(line)
	 res = json['remote_host'] + "," + json['request_method'] + "," + json['request_url'] + "," + json['status'] + "," + json['time_received'] + "\n"
	 fo.write(res)

