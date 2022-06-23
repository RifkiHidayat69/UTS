# RIFKI HIDAYAT 
# 210101035
# SISTEM INFORMASI 21A1


def garis():
    print("="*55)
def ulangi():
    print("Apakah Anda Ingin Mengulangi?")
    print("Ketik Iya Atau Tidak")
def keluar():
    garis()
    print(f"Terimakasih {nama} Semoga Sehat Selalu")

menu = 0
while menu != 9 :
    garis()
    print("PROGRAM RUMAH SAKIT IBUNDA")
    garis()

    garis()
    print("PILIH KODE PASIEN")
    garis()
    print("Kode Pasien  I   Status Pasien    I   Biaya Pendaftaran")
    print("RS001        I   Pasien Baru      I   Rp. 400.000")
    print("RS002        I   Pasien Lama      I   Rp. 300.000")
    print("RS003        I   Pasien BPJS      I   Rp. 200.000")
    print("RS004        I   Pasien Akses     I   Rp. 100.000")
    garis()

    nama = input("Masukkan Nama : ")
    kode = input("Masukkan Kode Pasien : ")
    if kode == "RS001":
        status = "Pasien Baru"
        biaya_pend = (400000)
    elif kode == "RS002" :
        status = "Pasien Lama"
        biaya_pend = (300000)
    elif kode == "RS003" :
        status = "Pasien BPJS"
        biaya_pend = (200000)
    elif kode == "RS004" :
        status = "Pasien Akses"
        biaya_pend = (100000)
    else :
        print("Kode Yang Anda Masukkan Salah!")
        continue
    
    garis()
    print("PILIH KODE KAMAR")
    garis()
    print("Kode Kamar   I   Nama Kamar      I   Biaya Kamar")
    print("1111         I   Kamar Anggrek   I   Rp. 1.000.000")
    print("2222         I   Kamar Melati    I   Rp. 2.000.000")
    print("3333         I   Kamar Mawar     I   Rp. 3.000.000")
    print("4444         I   Kamar Tulip     I   Rp. 4.000.000")
    print("5555         I   Kamar Dahlia    I   Rp. 5.000.000")
    garis()

    kode_kmr = input("Masukkan Kode Kamar : ")
    if kode_kmr == "1111" :
        nama_kmr = "Kamar Anggrek"
        biaya_kmr = (1000000)
    elif kode_kmr == "2222" :
        nama_kmr = "Kamar Melati"
        biaya_kmr = (2000000)
    elif kode_kmr == "3333" :
        nama_kmr = "Kamar Mawar"
        biaya_kmr = (3000000)
    elif kode_kmr == "4444" :
        nama_kmr = "Kamar Tulip"
        biaya_kmr = (4000000)
    elif kode_kmr == "5555" :
        nama_kmr = "Kamar Dahlia"
        biaya_kmr = (5000000)
    else :
        print("Kode Yang Anda Masukkan Salah!")
        continue
    
    garis()
    print("PILIH KODE DOKTER")
    garis()
    print("Kode Dokter   I   Nama Dokter    I   Biaya Pemeriksaan")
    print("DK001         I   Dr. Budi       I   Rp. 500.000")
    print("DK002         I   Dr. Ari        I   Rp. 500.000")
    print("DK003         I   Dr. Andi       I   Rp. 500.000")
    print("DK004         I   Dr. Rudi       I   Rp. 600.000")
    print("DK005         I   Dr. Agus       I   Rp. 700.000")
    garis()

    kode_dr =input("Masukkan Kode Dokter : ")
    if kode_dr == "DK001" :
        nama_dr = "Dr. Budi"
        biaya_periksa = (500000)
    elif kode_dr == "DK002" :
        nama_dr = "Dr. Ari"
        biaya_periksa = (500000)
    elif kode_dr == "DK003" :
        nama_dr = "Dr. Andi"
        biaya_periksa = (500000)
    elif kode_dr == "DK004" :
        nama_dr = "Dr. Rudi"
        biaya_periksa = (600000)
    elif kode_dr == "DK005" :
        nama_dr = "Dr. Agus"
        biaya_periksa = (700000)
    else :
        print("Kode Yang Anda Masukkan Salah!")
        continue
    
    garis()
    print("LAMA MENGINAP")
    garis()
    print("Lama Menginap   I   Diskon")
    print(">15 Hari        I   50%, dari biaya kamar")
    print(">10 Hari        I   40%, dari biaya kamar")
    print(">6 Hari         I   30%, dari biaya kamar")
    print(">3 Hari         I   20%, dari biaya kamar")
    print(">1 Hari         I   10%, dari biaya kamar")
    garis()

    lama = int(input("Lama Menginap : "))
    if lama >15 :
        diskon = biaya_kmr*0.5
    elif lama >10 :
        diskon = biaya_kmr*0.4
    elif lama >6 :
        diskon = biaya_kmr*0.3
    elif lama >3 :
        diskon = biaya_kmr*0.2
    elif lama >=1 :
        diskon = biaya_kmr*0.1

    total_biaya = (biaya_pend + biaya_kmr + biaya_periksa - diskon)

    garis()
    print("Nama Pasien         :",nama)
    print("Status Pasien       :",status)
    print("Biaya Daftar Pasien : Rp. ",biaya_pend)
    print("Nama Kamar          :",nama_kmr)
    print("Biaya Kamar         : Rp. ",biaya_kmr)
    print("Nama Dokter         :",nama_dr)
    print("Biaya Pemeriksaan   : Rp. ",biaya_periksa)
    print("Lama Mengiap        :",lama,"Hari")
    print("Diskon              : Rp. ",diskon)
    print("Total Bayar         : Rp. ",total_biaya)
    garis()
    ulangi()
    ulangi1 = input()
    if ulangi1 == "Iya":
        continue
    elif ulangi1 == "Tidak":
        keluar()
        break