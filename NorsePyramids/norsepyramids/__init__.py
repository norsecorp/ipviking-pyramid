from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    sess_factory = UnencryptedCookieSessionFactoryConfig("thisisareallysecretkey")
    config = Configurator(settings=settings, session_factory = sess_factory)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('next', '/next/')
    config.scan()
    return config.make_wsgi_app()