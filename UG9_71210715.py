class Node:
    def __init__(self, data, priority):
        self._data = data
        self._priority = priority # 1 (tertinggi), 2, 3, 4, ...
        self._next = None
        self._prev = None

#Struktur Dasar Class PriorityQueueSorted
class PriorityQueueSortedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False       
    
    def __len__(self):
        return self._size      
    
    def printIsiQueue(self):
        if self.is_empty() == True:
            print('Priority Queue is empty')
        else:

            bantu = self._head
            print("Isi semua Queue: ")
            while bantu != None:
                print("('", bantu._priority, "',", bantu._data, ')', end=' ')
                bantu = bantu._next
        print()


#penghapus data
    def remove(self): # implementasi ini tidak return
        if self.is_empty() == False:
            # yang akan dihapus pasti head
            hapus = self._head
            # jika cuma ada 1 node
            if self._size == 1:
                self._head = None
            else:
                self._head = self._head._next
                self._head._prev = None
            # hapus node
            del hapus
            self._size = self._size - 1
    
    def removePriority(self, prio):
        n = self._head
        while n._priority != prio:
            if n._priority == prio:
                self._head = self._head._next
                del n._priority
            n = n._next


    #pengambilan data
    def peek(self):
        if self.is_empty() == True:
            return None
        else:
            print("Data prioritas tertinggi : ('", self._head._data, "',", self._head._priority, ")")
    
    #penambahan data
    def add(self, data, priority):
        baru = Node(data, priority)
        if self.is_empty():
            self._head = baru
            self._tail = baru
        elif self._size == 1:
            # isinya cuma 1, insert sebelum atau setelah head?
            if self._head._priority > priority:
                # insert sebelum head
                baru._next = self._head
                self._head._prev = baru
                self._head = baru
            else:
                # insert setelah head
                self._head._next = baru
                baru._prev = self._head
                self._tail = baru
        else:
            # cek apakah harus insert depan?
            if self._head._priority > priority:
                baru._next = self._head
                self._head._prev = baru
                self._head = baru
            # cek apakah harus insert belakang?
            elif self._tail._priority <= priority:
                self._tail._next = baru
                baru._prev = self._tail
                self._tail = baru
                self._tail._next = None
            else:
            # berarti insert di tengah
            # letakkan bantu di posisi setelah insertion point
                bantu = self._head
                while bantu._priority < priority:
                    bantu = bantu._next
                # gunakan bantu2 di posisi sebelum insertion point
                bantu2 = bantu._prev
                baru._next = bantu
                bantu._prev = baru
                bantu2._next = baru
                baru._prev = bantu2
        self._size = self._size + 1

    def update(self, data, priority, newPrio, newData):
        if self.is_empty():
            print("kosong")
        else:
            if self.data == newData:
                self.priority == newPrio

sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
# sortedList.update(4, "Karin")
# sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printIsiQueue()