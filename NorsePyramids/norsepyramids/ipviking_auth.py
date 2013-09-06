"""This will be our IPViking authorizer"""
from ipviking_api_python.helpers.constants import SANDBOX_APIKEY, PROXIES
from ipviking_api_python.auth.objects import IPV_Rule, IPV_Response, ipvAuthorizer


#Here, we're setting up our authentication rules and the authorizer object
rf75 = IPV_Rule(['risk_factor'], lambda rf: rf > 75, "suspicious traffic", 2)
us = IPV_Rule(['geoloc','country'], lambda country: country != 'US', 'us not takin too kindly to Americans', 2)

block = IPV_Response("You been done blocked on account of %s", "{%state%}", {})

rules = [rf75, us]
responses = {2:block}

IPV = ipvAuthorizer()
IPV.configure(rules = rules, 
              responses = responses, 
              apikey = SANDBOX_APIKEY, 
              proxy = PROXIES['SANDBOX'])

def validate(request):
    """Method to validate a request and return blocked if they fail"""
    if not request.session.get('ipviking'):
        #we need to validate them
        ip = request.remote_addr
        if ip == '127.0.0.1':
            ip = '208.74.76.5' #the API doesn't like localhost, so we'll use the sandbox suggestion
        valid, request, level, context = IPV.validate_request(request, ip)
        if valid:
            return True, level, ''
        else:
            return False, 0, context['state']
    else:
        return True, None, ''
        
