import requests, json

api_key = "75sctd7yss5o0r"
secret_key = "Lb2o8KLx3WG9NIDR"

linkedin_url = ""
'''
https://www.linkedin.com/uas/oauth2/authorization?response_type=code
                                           &client_id=YOUR_API_KEY
                                           &scope=SCOPE
                                           &state=STATE
                                           &redirect_uri=YOUR_REDIRECT_URI
                                           
'''
                                           
# GET https://api.linkedin.com/v1/people/~
# GET /v1/people/~?oauth2_access_token=AQUfrQ959I6Pagkz6pLo6nuJ4TENgWV1A_nN5vjxYsIAA3pRx6_tI9Uitq0rlXQ7jvVzRlwJkQLe-5g9UG2V9f82LcC2NYaEcsJtnEmm53QGsO3u2WoudSbZt2887oKeWBSXOFj4A_CwEwQRgtFwL51hAIlMOqw-scnFmrmj08Ie-GQnUXw HTTP/1.1
 
# GET /v1/people-search?oauth2_access_token=AQUfrQ959I6Pagkz6pLo6nuJ4TENgWV1A_nN5vjxYsIAA3pRx6_tI9Uitq0rlXQ7jvVzRlwJkQLe-5g9UG2V9f82LcC2NYaEcsJtnEmm53QGsO3u2WoudSbZt2887oKeWBSXOFj4A_CwEwQRgtFwL51hAIlMOqw-scnFmrmj08Ie-GQnUXw&keywords=Kumar&sort=connections HTTP/1.1
                                           
# GET /v1/people-search?oauth2_access_token=AQUfrQ959I6Pagkz6pLo6nuJ4TENgWV1A_nN5vjxYsIAA3pRx6_tI9Uitq0rlXQ7jvVzRlwJkQLe-5g9UG2V9f82LcC2NYaEcsJtnEmm53QGsO3u2WoudSbZt2887oKeWBSXOFj4A_CwEwQRgtFwL51hAIlMOqw-scnFmrmj08Ie-GQnUXw&last-name=kumar&first-name=naveen HTTP/1.1

'''
<person>
      <id>wqsURMEfCO</id>
      <first-name>Naveen</first-name>
      <last-name>Kumar</last-name>
</person>
'''

# GET /v1/people/id=wqsURMEfCO?oauth2_access_token=AQUfrQ959I6Pagkz6pLo6nuJ4TENgWV1A_nN5vjxYsIAA3pRx6_tI9Uitq0rlXQ7jvVzRlwJkQLe-5g9UG2V9f82LcC2NYaEcsJtnEmm53QGsO3u2WoudSbZt2887oKeWBSXOFj4A_CwEwQRgtFwL51hAIlMOqw-scnFmrmj08Ie-GQnUXw HTTP/1.1

'''
<person>
  <first-name>Naveen</first-name>
  <last-name>Kumar</last-name>
  <headline>Engineer at Intel Corporation</headline>
  <site-standard-profile-request>
    <url>https://www.linkedin.com/profile/view?id=23553213&authType=name&authToken=VXnR&trk=api*a3227641*s3301901*</url>
  </site-standard-profile-request>
</person>

'''

# https://api.linkedin.com/v1/people/~:(id,first-name,last-name,industry,positions)
# GET /v1/people/~:(id,first-name,last-name,industry,positions)?oauth2_access_token=AQUfrQ959I6Pagkz6pLo6nuJ4TENgWV1A_nN5vjxYsIAA3pRx6_tI9Uitq0rlXQ7jvVzRlwJkQLe-5g9UG2V9f82LcC2NYaEcsJtnEmm53QGsO3u2WoudSbZt2887oKeWBSXOFj4A_CwEwQRgtFwL51hAIlMOqw-scnFmrmj08Ie-GQnUXw HTTP/1.1

# https://api.linkedin.com/v1/people/YglqAUOOqT:(id,first-name,last-name,positions,skills)

# https://api.linkedin.com/v1/people-search:(people:(id,first-name,last-name,skills,headline,positions))?first-name=matt&last-name=white
# GET /v1/people-search:(people:(id,first-name,last-name,skills,headline,positions))?oauth2_access_token=AQUfrQ959I6Pagkz6pLo6nuJ4TENgWV1A_nN5vjxYsIAA3pRx6_tI9Uitq0rlXQ7jvVzRlwJkQLe-5g9UG2V9f82LcC2NYaEcsJtnEmm53QGsO3u2WoudSbZt2887oKeWBSXOFj4A_CwEwQRgtFwL51hAIlMOqw-scnFmrmj08Ie-GQnUXw&first-name=matt&last-name=white HTTP/1.1

# https://api.linkedin.com/v1/people-search:(people:(id,first-name,last-name,headline,positions),num-results)?first-name=naveen&last-name=kumar
# GET /v1/people-search:(people:(id,first-name,last-name,headline,positions),num-results)?oauth2_access_token=AQUfrQ959I6Pagkz6pLo6nuJ4TENgWV1A_nN5vjxYsIAA3pRx6_tI9Uitq0rlXQ7jvVzRlwJkQLe-5g9UG2V9f82LcC2NYaEcsJtnEmm53QGsO3u2WoudSbZt2887oKeWBSXOFj4A_CwEwQRgtFwL51hAIlMOqw-scnFmrmj08Ie-GQnUXw&first-name=naveen&last-name=kumar HTTP/1.1


