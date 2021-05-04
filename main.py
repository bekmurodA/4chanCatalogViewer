import requests,sys
url ="https://a.4cdn.org/g/catalog.json"
urlThread="https://a.4cdn.org/g/thread/" #number.json
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
    

def Print_thread(n):
    response = requests.get(urlThread+n+".json").json()
    #print(response['posts'])
    for keys in response['posts']:
            try:
                print(f"{keys['no']}\v{keys['com']}\n")
                print()
            except KeyError:
                pass

if __name__ == '__main__':
    threads=input("Threads in g(g) or particular thread(t): ")
    if (threads == 'g'):
        Print_threads()
    elif(threads == 't'):
        thread_number=input("enter the thread number (quit 0) ")
        if (int(thread_number) == 0):
            sys.exit()
        Print_thread(thread_number)
    

