class TowerOfHanoi:
    def _init_(self, num_disks):
        self.num_disks = num_disks
        self.towers = [[], [], []]

        # Initialize the first tower with disks in decreasing order
        for disk in range(num_disks, 0, -1):
            self.towers[0].append(disk)

    def display_towers(self):
        for i in range(self.num_disks, 0, -1):
            print(f"{self.get_disk_symbol(0, i)}  {self.get_disk_symbol(1, i)}  {self.get_disk_symbol(2, i)}")
        print("-------------")

    def get_disk_symbol(self, tower_index, level):
        if level <= len(self.towers[tower_index]):
            return str(self.towers[tower_index][level - 1])
        else:
            return "|"

    def move_disk(self, source, destination):
        disk = self.towers[source].pop()
        self.towers[destination].append(disk)

    def dfs(self, source, target, auxiliary, num_disks):
        if num_disks == 1:
            self.move_disk(source, target)
            self.display_towers()
        else:
            self.dfs(source, auxiliary, target, num_disks - 1)
            self.move_disk(source, target)
            self.display_towers()
            self.dfs(auxiliary, target, source, num_disks - 1)

    def solve(self):
        print("Initial Configuration:")
        self.display_towers()

        print("\nTower of Hanoi Solution:")
        self.dfs(0, 2, 1, self.num_disks)

def main():
    num_disks = int(input("Enter the number of disks: "))
    hanoi = TowerOfHanoi(num_disks)
    hanoi.solve()
_name_="_main"
if _name_ == "_main_":
    main()
