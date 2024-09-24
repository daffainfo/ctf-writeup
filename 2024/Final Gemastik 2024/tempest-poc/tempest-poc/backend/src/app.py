import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.gen
import threading
import requests
import json
import asyncio
import ipaddress
import socket
import random
import uuid
import os
from urllib.parse import urlparse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Dictionary to keep track of WebSocket clients
clients = {}

# Expanded templates for more diverse scan results
vulnerability_templates = [
    {'template': 'CVE-2021-26855', 'severity': 'critical', 'description': 'Exchange Server SSRF vulnerability detected.'},
    {'template': 'CVE-2021-34473', 'severity': 'high', 'description': 'ProxyShell vulnerability detected.'},
    {'template': 'CVE-2021-34527', 'severity': 'critical', 'description': 'PrintNightmare vulnerability detected.'},
    {'template': 'CVE-2020-1472', 'severity': 'critical', 'description': 'Zerologon vulnerability detected.'},
    {'template': 'CVE-2019-19781', 'severity': 'medium', 'description': 'Citrix ADC Remote Code Execution detected.'},
    {'template': 'CVE-2020-0601', 'severity': 'high', 'description': 'CryptoAPI Spoofing vulnerability detected.'},
    {'template': 'CVE-2021-21972', 'severity': 'high', 'description': 'VMware vSphere Client RCE detected.'},
    {'template': 'CVE-2017-11882', 'severity': 'medium', 'description': 'Microsoft Office Memory Corruption detected.'}
]

# Let's simulate a scan. We are not doing an actual scan on this PoC to prevent unnecessary problem in the network.
# For actual scanning it should be straight forward. We just need to run all the tools with subprocess, catch the results and send them to the client.
async def simulate_scan(target, ws_handler, scan_id):
    ports = random.sample([22, 80, 443, 8080, 3306, 5432], random.randint(2, 4))
    dummy_progress = [
        "Initializing scan engine...",
        "Checking for internet connectivity...",
        "Loading vulnerability templates...",
        f"Starting scan with scan_id {scan_id}...",
        f"Target acquired: {target}",
        f"Scanning target IP: {random.randint(100, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}",
        f"Running OS fingerprinting...",
        f"Port scan started on {target}...",
        f"Detected services on ports: {ports}",
        "Loading 15 vulnerability templates for scanning...",
        "[info] Running template: CVE-2021-26855 (Exchange Server SSRF)",
        "[info] Running template: CVE-2021-34473 (ProxyShell)",
        "[info] Running template: CVE-2021-34527 (PrintNightmare)",
        "[info] Running template: CVE-2020-1472 (Zerologon)",
        "[info] Running template: CVE-2019-19781 (Citrix ADC Remote Code Execution)",
        "[info] Running template: CVE-2020-0601 (CryptoAPI Spoofing)",
        "[info] Running template: CVE-2021-21972 (VMware vSphere RCE)",
        "[info] Running template: CVE-2017-11882 (Office Memory Corruption)",
        "Analyzing detected vulnerabilities...",
        "Compiling result..."
    ]
    
    for progress in dummy_progress:
        await asyncio.sleep(0.5)
        try:
            ws_handler.write_message(json.dumps({"event": "scan_progress", 'data': progress}))
        except Exception:
            print("WebSocket connection closed, cannot send progress.", flush=True)
    
    # Emit the final scan results
    try:
        ws_handler.write_message(json.dumps({"event": "scan_result", 'data': f"Result saved to report/{scan_id}.json. Please contact admin for detailed report"}))
    except Exception:
        print("WebSocket connection closed, cannot send final result.", flush=True)

    # Final results
    dummy_results = random.sample(vulnerability_templates, random.randint(2, 5))

    with open(f"report/{scan_id}.json", "w") as f:
        json.dump(
            {
                "open_ports": [str(i) for i in ports],
                "vulnerabilities": dummy_results,
                "scan_status": "completed",
                "scan_duration": f"{random.randint(1,10)} minutes"
            }, f)

def start_scan_wrapper(target, ws_handler, scan_id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(simulate_scan(target, ws_handler, scan_id))
    loop.close()

def get_local_ips():
        """Get a list of all local IP addresses of the server."""
        local_ips = []
        hostname = socket.gethostname()
        for ip in socket.gethostbyname_ex(hostname)[2]:
            local_ips.append(ipaddress.ip_address(ip))
        return local_ips

def is_local_ip(ip, local_ips):
    """Check if the IP address is one of the local IP addresses of the server."""
    try:
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj in local_ips or ip_obj.is_loopback
    except ValueError:
        return False
        
def validate_url(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme != "http" and parsed_url.scheme != "https":
        return False
    
    local_ips = get_local_ips()
    netloc = parsed_url.netloc.split(":")[0]

    # domain check
    if not netloc.replace(".", "").isdigit():
        # resolve the domain to ip
        try:
            ip = socket.gethostbyname(netloc)
        except socket.gaierror:
            return False
        
        if is_local_ip(ip, local_ips):
            return False
    else:
        # check if the ip is local
        if is_local_ip(netloc, local_ips):
            return False
    return True

# WebSocket handler
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
    
    def open(self):
        self.cid = self.get_argument("client_id")
        print("WebSocket opened", flush=True)
        clients[self.cid] = self

    def on_message(self, message):
        print(f"Received message: {message}")

    def on_close(self):
        print("WebSocket closed", flush=True)
        if self.cid in clients:
            del clients[self.cid]

# Start scan endpoint
class StartScanHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        target = data.get('target')
        if not validate_url(target):
            self.set_status(400)
            self.write(json.dumps({'error': 'Invalid Target'}))
            return
        cid = data.get('client_id')
        scan_id = str(uuid.uuid4())

        if not target:
            self.set_status(400)
            self.finish(json.dumps({'error': 'No target provided'}))
        elif cid not in clients:
            self.set_status(400)
            self.finish(json.dumps({'error': 'Invalid client ID'}))
        else:
            # Simulate the scan in a background thread
            threading.Thread(target=start_scan_wrapper, args=(target, clients[cid], scan_id)).start()
            self.write(json.dumps({'status': 'scanning started', 'scan_id': scan_id}))

# Test website handler (GET/POST)
class TestWebsiteHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        url = data.get('url')
        if not url:
            self.set_status(400)
            self.write(json.dumps({'error': 'No URL provided'}))
            return

        self.check_url_alive(url)
    
    def check_url_alive(self, url):
        try:
            if not validate_url(url):
                self.set_status(400)
                self.write(json.dumps({'error': 'Invalid Target'}))
                return
            
            # cleanup url
            parsed_url = urlparse(url)
            cleaned_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

            # Check if the URL is alive
            response = requests.get(cleaned_url, allow_redirects=False, verify=False, timeout=10)
            self.set_status(response.status_code)
            self.finish()
        except requests.RequestException:
            self.set_status(500)
            self.finish()

# Generate Report Endpoint (reads from the saved JSON report file)
class GenerateReportHandler(tornado.web.RequestHandler):
    def get(self):
        scan_id = self.get_argument("scan_id", None)
        report_name = self.get_argument("report_name", "")
        
        if not scan_id:
            self.set_status(400)
            self.write(json.dumps({"error": "Missing scan_id"}))
            return
        
        # File path for the report
        report_file = f"report/{scan_id}.json"
        
        # Check if the report file exists
        if not os.path.exists(report_file):
            self.set_status(404)
            self.write(json.dumps({"error": f"Report for scan_id {scan_id} not found"}))
            return
        
        # Load the report data from the JSON file
        with open(report_file, "r") as f:
            scan_data = json.load(f)
        
        # Read the HTML template from the file
        with open("report_template.html", "r") as template:
            report_template = template.read()

        report_template = report_template.replace("<REPORT_NAME>", report_name)

        # Dynamically render the report with scan data
        self.write(tornado.template.Template(report_template).generate(
            scan_id=scan_id,
            scan_data=scan_data
        ))

def make_app():
    return tornado.web.Application([
        (r"/api/public/ws/", WebSocketHandler),
        (r"/api/public/startscan", StartScanHandler),
        (r"/api/public/test", TestWebsiteHandler),
        (r"/api/private/report", GenerateReportHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.instance().start()