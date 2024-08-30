# writed by ernakkc on 31/07/2024
# This is the main file of the project

import os
import sys
import ssl
import certifi
import sqlite3
import feedparser
import webbrowser
from time import sleep
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from selenium import webdriver
from PyQt5.QtGui import QIcon
import google.generativeai as genai
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

HABERLER = {
    'NTV'       : ["https://www.ntv.com.tr/gundem.rss","https://www.ntv.com.tr/dunya-kupasi-2018.rss","https://www.ntv.com.tr/turkiye.rss","https://www.ntv.com.tr/dunya.rss","https://www.ntv.com.tr/ekonomi.rss","https://www.ntv.com.tr/spor.rss","https://www.ntv.com.tr/teknoloji.rss","https://www.ntv.com.tr/yasam.rss","https://www.ntv.com.tr/seyahat.rss","https://www.ntv.com.tr/saglik.rss","https://www.ntv.com.tr/sanat.rss","https://www.ntv.com.tr/otomobil.rss","https://www.ntv.com.tr/egitim.rss"],
    "Cumhuriyet": ["http://www.cumhuriyet.com.tr/rss/son_dakika.xml","http://www.cumhuriyet.com.tr/rss/6.xml","http://www.cumhuriyet.com.tr/rss/17.xml","http://www.cumhuriyet.com.tr/rss/73.xml","http://www.cumhuriyet.com.tr/rss/24.xml","http://www.cumhuriyet.com.tr/rss/32.xml","http://www.cumhuriyet.com.tr/rss/33.xml","http://www.cumhuriyet.com.tr/rss/34.xml","http://www.cumhuriyet.com.tr/rss/35.xml","http://www.cumhuriyet.com.tr/rss/36.xml","http://www.cumhuriyet.com.tr/rss/46.xml","http://www.cumhuriyet.com.tr/rss/70.xml","http://www.cumhuriyet.com.tr/rss/19.xml","http://www.cumhuriyet.com.tr/rss/7.xml","http://www.cumhuriyet.com.tr/rss/14.xml","http://www.cumhuriyet.com.tr/rss/15.xml","http://www.cumhuriyet.com.tr/rss/16.xml","http://www.cumhuriyet.com.tr/rss/20.xml","http://www.cumhuriyet.com.tr/rss/72.xml","http://www.cumhuriyet.com.tr/rss/12.xml","http://www.cumhuriyet.com.tr/rss/3.xml","http://www.cumhuriyet.com.tr/rss/9.xml","http://www.cumhuriyet.com.tr/rss/11.xml","http://www.cumhuriyet.com.tr/rss/10.xml"],
    "Dünya"     : "https://www.dunya.com/rss?dunya",
    'CNN Türk'  : 'https://www.cnnturk.com/feed/rss/news',
    'Hürriyet'  : ["http://www.hurriyet.com.tr/rss/anasayfa","http://www.hurriyet.com.tr/rss/gundem","http://www.hurriyet.com.tr/rss/ekonomi","http://www.hurriyet.com.tr/rss/magazin","http://www.hurriyet.com.tr/rss/spor","http://www.hurriyet.com.tr/rss/dunya","http://www.hurriyet.com.tr/rss/teknoloji","http://www.hurriyet.com.tr/rss/saglik","http://www.hurriyet.com.tr/rss/astroloji"],
    'Milliyet'  : ["http://www.milliyet.com.tr/rss/rssNew/magazinRss.xml","http://www.milliyet.com.tr/rss/rssNew/gundemRss.xml"	,"http://www.milliyet.com.tr/rss/rssNew/kitapRss.xml","http://www.milliyet.com.tr/rss/rssNew/egitimRss.xml","http://www.milliyet.com.tr/rss/rssNew/dunyaRss.xml","http://www.milliyet.com.tr/rss/rssNew/ekonomiRss.xml","http://www.milliyet.com.tr/rss/rssNew/siyasetRss.xml","http://www.milliyet.com.tr/rss/rssNew/otomobilRss.xml","http://www.milliyet.com.tr/rss/rssNew/teknolojiRss.xml","http://www.milliyet.com.tr/rss/rssNew/milliyettatilRss.xml","http://www.milliyet.com.tr/rss/rssNew/teknolojiRss.xml","http://www.milliyet.com.tr/rss/rssNew/konutemlakRss.xml","http://www.milliyet.com.tr/rss/rssNew/aileRss.xml","http://www.milliyet.com.tr/rss/rssNew/saglikRss.xml","http://www.milliyet.com.tr/rss/rssNew/yemekRss.xml","http://www.milliyet.com.tr/rss/rssNew/diyetRss.xml","http://www.milliyet.com.tr/rss/rssNew/SonDakikaRss.xml"],
    'Sözcü'     : 'https://www.sozcu.com.tr/feeds-haberler',
    'Sabah'     : ["https://www.sabah.com.tr/rss/ekonomi.xml","https://www.sabah.com.tr/rss/spor.xml","https://www.sabah.com.tr/rss/gundem.xml","https://www.sabah.com.tr/rss/yasam.xml","https://www.sabah.com.tr/rss/dunya.xml","https://www.sabah.com.tr/rss/teknoloji.xml","https://www.sabah.com.tr/rss/turizm.xml","https://www.sabah.com.tr/rss/otomobil.xml","https://www.sabah.com.tr/rss/anasayfa.xml","https://www.sabah.com.tr/rss/saglik.xml","https://www.sabah.com.tr/rss/gununicinden.xml","https://www.sabah.com.tr/rss/sondakika.xml","https://www.sabah.com.tr/rss/galatasaray.xml","https://www.sabah.com.tr/rss/fenerbahce.xml","https://www.sabah.com.tr/rss/besiktas.xml","https://www.sabah.com.tr/rss/trabzonspor.xml","https://www.sabah.com.tr/rss/bursaspor.xml","https://www.sabah.com.tr/rss/kultur-sanat.xml","https://www.sabah.com.tr/rss/oyun.xml","https://www.sabah.com.tr/rss/adana.xml"],
    'Habertürk' : 'https://www.haberturk.com/rss',
    'T24'       : 'https://t24.com.tr/rss',
    'Yeni Şafak': 'https://www.yenisafak.com/rss',
    "Star"      : ["http://www.star.com.tr/rss/rss.asp","http://www.star.com.tr/rss/rss.asp?cid=500","http://www.star.com.tr/rss/rss.asp?cid=13","http://www.star.com.tr/rss/rss.asp?cid=15","http://www.star.com.tr/rss/rss.asp?cid=16","http://www.star.com.tr/rss/rss.asp?cid=17","http://www.star.com.tr/rss/rss.asp?cid=19","http://www.star.com.tr/rss/rss.asp?cid=125","http://www.star.com.tr/rss/rss.asp?cid=223","http://www.star.com.tr/rss/rss.asp?cid=130","http://www.star.com.tr/rss/rss.asp?cid=170"],
    "Takvim"    : ["https://www.takvim.com.tr/rss/anasayfa","https://www.takvim.com.tr/rss/son24saat","https://www.takvim.com.tr/rss/guncel","https://www.takvim.com.tr/rss/ekonomi","https://www.takvim.com.tr/rss/otomobil","https://www.takvim.com.tr/rss/saklambac","https://www.takvim.com.tr/rss/spor","https://www.takvim.com.tr/rss/yasam","https://www.takvim.com.tr/rss/video","https://www.takvim.com.tr/rss/televizyon"],
    "Türkiye'nin Gazetesi" : "http://www.turkiyegazetesi.com.tr/rss/rss.xml",
    "Yeni Asır" : "http://www.yeniasir.com.tr/rss/anasayfa.xml",
    "Türkiye Haber Ajansı" : "http://www.turkiyehaberajansi.com/rss.xml"


}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        gemini_api_key = "AIzaSyCdu0wQPtqzA4KOgs8r6Q70qjwAalsv9gQ"
        genai.configure(api_key=gemini_api_key)
        self.ai = genai.GenerativeModel('gemini-1.5-flash')
        
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-web-security")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
        self.options.add_argument("--user-data-dir={}".format(os.path.abspath("web_data")))
        self.driver = webdriver.Edge(options=self.options)


        self.setWindowTitle("Haberler")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(100, 100, 600, 500)


        self.menubar = self.menuBar()
        self.iletisim_menu = self.menubar.addMenu("İletişim")
        self.iletisim_menu.addAction("Web Site")
        self.iletisim_menu.addAction("GitHub")
        self.iletisim_menu.addAction("Mail")
        self.iletisim_menu.addAction("Instagram")
    
        self.iletisim_menu.triggered.connect(self.sosyal_medya_func)
        
        
        


        layout = QHBoxLayout()

        layout_sol = QVBoxLayout()
        layout_sag = QVBoxLayout()
        
        layout_sol.setAlignment(Qt.AlignCenter)
        layout_sag.setAlignment(Qt.AlignCenter)
        
        
        
        layout_sol.setSpacing(5)
        layout_sag.setSpacing(5)

        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
            
        if os.path.exists("haberler.db"):
            # Uyarı ile Veritabanı varsa kullanıcıya silinsin mi üstüne eklensin mi diye sor
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText("Veritabanı bulundu. Silinsin mi?")
            msg.setWindowTitle("Veritabanı Bulundu")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            
            if msg.exec() == QMessageBox.Yes:
                os.remove("haberler.db")
                self.connection = sqlite3.connect("haberler.db")
                self.cursor = self.connection.cursor()
        else:
            self.connection = sqlite3.connect("haberler.db")
            self.cursor = self.connection.cursor()

        self.haber_list = []

        self.baslik_cek = QLabel("HABERİ ÇEK")
        self.baslik_cek.setAlignment(Qt.AlignCenter)
        self.baslik_cek.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.baslik_cek.setFixedWidth(300)
        self.baslik_cek.setFixedHeight(50)
        layout_sol.addWidget(self.baslik_cek)

        self.ekran = QLabel()
        self.ekran.setStyleSheet("font-size: 11px; border: 1px solid black; padding: 10px;")
        self.ekran.setWordWrap(True)
        self.ekran.setText("HABER ÇEKMEK İÇİN HABER SİTELERİNİ SEÇİN VE HABERLERİ ÇEK'E TIKLAYIN.  \n\n" )
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.ekran)
        scroll_area.setWidgetResizable(True)  
        scroll_area.setFixedHeight(200)       
        scroll_area.setFixedWidth(400)        
        layout_sol.addWidget(scroll_area)


        ilk_sekiz = QVBoxLayout()
        ilk_sekiz.setAlignment(Qt.AlignTop)
        ilk_sekiz.setSpacing(5)
        
        self.ntv_check = QCheckBox("NTV")
        ilk_sekiz.addWidget(self.ntv_check)
        self.haber_list.append(self.ntv_check)
        
        self.cumhuriyet_check = QCheckBox("Cumhuriyet")
        ilk_sekiz.addWidget(self.cumhuriyet_check)
        self.haber_list.append(self.cumhuriyet_check)
        
        self.dunya_check = QCheckBox("Dünya")
        ilk_sekiz.addWidget(self.dunya_check)
        self.haber_list.append(self.dunya_check)
        
        self.cnnturk_check = QCheckBox("CNN Türk")
        ilk_sekiz.addWidget(self.cnnturk_check)
        self.haber_list.append(self.cnnturk_check)
        
        self.hurriyet_check = QCheckBox("Hürriyet")
        ilk_sekiz.addWidget(self.hurriyet_check)
        self.haber_list.append(self.hurriyet_check)
        
        self.milliyet_check = QCheckBox("Milliyet")
        ilk_sekiz.addWidget(self.milliyet_check)
        self.haber_list.append(self.milliyet_check)
        
        self.sozcu_check = QCheckBox("Sözcü")
        ilk_sekiz.addWidget(self.sozcu_check)
        self.haber_list.append(self.sozcu_check)
        
        self.sabah_check = QCheckBox("Sabah")
        ilk_sekiz.addWidget(self.sabah_check)
        self.haber_list.append(self.sabah_check)
        
        
        son_sekiz = QVBoxLayout()
        son_sekiz.setAlignment(Qt.AlignTop)
        son_sekiz.setSpacing(5)        
        
        self.haberturk_check = QCheckBox("Habertürk")
        son_sekiz.addWidget(self.haberturk_check)
        self.haber_list.append(self.haberturk_check)
        
        self.t24_check = QCheckBox("T24")
        son_sekiz.addWidget(self.t24_check)
        self.haber_list.append(self.t24_check)
        
        self.yenisafak_check = QCheckBox("Yeni Şafak")
        son_sekiz.addWidget(self.yenisafak_check)
        self.haber_list.append(self.yenisafak_check)
        
        self.star_check = QCheckBox("Star")
        son_sekiz.addWidget(self.star_check)
        self.haber_list.append(self.star_check)
        
        self.takvim_check = QCheckBox("Takvim")
        son_sekiz.addWidget(self.takvim_check)
        self.haber_list.append(self.takvim_check)
        
        self.turkiyegazetesi_check = QCheckBox("Türkiye'nin Gazetesi")
        son_sekiz.addWidget(self.turkiyegazetesi_check)
        self.haber_list.append(self.turkiyegazetesi_check)
        
        self.yeniasir_check = QCheckBox("Yeni Asır")
        son_sekiz.addWidget(self.yeniasir_check)
        self.haber_list.append(self.yeniasir_check)
        
        self.turkiyehaberajansi_check = QCheckBox("Türkiye Haber Ajansı")
        son_sekiz.addWidget(self.turkiyehaberajansi_check)
        self.haber_list.append(self.turkiyehaberajansi_check)
    
        sol_topla = QHBoxLayout()
        sol_topla.addLayout(ilk_sekiz)
        sol_topla.addLayout(son_sekiz)
        
        layout_sol.addLayout(sol_topla)

        self.button = QPushButton("Haberleri Çek")
        self.button.setFixedWidth(130)
        self.button.setFixedHeight(40)
        self.button.setStyleSheet("font-size: 15px; font-weight: bold;")
        self.button.clicked.connect(self.get_news)
        layout_sol.addWidget(self.button, alignment=Qt.AlignCenter)   
        
        
        self.baslik = QLabel("HABERİ PAYLAŞ")
        self.baslik.setAlignment(Qt.AlignCenter)
        self.baslik.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.baslik.setFixedWidth(300)
        self.baslik.setFixedHeight(50)
        layout_sag.addWidget(self.baslik)
        
        self.ekran2 = QLabel()
        self.ekran2.setStyleSheet("font-size: 11px; border: 1px solid black; padding: 10px;")
        self.ekran2.setWordWrap(True)
        self.ekran2.setText("Database'deki içeriği taramak için İÇERİĞİ TARA butonuna basınız. " )
        scroll_area1 = QScrollArea()
        scroll_area1.setWidget(self.ekran2)
        scroll_area1.setWidgetResizable(True)  
        scroll_area1.setFixedHeight(200)       
        scroll_area1.setFixedWidth(400)        
        layout_sag.addWidget(scroll_area1)
        
        self.icerigi_tara = QPushButton("İÇERİĞİ TARA")
        self.icerigi_tara.clicked.connect(self.tara)
        layout_sag.addWidget(self.icerigi_tara, alignment=Qt.AlignCenter)
        
        self.izle = QCheckBox("Paylaşımı izlemek istiyorum.")
        layout_sag.addWidget(self.izle, alignment=Qt.AlignCenter)
        
        gecikme_layout = QHBoxLayout()
        gecikme_layout.setAlignment(Qt.AlignCenter)
        
        self.gecikme = QSpinBox()
        self.gecikme.setRange(0, 60)
        self.gecikme.setValue(5)
        self.gecikme.setSuffix(" saniye")
        gecikme_layout.addWidget(self.gecikme)
        
        self.gecikme_label = QLabel("Paylaşım aralığı")
        gecikme_layout.addWidget(self.gecikme_label)
        
        layout_sag.addLayout(gecikme_layout)
        
        layout_sag.addWidget(self.izle)
        
        
        self.paylas = QPushButton("PAYLAŞ")
        self.paylas.setEnabled(False)
        self.paylas.clicked.connect(self.paylas_func)
        layout_sag.addWidget(self.paylas, alignment=Qt.AlignCenter)
        
        
        
        layout.addLayout(layout_sol)
        layout.addLayout(layout_sag)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def get_news(self):
        self.ekran.clear()
        self.ekran.setText(f"{self.ekran.text()}\nHaberler çekiliyor...")

        cekilecek = []
        for haber in self.haber_list:
            haber.setEnabled(False)
            if haber.isChecked():
                cekilecek.append(haber.text())
                
        for haber in cekilecek:
            source = haber
            url = HABERLER[haber]
            self.ekran.setText(f"{self.ekran.text()}\n-> {source} <- Sitesinin haberleri çekiliyor.")
            
            if source == "NTV":
                hbr_cnt = 0
                for url in HABERLER['NTV']:
                    feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                    for entry in feed.entries:
                        self.cursor.execute("CREATE TABLE IF NOT EXISTS ntv (title TEXT, link TEXT, published TEXT, summary TEXT)")
                        self.cursor.execute("SELECT COUNT(*) FROM ntv WHERE title = ?", (entry.title,))
                        if self.cursor.fetchone()[0] == 0:
                            self.cursor.execute("INSERT INTO ntv (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                            self.connection.commit()
                        hbr_cnt += 1
                self.ekran.setText(f"{self.ekran.text()}\n\nNTV haberleri çekildi.\nHaber sayısı: " + str(hbr_cnt))
                
            if source == "Cumhuriyet":
                hbr_cnt = 0
                for url in HABERLER['Cumhuriyet']:
                    feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                    for entry in feed.entries:
                        self.cursor.execute("CREATE TABLE IF NOT EXISTS cumhuriyet (title TEXT, link TEXT, published TEXT, summary TEXT)")
                        self.cursor.execute("SELECT COUNT(*) FROM cumhuriyet WHERE title = ?", (entry.title,))
                        if self.cursor.fetchone()[0] == 0:
                            self.cursor.execute("INSERT INTO cumhuriyet (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                            self.connection.commit()
                        hbr_cnt += 1
                self.ekran.setText(f"{self.ekran.text()}\n\nCumhuriyet haberleri çekildi.\nHaber sayısı: " + str(hbr_cnt))
            
            elif source == "Dünya":
                feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                for entry in feed.entries:
                    self.cursor.execute("CREATE TABLE IF NOT EXISTS dunya (title TEXT, link TEXT, published TEXT, summary TEXT)")
                    self.cursor.execute("SELECT COUNT(*) FROM dunya WHERE title = ?", (entry.title,))
                    if self.cursor.fetchone()[0] == 0:
                        self.cursor.execute("INSERT INTO dunya (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                        self.connection.commit()
                self.ekran.setText(f"{self.ekran.text()}\n\nDünya haberleri çekildi.\nHaber sayısı: " + str(len(feed.entries)))
            
            elif source == "CNN Türk":
                feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                for entry in feed.entries:
                    self.cursor.execute("CREATE TABLE IF NOT EXISTS cnnturk (title TEXT, link TEXT, published TEXT, summary TEXT)")
                    self.cursor.execute("SELECT COUNT(*) FROM cnnturk WHERE title = ?", (entry.title,))
                    if self.cursor.fetchone()[0] == 0:
                        self.cursor.execute("INSERT INTO cnnturk (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                        self.connection.commit()
                self.ekran.setText(f"{self.ekran.text()}\n\nCNN Türk haberleri çekildi.\nHaber sayısı: " + str(len(feed.entries)))
            
            elif source == "Hürriyet":
                hbr_cnt = 0
                for url in HABERLER['Hürriyet']:
                    feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                    for entry in feed.entries:
                        self.cursor.execute("CREATE TABLE IF NOT EXISTS hurriyet (title TEXT, link TEXT, published TEXT, summary TEXT)")
                        self.cursor.execute("SELECT COUNT(*) FROM hurriyet WHERE title = ?", (entry.title,))
                        if self.cursor.fetchone()[0] == 0:
                            self.cursor.execute("INSERT INTO hurriyet (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                            self.connection.commit()
                        hbr_cnt += 1
                self.ekran.setText(f"{self.ekran.text()}\n\nHürriyet haberleri çekildi.\nHaber sayısı: " + str(hbr_cnt))
                
            elif source == "Milliyet":
                hbr_cnt = 0
                for url in HABERLER['Milliyet']:
                    feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                    for entry in feed.entries:
                        self.cursor.execute("CREATE TABLE IF NOT EXISTS milliyet (title TEXT, link TEXT, published TEXT, summary TEXT)")
                        self.cursor.execute("SELECT COUNT(*) FROM milliyet WHERE title = ?", (entry.title,))
                        if self.cursor.fetchone()[0] == 0:
                            self.cursor.execute("INSERT INTO milliyet (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                            self.connection.commit()
                        hbr_cnt += 1
                self.ekran.setText(f"{self.ekran.text()}\n\nMilliyet haberleri çekildi.\nHaber sayısı: " + str(hbr_cnt))
                
            elif source == "Sözcü":
                feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                for entry in feed.entries:
                    self.cursor.execute("CREATE TABLE IF NOT EXISTS sozcu (title TEXT, link TEXT, published TEXT, summary TEXT)")
                    self.cursor.execute("SELECT COUNT(*) FROM sozcu WHERE title = ?", (entry.title,))
                    if self.cursor.fetchone()[0] == 0:
                        self.cursor.execute("INSERT INTO sozcu (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                        self.connection.commit()
                self.ekran.setText(f"{self.ekran.text()}\n\nSözcü haberleri çekildi.\nHaber sayısı: " + str(len(feed.entries)))

            elif source == "Sabah":
                hbr_cnt = 0
                for url in HABERLER['Sabah']:
                    feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                    for entry in feed.entries:
                        self.cursor.execute("CREATE TABLE IF NOT EXISTS sabah (title TEXT, link TEXT, published TEXT, summary TEXT)")
                        self.cursor.execute("SELECT COUNT(*) FROM sabah WHERE title = ?", (entry.title,))
                        if self.cursor.fetchone()[0] == 0:
                            self.cursor.execute("INSERT INTO sabah (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                            self.connection.commit()
                        hbr_cnt += 1
                self.ekran.setText(f"{self.ekran.text()}\n\nSabah haberleri çekildi.\nHaber sayısı: " + str(hbr_cnt))
                
            elif source == "Habertürk":
                feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                for entry in feed.entries:
                    self.cursor.execute("CREATE TABLE IF NOT EXISTS haberturk (title TEXT, link TEXT, published TEXT, summary TEXT)")
                    self.cursor.execute("SELECT COUNT(*) FROM haberturk WHERE title = ?", (entry.title,))
                    if self.cursor.fetchone()[0] == 0:
                        self.cursor.execute("INSERT INTO haberturk (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                        self.connection.commit()
                self.ekran.setText(f"{self.ekran.text()}\n\nHabertürk haberleri çekildi.\nHaber sayısı: " + str(len(feed.entries)))
                
            elif source == "T24":
                feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                for entry in feed.entries:
                    entry.summary = entry.title
                    self.cursor.execute("CREATE TABLE IF NOT EXISTS t24 (title TEXT, link TEXT, published TEXT, summary TEXT)")
                    self.cursor.execute("SELECT COUNT(*) FROM t24 WHERE title = ?", (entry.title,))
                    if self.cursor.fetchone()[0] == 0:
                        self.cursor.execute("INSERT INTO t24 (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                        self.connection.commit()
                self.ekran.setText(f"{self.ekran.text()}\n\nT24 haberleri çekildi.\nHaber sayısı: " + str(len(feed.entries)))
                
            elif source == "Yeni Şafak":
                feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                for entry in feed.entries:
                    self.cursor.execute("CREATE TABLE IF NOT EXISTS yenisafak (title TEXT, link TEXT, published TEXT, summary TEXT)")
                    self.cursor.execute("SELECT COUNT(*) FROM yenisafak WHERE title = ?", (entry.title,))
                    if self.cursor.fetchone()[0] == 0:
                        self.cursor.execute("INSERT INTO yenisafak (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                        self.connection.commit()
                self.ekran.setText(f"{self.ekran.text()}\n\nYeni Şafak haberleri çekildi.\nHaber sayısı: " + str(len(feed.entries)))
                
            elif source == "Star":
                hbr_cnt = 0
                for url in HABERLER['Star']:
                    feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                    for entry in feed.entries:
                        self.cursor.execute("CREATE TABLE IF NOT EXISTS star (title TEXT, link TEXT, published TEXT, summary TEXT)")
                        self.cursor.execute("SELECT COUNT(*) FROM star WHERE title = ?", (entry.title,))
                        if self.cursor.fetchone()[0] == 0:
                            self.cursor.execute("INSERT INTO star (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                            self.connection.commit()
                        hbr_cnt += 1
                self.ekran.setText(f"{self.ekran.text()}\n\nStar haberleri çekildi.\nHaber sayısı: " + str(hbr_cnt))
                    
            elif source == "Takvim":
                hbr_cnt = 0
                for url in HABERLER['Takvim']:
                    feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                    for entry in feed.entries:
                        self.cursor.execute("CREATE TABLE IF NOT EXISTS takvim (title TEXT, link TEXT, published TEXT, summary TEXT)")
                        self.cursor.execute("SELECT COUNT(*) FROM takvim WHERE title = ?", (entry.title,))
                        if self.cursor.fetchone()[0] == 0:
                            self.cursor.execute("INSERT INTO takvim (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                            self.connection.commit()
                        hbr_cnt += 1
                self.ekran.setText(f"{self.ekran.text()}\n\nTakvim haberleri çekildi.\nHaber sayısı: " + str(hbr_cnt))
        
            elif source == "Türkiye'nin Gazetesi":
                feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                for entry in feed.entries:
                    self.cursor.execute("CREATE TABLE IF NOT EXISTS turkiyegazetesi (title TEXT, link TEXT, published TEXT, summary TEXT)")
                    self.cursor.execute("SELECT COUNT(*) FROM turkiyegazetesi WHERE title = ?", (entry.title,))
                    if self.cursor.fetchone()[0] == 0:
                        self.cursor.execute("INSERT INTO turkiyegazetesi (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                        self.connection.commit()
                self.ekran.setText(f"{self.ekran.text()}\n\nTürkiye'nin Gazetesi haberleri çekildi.\nHaber sayısı: " + str(len(feed.entries)))
        
            elif source == "Yeni Asır":
                feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                for entry in feed.entries:
                    self.cursor.execute("CREATE TABLE IF NOT EXISTS yeniasir (title TEXT, link TEXT, published TEXT, summary TEXT)")
                    self.cursor.execute("SELECT COUNT(*) FROM yeniasir WHERE title = ?", (entry.title,))
                    if self.cursor.fetchone()[0] == 0:
                        self.cursor.execute("INSERT INTO yeniasir (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                        self.connection.commit()
                self.ekran.setText(f"{self.ekran.text()}\n\nYeni Asır haberleri çekildi.\nHaber sayısı: " + str(len(feed.entries)))
                
            elif source == "Türkiye Haber Ajansı":
                feed = feedparser.parse(url,  request_headers={'User-Agent': 'Mozilla/5.0'})
                for entry in feed.entries:
                    self.cursor.execute("CREATE TABLE IF NOT EXISTS turkiyehaberajansi (title TEXT, link TEXT, published TEXT, summary TEXT)")
                    self.cursor.execute("SELECT COUNT(*) FROM turkiyehaberajansi WHERE title = ?", (entry.title,))
                    if self.cursor.fetchone()[0] == 0:
                        self.cursor.execute("INSERT INTO turkiyehaberajansi (title, link, published, summary) VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, entry.summary))
                        self.connection.commit()
                self.ekran.setText(f"{self.ekran.text()}\n\nTürkiye Haber Ajansı haberleri çekildi.\nHaber sayısı: " + str(len(feed.entries)))
        
        self.ekran.setText(f"{self.ekran.text()}\n\nHaberler çekildi.\n\n")
        for haber in self.haber_list:
            haber.setEnabled(True)
        
        
        
    def tara(self):
        # bulunduğu dizindeki sonu .db olan dosyaları tarasın
        self.total_haber = 0
        databaseler = os.listdir()
        if databaseler:
            for db in databaseler:
                if db == "haberler.db":
                    self.connection = sqlite3.connect(db)
                    self.cursor = self.connection.cursor()
                    self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                    tables = self.cursor.fetchall()
                    for table in tables:
                        self.cursor.execute(f"SELECT * FROM {table[0]}")
                        data = self.cursor.fetchall()
                        self.ekran2.setText(f"{self.ekran2.text()}\n{table[0]} tablosundaki veri sayısı: {len(data)}")
                        self.ekran2.setText(f"{self.ekran2.text()}\nTablo adı: {table[0]}")
                        self.ekran2.setText(f"{self.ekran2.text()}\n")
                        self.total_haber += len(data)
        self.paylas.setEnabled(True)
                        
    def paylas_func(self):
        self.paylas.setEnabled(False)
        gecikme = self.gecikme.value()
        izle = self.izle.isChecked()
        
        self.gecikme.setEnabled(False)
        self.izle.setEnabled(False)
        
        self.ekran2.setText(f"{self.ekran2.text()}\n\nPaylaşım başlatıldı.\nPaylaşım aralığı: {gecikme} saniye")
    
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Haberlerin tamamını paylaşmak istiyor musunuz?")
        msg.setWindowTitle("PAYLAŞ")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.Yes)
            
        if msg.exec() == QMessageBox.Yes:
            num = self.total_haber
        else:
            num,ok = QInputDialog.getInt(self,"integer input dualog","Paylaşmak istediğiniz haber sayısını giriniz")      
            if ok:
                if num <= self.total_haber:
                    pass
            else:
                num = self.total_haber 
        self.paylasilan = 0
        
        self.ekran2.setText(f"{self.ekran2.text()}\n\nToplam haber sayısı: {self.total_haber}\nPaylaşılacak haber sayısı: {num}\n\nPaylaşılıyor...\nPaylaşılan haber sayısı: {self.paylasilan}")
            
        self.haberler = []
        self.connection = sqlite3.connect("haberler.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        for table in tables:
            self.cursor.execute(f"SELECT * FROM {table[0]}")
            data = self.cursor.fetchall()
            for haber in data:
                self.haberler.append(haber)
           
        if izle:
            self.options = Options()
            self.options.add_argument("--disable-notifications")
            self.options.add_argument("--disable-popup-blocking")
            self.options.add_argument("--disable-infobars")
            self.options.add_argument("--disable-extensions")
            self.options.add_argument("--disable-web-security")
            self.options.add_argument("--disable-blink-features=AutomationControlled")
            self.options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
            self.options.add_argument("--user-data-dir={}".format(os.path.abspath("web_data")))
            self.driver = webdriver.Edge(options=self.options)
        
        self.driver.get(r"https://www.cnnturkiye.com.tr/wp-login.php?redirect_to=https%3A%2F%2Fwww.cnnturkiye.com.tr%2Fwp-admin%2F&reauth=1 ")
        
        
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "user_login"))).send_keys("admin")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "user_pass"))).send_keys("Meseli3363+")
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "wp-submit"))).click()
                
        for haber in self.haberler:
            prompt = f"Sana verdiğim haber metinini özgün cümlelerle tekrar yazıp html koduna çevir ve sadece çıktı olarak html verisini bana gönder. Türkçe karakterler var UTF-8 şeklinde olması gerektiğine dikkat et. \n\nBaşlık: {haber[0]}\n\nLink: {haber[1]}\n\nTarih: {haber[2]}\n\nÖzet: {haber[3]}"
            req = self.ai.generate_content(prompt)
            req = req.text.replace("```","")
            
            self.driver.get("https://www.cnnturkiye.com.tr/wp-admin/post-new.php")
            
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "title"))).send_keys(haber[0])
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "content"))).send_keys(req)
            # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "set-post-thumbnail"))).click()
            # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "__wp-uploader-id-1"))).click()
            # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPath("//input[@type='file']"))).send_keys(")
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "publish"))).submit()
            
            sleep(gecikme)
            self.paylasilan += 1
            self.ekran2.setText(f"{self.ekran2.text().split('Paylaşılan haber sayısı:')[0]}Paylaşılan haber sayısı: {self.paylasilan}")
            if self.paylasilan == num: break
        
        self.ekran2.setText(f"{self.ekran2.text()}\n\nHaberler paylaşıldı.")
        self.gecikme.setEnabled(True)
        self.izle.setEnabled(True)
        self.paylas.setEnabled(True)
        
    def sosyal_medya_func(self, action):
        if action.text() == "Web Site":
            webbrowser.open("https://ernakkc.online")
        elif action.text() == "GitHub":
            webbrowser.open("https://github.com/ernakkc")
        elif action.text() == "Mail":
            webbrowser.open("mailto:ern.akkc@gmail.com")
        elif action.text() == "Instagram":
            webbrowser.open("https://www.instagram.com/ern.akkc/")
    
    
    
if not os.path.exists("web_data"):
    os.makedirs("web_data")     

app = QApplication(sys.argv)
app.setWindowIcon(QIcon('icon.ico'))
window = MainWindow()
window.show()
sys.exit(app.exec_())