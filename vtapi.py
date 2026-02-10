import time
import requests

def main():
    print("=== SOC VT TOOL ===")
    choice = int(input(f"file (1) or IP (2) or Hash(3) or Domain (4)?: "))
    API_KEY = input("YOUR VT API KEY")
    url = f"https://www.virustotal.com/api/v3/"
    headers: dict[str, str] = {"accept": "application/json",
               "x-apikey": API_KEY}

    if choice==1:
        check_file(headers)
    elif choice==2:
        check_ip(headers)
    elif choice==3:
        check_hash(headers)
    elif choice==4:
        check_domain(headers)
def check_ip(headers,url):
    ip=input("what's the ip you wanna check? ")
    url +=ip_addresses/{ip}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        stats = result['data']['attributes']['last_analysis_stats']
        print(f"--- SCAN REPORT ---")
        print(f"Type:      {result['data']['type']}")
        print(f"Verdict:   {stats['malicious']} engines flagged this as malicious.")

        if stats['malicious'] > 0:
            print("Status:    [!] DANGER DETECTED")
        else:
            print("Status:    [+] CLEAN")
    else:
        print("Something went wrong")
def check_file(headers,url):
    userfile = input("what file do you wanna check?").strip('"')
    url += f"files"

    with open(userfile, "rb") as f:
        files = {"file": (userfile, f)}
        response = requests.post(url, headers=headers, files=files)
    result = response.json()
    analysis_id = result['data']['id']
    print(f"your analysis_ ID: {analysis_id}I'll deliver the results as soon as possible(2min+<)")
    time.sleep(120)

    while True:
        results_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
        response = requests.get(results_url, headers=headers)
        data = response.json()
        if data['data']['attributes']['status']=="completed":
            if data['data']['attributes']['stats']['malicious']>0:
                print(f"{data['data']['attributes']['stats']['malicious']} number of engines thinks its malicious")
            else:
                print("this file is fine")
            break
        else:
            time.sleep(15)
            continue


def check_hash(headers,url):
    userhash=input("Input the hash you want to check?")

    url += f"files/id/{userhash}"
    response = requests.get(url,headers=headers)
    result = response.json()

    print(f"${result['data']['attributes']['last_analysis_stats']['malicious']} engines flagged this as malicious.")

def check_domain(headers,url):
    domain=input("what is the domain you wanna check? ").rstrip('/').replace("https://","")
    print(domain)
    url += f"domains/{domain}"
    response = requests.get(url, headers=headers)
    result = response.json()
    if response.status_code == 200:
        print(f"{result['data']['attributes']['last_analysis_stats']['malicious']} engines flagged this as malicious.")
    else:
        print("Something went wrong")


if __name__=="__main__":
    main()
