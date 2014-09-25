#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
# 
# kalkuluvtsains.py
#
# Copyright 2014 Universitas Virtual Terbuka
#
# Referensi program:
# 1. http://code.google.com/p/calculator-using-pygtk
# 2. http://code.google.com/p/calculator-python-glade
# 3. http://zetcode.com/gui/pygtk/layout
# 4. http://www.vrsets.com/index.php?topic=25484.0
# 5. https://github.com/davidmalcolm/pygobject/blob/master/pygi-convert.sh
# 
# Program ini buat pembelajaran di Universitas Virtual Terbuka

from gi.repository import Gtk, Gdk, GdkPixbuf

from math import *

license = """Kalkulator Saintifik UVT is free software; you can redistribute it 
and/or modify it under the terms of the GNU General Public License(GPL v3) 
as published by the Free Software Foundation.

Kalkulator Saintifik UVT is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Kalkulator Saintifik UVT; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA."""

authors = ["Raviyanto Ahmad <raviyanto@gmail.com>", "Rajeswari Seetharaman <sraji.me@gmail.com>", 
           "Jan Bodnar <vronskij@gmail.com>"]

class Kalkulator:
    def __init__(self):
        self.jendela = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        self.jendela.set_size_request(300, 300)
        self.jendela.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0, 128, 0, 0.3))
        self.jendela.set_resizable(True)
        self.jendela.set_position(Gtk.WindowPosition.CENTER)
        self.jendela.set_border_width(5)
        self.jendela.set_title("Kalkulator Saintifik UVT")
        
        try:
            self.jendela.set_icon_from_file("/usr/share/kalkuluvtsains/gambar/kalkulatorsains.png")
        except Exception, e:
            print e.message
          
        self.tombol()
        self.menu()
        self.tabel()
        self.masukan()
        self.kotak()
        self.konek()
        self.jendela.show_all()

    def tombol(self):
        self.tombol_hapus = Gtk.Button("CE")
        self.tombol_kurung_buka = Gtk.Button("(")
        self.tombol_kurung_tutup = Gtk.Button(")")
        self.tombol_tutup = Gtk.Button("Tutup")
        
        self.tombol_tujuh = Gtk.Button("7")
        self.tombol_delapan = Gtk.Button("8")
        self.tombol_sembilan = Gtk.Button("9")
        self.tombol_bagi = Gtk.Button("/")
        
        self.tombol_empat = Gtk.Button("4")
        self.tombol_lima = Gtk.Button("5")
        self.tombol_enam = Gtk.Button("6")
        self.tombol_kali = Gtk.Button("*")
    
        self.tombol_satu = Gtk.Button("1")
        self.tombol_dua = Gtk.Button("2")
        self.tombol_tiga = Gtk.Button("3")
        self.tombol_kurang = Gtk.Button("-")

        self.tombol_nol = Gtk.Button("0")
        self.tombol_titik = Gtk.Button(".")
        self.tombol_sama_dengan = Gtk.Button("=")
        self.tombol_tambah = Gtk.Button("+")

        self.tombol_radians = Gtk.Button("radians")
        self.tombol_e = Gtk.Button("e")
        self.tombol_log = Gtk.Button("log")
        self.tombol_log10 = Gtk.Button("log10")

        self.tombol_degrees = Gtk.Button("degrees")
        self.tombol_pi = Gtk.Button("pi")
        self.tombol_sinh = Gtk.Button("sinh")
        self.tombol_cosh = Gtk.Button("cosh")

        self.tombol_tanh = Gtk.Button("tanh")
        self.tombol_sqrt = Gtk.Button("sqrt")
        self.tombol_asin = Gtk.Button("asin")
        self.tombol_acos = Gtk.Button("acos")

        self.tombol_atan = Gtk.Button("atan")
        self.tombol_sin = Gtk.Button("sin")
        self.tombol_cos = Gtk.Button("cos")
        self.tombol_tan = Gtk.Button("tan")

    def menu(self):
        self.papan_menu = Gtk.MenuBar()
        
        self.pilihan = Gtk.Menu()

        self.tentang = Gtk.Menu()

        self.keluar = Gtk.MenuItem("Keluar")
        
        self.pilihan.append(self.keluar)

        self.keterangan = Gtk.MenuItem("Keterangan")

        self.tentang.append(self.keterangan)

        self.pokok_pilihan = Gtk.MenuItem("Berkas")

        self.pokok_tentang = Gtk.MenuItem("Ihwal")

        self.pokok_pilihan.set_submenu(self.pilihan)

        self.pokok_tentang.set_submenu(self.tentang)

        self.papan_menu.append(self.pokok_pilihan)

        self.papan_menu.append(self.pokok_tentang) 

    def masukan(self):
        self.masukan_data = Gtk.Entry()
        self.x = self.masukan_data.get_text()

    def tabel(self):
        self.tabel_kalkulator = Gtk.Table(rows = 9, columns = 4, homogeneous = True)
        self.tabel_kalkulator.attach(self.tombol_hapus, 0, 1, 0, 1)
        self.tabel_kalkulator.attach(self.tombol_kurung_buka, 1, 2, 0, 1)
        self.tabel_kalkulator.attach(self.tombol_kurung_tutup, 2, 3, 0, 1)
        self.tabel_kalkulator.attach(self.tombol_tutup, 3, 4, 0, 1)

        self.tabel_kalkulator.attach(self.tombol_tujuh, 0, 1, 1, 2)
        self.tabel_kalkulator.attach(self.tombol_delapan, 1, 2, 1, 2)
        self.tabel_kalkulator.attach(self.tombol_sembilan, 2, 3, 1, 2)
        self.tabel_kalkulator.attach(self.tombol_bagi, 3, 4, 1, 2)

        self.tabel_kalkulator.attach(self.tombol_empat, 0, 1, 2, 3)
        self.tabel_kalkulator.attach(self.tombol_lima, 1, 2, 2, 3)
        self.tabel_kalkulator.attach(self.tombol_enam, 2, 3, 2, 3)
        self.tabel_kalkulator.attach(self.tombol_kali, 3, 4, 2, 3)

        self.tabel_kalkulator.attach(self.tombol_satu, 0, 1, 3, 4)
        self.tabel_kalkulator.attach(self.tombol_dua, 1, 2, 3, 4)
        self.tabel_kalkulator.attach(self.tombol_tiga, 2, 3, 3, 4)
        self.tabel_kalkulator.attach(self.tombol_kurang, 3, 4, 3, 4)

        self.tabel_kalkulator.attach(self.tombol_nol, 0, 1, 4, 5)
        self.tabel_kalkulator.attach(self.tombol_titik, 1, 2, 4, 5)
        self.tabel_kalkulator.attach(self.tombol_sama_dengan, 2, 3, 4, 5)
        self.tabel_kalkulator.attach(self.tombol_tambah, 3, 4, 4, 5)

        self.tabel_kalkulator.attach(self.tombol_radians, 0, 1, 5, 6)
        self.tabel_kalkulator.attach(self.tombol_e, 1, 2, 5, 6)
        self.tabel_kalkulator.attach(self.tombol_log, 2, 3, 5, 6)
        self.tabel_kalkulator.attach(self.tombol_log10, 3, 4, 5, 6)

        self.tabel_kalkulator.attach(self.tombol_degrees, 0, 1, 6, 7)
        self.tabel_kalkulator.attach(self.tombol_pi, 1, 2, 6, 7)
        self.tabel_kalkulator.attach(self.tombol_sinh, 2, 3, 6, 7)
        self.tabel_kalkulator.attach(self.tombol_cosh, 3, 4, 6, 7)

        self.tabel_kalkulator.attach(self.tombol_tanh, 0, 1, 7, 8)
        self.tabel_kalkulator.attach(self.tombol_sqrt, 1, 2, 7, 8)
        self.tabel_kalkulator.attach(self.tombol_asin, 2, 3, 7, 8)
        self.tabel_kalkulator.attach(self.tombol_acos, 3, 4, 7, 8)
        
        self.tabel_kalkulator.attach(self.tombol_atan, 0, 1, 8, 9)
        self.tabel_kalkulator.attach(self.tombol_sin, 1, 2, 8, 9)
        self.tabel_kalkulator.attach(self.tombol_cos, 2, 3, 8, 9)
        self.tabel_kalkulator.attach(self.tombol_tan, 3, 4, 8, 9)        

    def kotak(self):
        self.kotak_vertikal = Gtk.VBox(spacing = 5)
        
        self.kotak_horizontal_1 = Gtk.HBox(spacing = 10)
        self.kotak_horizontal_1.pack_start(self.papan_menu, True, True, 0)
        
        self.kotak_horizontal_2 = Gtk.HBox(spacing = 10)
        self.kotak_horizontal_2.pack_start(self.masukan_data, True, True, 0)

        self.kotak_horizontal_3 = Gtk.HBox(spacing = 10)
        self.kotak_horizontal_3.pack_start(self.tabel_kalkulator, True, True, 0)

        self.kotak_vertikal.pack_start(self.kotak_horizontal_1, True, True, 0)
        self.kotak_vertikal.pack_start(self.kotak_horizontal_2, True, True, 0)
        self.kotak_vertikal.pack_start(self.kotak_horizontal_3, True, True, 0)

        self.jendela.add(self.kotak_vertikal)

    def konek(self):
        self.keluar.connect("activate", Gtk.main_quit)
        self.keterangan.connect("activate", self.ihwal)
        
        self.tombol_tutup.connect("clicked", self.panggilan_keluar)
        self.jendela.connect("destroy", self.panggilan_keluar)
        
        self.tombol_satu.connect("clicked", self.klik, "1")    
        self.tombol_dua.connect("clicked", self.klik, "2")
        self.tombol_tiga.connect("clicked", self.klik, "3")
        self.tombol_empat.connect("clicked", self.klik, "4")
        self.tombol_lima.connect("clicked", self.klik, "5")

        self.tombol_enam.connect("clicked", self.klik, "6")
        self.tombol_tujuh.connect("clicked", self.klik, "7")
        self.tombol_delapan.connect("clicked", self.klik, "8")
        self.tombol_sembilan.connect("clicked", self.klik, "9")
        self.tombol_nol.connect("clicked", self.klik, "0")
        self.tombol_titik.connect("clicked", self.klik, ".")
        
        self.tombol_kurung_tutup.connect("clicked", self.klik, ")")
        self.tombol_kurung_buka.connect("clicked", self.klik, "(")

        self.tombol_hapus.connect("clicked", self.klik, "CE")
        self.tombol_sama_dengan.connect("clicked", self.klik, "=")

        self.tombol_kali.connect("clicked", self.klik, "*")
        self.tombol_bagi.connect("clicked", self.klik, "/")
        self.tombol_tambah.connect("clicked", self.klik, "+")
        self.tombol_kurang.connect("clicked", self.klik, "-")

        self.tombol_sin.connect("clicked", self.klik, "sin(")
        self.tombol_cos.connect("clicked", self.klik, "cos(")
        self.tombol_tan.connect("clicked", self.klik, "tan(")
        self.tombol_atan.connect("clicked", self.klik, "atan(")

        self.tombol_tanh.connect("clicked", self.klik, "tanh(")
        self.tombol_sqrt.connect("clicked", self.klik, "sqrt(") 
        self.tombol_asin.connect("clicked", self.klik, "asin(") 
        self.tombol_acos.connect("clicked", self.klik, "acos(")

        self.tombol_degrees.connect("clicked", self.klik, "degrees(")
        self.tombol_pi.connect("clicked", self.klik, "pi")
        self.tombol_sinh.connect("clicked", self.klik, "sinh(")
        self.tombol_cosh.connect("clicked", self.klik, "cosh(")

        self.tombol_radians.connect("clicked", self.klik,"radians(")
        self.tombol_e.connect("clicked", self.klik,"e")
        self.tombol_log.connect("clicked", self.klik, "log(")
        self.tombol_log10.connect("clicked", self.klik, "log10(")

    def klik(self, a, b):
        if b == "=":
            self.tanda = False
            x = "self.x=" + self.masukan_data.get_text()
            exec(x)
        elif b == "CE":
            self.masukan_data.set_text("")
            self.tanda = False
            self.hapus = True
            self.x = None
        else:
            self.tanda = True
            self.hapus = False
            
        if self.tanda:
            if not self.x:
                self.x = b
            else:
                self.x = self.x + b
                
        if not self.hapus:
            self.masukan_data.set_text(str(self.x))
            self.x == None

        if b == "=":
            self.x = self.masukan_data.get_text()
      
    def ihwal(self, a):
        self.tentang = Gtk.AboutDialog()
        self.tentang.set_program_name("Kalkulator Sains UVT")
        self.tentang.set_version("0.2")
        self.tentang.set_license(license)
        self.tentang.set_copyright("(c) 2014 UVT")
        self.tentang.set_authors(authors)
        self.tentang.set_comments("Kalkulator Saintifik")
        self.tentang.set_website("http://uvt.web.id")
        self.tentang.set_logo(GdkPixbuf.Pixbuf.new_from_file("/usr/share/kalkuluvtsains/gambar/kalkulatorsains.png"))
        self.tentang.run()
        self.tentang.destroy()

    def panggilan_keluar(self, a):
        Gtk.main_quit()

if __name__ == "__main__":
    Kalkulator()
    Gtk.main()
