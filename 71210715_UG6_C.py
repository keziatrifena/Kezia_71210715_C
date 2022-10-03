class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self._no_rekening = no_rekening
        self._nama = nama
        self._saldo = saldo
        self._next = None

class SLNC:
    def __init__ (self):
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def insert_head(self, no_rekening, nama, saldo):
        baru = NodeTabungan(no_rekening, nama, saldo)
        if self.isEmpty() == True:
            self._head = baru
            self._tail = baru
        else:
            baru._next = self._head 
            self._head = baru 
        self._size += 1

    def delete(self,posisi):
        if self._size == 0:
            return False
        elif posisi == 0:
            self._delete_head()
        elif posisi + 1 >= self.size:
            self._delete_tail()
        else:
            delete_node = self._head
            for i in range(posisi):
                delete_node = delete_node._next
            bantu = self._head
            while bantu._next != delete_node:
                bantu = bantu._next
        bantu._next = delete_node._next
        del delete_node
        self._size -= 1

    def print(self):
        if self.isEmpty() == False:
            bantu = self._head
            while(bantu!=None):
                print(bantu._no_rekening," ", bantu._nama, " ", bantu._saldo, end= "|")
                bantu = bantu._next
            print()
        else:
            print("Kosong!")

    def filter(self,nilai):
        hilang = self._head._saldo
        while hilang < nilai :
            if hilang < nilai:
                move = self._head._next
                del hilang
                self._head = move
                hilang = move
            hilang = self._head._next

    def update(self,bunga):
        if bunga > 0 and bunga <= 100:
            d = self._head._saldo
            while d > 0:
                tambah = d * bunga / 100
                d += tambah
                d = self._head._next._saldo
                
        else:
            print("Maaf besaran persen harus diantara  0-100!")


slnc=SLNC()
slnc.insert_head(201,"Hanif", 250000)
slnc.insert_head(110,"Yudha", 150000)
slnc.print()
slnc.filter(100)
slnc.print()
slnc.update(200)
slnc.update(50)
slnc.print()