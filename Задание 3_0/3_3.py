class StringVar:
    string = ""
    def set(self,in_string):
        self.string = in_string
    def get(self):
        print(self.string)

string = StringVar()
string.set("Строка")
string.get()
