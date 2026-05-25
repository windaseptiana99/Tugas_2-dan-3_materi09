class Lagu:
    def __init__(self, judul):
        self.judul = judul
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def tambah_lagu(self, judul):
        lagu_baru = Lagu(judul)

        if self.head is None:
            self.head = lagu_baru
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = lagu_baru

    def tampilkan_playlist(self):
        current = self.head

        while current:
            print(current.judul)
            current = current.next


playlist = Playlist()

playlist.tambah_lagu("Hindia - Evaluasi")
playlist.tambah_lagu("Tulus - Monokrom")
playlist.tambah_lagu("Nadin Amizah - Bertaut")

print("Daftar Playlist:")
playlist.tampilkan_playlist()