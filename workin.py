from bottle import route,static_file,run

def server_static(fname):
   txt = static_file(fname, root='/webpage/index.html')
   return txt

route('/static/webpage/index.html','GET',server_static)
run(debug=True)