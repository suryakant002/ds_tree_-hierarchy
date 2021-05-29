class Treenode():
    def __init__(self, mylsit =[]):
        self.data = mylsit
        self.children = []
        self.parent = None

    # for addig child to Treenode
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    # For getting the level of Treenode
    def get_level(self):
        level = 0
        p= self.parent
        #if p.parent:
        while p:
            level+=1
            p= p.parent
        return level
    
    # For printing the Tree in standard format
    def print_tree(self, way_of_output, level):
        if self.get_level() > level:
            return

        spaces =  ' ' *  self.get_level() * 5
        prefix = spaces + "|__" if self.parent else ""

        if way_of_output == "both":
            print(prefix + self.data[0] + self.data[1])

        elif way_of_output == "designation":
            print(prefix + self.data[1])

        elif way_of_output == "name":
            print(prefix + self.data[0])
        #print(self.data)
        if (self.children):
            for child in self.children:
                child.print_tree(way_of_output, level)


#Forming the Tree Structure
def get_tree_node():
    root = Treenode(["Nilpul", "(CEO)"])

    reporting_Nilpul_1 =Treenode(["Chinmay", "(CTO)"])
    reporting_Chinamy_1 = Treenode(["Vishwa", "(Infrastructure Head)"])
    reporting_Vishwa_1=Treenode(["Dhaval", "(Cloud Manager)"])
    reporting_Vishwa_2= Treenode(["Abhijit", "(App Manager)"])
    reporting_Chinamy_2 = Treenode(["Aamir", "(Application Head)"])

    reporting_Nilpul_2 = Treenode(["Gels", "(HR Head)"])
    reporting_Gels_1 = Treenode(["Peter", "(Recruitment Manager)"])
    reporting_Gels_2 = Treenode(["Waqs", "(Policy Manger)"])



    root.add_child(reporting_Nilpul_1)
    root.add_child(reporting_Nilpul_2)
    reporting_Nilpul_1.add_child(reporting_Chinamy_1)
    reporting_Nilpul_1.add_child(reporting_Chinamy_2)
    reporting_Nilpul_2.add_child(reporting_Gels_1)
    reporting_Nilpul_2.add_child(reporting_Gels_2)
    reporting_Chinamy_1.add_child(reporting_Vishwa_1)
    reporting_Chinamy_1.add_child(reporting_Vishwa_2)

    print(root.get_level())
    return root

if __name__ == '__main__':
    root = get_tree_node()
    root.print_tree("designation",2)
