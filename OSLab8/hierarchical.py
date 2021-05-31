class Node:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.subfolders = {}
        self.files = []


class Directory:
    def __init__(self):
        self.root = Node(None, "C:")
        self.curr_node = self.root

    def create_folder(self, name):
        curr = self.curr_node
        curr.subfolders[name] = Node(curr, name)

    def create_file(self, name):
        curr = self.curr_node
        curr.files.append(name)

    def change_directory(self, directory):
        curr = self.curr_node

        if directory in curr.subfolders:
            self.curr_node = curr.subfolders[directory]

        else:
            print("Directory does not exist")

    def print_files(self):
        curr = self.curr_node

        if len(curr.subfolders) == 0:
            print("No Folders")

        else:
            print("Folders: ")
            for folder in curr.subfolders:
                print(folder)

        if len(curr.files) == 0:
            print("No files")

        else:
            print("Files: ")
            for file in curr.files:
                print(file)

    # Visi masa hadapan nepu

    def print_directory(self):
        self.print_dfs(self.root, 0)

    def print_dfs(self, curr_node, depth):
        if depth == 0:
            print("Directory:")

        print("\t-->"*depth, curr_node.name)

        if len(curr_node.files) != 0:
            for file in curr_node.files:
                print("\t"*(depth), "-", file)

        for subfolder in curr_node.subfolders:
            self.print_dfs(curr_node.subfolders[subfolder], depth+1)

    def prev_directory(self):
        if self.curr_node == self.root:
            print("Already at root node")
        else:
            self.curr_node = self.curr_node.parent

    def print_cd(self):
        if self.curr_node == self.root:
            return "C:"

        else:
            curr = self.curr_node
            paths = []

            while curr != self.root:
                paths.append(curr.name)
                curr = curr.parent

            paths.append("C:")
            paths.reverse()
            return "/".join(paths)


def main():

    dc = Directory()

    # Add other functions, eg. go back on directory,
    while True:
        print("Current Directory: ", dc.print_cd())
        x = input(
            "Select the Function\n1 - Create Folder\n2 - Create File\n3 - Print Current Directory\n4 - Back to Previous Directory\nFileName - Change Directory\nExit - End\n")
        if x == "1":
            name = input("Insert Folder Name: ")
            # if already exist
            dc.create_folder(name)

        elif x == "2":
            file_name = input("Insert File Name: ")
            dc.create_file(file_name)
            # create file
        elif x == "3":
            dc.print_files()

        elif x == "4":
            dc.prev_directory()

        elif x == "exit":
            break

        else:
            dc.change_directory(x)
        print()

    # after exit the loop print complete directory eg: C:/Naim/Afiq
    # also print all the subfolder inside the current folder + files
    dc.print_files()
    dc.print_directory()


main()
