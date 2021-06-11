from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route('/postjson', methods=['POST'])
def postJsonHandler():
    print(request.is_json)
    content = request.get_json()
    dataframe = pd.DataFrame.from_dict(content)
    print(dataframe.head(5))
    return 'JSON Berhasil Di Post'

app.run(host='0.0.0.0', port=5000)