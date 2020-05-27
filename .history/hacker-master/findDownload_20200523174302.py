import dpkt
import socket

def findDownload(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            tcp = ip.data
            print('#',tcp)
            http = dpkt.http.Request(tcp.data)
            @staticmethod
            def funcname(parameter_list):
                pass
            if http.method == 'GET':
                print("**",http)
                uri = http.uri.lower()
                if '.zip' in uri and 'loic' in uri:
                    print('[!] ' + src + ' Downloaded LOIC.')
        except:
            pass

f = open('loic.pcap','rb')
pcap = dpkt.pcap.Reader(f)
findDownload(pcap)