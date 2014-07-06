import oauth2 as oauth
import urllib2 as urllib

'''
The steps below will help you set up your twitter account to be able to access the live 1% stream.

1) Create a twitter account if you do not already have one.
2) Go to https://dev.twitter.com/apps and log in with your twitter credentials.
3) Click "Create New App"
4) Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.
5) On the next page, click the "API Keys" tab along the top, then scroll all the way down until you see the section "Your Access Token"
6) Click the button "Create My Access Token". You can Read more about Oauth authorization.
7) You will now copy four values into twitterstream.py. 
    These values are your "API Key", your "API secret", your "Access token" and your "Access token secret". 
    All four should now be visible on the API Keys page.
8) Run the following and make sure you see data flowing and that no errors occur. 
    $ python twitterstream.py > output.txt
9) Stop the program with Ctrl-C, but wait at least 5 minutes for data to accumulate. 
'''


# See assignment1.html instructions or README for how to get these credentials
api_key = "api_key"
api_secret = "api_secret"
access_token_key = "access_token_key"
access_token_secret = "access_token_secret"

_debug = 0

oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
    url = req.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response

def fetchsamples():
    url = "https://stream.twitter.com/1/statuses/sample.json"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    for line in response:
        print line.strip()

if __name__ == '__main__':
    fetchsamples()
