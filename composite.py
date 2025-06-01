class FileSystemComponent:
    def display(self):
        ...

class File(FileSystemComponent):
    def __init__(self,
                name) -> None:
        self.name = name

    def display(self):
        print(f"a file with name {self.name}")

class Folder(FileSystemComponent):
    def __init__(self,
                name) -> None:
        self.name = name
        self.files : list[FileSystemComponent] = []

    def display(self):
        print(f"a folder with name {self.name}")
        if self.files:
            print("------------folder content----------")
            for file in self.files:
                file.display()
        else:
            print("empty.")


def main():
    f1 = Folder("hello_world")
    file1 = File("fjeksfjkj")
    file2 = File("jfkesj")
    f1.files = [file1,file2]
    f1.display()
    file1.display()


main()