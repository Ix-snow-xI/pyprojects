import time
import requests

def main():
    print("=== SOC VT TOOL v1.0 ===")
    choice = int(input(f"file (1) or IP (2): "))
    API_KEY = input("YOUR VT API KEY")
    if choice==1:
        check_file(API_KEY)
    else:
        check_ip(API_KEY)

def check_ip(api):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/"
    ip=input("what's the ip you wanna check? ")
    url+=ip
    headers = {"accept": "application/json",
                "x-apikey": api}
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
def check_file(api):
    url = f"https://www.virustotal.com/api/v3/files"
    userfile = input("what file do you wanna check?").strip('"')
    headers = {"accept": "application/json",
               "x-apikey": api}
    with open(userfile, "rb") as f:
        files = {"file": (userfile, f)}
        response = requests.post(url, headers=headers, files=files)
    result = response.json()
    analysis_id = result['data']['id']
    print("your analysis_ ID: ", analysis_id,"I'll deliver the results as soon as possible(2min+<)")
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

if __name__=="__main__":
    main()












