import urllib 
import re

targets = open("targets.txt", 'r').readlines()

for target in targets:
  target = target.rstrip()
  
  response = urllib.urlopen(target).read()  

  scanjs = re.findall(r'src="([^"]+\.js|json)?"',response) 

  for i in scanjs:

    new_target = target + i

    if(re.match(r'(http|https)\:\/\/',i)):
      new_target = i

    js_file_request = urllib.urlopen(new_target).read()
    callback_possibru = re.findall(r'(jsonpCallback)', js_file_request)

    for x in callback_possibru:
      print " --- VULN --- \n"
      print "["+target+"] " + new_target + " " + x  
      
