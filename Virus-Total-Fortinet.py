'''
Title: Virus-Total Hash Scanner
Author: Naeem Patel
Date: 2021-04-25
Software Link: https://github.com/mayfled/Virus-total-scanner
---------------------
I have specified my api key for demonstration purposes.
To ensure this script work accordingly please make sure that you enter 1 hash per line with no commas separating them

Example: sample_hash_input.txt

0496f4962d3dce3caa849f605749f7f2
82a02a0864447d51bb8c18ab4554a77e
e85463d19104cacd79a25cacb0b57c1d
'''


import requests
from tqdm import tqdm
import time
import argparse
from datetime import datetime
import json
from prettytable import PrettyTable

key = '01332cba9c5f32631d9c035bc4eee3cfc61c9c865fffc21aa4589a938289d9d8'
url = 'https://www.virustotal.com/vtapi/v2/file/report'
now = datetime.now()
p = PrettyTable()
p.field_names = ["MD5 hash","Detection Name","Total Detected","Scan Date"]


def main():
    parser = argparse.ArgumentParser(description="Verify if hash is malicious on Fortinet's Platform using Virus Total\nThe results will be stored in the results.txt file in the current directory\nThe results will be displayed once all hashes are scanned")
    parser.add_argument("-f", "--file", help="The text file you want to scan", required=True)
    parser.set_defaults(function=hash_file)
    args = parser.parse_args()
    args.function(args)
def hash_file(args):
    filename = args.file
    with open(filename,'r') as f:
        line = f.read().splitlines()
    results(line)
def results(line):
    numbers = line
    print("Please wait as the hashes are being verified")
    for i in tqdm(numbers):
        params = {'apikey': key, 'resource': i}
        response_url = requests.get(url, params=params)
        response_json = response_url.json()
        response_code = int(response_json.get('response_code'))
        if response_code == 0:
            file = open("results.txt", 'w+')
            p.add_row(["No information for this hash " + i,"N/A","N/A",now.strftime("%Y-%m-%d %H:%M:%S")])
            file.write(str(p))
            file.close()
        elif response_code == 1:
            response_json = json.loads(response_url.content)
            hash = i
            positive = response_json['positives']
            results = response_json['scans']['Fortinet']['result']
            file = open("results.txt", 'w+')
            p.add_row([hash,results,positive,now.strftime("%Y-%m-%d %H:%M:%S")])
            file.write(str(p))
            file.close()
        else:
            file = open("results.txt", 'w+')
            p.add_row(["No results found for this hash " + i, "N/A", "N/A", now.strftime("%Y-%m-%d %H:%M:%S")])
            file.write("There were no results found for the following hash in the database: {}\n".format(i))
            file.close()
        time.sleep(30)
    print("\n",p)
main()
