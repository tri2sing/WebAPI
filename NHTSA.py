from urllib2 import urlopen
from json import load

apiUrl = 'http://www.nhtsa.gov/webapi/api/SafetyRatings'
# Different levels of params to explore the data

# apiParam = ''
# apiParam = '/modelyear/2005'
# apiParam = '/modelyear/2005/make/acura'
# apiParam = '/modelyear/2005/make/acura/model/rsx'

# Finally we get safety ratings for a specific id
apiParam = '/vehicleid/1491'

outputFormat = '?format=json'
print apiUrl + apiParam + outputFormat

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
