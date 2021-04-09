#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################
#                        #
#Emre Yılmaz (delosemre) #
#                        #
##########################
import sys
import argparse
import os
import time
import httplib
import subprocess
import re, urllib2
import socket
import urllib,sys,json
import telnetlib
import glob
import random
import Queue 
import threading
import base64
from getpass import getpass
from commands import *
from sys import argv
from platform import system
from urlparse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep


print ( """\033[1;91m
 _  __                    _ ____  _             
| |/ /___ _ __ _ __   ___| | __ )| | ___   __ _ 
| ' // _ \ '__| '_ \ / _ \ |  _ \| |/ _ \ / _` |
| . \  __/ |  | | | |  __/ | |_) | | (_) | (_| |
|_|\_\___|_|  |_| |_|\___|_|____/|_|\___/ \__, |
                                          |___/ .org\033[1;m
\033[1;93mDeneyimsizler İçin Bir Penetrasyon Aracı\033[1;m 

     \033[1;91m
     KernelBlog.org
     Forum.kernelblog.org
     ---
     KernelBlog devepoler team
     Kernelblog geliştirici ekibi\033[1;m
      """)

def logo():
     print ( """
\033[1;91m    
 _  __                    _ ____  _             
| |/ /___ _ __ _ __   ___| | __ )| | ___   __ _ 
| ' // _ \ '__| '_ \ / _ \ |  _ \| |/ _ \ / _` |
| . \  __/ |  | | | |  __/ | |_) | | (_) | (_| |
|_|\_\___|_|  |_| |_|\___|_|____/|_|\___/ \__, |
                                          |___/ .org
Deneyimsizler İçin Bir Penetrasyon Aracı
\033[1;m      """)

def logohack():
     print ("""
\033[1;91m
     )                          (                
  ( /(                   (   (  )\ )             
  )\()) (  (           ( )\( )\(()/(      (  (   
|((_)\ ))\ )(   (     ))((_)((_)/(_)) (   )\))(  
|_ ((_)((_|()\  )\ ) /((_)((_)_(_))   )\ ((_))\  
| |/ (_))  ((_)_(_/((_))| || _ ) |   ((_) (()(_) 
  ' </ -_)| '_| ' \)) -_) || _ \ |__/ _ \/ _` |  
 _|\_\___||_| |_||_|\___|_||___/____\___/\__, |  
               KernelBlog | delosemre    |___/   
                                     \033[1;m

          """)


#giriş kısmı

kullanici = raw_input("    [ > ] Kullanıcı Adı Giriniz : ")
time.sleep(0.5)

#kullanıcı sorgusu

print("")
print("    [ + ] Hoşgeldin " + " " + kullanici) 
print("")
time.sleep(1)


#repo ekleme


print("   \033[1;91mBirkaç Düzenleme Yapıyoruz...\033[1;m")
print("   \033[1;91mRepo Ekleniyor...\033[1;m")
time.sleep(1)
#os.system()

packetmanbul = os.popen("whereis pacman | grep /pacman").read()

if (packetmanbul != ""):
     if (os.popen("cat /etc/pacman.d/blackarch-mirrorlist").read() == "cat: /etc/pacman.d/blackarch-mirrorlist: No such file or directory"):
          os.system("curl -O https://blackarch.org/strap.sh && bash strap.sh")
          time.sleep(1)
          os.system("rm -rf strap.sh")
     os.system("clear")
     packet = "pacman -S "
else:
     if (os.popen("cat /etc/apt/sources.list | grep kali").read() == ""):
          repo = open('/etc/apt/sources.list','r+')                                                 
          repo.write('\n deb http://http.kali.org/kali kali-rolling main contrib non-free') # her başladığında sourcese yeni kayıt ekleyecek!
          os.system("wget -q -O - https://www.kali.org/archive-key.asc | gpg --import")
          os.system("gpg --fingerprint 7D8D0BF6")
          print(" ")
          print("   \033[1;91mrepo Güncelleniyor...\033[1;m")
          print(" ")
          time.sleep(1)
          os.system("apt-get update")
          repo.close()
          print("   \033[1;91mRepo Eklendi.\033[1;m")
          print("   \033[1;91mEkran Temizleniyor...\033[1;m")
          print("   \033[1;91mAçlıyor...\033[1;m")
          time.sleep(2)
          cmd1 = os.system ("clear")
     packet = "apt install "
     os.system("clear")


#Menü

def baslangicmenu():
     print ("""
          
          Seçenekler

     1-) Bilgi Toplama
     2-) Zaafiyet Tarama
     3-) Hakkımızda
     4-) Sistemi Güncelle
     99-) Çıkış
     
     """)

#bilgi menüsü
def bilgi():
     print ("""\033[1;91m
               Bilgi Toplama

          1 : Dmitry
          2 : GoLismero
          3 : Theharvester
          4 : Sublist3r
          5 : Nmap Port Taraması
          99 : Çıkış

      \033[1;m""")

#zaafiyet tarama menüsü
def zaafiyettarama():
     print ("""\033[1;91m
               
               Zaafiyet Tarama
          1 : Fimap
          2 : Uniscan
          3 : JoomScan
          4 : WPScan
          5 : Skipfish
          99 : Çıkış

      \033[1;m""")




#Bilgi toplama komutlar
def dmitry():
     print ("""
               Bu araç oldukça kullanışlı bir Information Gathering aracıdır. 
               Bu araç ile bir host üzerinden birçok bilgi toplanabilir.
               Bunlar subdomain'ler,email adresleri, port tarama gibi birçok şey olabilir.""")

     secimdmitry = raw_input("       Devam (E/H): ")
     if secimdmitry == "e" or secimdmitry == "E":
               print("   \033[1;91mDmitry Yükleniyor...\033[1;m")
               time.sleep(1)
               os.system(packet + "dmitry")
               print("   \033[1;91mDmitry Başlatılıyor...\033[1;m")
               time.sleep(1)
               os.system("clear")
               logohack()
               dmitryhedef = raw_input("     Hedef Giriniz: ")
               os.system("dmitry -p -n -i -s -e " + dmitryhedef)
               

     elif secimdmitry == "h" or secimdmitry == "H":
               bilgi() 
               os.system("clear")



def golismero():
     print("""
               GoLismero, güvenlik testi ve pentest analizlerinde kullanılan 
               çok fonksiyonlu bir açık kaynaklı yazılımdır.
               Nmap, Sql, Database, dns, bruteforce, 
               harvaster, ssh gibi birçok fonksiyonu vardır.

               """)
     secimgolis = raw_input("       Devam (E/H): ")
     if secimgolis == "e" or secimgolis == "E":
          print("   \033[1;91mGoLismero Yükleniyor...\033[1;m")
          time.sleep(1)
          os.system(packet + "golismero")
          os.system("clear")
          print("   \033[1;91mGoLismero Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          golishedef = raw_input("     Hedef Giriniz: ")
          os.system("golismero" + golishedef)
         
     elif secimgolis == "h" or secimgolis == "H":
          bilgi() 
          os.system("clear")


def theharvester():
     print(""" 
          Theharvester
          sub domain ve emailleri tespit etmek için kullanılır.

          """)
     secimtheharvester = raw_input("       Devam (E/H): ")
     if secimtheharvester == "e" or secimtheharvester == "E":
          print("   \033[1;91mTheharvester Yükleniyor...\033[1;m")
          time.sleep(1)
          os.system(packet + "theharvester")
          os.system("clear")
          print("   \033[1;91mTheharvester Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          theharvesterhedef = raw_input("     Hedef Giriniz: ")
          os.system("theharvester -d " + theharvesterhedef + " -l 50 -b all")
          

     elif secimtheharvester == "h" or secimtheharvester == "H":
          bilgi() 
          os.system("clear")

def sublist3r():
     print(""" 
          Sublist3r
          OSINT kullanan web sitelerinin alt alanlarını numaralandırmak 
          için tasarlanmış bir python araçtır.
          Penetrasyon test cihazları ve hata avcılarının hedefledikleri
          alan adına alt alanlar toplamaları için yardımcı olur.
          Sublist3r, Google, Yahoo, Bing, Baidu ve Ask gibi birçok arama
          motorunu kullanan alt alanları numaralandırır. Sublist3r ayrıca Netcraft, 
          Virustotal, ThreatCrowd, DNSdumpster ve ReverseDNS'yi 
          kullanarak alt alanları numaralandırır.

          """)
     secimsublist3r = raw_input("       Devam (E/H): ")
     if secimsublist3r == "e" or secimsublist3r == "E":
          print("   \033[1;91mSublist3r Yükleniyor...\033[1;m")
          time.sleep(1)
          os.system(packet + "sublist3r")
          os.system("clear")
          print("   \033[1;91mSublist3r Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          sublist3rhedef = raw_input("     Hedef Giriniz: ")
          os.system("sublist3r -d "+sublist3rhedef+" -t 3 -e bing")
          

     elif secimsublist3r == "h" or secimsublist3r == "H":
          bilgi() 
          os.system("clear")

def nmap():
     print(""" 
          Nmap
          Nmap, ağdaki cihazlara ve cihazların portlarına
          çeşitli paketler gönderip ve cevaplara bakarak
          cihazın açık olup olmadığını, açık olan portlar 
          üzerinde hangi servislerin çalıştığını, cihazların
          hangi işletim sistemini kullandığını öğrenmemize
          olanak sağlayan open-source bir araçtır.

          """)
     secimnmap = raw_input("       Devam (E/H): ")
     if secimnmap == "e" or secimnmap == "E":
          print("   \033[1;91mNmap Yükleniyor...\033[1;m")
          time.sleep(1)
          os.system(packet + "nmap")
          os.system("clear")
          print("   \033[1;91mNmap Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          print ("  varsayılan Tarama")
          nmaphedef = raw_input("     Hedef Giriniz: ")
          os.system("nmap "+nmaphedef)
          

     elif secimnmap == "h" or secimnmap == "H":
          bilgi() 
          os.system("clear")
#Bilgi toplama komutlar son

#Zaafiyet Tarama komutlar Başlangıç
def fimap():
     print(""" 
          fimap, webapps'deki yerel ve uzak dosya içerme
          hataları için otomatik olarak bulabileceğiniz,
          hazırlayabilen, denetleyebilen, kullanabilen 
          ve hatta otomatik olarak kullanabilen küçük 
          bir python aracıdır. 

          """)
     secimfimap = raw_input("       Devam (E/H): ")
     if secimfimap == "e" or secimfimap == "E":
          print("   \033[1;91mFimap Yükleniyor...\033[1;m")
          time.sleep(1)
          os.system(packet + "fimap")
          print("   \033[1;91mBagımlılıklar Yükleniyor...\033[1;m")
          time.sleep(1)
          os.system(packet + "python-pip")
          os.system("pip install httplib2")
          os.system("clear")
          print("   \033[1;91mFimap Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          print("   Hedef url 'http://localhost/test.php?file=bang&id=23' şeklinde olmalıdır.")
          fimaphedef = raw_input("     Hedef Giriniz: ")
          os.system("fimap -u "+fimaphedef)
          

     elif secimfimap == "h" or secimfimap == "H":
           
          os.system("clear")

def uniscan():
     print("""
          Uniscan
          hedef sistem üzerindeki XSS ,SQL ,Rfi gibi açıkları tarayabilir,
          Sisteme ait bir çok bilgi bulabilirsiniz
          ( Yedek Dosyalar , E-Mail , Hostlar ).

          """)
     secimuniscan = raw_input("       Devam (E/H): ")
     if secimuniscan == "e" or secimuniscan == "E":
          print("   \033[1;91mUniscan Yükleniyor...\033[1;m")
          time.sleep(1)
          os.system(packet + "uniscan")
          print("   \033[1;91mUniscan Güncelleniyor...\033[1;m")
          time.sleep(0.5)
          os.system("clear")
          print("   \033[1;91muniscan Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          uniscanhedef = raw_input("     Hedef Giriniz: ")
          os.system("uniscan -u "+ uniscanhedef + " --qweds")
          

     elif secimuniscan == "h" or secimuniscan == "H":
          os.system("clear")

def joomscan():
     print(""" 
          Joomscan, joomla sitelerde açık taramaya yarayan bir araçtır.
          Bu araç sayesinde joomla sitelerdeki açıkları tespit edebiliriz
          ve buna ek olarak sitede bulunan açığın türüne göre exploit
          bulup bize sunuyor.

          """)
     secimjoomscan = raw_input("       Devam (E/H): ")
     if secimjoomscan == "e" or secimjoomscan == "E":
          print("   \033[1;91mJoomScan Yükleniyor...\033[1;m")
          time.sleep(1)
          os.system(packet + "joomscan")
          print("   \033[1;91mJoomScan Güncelleniyor...\033[1;m")
          time.sleep(0.5)
          os.system("clear")
          print("   \033[1;91mJoomScan Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          joomscanhedef = raw_input("     Hedef Giriniz: ")
          os.system("joomscan -u "+joomscanhedef)
          

     elif secimjoomscan == "h" or secimjoomscan == "H": 
          os.system("clear")

def wpscan():
     print("""
          WpScan 
          WordPress siteleri üzerinde zafiyet taramaları yapan
          açık kaynak kodlu bir güvenlik uygulamasıdır. 
          Bu uygulamayı kullanmak size saldırganın gözünden
          sitenize bakmanızı sağlıyacaktır.
          WPScan aracı ile bir wordpress sitesinde 
          “kullanıcı Adını bulma, bruteforce saldırısı, 
          wordpress Versiyon numarası , yüklü eklentilerin ve 
          temanın güvenlik açığının” taramasını yapar.

          """)
     secimwpscan = raw_input("       Devam (E/H): ")
     if secimwpscan == "e" or secimwpscan == "E":
          print("   \033[1;91mwpscan Yükleniyor...\033[1;m")
          time.sleep(1)
          os.system(packet + "wpscan")
          print("   \033[1;91mwpscan Güncelleniyor...\033[1;m")
          time.sleep(0.5)
          os.system("clear")
          print("   \033[1;91mwpscan Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          wpscanhedef = raw_input("     Hedef Giriniz: ")
          os.system("wpscan -u "+wpscanhedef+ " --enumerate p")
          

     elif secimwpscan == "h" or secimwpscan == "H":
          os.system("clear")

def skipfish():
     print("""
          skipfish
          Skipfish genelde hızlı tarama ve raporlama
          sistemiyle ön plana çıkan bir scanner aracıdır.

          """)
     secimskipfish = raw_input("       Devam (E/H): ")
     if secimskipfish == "e" or secimskipfish == "E":
          print("   \033[1;91mskipfish Yükleniyor...\033[1;m")
          time.sleep(1)
          os.system(packet + "skipfish")
          print("   \033[1;91mskipfish Güncelleniyor...\033[1;m")
          time.sleep(0.5)
          print("   91mBagımlılıklar Yükleniyor...")
          os.system("clear")
          print("   \033[1;91mskipfish Başlatılıyor...\033[1;m")
          time.sleep(1)
          logohack()
          skipfishhedef = raw_input("     Hedef Giriniz: ")
          os.system("skipfish -o /home/skipfishtarama http://"+skipfishhedef)
          print(" ")
          print("   \033[1;91m/home/skipfishtarama/ dizinine tarama çıktısı kaydedildi.\033[1;m")
          


     elif secimsqlsus == "h" or secimsqlsus == "H":
          os.system("clear")

#Zaafiyet Tarama komutlar Son

#Başlangıç
logo()
baslangicmenu()
print("   Seçeneklerden Birini Giriniz.")
secim = raw_input("    " + kullanici + "" "\033[1;91m@KernelBlog:~$\033[1;m ")

if secim == "1":
          os.system("clear")
          logohack()
          bilgi()
          
          print("   Seçeneklerden Birini Giriniz.")
          secimbilgi = raw_input("    " + kullanici + "" "\033[1;91m@KernelBlog:~$\033[1;m ")

          if secimbilgi == "1":
               dmitry()
          if secimbilgi == "2":
               golismero()     
          if secimbilgi == "3":
               theharvester()
          if secimbilgi == "4":
               sublist3r()
          if secimbilgi == "5":
               nmap()               
              
          if secimbilgi == "99":
               print ("  Güle Güle " + " " + kullanici)
               time.sleep(1)
               sys.exit()


if secim == "2":
          os.system("clear")
          logohack()
          zaafiyettarama()
          print("   Seçeneklerden Birini Giriniz.")
          secimzaafiyettarama = raw_input("    " + kullanici + "" "\033[1;91m@KernelBlog:~$\033[1;m ")

          if secimzaafiyettarama == "1":
               fimap()     
          if secimzaafiyettarama == "2":
               uniscan()
          if secimzaafiyettarama == "3":
               joomscan()
          if secimzaafiyettarama == "4":
               wpscan()
          if secimzaafiyettarama == "5":
               skipfish()
          if secimzaafiyettarama == "99":
               print ("  Güle Güle " + " " + kullanici)
               time.sleep(1)
               sys.exit()
if secim == "3":
     print ("""
          Hata ve Düzeltmeler için iletişime geçiniz.
          \033[1;91m
          Telegram:
          @delosemre
          @kernelblog

          Twitter: 
          @delosemre
          @kernel_blog
          ---
          www.kernelblog.org
          www.forum.kernelblog.org
          info@kernelblog.org
          delosemre@outlook.com
          delosemre@delosemre.xyz\033[1;m

          1-) Geri Dön
          2-) Çıkış
          """)
     
          
     secim3 = raw_input("    " + kullanici + "" "\033[1;91m@KernelBlog:~$\033[1;m ")
     if secim3 == "1":
               os.system("clear")
               logo()
               baslangicmenu()
     if secim3 == "2":
               print ("  Güle Güle " + " " + kullanici)
               time.sleep(1)
               sys.exit()

if secim == "Sistemi Güncelle" or secim == "sistemi güncelle" or secim == "4":
          print("Sistem Güncelleniyor" + " " + kullanici)

          if (packet == "apt install "):
               os.system("apt-get update")
          else:
               os.system(pacman -Syy)
          logo()
          menu()
if secim == "çıkış" or secim == "Çıkış" or secim == "99":
          print ("  Güle Güle " + " " + kullanici)
          time.sleep(1)
          sys.exit()