from pyramid.view import view_config
from .ipviking_auth import validate
from pyramid.httpexceptions import HTTPForbidden

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'NorsePyramids'}

@view_config(route_name='next', renderer='templates/nextpage.pt')
def next_page(request):
    valid, level, message = validate(request)
    if not valid:
        return HTTPForbidden(explanation = message)
    else:
        request.session['ipviking'] = level
        return {'project':'NorsePyramids'}