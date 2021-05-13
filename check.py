from pathlib import Path
import datetime
import json
import requests
import sys

argument = sys.argv[1]

if len(sys.argv) > 2:
    threshold = sys.argv[2]

if argument == '-h' or argument == '--help':
    print('python </path/to/>checkStaging.py <comma separated branches> <optional threshold (negative selects within, positive without>')
    quit()

branches = argument.split(',')

with open(Path(__file__).parent / 'config.json', 'r') as config:
    data = config.read()

configObj = json.loads(data)

reqHeaders = { 'PRIVATE-TOKEN': configObj['privateToken'] }
reqEndpoint = configObj['url'] + '/api/v' + configObj['apiVersion']

print()

for project in configObj['projects']:
    print('\033[1m' + project['label'] + '\033[0m')
    print()
    for branch in branches:
        reqUrl = reqEndpoint + '/projects/' + project['id'] + '/repository/commits?ref_name=' + branch
        reqResponse = requests.get(reqUrl, headers=reqHeaders)
        mostRecent = reqResponse.json()[0]
        if 'threshold' in vars():
            timedelta = datetime.timedelta(days=abs(int(threshold)))
            now = datetime.datetime.now(datetime.timezone.utc)
            cutoffdate = now - timedelta
            commitdate = datetime.datetime.fromisoformat(mostRecent['created_at'])
            if int(threshold) < 0 and commitdate < cutoffdate:
                continue
            if int(threshold) > 0 and commitdate > cutoffdate:
                continue
        print('branch: ' + branch)
        print('title: ' + mostRecent['title'])
        print('author: ' + mostRecent['author_name'])
        print('when: ' + mostRecent['created_at'])
        print()
    print()

