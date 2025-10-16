# 💡 Example 2: Self se object ka data access karna

class linunxModel:
    def __init__(self, name, versions):
        self.name = name
        self.versions = versions

    def show(self):
        print(f"{self.name} > has versions: {self.versions}")

l1 = linunxModel("Ububuntu", [18.04, 20.04, 22.04])

l1.show()
