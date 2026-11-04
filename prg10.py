app= Flask(__name__)

@app.route('/n8n-webhook',methods=['POST'])
def n8n_webhook():
    data=request.get_json()
    print("Received from n8n:",data)
    return jsonify({"status":"received","data":data})

    if__name__=='__main__':
    app.run(debug=True,port=5000)