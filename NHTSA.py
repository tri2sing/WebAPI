from urllib2 import urlopen
from json import load

apiUrl = 'http://www.nhtsa.gov/webapi/api/SafetyRatings'
apiParam = ''
outputFormat = '?format=json'

response = urlopen(apiUrl + apiParam + outputFormat)
json_obj = load(response)
#print json_obj

print json_obj.keys()
print ''

for objColl in json_obj['Results']:
    print objColl
    # Loop each vehicle in the vehicles collection
    #for safetyRatingAttribute, safetyRatingValue in objColl.iteritems():
    #    print safetyRatingAttribute, ": ", safetyRatingValue
