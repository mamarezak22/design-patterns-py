class File:
    def __init__(self,
                name) -> None:
        self.name = name

    def open(self):
        print(f"file {self.name} opened")

class User:
    def __init__(self,
                name):
        self.name = name
        self.is_authnicated = False
    
    def authnicate(self):
        self.is_authnicated = True
    
    
class FileProxy:
    def __init__(self,
                file : File) -> None:
        self.file = file
    
    def get_file(self,user : User):
        if not user.is_authnicated:
            print("you are not authnicated yet")
            return
        self.file.open()
        