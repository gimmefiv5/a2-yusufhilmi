from bottle import *


@route("/")
def index():
    return template("index")


@route("/static/<filename>")
def static_file_callback(filename):
    return static_file(filename, root="./static")

#####################################################################
# Don't alter the below code.
# It allows this website to be hosted on Heroku
# OR run on your computer.
#####################################################################
# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
    run()
