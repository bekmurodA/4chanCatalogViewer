import requests
url ="https://a.4cdn.org/g/catalog.json"
def Print_threads():
    response = requests.get(url)
    jresponse = response.json()
    print("Hello")
    for pages in jresponse:
        for threads in pages['threads']:
            try:
                print(f"{threads['no']}\t{threads['replies']}\v{threads['com']}\n")
                print()
            except KeyError:
                pass
    response.close()

if __name__ == '__main__':
    Print_threads()
    

