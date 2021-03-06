# run.py
from waitress import serve
from proj1 import wsgi

# touch app-initialized
open('/tmp/app-initialized', 'w').close()
# start waitress
serve(wsgi.application, unix_socket='/tmp/nginx1.socket')
