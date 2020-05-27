import dpkt
import socket

def findDownload(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            tcp = ip.data
            print('#',tcp.data)
            http = dpkt.http.Request(tcp.data)
            print('SS',http.data)
            
            if http.method == 'GET':
                print("**",http)
                uri = http.uri.lower()
                if '.zip' in uri and 'loic' in uri:
                    print('[!] ' + src + ' Downloaded LOIC.')
        except dpkt.UnpackError:
            #pass



f=open('loic.pcap','rb')
pcap = dpkt.pcap.Reader(f)
findDownload(pcap)