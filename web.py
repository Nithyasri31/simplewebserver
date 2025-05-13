from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Layers and Protocols</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #white ;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            width: 80%;
            max-width: 1000px;
            padding: 20px;
            background-color: #2e2e2e;
            border-radius: 12px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #b8ff33;
            margin-bottom: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ffffff;
            padding: 12px 20px;
            font-size: 18px;
            text-align: center;
        }
        th {
            background-color: #b8ff33;
            color: #000000;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>TCP/IP Layers and Protocols</h2>
        <table>
            <tr>
                <th>TCP/IP Layers</th>
                <th>Protocols (Examples)</th>
            </tr>
            <tr>
                <td>Application Layer</td>
                <td>HTTP, RDP, DNS, SMTP, Telnet, SNMP</td>
            </tr>
            <tr>
                <td>Transport Layer</td>
                <td>TCP, UDP</td>
            </tr>
            <tr>
                <td>Internet Layer</td>
                <td>ICMP, IGMP, ARP, IP, IPSec</td>
            </tr>
            <tr>
                <td>Network Access Layer</td>
                <td>Ethernet (IEEE 802.3), Token Ring, PPP, Frame Relay</td>
            </tr>
        </table>
    </div>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request received...")
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

print("My webserver is running")
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()
