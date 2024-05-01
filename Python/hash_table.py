class HashTable:
    def __init__(self, slots):
        self.slots = slots
        self.table = []
        self.create_table()

    def create_table(self):
        self.table = [[] for _ in range(self.slots)]

    def hash_key(self, value):
        return value % self.slots
    
    def add_item(self, value):
        hash_key_index = self.hash_key(value)
        self.table[hash_key_index].append(value)

    def find_item(self, item):
        hash_key_index = self.hash_key(item)
        return hash_key_index
    

if __name__ == "__main__":
    slots = 3
    values = [1, 3, 5, 7, 9]
    find_item_value = 3
    hash_table_instance = HashTable(slots)
    for i in values:
        hash_table_instance.add_item(i)

    location = hash_table_instance.find_item(find_item_value)

    print(f"item allocation are {hash_table_instance.table}")
    print(f"location of item {location}")
