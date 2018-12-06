from tornado import gen, httpclient
from tornado.httputil import HTTPHeaders
from jaqpotpy.mappers import decode


feat_path = "feature"


@gen.coroutine
def create_feature_async(baseurl, api_key, json_feat):
    uri = baseurl + feat_path
    jclient = httpclient.AsyncHTTPClient()
    h = HTTPHeaders({'Content-Type': 'application/json'})
    h.add('Accept', 'application/json')
    h.add('Authorization', "Bearer " + api_key)
    try:
        response = yield jclient.fetch(uri,
                                       method='POST',
                                       headers=h,
                                       body=json_feat,
                                       validate_cert=False)
        resp = decode.decode_feature(response.body)
        raise gen.Return(resp)
    except httpclient.HTTPError as e:
        print("Error 1: " + str(e))
    finally:
        jclient.close()


async def create_feature_async_(baseurl, api_key, json_feat):
    uri = baseurl + feat_path
    jclient = httpclient.AsyncHTTPClient()
    h = HTTPHeaders({'Content-Type': 'application/json'})
    h.add('Accept', 'application/json')
    h.add('Authorization', "Bearer " + api_key)
    try:
        response = await jclient.fetch(uri, method='POST', headers=h, body=json_feat, validate_cert=False)
        # au_req = decode.decode_feature(response.body)
        # print(response.body)
        # print(gen.Return(decode.decode_feature(response.body)))
    except httpclient.HTTPError as e:
        print("Error: " + str(e))
    except Exception as e:
        print("Error: " + str(e))
    else:
        print(decode.decode_feature(response.body))
    jclient.close()


def create_feature_sync(baseurl, api_key, json_feat):
    uri = baseurl + feat_path
    jclient = httpclient.HTTPClient()
    h = HTTPHeaders({'Content-Type': 'application/json'})
    h.add('Accept', 'application/json')
    h.add('Authorization', "Bearer " + api_key)
    try:
        response = jclient.fetch(uri, method='POST', headers=h, body=json_feat, validate_cert=False)
        au_req = decode.decode_feature(response.body)
        return au_req
    except httpclient.HTTPError as e:
        print("Error: " + str(e))
    except Exception as e:
        print("Error: " + str(e))
    jclient.close()