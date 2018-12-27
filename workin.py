from bottle import *
from hashlib import sha256


def create_hash(password):              # This function is taken from hash_password.py
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()


@route("/static/<filename>")
def static_file_callback(filename):
    return static_file(filename, root="./static")


def htmlify(comment):
    page = """
        <!DOCTYPE html>
<html>
    
    <head>
        <meta charset="utf-8">
        <title>The Black Keys</title>
        <link rel="stylesheet" href="/static/style.css">
        </head>
            </head>
            <body>
            <div>
            <h1 id="header_keys">
                <img id="logo_left" src="./static/logo.png" alt="logo">THE BLACK KEYS<img id="logo_right" src="./static/logo.png" alt="logo">
            </h1>
        </div>
        
        <nav>   
        <ul class= "lists">
                 <li id="listen_on">Find The Black Keys On</li>
                <li>
                 <ul>
                     <li ><a href="https://open.spotify.com/artist/7mnBLXK823vNxN3UWB7Gfz?si=h4aGYtRDRLioG5d8YCPwBA"><img class="spotify" src="./static/Spotify_Logo.png" alt="spotify"></a></li>
                     <li ><a href="https://www.youtube.com/channel/UCJL3h2-wEOB6EigQOBZ3ryg"><img class="spotify" src="./static/Youtube.png" alt="youtube"></a></li>
                     <li><a href="https://www.instagram.com/theblackkeys/"><img class="spotify" src="./static/instagram.png" alt="instagram"></a></li>
                     <li><a href="https://twitter.com/theblackkeys"><img class="spotify" src="./static/twitter.png" alt="twitter"></a></li>
                     <li><a href="https://www.deezer.com/us/artist/2483?autoplay=true"><img class="spotify" src="./static/deezer.png" alt="deezer"> </a></li>
               </ul></li>
                
                 
            </ul>
        </nav>  
          
        <div class="para">
            <p>The Black Keys is a known American rock band which has been formed in 2001 at United States. The Band is consist of 2 amazing musicians, Dan Auerbach and Patrick Carney. These 2 was friends since childhood they attended the same high school and dropped out at University of Akron.Dan plays the guitar and sings at the same time. Patrick is the drummer of the band. These two started recording in basements and this situation kept going on until 2010's. With the Tighten Up song they appeared as a popular garage rock band during second wave of the genre's revival in the 2010's<br><br> Here are some pictures of Dan and Patrick</p>
        </div>
        
        <div class= "images">
            <img class="black_keys" src="./static/tbk_play.jpg" alt="Dan and Patrick playing">
            <img class="black_keys" src= "./static/the-black-keys-fever.jpg" alt="Dan and Patrick" >
            <img  class="black_keys" src="./static/concert.jpg" alt="Dan and Patrick at concert">
            <img class="black_keys" src="./static/black_n_white_1_manipulated.jpg" alt="A charismatic photo of Dan and Patrick">
            <img class="black_keys" src="./static/blackkeys_sit.jpg" alt="Dan and Patrick are sitting in front of a piano">
            <img class="black_keys" src="./static/fini_manipulated.jpg" alt="Another charismatic photo of Dan and Patrick" >
        </div>
        <div class="form">
            <form action="/" method="post">
                <div>
                    
                    <label for="radio">Which one did you like most?</label>
                    <br><br>
                    
                    <input type ="radio" name="user_choice" value="dan">Dan Auerbach<br>
                    <input type ="radio" name="user_choice" value="patrick">Patrick Carney<br>
                </div>
                
                <div>
                    <br><br><br>
                    <label for="name">Enter Your Comment:</label>
                    <input class="comment" type="text"  name="user_name">
                </div>
                <div>
                    <br>
                    <label for="mail">Enter Your Password:</label>
                    <input class="password" type="password" name="user_password">
                    <br><br>
                        
                    <input style="margin-left: 150px;" type="submit" name="user_submit" value="Submit My Comment">
                </div>
                <ol>
                    %s
                </ol>
            </form>
        </div>
            </body>
        </html>
    """ % (comment)
    return page


@route('/', method='get')
def index():
    return htmlify("")


hshoriginal = "da30e45705f79aa7555b538e098d0ab284fbc6c890f92ed8ad1722b63aa69201"       # This line is taken from hash_password.py
comments=[]
printed_comments=[]

@route('/', method='post')
def handle_form():
    user_comment = request.forms.get('user_name')
    password = request.forms.get('user_password')
    hsh1 = create_hash(password)                # This line is taken from hash_password.py

    if hsh1 == hshoriginal:
        comments.append(user_comment)
        for i in range(len(comments)):
            fixed_comments = "<li>"+ comments[i] + "</li>"
        printed_comments.append(fixed_comments)
        return htmlify(''.join(printed_comments))
    else:
        return htmlify("Wrong Password")






debug(True)
app = default_app()
if __name__ == "__main__":
    run()
