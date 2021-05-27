class MaxSizeList:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.thislist = []

    def push(self, lyric):
        maxsize = self.maxsize       #creating maxsize variable so it's easier to call
        thislist = self.thislist
        thislist.append(lyric)
        if len(thislist) > maxsize:  #if length of list is greater than the maxsize, get rid of the last
            thislist.pop(0)          # thing added to the list

    def get_list(self):
        return self.thislist         #return list

#when i ran the full test code, it returned
# ['ho', "let's", 'go']
# ['ho', "let's", 'go']
# but running the variables seperately it returned
#['ho', "let's", 'go']
#['go']
# as expected. do you see any weird bugs that may have caused that?


a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("ho")
a.push("let's")
a.push("go")

b.push("hey")
b.push("ho")
b.push("let's")
b.push("go")

print(a.get_list())     # ['ho', "let's", 'go']
print(b.get_list())

