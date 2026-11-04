from flask import Flask,request,jsonify
import openai 
app=Flask(__name__)
openai.api_key='your-openai-api-key'
@approute('/chat',method=['POST'])
def chat():
    data=request.get_json()
    user_message=data.get('message','')
    if not user_message:
        return jsonify({"error":"Message is requried"}),400
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"user","content":user_message}
            ]
        )
        ai_reply = response['choices'][0]['message']['content']
        return jsonify({
            "user_message":user_message,
            "ai_response":ai_reply
        })
        if__name__=='__main__':
        app.run(debug=True)