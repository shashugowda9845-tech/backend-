from flask Import Flask,request,jsonify
import re
app=Flask(__name__)
def is_valid_email(email):
    pattern= r'^[a-zA-Z0-9._%+]+@[a-zA-Z0-9,-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email)is not None
    @app.route('/register',methods=['POST'])
    def register():
        data=request.get_json()
        name=data.get('name','')
        email=data.get('email','')
if not name or not email: