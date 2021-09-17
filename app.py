from flask import Flask, jsonify, request
import scraper
import time

#init app
app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    amazonRes = scraper.searchAmazon(query)
    walmartRes = scraper.searchWalmart(query)
    results = {
        'timestamp': time.time(),
        'searchedString': query.replace("+"," "),
        'results': amazonRes + walmartRes,
    }
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)