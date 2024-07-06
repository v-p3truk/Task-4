import re

import requests

def task():
    response = requests.get('https://www.lejobadequat.com/emplois')
    content = response.text
    job = re.findall(r'>([^<]+ H/F)<', content)
    print(job)

    with open('job.txt', 'w', encoding='utf-8') as f:
        f.write('[\n')
        for title in job:
            f.write(f'  "{title}",\n')
        f.write(']')

if __name__ == "__main__":
    task()