from bs4 import BeautifulSoup
import requests
import json

def main():
    r = requests.get('https://www.netlingo.com/acronyms.php')
    soup = BeautifulSoup(r.content, 'html.parser')
    body = soup.find("div", {"class": "list_box3"})
    body_li = body.ul.find_all('li')
    
    abbreviations = []
    for i in body_li:
        key = i.find('a').string
        value = i.find('div').string
        if 4 <= len(key) <= 6 and key.isalpha():
            abbreviations.append({'name': key, 'meaning': value})

    #print(abbreviations)
    print(f"number of abbreviations collected: {len(abbreviations)}")
    json_result = json.dumps(abbreviations, indent=4)
    with open('filtered-internet-abbreviations.json', 'w') as f:
        f.write(json_result)

if __name__ == "__main__":
    main()

