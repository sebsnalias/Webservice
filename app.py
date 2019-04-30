#Author : Salvador Hernandez Mendoza
#Email  : salvadorhm@gmail.com
#Twitter: @salvadorhm
import web
import application

ssl = False #activate ssl certificate 

if ssl == True:
    from web.wsgiserver import CherryPyWSGIServer
    '''
    Use OpenSSL to generate  keys

    user@host$ openssl genrsa -out server.key 1024
    user@host$ openssl req -new -key server.key -out server.csr
    user@host$ openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

    '''
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt" 
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

urls = (
    '/', 'application.controllers.main.index.Index',
    '/clientes', 'application.controllers.clientes.index.Index',
    '/clientes/view/(.+)', 'application.controllers.clientes.view.View',
    '/clientes/edit/(.+)', 'application.controllers.clientes.edit.Edit',
    '/clientes/delete/(.+)', 'application.controllers.clientes.delete.Delete',
    '/clientes/insert', 'application.controllers.clientes.insert.Insert',
    '/api_clientes/?', 'application.api.clientes.api_clientes.Api_clientes',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()
