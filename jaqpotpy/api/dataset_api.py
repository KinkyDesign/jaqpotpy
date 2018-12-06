from tornado import gen, httpclient
from tornado.httputil import HTTPHeaders
from jaqpotpy.mappers import decode

dataset_path = "dataset"


def create_dataset_sync(baseurl, api_key, json_dataset):
    uri = baseurl + dataset_path
    jclient = httpclient.HTTPClient()
    h = HTTPHeaders({'Content-Type': 'application/json'})
    h.add('Accept', 'application/json')
    h.add('Authorization', "Bearer " + api_key)
    try:
        response = jclient.fetch(uri, method='POST', headers=h, body=json_dataset, validate_cert=False)
        au_req = decode.decode_dataset(response.body)
        return au_req
    except httpclient.HTTPError as e:
        print("Error http: " + str(e))
    except Exception as e:
        print("Error generic: " + str(e))
    jclient.close()