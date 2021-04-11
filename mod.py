# Encoding: utf-8


"""
JOIN US : t.me/tempatconfig - t.me/bebas_berinternet

"""








# FOLLOW : github.com/Kgyya













import os
os.system("clear")
import sys
import requests
import re
from bs4 import BeautifulSoup as bs
judul = []
count = 0
garis = 43*"="
q = input("Cari Apk > ").replace(" ","+")
url = f"https://an1.com/?story={q}&do=search&subaction=search"
raw = requests.get(url).text
soup = bs(raw, "html.parser")
for title in soup.find_all("div",class_="title"):
 for link in re.findall('href="(.*?)">',str(title)):
  count += 1
  print(str(count)+") Judul : "+str(title.text))
  print(garis)
  judul.append(link)
owh = input("Input Nomor > ")
try:
 down = judul[int(owh) - 1]
except (ValueError,IndexError):
 exit("Masukkin Nomor Nya Aja Kntl")
raww = requests.get(down).text
supp = bs(raww, "html.parser")
deskripsi = supp.find("div",attrs={"itemprop":"description"})
dev = supp.find("div",attrs={"itemprop":"author"})
kategori = supp.find("span",attrs={"itemprop":"applicationCategory"})
subkategori = supp.find("span",attrs={"itemprop":"applicationSubCategory"})
os = supp.find("span",attrs={"itemprop":"operatingSystem"})
versi = supp.find("span",attrs={"itemprop":"softwareVersion"})
ukuran = supp.find("span",attrs={"class":"size"})
print("Developer    :"+str(dev.text))
print("Kategori     : "+str(kategori.text))
print("Ukuran       : "+str(ukuran.text))
print("Sub Kategori : "+str(subkategori.text))
print("Support      : "+str(os.text))
print("Deskripsi    : "+str(deskripsi.text))
print("\n1) Download APK\n")
owhh = input("Pilih Nomor > ")
out = input("Output > ").replace(" ","_")
def unduh():
 print("[...] Tunggu Bang")
 linkk = supp.find("a",attrs={"class":"get-product"})
 rawww = requests.get("https://an1.com"+linkk.get("href")).text
 linkkk = re.search("div><a href=(.*?)>",str(rawww)).group(1)
 r = requests.get(linkkk,stream=True,allow_redirects=True)
 with open(f"{out}.apk", "wb") as s:
    dl = 0
    total_panjang = int(r.headers.get("content-length"))
    for KNTL in r.iter_content(chunk_size=4096):
     dl += len(KNTL)
     s.write(KNTL)
     done = int(43 * dl / total_panjang)
     sys.stdout.write("\r[%s%s]" % ('#' * done, ' ' * (43-done)) )
     sys.stdout.flush()
 print(f"Sukses Terdownload\nTersimpan Sebagai {out}.apk")
 print("Mau Di Pindahin Kemana?")
 print(" [01] storage/emulated/0/")
 print(" [02] data/data/com.termux/files/")
 owhhh = input("Input Nomor > ")
 if owhhh in ("01","1"):
  os.system(f"mv {out}.apk storage/emulated/0")
  print(f"Sukses > storage/emulated/0/{out}.apk")
 elif owhhh in ("02","2"):
  print(f"Sukses > data/data/com.termux/files/{out}.apk")
 else:
  exit("dahlah")
unduh()
