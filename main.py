class Browser:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.history = []

    def about(self):
        print(f"Name: {self.name} \nVersion: {self.version} \n.........")

    def deleteHistory(self):
        print("Deleting history☠️☠️\n.........")
        self.history = []

    def showHistory(self):
        print("Latest Visits:")
        for i in range(len(self.history)):
            print(self.history[i])
        print(".........")

    def goto(self, url):
        self.history.append(url)
        print(f"visiting {url}\n.........")


chrome = Browser("Google Chrome", "121.214.366")
chrome.about()
chrome.goto("https://google.com")
chrome.goto("https://youtube.com")
chrome.showHistory()

chrome.deleteHistory()
chrome.showHistory()
