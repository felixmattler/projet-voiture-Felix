from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.server.wsgi import WsgiApplication
from spyne.model.primitive import Integer
from wsgiref.simple_server import make_server
from spyne.protocol.soap import Soap11
from spyne.model.complex import Iterable
from spyne.model.primitive import String
from spyne.model.primitive import Float

class GetTimeService(ServiceBase):
	
	@srpc(Integer, Integer, _returns=Float)
	def get_time(distance, loading_time):
		time=distance/130 + loading_time
		return time

application = Application([GetTimeService], 'spyne.get_time.soap', 
                          in_protocol=Soap11(validator='lxml'), 
                          out_protocol=Soap11()) 
wsgi_application = WsgiApplication(application)


server = make_server('127.0.0.1', 8000, wsgi_application) 
server.serve_forever()

