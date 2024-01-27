import webbrowser

def validator(func):
    def wrapper(url):
        print("Validating...")
        if url.startswith("https://") or url.startswith("http://"):
            func(url)
        else:
            print('Invalid URL')
        print('Done!')
    return wrapper
@validator
def open_url(url):
    webbrowser.open(url)

@validator
def send_url(url):
    print(url)

open_url('ht://www.youtube.com/')
send_url('https://www.youtube.com/')