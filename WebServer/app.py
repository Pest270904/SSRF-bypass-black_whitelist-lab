from flask import Flask, render_template, request
from flask_cors import CORS
import requests
import dns.resolver
from urllib.parse import urlparse
import re
from urllib.parse import unquote

app = Flask(__name__)
CORS(app)

def is_domain(hostname):
    DOMAIN_REGEX = r"^(?![0-9]+$)(?!-)[A-Za-z0-9-]{1,63}(?<!-)$"
    if hostname:
        parts = hostname.split('.')
        return all(re.match(DOMAIN_REGEX, part) for part in parts)
    return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/zekrom_easy', methods=['GET', 'POST'])
def lab_b_ez():
    if request.method == 'GET':
        return render_template('zekrom_easy.html')
    else:
        url = request.json.get('url', '')
        for a in ['localhost', '127.0.0.1']:
            if a in url:
                return f"{a} is not allowed";
        return requests.get(url).text

@app.route('/zekrom', methods=['GET', 'POST'])
def lab_b():
    if request.method == 'GET':
        return render_template('zekrom.html')
    else:
        url = unquote(request.json.get('url', ''))

        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        for a in ['localhost', '127.0.0.1']:
            if a in url:
                return f"{a} is not allowed";
    
        # if hostname is a domain
        if is_domain(hostname):
            resolved_ips = dns.resolver.resolve(hostname, 'A')
            resolved_ips = [str(ip) for ip in resolved_ips]
            if "127.0.0.1" in resolved_ips:
                return f"Host '{hostname}' redirect to localhost, not allowed.....";
        return requests.get(url).text

@app.route('/reshiram', methods=['GET', 'POST'])
def getAPI_white():
    if request.method == 'GET':
        return render_template('reshiram.html')
    else:
        url = unquote(request.json.get('url', ''))

        whitelist = ["a-m7z4.onrender.com"]

        for allowed_domain in whitelist:
            if allowed_domain in url:
                return requests.get(url).text
        
        return "You can only access to host a-m7z4.onrender.com"
    
@app.route('/zeshiram', methods=['GET', 'POST'])
def lab_bw():
    if request.method == 'GET':
        return render_template('zeshiram.html')
    else:
        url = unquote(request.json.get('url', ''))
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        # whitelist filter
        whitelist = ["a-m7z4.onrender.com"]
        whitelist_check = 0

        for allowed_domain in whitelist:
            if allowed_domain in url:
                whitelist_check = 1

        if whitelist_check == 0:
            return "You can only access to host a-m7z4.onrender.com"

        # blacklist filter
        for a in ['localhost', '127.0.0.1']:
            if a in url:
                return f"{a} is not allowed";

        # if hostname is a domain
        if is_domain(hostname):
            resolved_ips = dns.resolver.resolve(hostname, 'A')
            resolved_ips = [str(ip) for ip in resolved_ips]
            if "127.0.0.1" in resolved_ips:
                return f"Host '{hostname}' redirect to localhost, not allowed....."; 
        return requests.get(url).text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)