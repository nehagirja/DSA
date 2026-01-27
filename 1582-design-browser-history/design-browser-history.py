class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0 #similar to curr in LL solution 
        self.length = 1
        self.history = [homepage]

    def visit(self, url: str) -> None:
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else: 
            self.history[self.i + 1] = url #replace the old url by new url
       
        self.i += 1
        self.length = self.i + 1 # we do this so that we can remove all the urls after the ith position

    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.length-1)
        return self.history[self.i]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)