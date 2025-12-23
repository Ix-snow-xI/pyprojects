import json

def check_security(services):
    ports_services = {
        20: "FTP Data Transfer",
        21: "FTP Control",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        67: "DHCP Server",
        68: "DHCP Client",
        69: "TFTP",
        80: "HTTP",
        110: "POP3",
        123: "NTP",
        135: "RPC",
        137: "NetBIOS Name Service",
        138: "NetBIOS Datagram Service",
        139: "NetBIOS Session Service",
        143: "IMAP",
        161: "SNMP",
        389: "LDAP",
        443: "HTTPS",
        445: "SMB",
        514: "Syslog",
        587: "SMTP Submission",
        631: "IPP",
        993: "IMAP over SSL",
        995: "POP3 over SSL",
        1433: "MSSQL",
        1521: "Oracle DB",
        2049: "NFS",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        5900: "VNC",
        6379: "Redis",
        8080: "HTTP Proxy / Alternative HTTP",
        9200: "Elasticsearch",
        27017: "MongoDB"
    }
    found_threats = {22, 3389}
    threats=[]
    for el in found_threats.intersection(services):
        threats.append(f"[ALERT] Port {el} detected! Service: {ports_services.get(el)}")
    if len(threats)==0:
        threats=['NO dangerous open service detected']
    return threats

try:
    user_input = input("какой файл прочитать?: ")
    with open(user_input, "r") as f:
        data = (json.load(f))
    for server, ports in data.items():
        output = check_security(ports)
        print(output)
except FileNotFoundError:
    # What to do if the wrong file name
    print("Error: no such file.")
    exit()
except json.JSONDecodeError:
    # if its filled with thrash and not json type info
    print("Error: file corrupted or not .JSON format.")
    exit()

def main():
    try:
        user_input = input("which file to read?: ")
        with open(user_input, "r") as f:
            data = (json.load(f))
        for server, ports in data.items():
            output = check_security(ports)
            print(output)
    except FileNotFoundError:
        # What to do if the wrong file name
        print("Error: no such file.")
        exit()  
    except json.JSONDecodeError:
        # if its filled with thrash and not json type info
        print("Error: file corrupted or not .JSON format.")
        exit()
if __name__=="__main__":

    main()
