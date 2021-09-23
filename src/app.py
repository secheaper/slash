from flask import Flask, jsonify, request
import scraper
import time

#init app
app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    amazonProd = scraper.searchAmazon(query)
    walmartProd = scraper.searchWalmart(query)
    results = {
        'timestamp': round(time.time()*1000),
        'searchedString': query.replace("+"," "),
        'results': amazonProd + walmartProd,
    }
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)