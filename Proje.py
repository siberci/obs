from tkinter import *
from tkinter import ttk
import pypyodbc
import os
from tkinter import messagebox


class Student:
    def __init__(self, pro):
        def ogrenci_sayfasi():
            dogrulama_frame=Frame(ilk_sayfa,bg="#27374D")
            dogrulama_frame.place(x=0,y=0,width=400,height=450)

            title_top68=Label(dogrulama_frame,text='Kimlik Doğrulama Sistemi',bg='#9DB2BF',fg='#27374D',font=('Calibri',23,"bold"))
            title_top68.pack(fill=X)

            kul_adi=StringVar()
            kul_sifre=StringVar()

            def on_entry_click(event):
                if entry_kul_adi.get() == "Kullanıcı Adı":
                    entry_kul_adi.delete(0, END)
                    entry_kul_adi.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)

            def on_sifre_click(event):
                if entry_sifre.get() == "Şifre":
                    entry_sifre.delete(0, END)
                    entry_sifre.config(show="*")  # İsteğe bağlı: Şifreyi gizleme karakterini ayarla
                    entry_sifre.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)

            entry_kul_adi = Entry(dogrulama_frame,justify="center",width=27,fg="#526D82",textvariable=kul_adi)
            entry_kul_adi.place(x=120, y=160,height=30)
            entry_kul_adi.insert(0, "Kullanıcı Adı")
            entry_kul_adi.bind("<FocusIn>", on_entry_click)

            entry_sifre = Entry(dogrulama_frame,justify="center",width=27,fg="#526D82",textvariable=kul_sifre)
            entry_sifre.place(x=120, y=200,height=30)
            entry_sifre.insert(0, "Şifre")
            entry_sifre.bind("<FocusIn>", on_sifre_click)

            def giris_def():
                db = pypyodbc.connect(
                'Driver={SQL Server};'
                'Server=YAZILIMCI\SQLEXPRESS01;'
                'Database=Proje;'
                'Trusted_Connection=True;')
                
                cr = db.cursor()
                try:
                    cr.execute(f"SELECT Ogr_Sifre from Ogrenciler where Ogr_No='{kul_adi.get().strip()}'")
                    db_sifre=cr.fetchall()
                
                    if(db_sifre[0][0]==kul_sifre.get().strip()):
                        kul_adi1=kul_adi.get()
                        self.pro.destroy()
                        self.omer = Tk()
                        self.omer.geometry("{width}x{height}+0+0".format(width=self.omer.winfo_screenwidth(),height=self.omer.winfo_screenheight()))
                        self.omer.title("Öğrenci Bilgi Sistemi")
                        self.omer.config(bg="#27374D")

                        titl=Label(self.omer,text="Öğrenci Bilgi Sistemi",bg='#DDE6ED',fg='#27374D',font=('Calibri',16,"bold"))
                        titl.pack(fill=X)

                        #-------Frame_b--------#
                        frame_b=Frame(self.omer,bg='#9DB2BF')
                        frame_b.place(x=0,y=32,width=220,height=805)

                        title_top93=Label(frame_b,
                        text='Kontrol Paneli',
                        bg='#526D82',
                        fg='#DDE6ED',
                        font=('calisto mt',22,'bold'))
                        title_top93.place(x=0,y=0,width=220,height=45)
                        
                        #-----Not Listesi Fonksiyonu-----#
                        def not_listesi_fonksiyonu():       

                            #----------Frame not listesi-----------#
                            frame_not_listesi=Frame(self.omer,bg='red')
                            frame_not_listesi.place(x=220,y=77,width=1316,height=760)

                            scrol_x=Scrollbar(frame_not_listesi,orient=HORIZONTAL)  
                            scrol_y=Scrollbar(frame_not_listesi,orient=VERTICAL)

                            not_listesi=ttk.Treeview(frame_not_listesi,
                                                            columns=('no','kod','ad','vize','final','ort'),
                                                            xscrollcommand=scrol_x.set,
                                                            yscrollcommand=scrol_y.set,)
                            
                            not_listesi.place(x=0,y=0,width=1299,height=745)
                            scrol_x.pack(side=BOTTOM,fill=X)
                            scrol_y.pack(side=RIGHT,fill=Y)
                            scrol_x.config(command=not_listesi.xview)
                            scrol_y.config(command=not_listesi.yview)

                            not_listesi['show']='headings'
                            not_listesi.heading('no',text='No')
                            not_listesi.heading('kod',text='Ders Kodu')
                            not_listesi.heading('ad',text='Ders Adı')
                            not_listesi.heading('vize',text='Vize Notu')
                            not_listesi.heading('final',text='Final Notu')
                            not_listesi.heading('ort',text='Ortalama')
                            
                            not_listesi.column('no',width=35,anchor='center')
                            not_listesi.column('kod',width=210,anchor='center')
                            not_listesi.column('ad',width=415,anchor='center')
                            not_listesi.column('vize',width=210,anchor='center')
                            not_listesi.column('final',width=210,anchor='center')
                            not_listesi.column('ort',width=210,anchor='center')

                            #not_listesi.bind("<ButtonRelease-1>",self.get_cursor)


                            cr.execute(f"SELECT Ders_Id, Vize_puan, Final_Puan from Puan where Ogr_No='{kul_adi.get().strip()}'")
                            ders_puanlar=cr.fetchall()

                            son_liste = []
                            for i in range(len(ders_puanlar)):
                                cr.execute(f"SELECT Ders_Kodu, Ders_Ad FROM Dersler WHERE Ders_Id={ders_puanlar[i][0]}")
                                Ders_Adlar = cr.fetchall()

                                ders_bilgileri = []
                                
                                # Elemanları alt liste içine ekle
                                ders_bilgileri.append(i + 1)  # Sıra numarası ekle
                                ders_bilgileri.append(Ders_Adlar[0][0])  # Ders kodu ekle
                                ders_bilgileri.append(Ders_Adlar[0][1])  # Ders adı ekle
                                if(ders_puanlar[i][1]==None):
                                    ders_bilgileri.append('-')  # Vize puanı ekle
                                else:
                                    ders_bilgileri.append(ders_puanlar[i][1])  # Vize puanı ekle
                                if(ders_puanlar[i][2]==None):
                                    ders_bilgileri.append('-')  # Vize puanı ekle
                                else:
                                    ders_bilgileri.append(ders_puanlar[i][2])  # Vize puanı ekle

                               

                                if ders_puanlar[i][1] is not None and ders_puanlar[i][2] is not None:
                                    ders_bilgileri.append((ders_puanlar[i][1] * 0.4) + (ders_puanlar[i][2] * 0.6))  # Ortalama ekle
                                else:
                                    ders_bilgileri.append('-')

                                # Oluşturulan alt listeyi 'son_liste' listesine ekle
                                son_liste.append(ders_bilgileri)
                                

                            if(len(son_liste)!=0):
                                for alt_liste in son_liste:
                                    not_listesi.insert("", END, values=alt_liste)

                            

                        def mufredat_fonksiyonu():
                            #----------Frame mufredat-----------#
                            frame_mufredat=Frame(self.omer,bg='red')
                            frame_mufredat.place(x=220,y=77,width=1316,height=715)#2620


                            frame_mufredat.grid_rowconfigure(0, weight=1)
                            #frame_mufredat.grid_columnconfigure(0, weight=1)

                            canvas = Canvas(frame_mufredat, bg='#27374D', width=1295, height=710)
                            canvas.grid(row=0, column=0, sticky='nsew')

                            scrollbar = Scrollbar(frame_mufredat, command=canvas.yview)
                            scrollbar.grid(row=0, column=1, sticky='ns')

                            canvas.configure(yscrollcommand=scrollbar.set)

                            

                            frame_mufredat_ust=Frame(canvas,bg='#526D82',width=500,height=80)
                            canvas.create_window((400,95), window=frame_mufredat_ust, anchor='nw')

                            titl_mufredat_ust=Label(frame_mufredat_ust,text="MÜFREDAT",bg='#526D82',fg='#DDE6ED',font=('Calibri',40,"bold"))
                            titl_mufredat_ust.place(x=0,y=15,width=500,height=50)

                            frame_mufredat_11=Frame(canvas,bg='#526D82',width=1240,height=300)
                            canvas.create_window((30,220), window=frame_mufredat_11, anchor='nw')

                            frame_mufredat_12=Frame(canvas,bg='#526D82',width=1240,height=300)
                            canvas.create_window((30,550), window=frame_mufredat_12, anchor='nw')

                            frame_mufredat_21=Frame(canvas,bg='#526D82',width=1240,height=300)
                            canvas.create_window((30,880), window=frame_mufredat_21, anchor='nw')

                            frame_mufredat_22=Frame(canvas,bg='#526D82',width=1240,height=300)
                            canvas.create_window((30,1210), window=frame_mufredat_22, anchor='nw')

                            frame_mufredat_31=Frame(canvas,bg='#526D82',width=1240,height=300)
                            canvas.create_window((30,1540), window=frame_mufredat_31, anchor='nw')

                            frame_mufredat_32=Frame(canvas,bg='#526D82',width=1240,height=300)
                            canvas.create_window((30,1870), window=frame_mufredat_32, anchor='nw')

                            frame_mufredat_41=Frame(canvas,bg='#526D82',width=1240,height=300)
                            canvas.create_window((30,2200), window=frame_mufredat_41, anchor='nw')

                            frame_mufredat_42=Frame(canvas,bg='#526D82',width=1240,height=300)
                            canvas.create_window((30,2530), window=frame_mufredat_42, anchor='nw')

                            content_frame1 = Frame(canvas,bg='#27374D',width=400,height=30)
                            canvas.create_window((30,2960), window=content_frame1, anchor='nw')

                            content_frame = Frame(canvas,bg='#27374D',width=400,height=30)
                            canvas.create_window((50,50), window=content_frame, anchor='nw')


                            canvas.update_idletasks()


                            canvas.configure(scrollregion=canvas.bbox('all'))


                            
                            titl_hangi_donem_11=Label(frame_mufredat_11,text="1. YIL GÜZ DÖNEMİ",bg='#526D82',fg='#DDE6ED',font=('Calibri',20,"bold"))
                            titl_hangi_donem_11.place(x=0,y=0,width=1240,height=40)

                            mufredat_listesi_11=ttk.Treeview(frame_mufredat_11,
                                                            columns=('no','kod','ad','krd','akts','teori/uyg','ogrt')
                                                            )
                            
                            mufredat_listesi_11.place(x=0,y=40,width=1265,height=299)

                            mufredat_listesi_11['show']='headings'
                            mufredat_listesi_11.heading('no',text='No')
                            mufredat_listesi_11.heading('kod',text='Ders Kodu')
                            mufredat_listesi_11.heading('ad',text='Ders Adı')
                            mufredat_listesi_11.heading('krd',text='Kredi')
                            mufredat_listesi_11.heading('akts',text='Akts')
                            mufredat_listesi_11.heading('teori/uyg',text='Teori/Uygulama')
                            mufredat_listesi_11.heading('ogrt',text='Ders Öğretmeni')

                            mufredat_listesi_11.column('no',width=35,anchor='center')
                            mufredat_listesi_11.column('kod',width=165,anchor='center')
                            mufredat_listesi_11.column('ad',width=430,anchor='center')
                            mufredat_listesi_11.column('krd',width=70,anchor='center')
                            mufredat_listesi_11.column('akts',width=70,anchor='center')
                            mufredat_listesi_11.column('teori/uyg',width=100,anchor='center')
                            mufredat_listesi_11.column('ogrt',width=340,anchor='center')

                            cr.execute(f"SELECT Bolum_Id from Ogrenciler where Ogr_No='{kul_adi.get().strip()}'")
                            bolum_idsi_11=cr.fetchone()

                            cr.execute(f"SELECT Ders_Kodu, Ders_Ad, Kredi, Akts, Teori, Uygulama, Ogrt_No from Dersler where Bolum_Id={bolum_idsi_11[0]} AND Ogr_Sinif=1 AND Donem=1")
                            sonuc_11=cr.fetchall()
                            
                            Ogretmen_Adlari_11=[]
                            for i in range(len(sonuc_11)):
                                cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad from Ogretmenler where Ogrt_No={sonuc_11[i][6]}")
                                db_Ogrt_No=cr.fetchone()
                                Ogretmen_Adlari_11.append(db_Ogrt_No[0]+ " " + db_Ogrt_No[1])

                            son_liste_11 = []
                            for i in range(len(sonuc_11)):
                                ders_bilgileri = []
                                
                                ders_bilgileri.append(i + 1)  # Sıra numarası ekle
                                ders_bilgileri.append(sonuc_11[i][0])  # Ders kodu ekle
                                ders_bilgileri.append(sonuc_11[i][1])  # Ders adı ekle
                                ders_bilgileri.append(sonuc_11[i][2])  # Kredi ekle
                                ders_bilgileri.append(sonuc_11[i][3])  # Akts  ekle
                                ders_bilgileri.append(f"{sonuc_11[i][4]}"+"/"+f"{sonuc_11[i][5]}")  # Teori/Uygulama  ekle
                                ders_bilgileri.append(Ogretmen_Adlari_11[i])  # Ogrt_No  ekle

                                # Oluşturulan alt listeyi 'son_liste' listesine ekle
                                son_liste_11.append(ders_bilgileri)
                            

                            if(len(son_liste_11)!=0):
                                for alt_liste in son_liste_11:
                                    mufredat_listesi_11.insert("", END, values=alt_liste)
                            

                            #------------------------------------------------------------------------------------------------

                            titl_hangi_donem_12=Label(frame_mufredat_12,text="1. YIL BAHAR DÖNEMİ",bg='#526D82',fg='#DDE6ED',font=('Calibri',20,"bold"))
                            titl_hangi_donem_12.place(x=0,y=0,width=1240,height=40)

                            mufredat_listesi_12=ttk.Treeview(frame_mufredat_12,
                                                            columns=('no','kod','ad','krd','akts','teori/uyg','ogrt')
                                                            )
                            
                            mufredat_listesi_12.place(x=0,y=40,width=1265,height=299)

                            mufredat_listesi_12['show']='headings'
                            mufredat_listesi_12.heading('no',text='No')
                            mufredat_listesi_12.heading('kod',text='Ders Kodu')
                            mufredat_listesi_12.heading('ad',text='Ders Adı')
                            mufredat_listesi_12.heading('krd',text='Kredi')
                            mufredat_listesi_12.heading('akts',text='Akts')
                            mufredat_listesi_12.heading('teori/uyg',text='Teori/Uygulama')
                            mufredat_listesi_12.heading('ogrt',text='Ders Öğretmeni')
                            
                            mufredat_listesi_12.column('no',width=35,anchor='center')
                            mufredat_listesi_12.column('kod',width=165,anchor='center')
                            mufredat_listesi_12.column('ad',width=430,anchor='center')
                            mufredat_listesi_12.column('krd',width=70,anchor='center')
                            mufredat_listesi_12.column('akts',width=70,anchor='center')
                            mufredat_listesi_12.column('teori/uyg',width=100,anchor='center')
                            mufredat_listesi_12.column('ogrt',width=340,anchor='center')

                            cr.execute(f"SELECT Bolum_Id from Ogrenciler where Ogr_No='{kul_adi.get().strip()}'")
                            bolum_idsi_12=cr.fetchone()

                            cr.execute(f"SELECT Ders_Kodu, Ders_Ad, Kredi, Akts, Teori, Uygulama, Ogrt_No from Dersler where Bolum_Id={bolum_idsi_12[0]} AND Ogr_Sinif=1 AND Donem=2")
                            sonuc_12=cr.fetchall()
                            
                            Ogretmen_Adlari_12=[]
                            for i in range(len(sonuc_12)):
                                cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad from Ogretmenler where Ogrt_No={sonuc_12[i][6]}")
                                db_Ogrt_No=cr.fetchone()
                                Ogretmen_Adlari_12.append(db_Ogrt_No[0]+ " " + db_Ogrt_No[1])

                            son_liste_12 = []
                            for i in range(len(sonuc_12)):
                                ders_bilgileri = []
                                
                                ders_bilgileri.append(i + 1)  # Sıra numarası ekle
                                ders_bilgileri.append(sonuc_12[i][0])  # Ders kodu ekle
                                ders_bilgileri.append(sonuc_12[i][1])  # Ders adı ekle
                                ders_bilgileri.append(sonuc_12[i][2])  # Kredi ekle
                                ders_bilgileri.append(sonuc_12[i][3])  # Akts  ekle
                                ders_bilgileri.append(f"{sonuc_12[i][4]}"+"/"+f"{sonuc_12[i][5]}")  # Teori/Uygulama  ekle
                                ders_bilgileri.append(Ogretmen_Adlari_12[i])  # Ogrt_No  ekle

                                # Oluşturulan alt listeyi 'son_liste' listesine ekle
                                son_liste_12.append(ders_bilgileri)
                            

                            if(len(son_liste_12)!=0):
                                for alt_liste in son_liste_12:
                                    mufredat_listesi_12.insert("", END, values=alt_liste)

                            #------------------------------------------------------------------------------------------------

                            titl_hangi_donem_21=Label(frame_mufredat_21,text="2. YIL GÜZ DÖNEMİ",bg='#526D82',fg='#DDE6ED',font=('Calibri',20,"bold"))
                            titl_hangi_donem_21.place(x=0,y=0,width=1240,height=40)

                            mufredat_listesi_21=ttk.Treeview(frame_mufredat_21,
                                                            columns=('no','kod','ad','krd','akts','teori/uyg','ogrt')
                                                            )
                            
                            mufredat_listesi_21.place(x=0,y=40,width=1265,height=299)

                            mufredat_listesi_21['show']='headings'
                            mufredat_listesi_21.heading('no',text='No')
                            mufredat_listesi_21.heading('kod',text='Ders Kodu')
                            mufredat_listesi_21.heading('ad',text='Ders Adı')
                            mufredat_listesi_21.heading('krd',text='Kredi')
                            mufredat_listesi_21.heading('akts',text='Akts')
                            mufredat_listesi_21.heading('teori/uyg',text='Teori/Uygulama')
                            mufredat_listesi_21.heading('ogrt',text='Ders Öğretmeni')
                            
                            mufredat_listesi_21.column('no',width=35,anchor='center')
                            mufredat_listesi_21.column('kod',width=165,anchor='center')
                            mufredat_listesi_21.column('ad',width=430,anchor='center')
                            mufredat_listesi_21.column('krd',width=70,anchor='center')
                            mufredat_listesi_21.column('akts',width=70,anchor='center')
                            mufredat_listesi_21.column('teori/uyg',width=100,anchor='center')
                            mufredat_listesi_21.column('ogrt',width=340,anchor='center')

                            cr.execute(f"SELECT Bolum_Id from Ogrenciler where Ogr_No='{kul_adi.get().strip()}'")
                            bolum_idsi_21=cr.fetchone()

                            cr.execute(f"SELECT Ders_Kodu, Ders_Ad, Kredi, Akts, Teori, Uygulama, Ogrt_No from Dersler where Bolum_Id={bolum_idsi_21[0]} AND Ogr_Sinif=2 AND Donem=1")
                            sonuc_21=cr.fetchall()
                            
                            Ogretmen_Adlari_21=[]
                            for i in range(len(sonuc_21)):
                                cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad from Ogretmenler where Ogrt_No={sonuc_21[i][6]}")
                                db_Ogrt_No=cr.fetchone()
                                Ogretmen_Adlari_21.append(db_Ogrt_No[0]+ " " + db_Ogrt_No[1])

                            son_liste_21 = []
                            for i in range(len(sonuc_21)):
                                ders_bilgileri = []
                                
                                ders_bilgileri.append(i + 1)  # Sıra numarası ekle
                                ders_bilgileri.append(sonuc_21[i][0])  # Ders kodu ekle
                                ders_bilgileri.append(sonuc_21[i][1])  # Ders adı ekle
                                ders_bilgileri.append(sonuc_21[i][2])  # Kredi ekle
                                ders_bilgileri.append(sonuc_21[i][3])  # Akts  ekle
                                ders_bilgileri.append(f"{sonuc_21[i][4]}"+"/"+f"{sonuc_21[i][5]}")  # Teori/Uygulama  ekle
                                ders_bilgileri.append(Ogretmen_Adlari_21[i])  # Ogrt_No  ekle

                                # Oluşturulan alt listeyi 'son_liste' listesine ekle
                                son_liste_21.append(ders_bilgileri)
                            

                            if(len(son_liste_21)!=0):
                                for alt_liste in son_liste_21:
                                    mufredat_listesi_21.insert("", END, values=alt_liste)


                            #------------------------------------------------------------------------------------------------

                            titl_hangi_donem_22=Label(frame_mufredat_22,text="2. YIL BAHAR DÖNEMİ",bg='#526D82',fg='#DDE6ED',font=('Calibri',20,"bold"))
                            titl_hangi_donem_22.place(x=0,y=0,width=1240,height=40)

                            mufredat_listesi_22=ttk.Treeview(frame_mufredat_22,
                                                            columns=('no','kod','ad','krd','akts','teori/uyg','ogrt')
                                                            )
                            
                            mufredat_listesi_22.place(x=0,y=40,width=1265,height=299)

                            mufredat_listesi_22['show']='headings'
                            mufredat_listesi_22.heading('no',text='No')
                            mufredat_listesi_22.heading('kod',text='Ders Kodu')
                            mufredat_listesi_22.heading('ad',text='Ders Adı')
                            mufredat_listesi_22.heading('krd',text='Kredi')
                            mufredat_listesi_22.heading('akts',text='Akts')
                            mufredat_listesi_22.heading('teori/uyg',text='Teori/Uygulama')
                            mufredat_listesi_22.heading('ogrt',text='Ders Öğretmeni')
                            
                            mufredat_listesi_22.column('no',width=35,anchor='center')
                            mufredat_listesi_22.column('kod',width=165,anchor='center')
                            mufredat_listesi_22.column('ad',width=430,anchor='center')
                            mufredat_listesi_22.column('krd',width=70,anchor='center')
                            mufredat_listesi_22.column('akts',width=70,anchor='center')
                            mufredat_listesi_22.column('teori/uyg',width=100,anchor='center')
                            mufredat_listesi_22.column('ogrt',width=340,anchor='center')

                            cr.execute(f"SELECT Bolum_Id from Ogrenciler where Ogr_No='{kul_adi.get().strip()}'")
                            bolum_idsi_22=cr.fetchone()

                            cr.execute(f"SELECT Ders_Kodu, Ders_Ad, Kredi, Akts, Teori, Uygulama, Ogrt_No from Dersler where Bolum_Id={bolum_idsi_22[0]} AND Ogr_Sinif=2 AND Donem=2")
                            sonuc_22=cr.fetchall()
                            
                            Ogretmen_Adlari_22=[]
                            for i in range(len(sonuc_22)):
                                cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad from Ogretmenler where Ogrt_No={sonuc_22[i][6]}")
                                db_Ogrt_No=cr.fetchone()
                                Ogretmen_Adlari_22.append(db_Ogrt_No[0]+ " " + db_Ogrt_No[1])

                            son_liste_22 = []
                            for i in range(len(sonuc_22)):
                                ders_bilgileri = []
                                
                                ders_bilgileri.append(i + 1)  # Sıra numarası ekle
                                ders_bilgileri.append(sonuc_22[i][0])  # Ders kodu ekle
                                ders_bilgileri.append(sonuc_22[i][1])  # Ders adı ekle
                                ders_bilgileri.append(sonuc_22[i][2])  # Kredi ekle
                                ders_bilgileri.append(sonuc_22[i][3])  # Akts  ekle
                                ders_bilgileri.append(f"{sonuc_22[i][4]}"+"/"+f"{sonuc_22[i][5]}")  # Teori/Uygulama  ekle
                                ders_bilgileri.append(Ogretmen_Adlari_22[i])  # Ogrt_No  ekle

                                # Oluşturulan alt listeyi 'son_liste' listesine ekle
                                son_liste_22.append(ders_bilgileri)
                            

                            if(len(son_liste_22)!=0):
                                for alt_liste in son_liste_22:
                                    mufredat_listesi_22.insert("", END, values=alt_liste)

                            #------------------------------------------------------------------------------------------------
                            
                            titl_hangi_donem_31=Label(frame_mufredat_31,text="3. YIL GÜZ DÖNEMİ",bg='#526D82',fg='#DDE6ED',font=('Calibri',20,"bold"))
                            titl_hangi_donem_31.place(x=0,y=0,width=1240,height=40)

                            mufredat_listesi_31=ttk.Treeview(frame_mufredat_31,
                                                            columns=('no','kod','ad','krd','akts','teori/uyg','ogrt')
                                                            )
                            
                            mufredat_listesi_31.place(x=0,y=40,width=1265,height=299)

                            mufredat_listesi_31['show']='headings'
                            mufredat_listesi_31.heading('no',text='No')
                            mufredat_listesi_31.heading('kod',text='Ders Kodu')
                            mufredat_listesi_31.heading('ad',text='Ders Adı')
                            mufredat_listesi_31.heading('krd',text='Kredi')
                            mufredat_listesi_31.heading('akts',text='Akts')
                            mufredat_listesi_31.heading('teori/uyg',text='Teori/Uygulama')
                            mufredat_listesi_31.heading('ogrt',text='Ders Öğretmeni')
                            
                            mufredat_listesi_31.column('no',width=35,anchor='center')
                            mufredat_listesi_31.column('kod',width=165,anchor='center')
                            mufredat_listesi_31.column('ad',width=430,anchor='center')
                            mufredat_listesi_31.column('krd',width=70,anchor='center')
                            mufredat_listesi_31.column('akts',width=70,anchor='center')
                            mufredat_listesi_31.column('teori/uyg',width=100,anchor='center')
                            mufredat_listesi_31.column('ogrt',width=340,anchor='center')

                            cr.execute(f"SELECT Bolum_Id from Ogrenciler where Ogr_No='{kul_adi.get().strip()}'")
                            bolum_idsi_31=cr.fetchone()

                            cr.execute(f"SELECT Ders_Kodu, Ders_Ad, Kredi, Akts, Teori, Uygulama, Ogrt_No from Dersler where Bolum_Id={bolum_idsi_31[0]} AND Ogr_Sinif=3 AND Donem=1")
                            sonuc_31=cr.fetchall()
                            
                            Ogretmen_Adlari_31=[]
                            for i in range(len(sonuc_31)):
                                cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad from Ogretmenler where Ogrt_No={sonuc_31[i][6]}")
                                db_Ogrt_No=cr.fetchone()
                                Ogretmen_Adlari_31.append(db_Ogrt_No[0]+ " " + db_Ogrt_No[1])

                            son_liste_31 = []
                            for i in range(len(sonuc_31)):
                                ders_bilgileri = []
                                
                                ders_bilgileri.append(i + 1)  # Sıra numarası ekle
                                ders_bilgileri.append(sonuc_31[i][0])  # Ders kodu ekle
                                ders_bilgileri.append(sonuc_31[i][1])  # Ders adı ekle
                                ders_bilgileri.append(sonuc_31[i][2])  # Kredi ekle
                                ders_bilgileri.append(sonuc_31[i][3])  # Akts  ekle
                                ders_bilgileri.append(f"{sonuc_31[i][4]}"+"/"+f"{sonuc_31[i][5]}")  # Teori/Uygulama  ekle
                                ders_bilgileri.append(Ogretmen_Adlari_31[i])  # Ogrt_No  ekle

                                # Oluşturulan alt listeyi 'son_liste' listesine ekle
                                son_liste_31.append(ders_bilgileri)
                            

                            if(len(son_liste_31)!=0):
                                for alt_liste in son_liste_31:
                                    mufredat_listesi_31.insert("", END, values=alt_liste)


                            #------------------------------------------------------------------------------------------------
                            
                            titl_hangi_donem_32=Label(frame_mufredat_32,text="3. YIL BAHAR DÖNEMİ",bg='#526D82',fg='#DDE6ED',font=('Calibri',20,"bold"))
                            titl_hangi_donem_32.place(x=0,y=0,width=1240,height=40)

                            mufredat_listesi_32=ttk.Treeview(frame_mufredat_32,
                                                            columns=('no','kod','ad','krd','akts','teori/uyg','ogrt')
                                                            )
                            
                            mufredat_listesi_32.place(x=0,y=40,width=1265,height=299)

                            mufredat_listesi_32['show']='headings'
                            mufredat_listesi_32.heading('no',text='No')
                            mufredat_listesi_32.heading('kod',text='Ders Kodu')
                            mufredat_listesi_32.heading('ad',text='Ders Adı')
                            mufredat_listesi_32.heading('krd',text='Kredi')
                            mufredat_listesi_32.heading('akts',text='Akts')
                            mufredat_listesi_32.heading('teori/uyg',text='Teori/Uygulama')
                            mufredat_listesi_32.heading('ogrt',text='Ders Öğretmeni')
                            
                            mufredat_listesi_32.column('no',width=35,anchor='center')
                            mufredat_listesi_32.column('kod',width=165,anchor='center')
                            mufredat_listesi_32.column('ad',width=430,anchor='center')
                            mufredat_listesi_32.column('krd',width=70,anchor='center')
                            mufredat_listesi_32.column('akts',width=70,anchor='center')
                            mufredat_listesi_32.column('teori/uyg',width=100,anchor='center')
                            mufredat_listesi_32.column('ogrt',width=340,anchor='center')

                            cr.execute(f"SELECT Bolum_Id from Ogrenciler where Ogr_No='{kul_adi.get().strip()}'")
                            bolum_idsi_32=cr.fetchone()

                            cr.execute(f"SELECT Ders_Kodu, Ders_Ad, Kredi, Akts, Teori, Uygulama, Ogrt_No from Dersler where Bolum_Id={bolum_idsi_32[0]} AND Ogr_Sinif=3 AND Donem=2")
                            sonuc_32=cr.fetchall()
                            
                            Ogretmen_Adlari_32=[]
                            for i in range(len(sonuc_32)):
                                cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad from Ogretmenler where Ogrt_No={sonuc_32[i][6]}")
                                db_Ogrt_No=cr.fetchone()
                                Ogretmen_Adlari_32.append(db_Ogrt_No[0]+ " " + db_Ogrt_No[1])

                            son_liste_32 = []
                            for i in range(len(sonuc_32)):
                                ders_bilgileri = []
                                
                                ders_bilgileri.append(i + 1)  # Sıra numarası ekle
                                ders_bilgileri.append(sonuc_32[i][0])  # Ders kodu ekle
                                ders_bilgileri.append(sonuc_32[i][1])  # Ders adı ekle
                                ders_bilgileri.append(sonuc_32[i][2])  # Kredi ekle
                                ders_bilgileri.append(sonuc_32[i][3])  # Akts  ekle
                                ders_bilgileri.append(f"{sonuc_32[i][4]}"+"/"+f"{sonuc_32[i][5]}")  # Teori/Uygulama  ekle
                                ders_bilgileri.append(Ogretmen_Adlari_32[i])  # Ogrt_No  ekle

                                # Oluşturulan alt listeyi 'son_liste' listesine ekle
                                son_liste_32.append(ders_bilgileri)
                            

                            if(len(son_liste_32)!=0):
                                for alt_liste in son_liste_32:
                                    mufredat_listesi_32.insert("", END, values=alt_liste)

                            #------------------------------------------------------------------------------------------------
                            
                            titl_hangi_donem_41=Label(frame_mufredat_41,text="4. YIL GÜZ DÖNEMİ",bg='#526D82',fg='#DDE6ED',font=('Calibri',20,"bold"))
                            titl_hangi_donem_41.place(x=0,y=0,width=1240,height=40)

                            mufredat_listesi_41=ttk.Treeview(frame_mufredat_41,
                                                            columns=('no','kod','ad','krd','akts','teori/uyg','ogrt')
                                                            )
                            
                            mufredat_listesi_41.place(x=0,y=40,width=1265,height=299)

                            mufredat_listesi_41['show']='headings'
                            mufredat_listesi_41.heading('no',text='No')
                            mufredat_listesi_41.heading('kod',text='Ders Kodu')
                            mufredat_listesi_41.heading('ad',text='Ders Adı')
                            mufredat_listesi_41.heading('krd',text='Kredi')
                            mufredat_listesi_41.heading('akts',text='Akts')
                            mufredat_listesi_41.heading('teori/uyg',text='Teori/Uygulama')
                            mufredat_listesi_41.heading('ogrt',text='Ders Öğretmeni')
                            
                            mufredat_listesi_41.column('no',width=35,anchor='center')
                            mufredat_listesi_41.column('kod',width=165,anchor='center')
                            mufredat_listesi_41.column('ad',width=430,anchor='center')
                            mufredat_listesi_41.column('krd',width=70,anchor='center')
                            mufredat_listesi_41.column('akts',width=70,anchor='center')
                            mufredat_listesi_41.column('teori/uyg',width=100,anchor='center')
                            mufredat_listesi_41.column('ogrt',width=340,anchor='center')

                            cr.execute(f"SELECT Bolum_Id from Ogrenciler where Ogr_No='{kul_adi.get().strip()}'")
                            bolum_idsi_41=cr.fetchone()

                            cr.execute(f"SELECT Ders_Kodu, Ders_Ad, Kredi, Akts, Teori, Uygulama, Ogrt_No from Dersler where Bolum_Id={bolum_idsi_41[0]} AND Ogr_Sinif=4 AND Donem=1")
                            sonuc_41=cr.fetchall()
                            
                            Ogretmen_Adlari_41=[]
                            for i in range(len(sonuc_41)):
                                cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad from Ogretmenler where Ogrt_No={sonuc_41[i][6]}")
                                db_Ogrt_No=cr.fetchone()
                                Ogretmen_Adlari_41.append(db_Ogrt_No[0]+ " " + db_Ogrt_No[1])

                            son_liste_41 = []
                            for i in range(len(sonuc_41)):
                                ders_bilgileri = []
                                
                                ders_bilgileri.append(i + 1)  # Sıra numarası ekle
                                ders_bilgileri.append(sonuc_41[i][0])  # Ders kodu ekle
                                ders_bilgileri.append(sonuc_41[i][1])  # Ders adı ekle
                                ders_bilgileri.append(sonuc_41[i][2])  # Kredi ekle
                                ders_bilgileri.append(sonuc_41[i][3])  # Akts  ekle
                                ders_bilgileri.append(f"{sonuc_41[i][4]}"+"/"+f"{sonuc_41[i][5]}")  # Teori/Uygulama  ekle
                                ders_bilgileri.append(Ogretmen_Adlari_41[i])  # Ogrt_No  ekle

                                # Oluşturulan alt listeyi 'son_liste' listesine ekle
                                son_liste_41.append(ders_bilgileri)
                            

                            if(len(son_liste_41)!=0):
                                for alt_liste in son_liste_41:
                                    mufredat_listesi_41.insert("", END, values=alt_liste)

                            #------------------------------------------------------------------------------------------------
                            
                            titl_hangi_donem_42=Label(frame_mufredat_42,text="4. YIL BAHAR DÖNEMİ",bg='#526D82',fg='#DDE6ED',font=('Calibri',20,"bold"))
                            titl_hangi_donem_42.place(x=0,y=0,width=1240,height=40)

                            mufredat_listesi_42=ttk.Treeview(frame_mufredat_42,
                                                            columns=('no','kod','ad','krd','akts','teori/uyg','ogrt')
                                                            )
                            
                            mufredat_listesi_42.place(x=0,y=40,width=1265,height=299)

                            mufredat_listesi_42['show']='headings'
                            mufredat_listesi_42.heading('no',text='No')
                            mufredat_listesi_42.heading('kod',text='Ders Kodu')
                            mufredat_listesi_42.heading('ad',text='Ders Adı')
                            mufredat_listesi_42.heading('krd',text='Kredi')
                            mufredat_listesi_42.heading('akts',text='Akts')
                            mufredat_listesi_42.heading('teori/uyg',text='Teori/Uygulama')
                            mufredat_listesi_42.heading('ogrt',text='Ders Öğretmeni')
                            
                            mufredat_listesi_42.column('no',width=35,anchor='center')
                            mufredat_listesi_42.column('kod',width=165,anchor='center')
                            mufredat_listesi_42.column('ad',width=430,anchor='center')
                            mufredat_listesi_42.column('krd',width=70,anchor='center')
                            mufredat_listesi_42.column('akts',width=70,anchor='center')
                            mufredat_listesi_42.column('teori/uyg',width=100,anchor='center')
                            mufredat_listesi_42.column('ogrt',width=340,anchor='center')

                            cr.execute(f"SELECT Bolum_Id from Ogrenciler where Ogr_No='{kul_adi.get().strip()}'")
                            bolum_idsi_42=cr.fetchone()

                            cr.execute(f"SELECT Ders_Kodu, Ders_Ad, Kredi, Akts, Teori, Uygulama, Ogrt_No from Dersler where Bolum_Id={bolum_idsi_42[0]} AND Ogr_Sinif=4 AND Donem=2")
                            sonuc_42=cr.fetchall()
                            
                            Ogretmen_Adlari_42=[]
                            for i in range(len(sonuc_42)):
                                cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad from Ogretmenler where Ogrt_No={sonuc_42[i][6]}")
                                db_Ogrt_No=cr.fetchone()
                                Ogretmen_Adlari_42.append(db_Ogrt_No[0]+ " " + db_Ogrt_No[1])

                            son_liste_42 = []
                            for i in range(len(sonuc_42)):
                                ders_bilgileri = []
                                
                                ders_bilgileri.append(i + 1)  # Sıra numarası ekle
                                ders_bilgileri.append(sonuc_42[i][0])  # Ders kodu ekle
                                ders_bilgileri.append(sonuc_42[i][1])  # Ders adı ekle
                                ders_bilgileri.append(sonuc_42[i][2])  # Kredi ekle
                                ders_bilgileri.append(sonuc_42[i][3])  # Akts  ekle
                                ders_bilgileri.append(f"{sonuc_42[i][4]}"+"/"+f"{sonuc_42[i][5]}")  # Teori/Uygulama  ekle
                                ders_bilgileri.append(Ogretmen_Adlari_42[i])  # Ogrt_No  ekle

                                # Oluşturulan alt listeyi 'son_liste' listesine ekle
                                son_liste_42.append(ders_bilgileri)
                            

                            if(len(son_liste_42)!=0):
                                for alt_liste in son_liste_42:
                                    mufredat_listesi_42.insert("", END, values=alt_liste)

                            #------------------------------------------------------------------------------------------------

                                    
                        def kapatma():
                            try:
                                self.omer.destroy()
                            except:
                                pass



                        def change_color_Not_Listesi_btn1(event):
                            Not_Listesi_btn.config(bg="#526D82", fg="#DDE6ED")  
                        def change_color_Not_Listesi_btn2(event):
                            Not_Listesi_btn.config(bg="#27374D", fg="#DDE6ED")
                        Not_Listesi_btn=Button(frame_b,text='Not Listesi',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=not_listesi_fonksiyonu)
                        Not_Listesi_btn.place(x=5,y=50,width=207,height=40)
                        Not_Listesi_btn.bind("<Enter>", change_color_Not_Listesi_btn1)  
                        Not_Listesi_btn.bind("<Leave>", change_color_Not_Listesi_btn2) 

                        def change_color_Mufredat_btn1(event):
                            Mufredat_btn.config(bg="#526D82", fg="#DDE6ED")  
                        def change_color_Mufredat_btn2(event):
                            Mufredat_btn.config(bg="#27374D", fg="#DDE6ED")
                        Mufredat_btn=Button(frame_b,text='Müfredat',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=mufredat_fonksiyonu)
                        Mufredat_btn.place(x=5,y=93,width=207,height=40)
                        Mufredat_btn.bind("<Enter>", change_color_Mufredat_btn1)  
                        Mufredat_btn.bind("<Leave>", change_color_Mufredat_btn2) 

                        def change_color_exit_btn1(event):
                            exit_btn.config(bg="#526D82", fg="#DDE6ED")  
                        def change_color_exit_btn2(event):
                            exit_btn.config(bg="#27374D", fg="#DDE6ED")
                        exit_btn=Button(frame_b,text='Programı Kapat',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=kapatma)
                        exit_btn.place(x=5,y=145,width=207,height=40)
                        exit_btn.bind("<Enter>", change_color_exit_btn1)  
                        exit_btn.bind("<Leave>", change_color_exit_btn2) 


                        #--------frame_ust-------#
                        frame_ust=Frame(self.omer,bg='#9DB2BF')
                        frame_ust.place(x=222,y=32,width=1314,height=45)


                        cr.execute(f"SELECT Ogr_Ad, Ogr_Soyad from Ogrenciler WHERE Ogr_No='{kul_adi.get().strip()}'")
                        prof_ad_soyad=cr.fetchall()
                        def def_profil_sayfasi():
                            profil = Frame(self.omer,bg="blue")
                            profil.place(x=1150,y=80,width=380,height=430)

                            profil1 = Frame(profil,bg="#9DB2BF")
                            profil1.place(x=0,y=32,width=150,height=400)

                            profil_lbl_no=Label(profil1,text='Öğrenci No            : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))         #no
                            profil_lbl_no.place(x=4,y=20)               
                            profil_lbl_ad_soyad=Label(profil1,text='Ad Soyad                : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))   #ad soyad
                            profil_lbl_ad_soyad.place(x=4,y=55)
                            profil_lbl_tc=Label(profil1,text='TC No                       : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))            #TC
                            profil_lbl_tc.place(x=4,y=90)
                            profil_lbl_dogum=Label(profil1,text='Doğum Tarihi        : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))  #Dogum
                            profil_lbl_dogum.place(x=4,y=125)
                            profil_lbl_tel=Label(profil1,text='Tel. No                    : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))         #Tel
                            profil_lbl_tel.place(x=4,y=160)
                            profil_lbl_eposta=Label(profil1,text='Eposta                     : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))       #Eposta
                            profil_lbl_eposta.place(x=4,y=195)
                            profil_lbl_cinsiyet=Label(profil1,text='Cinsiyet                  : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))   #Cinsiyet
                            profil_lbl_cinsiyet.place(x=4,y=230)
                            profil_lbl_bolum=Label(profil1,text='Bölum                     : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))   #Cinsiyet
                            profil_lbl_bolum.place(x=4,y=265)
                            profil_lbl_sinif=Label(profil1,text='Sınıf                         : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))   #Cinsiyet
                            profil_lbl_sinif.place(x=4,y=300)


                            profil2 = Frame(profil,bg="#9DB2BF")
                            profil2.place(x=150,y=32,width=230,height=400)

                            cr.execute(f"SELECT Ogr_Tc, Ogr_DT, Ogr_TelNo, Ogr_Eposta, Ogr_Cinsiyeti, Bolum_Id, Ogr_Sinif from Ogrenciler where Ogr_No='{kul_adi.get()}'")
                            prof_db=cr.fetchall()

                            profil_db_no=Label(profil2,text=kul_adi.get().strip(),bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold")) #no
                            profil_db_no.place(x=4,y=20)
                            profil_db_ad_soyad=Label(profil2,text=prof_ad_soyad[0][0]+" "+ prof_ad_soyad[0][1],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))    #ad soyad
                            profil_db_ad_soyad.place(x=4,y=55)
                            profil_db_tc=Label(profil2,text=prof_db[0][0],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))         #TC
                            profil_db_tc.place(x=4,y=90)
                            profil_db_dogum=Label(profil2,text=prof_db[0][1],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))      #Dogum
                            profil_db_dogum.place(x=4,y=125)
                            profil_db_tel=Label(profil2,text=prof_db[0][2],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))        #Tel
                            profil_db_tel.place(x=4,y=160)
                            profil_db_eposta=Label(profil2,text=prof_db[0][3],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))     #Eposta
                            profil_db_eposta.place(x=4,y=195)
                            profil_db_cinsiyet=Label(profil2,text=prof_db[0][4],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))   #Cinsiyet
                            profil_db_cinsiyet.place(x=4,y=230)
                            profil_db_sinif=Label(profil2,text=prof_db[0][6],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))   #Sinif
                            profil_db_sinif.place(x=4,y=300)

                            cr.execute(f"SELECT Bolum_Ad from Bolumler where Bolum_Id='{prof_db[0][5]}'")
                            prof_db1=cr.fetchall()
                            profil_db_bolum=Label(profil2,text=prof_db1[0][0],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))   #Bolum
                            profil_db_bolum.place(x=4,y=265)

                            def ana():
                                self.omer.destroy()
                                os.system("python Proje.py")
                                
                                


                            profil_cikis1=Button(profil,text="Çıkış", bg="#75163F",fg="#DDE6ED",font=40,command=ana)
                            profil_cikis1.place(x=130,y=370,width=120,height=45)



                            
                            kişisel_bligiler=Label(profil,text="Kişisel Bilgiler",bg='#526D82',fg='#DDE6ED',font=('Calibri',16,"bold"))
                            kişisel_bligiler.pack(fill=X)

                            def change_color_on_hover_enter(event):
                                profil_cikis.config(bg="red", fg="white")  # Fare butona yaklaştığında rengi değiştir

                            def change_color_on_hover_leave(event):
                                profil_cikis.config(bg="#526D82", fg="#DDE6ED")  # Fare butondan ayrıldığında orijinal rengine geri dön

                            profil_cikis=Button(profil,text="X", bg="#526D82",fg="#DDE6ED",font=30,command=profil.destroy, borderwidth=0, highlightthickness=0)
                            profil_cikis.place(x=345,y=2,width=32,height=28)

                            profil_cikis.bind("<Enter>", change_color_on_hover_enter)  # Fare butona geldiğinde rengi değiştir
                            profil_cikis.bind("<Leave>", change_color_on_hover_leave)  # Fare butondan ayrıldığında orijinal rengine geri dön
                            
                        def change_color_1(event):
                            prof_btn.config(bg="#526D82", fg="#9DB2BF")  

                        def change_color_2(event):
                            prof_btn.config(bg="#9DB2BF", fg="#27374D")

                        prof_btn=Button(frame_ust,text=prof_ad_soyad[0][0]+ " "+ prof_ad_soyad[0][1] + " - " + kul_adi.get(),bg='#9DB2BF',fg='#27374D',font=20, borderwidth=0, highlightthickness=0,cursor='hand2',command=def_profil_sayfasi)
                        prof_btn.place(x=984,y=3,width=270,height=38)

                        prof_btn.bind("<Enter>", change_color_1)  
                        prof_btn.bind("<Leave>", change_color_2) 

                    else:
                        hata_lbl=Label(dogrulama_frame,text="Kullanıcı Adı Yada Şifre Yanlıştır",font=('Calibri',11),bg="#27374D",fg="red")
                        hata_lbl.place(x=107,y=235)
                        
                except:
                    hata_lbl=Label(dogrulama_frame,text="Kullanıcı Adı Yada Şifre Yanlıştır",font=('Calibri',11),bg="#27374D",fg="red")
                    hata_lbl.place(x=107,y=235)

                cr.commit()
              
                



            ake_bt = Button(dogrulama_frame, text="GİRİŞ", font=("Calibri", 18, "bold"), bg="#DDE6ED", fg="#27374D",command=giris_def)
            ake_bt.place(x=142,y=280, width=120,height=30)
            

            geri_bt=Button(dogrulama_frame,text="<", bg="#9DB2BF",fg="#27374D",font=20,command=dogrulama_frame.destroy)
            geri_bt.place(x=0,y=45,width=45,height=40)



        def Akademisyen_sayfasi():
            dogrulama_frame=Frame(ilk_sayfa,bg="#27374D")
            dogrulama_frame.place(x=0,y=0,width=400,height=450)

            title_top68=Label(dogrulama_frame,text='Kimlik Doğrulama Sistemi',bg='#9DB2BF',fg='#27374D',font=('Calibri',23,"bold"))
            title_top68.pack(fill=X)

            kul_adi=StringVar()
            kul_sifre=StringVar()

            def on_entry_click(event):
                if entry_kul_adi.get() == "Kullanıcı Adı":
                    entry_kul_adi.delete(0, END)
                    entry_kul_adi.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)

            def on_sifre_click(event):
                if entry_sifre.get() == "Şifre":
                    entry_sifre.delete(0, END)
                    entry_sifre.config(show="*")  # İsteğe bağlı: Şifreyi gizleme karakterini ayarla
                    entry_sifre.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)

            entry_kul_adi = Entry(dogrulama_frame,justify="center",width=27,fg="#526D82",textvariable=kul_adi)
            entry_kul_adi.place(x=120, y=160,height=30)
            entry_kul_adi.insert(0, "Kullanıcı Adı")
            entry_kul_adi.bind("<FocusIn>", on_entry_click)

            entry_sifre = Entry(dogrulama_frame,justify="center",width=27,fg="#526D82",textvariable=kul_sifre)
            entry_sifre.place(x=120, y=200,height=30)
            entry_sifre.insert(0, "Şifre")
            entry_sifre.bind("<FocusIn>", on_sifre_click)

            def giris_def():
                db = pypyodbc.connect(
                'Driver={SQL Server};'
                'Server=YAZILIMCI\SQLEXPRESS01;'
                'Database=Proje;'
                'Trusted_Connection=True;')
                
                cr = db.cursor()

                try:
                    cr.execute(f"SELECT Ogrt_Sifre from Ogretmenler where Ogrt_No='{kul_adi.get().strip()}'")
                    db_sifre=cr.fetchall()

                    if(db_sifre[0][0]==kul_sifre.get().strip()):
                        kul_adi1=kul_adi.get()
                        self.pro.destroy()
                        self.omer = Tk()
                        self.omer.geometry("{width}x{height}+0+0".format(width=self.omer.winfo_screenwidth(),height=self.omer.winfo_screenheight()))
                        self.omer.title("Öğrenci Bilgi Sistemi")
                        self.omer.config(bg="#27374D")

                        titl=Label(self.omer,text="Öğrenci Bilgi Sistemi",bg='#DDE6ED',fg='#27374D',font=('Calibri',16,"bold"))
                        titl.pack(fill=X)

                        #------Frame_orta------#
                        frame_orta=Frame(self.omer,bg='#27374D')
                        frame_orta.place(x=220,y=77,width=1312,height=self.omer.winfo_screenheight()-148)

                        #-------Frame_b--------#
                        frame_b=Frame(self.omer,bg='#9DB2BF')
                        frame_b.place(x=0,y=32,width=220,height=self.omer.winfo_screenheight())

                        title_top93=Label(frame_b,
                        text='Kontrol Paneli',
                        bg='#526D82',
                        fg='#DDE6ED',
                        font=('calisto mt',22,'bold'))
                        title_top93.place(x=0,y=0,width=220,height=45)

                        #--------frame_ust------#
                        frame_ust=Frame(self.omer,bg='#9DB2BF')
                        frame_ust.place(x=222,y=32,width=1310,height=45)

                        #-----Ders Bilgileri Fonksiyonu-----#
                        def ders_bilgileri_fonksiyonu():  
                            
                            try:
                                Akademisyen_sayfasi.arama_bilgileri_frame.destroy()
                            except:
                                pass     

                            #----------Frame  ders bilgileri-----------#


                            Akademisyen_sayfasi.frame_ders_bilgileri=Frame(self.omer,bg='#27374D')
                            Akademisyen_sayfasi.frame_ders_bilgileri.place(x=220,y=77,width=1316,height=760)

                            scrol_x=Scrollbar(Akademisyen_sayfasi.frame_ders_bilgileri,orient=HORIZONTAL)
                            scrol_y=Scrollbar(Akademisyen_sayfasi.frame_ders_bilgileri,orient=VERTICAL)

                            ders_bilgileri_agaci=ttk.Treeview(Akademisyen_sayfasi.frame_ders_bilgileri,
                                                            columns=('no','kod','ad','sayi'),
                                                            xscrollcommand=scrol_x.set,
                                                            yscrollcommand=scrol_y.set,)
                            
                            ders_bilgileri_agaci.place(x=0,y=0,width=1299,height=745)
                            scrol_x.pack(side=BOTTOM,fill=X)
                            scrol_y.pack(side=RIGHT,fill=Y)
                            scrol_x.config(command=ders_bilgileri_agaci.xview)
                            scrol_y.config(command=ders_bilgileri_agaci.yview)

                            ders_bilgileri_agaci['show']='headings'
                            ders_bilgileri_agaci.heading('no',text='No')
                            ders_bilgileri_agaci.heading('kod',text='Ders Kodu')
                            ders_bilgileri_agaci.heading('ad',text='Ders Adı')
                            ders_bilgileri_agaci.heading('sayi',text='Öğrenci Sayısı')
                            
                            ders_bilgileri_agaci.column('no',width=35,anchor='center')
                            ders_bilgileri_agaci.column('kod',width=210,anchor='center')
                            ders_bilgileri_agaci.column('ad',width=415,anchor='center')
                            ders_bilgileri_agaci.column('sayi',width=210,anchor='center')

                            def puan_ekleme_fonk(event):
                                cursor_row=ders_bilgileri_agaci.focus()
                                contents=ders_bilgileri_agaci.item(cursor_row)
                                row=contents['values']
                                print(row)

                                ders_bilgileri_agaci.destroy()
                                scrol_x.destroy()
                                scrol_y.destroy()

                                lbl_ders_adi=Label(Akademisyen_sayfasi.frame_ders_bilgileri,text=row[2]+" Dersini Alan Öğrenciler",bg="#27374D",fg="#DDE6ED",font=('calisto mt',30,'bold'))
                                lbl_ders_adi.pack(fill=X)

                                scrol_x_puan=Scrollbar(Akademisyen_sayfasi.frame_ders_bilgileri,orient=HORIZONTAL)
                                scrol_y_puan=Scrollbar(Akademisyen_sayfasi.frame_ders_bilgileri,orient=VERTICAL)
                                puan_verme_agaci=ttk.Treeview(Akademisyen_sayfasi.frame_ders_bilgileri,
                                                            columns=('no','ogr_no','ad','vize','final','ort'),
                                                            xscrollcommand=scrol_x_puan.set,
                                                            yscrollcommand=scrol_y_puan.set,)
                                
                                puan_verme_agaci.place(x=0,y=50,width=1299,height=695)
                                scrol_x_puan.pack(side=BOTTOM,fill=X)
                                scrol_y_puan.pack(side=RIGHT,fill=Y)
                                scrol_x_puan.config(command=puan_verme_agaci.xview)
                                scrol_y_puan.config(command=puan_verme_agaci.yview)

                                puan_verme_agaci['show']='headings'
                                puan_verme_agaci.heading('no',text='No')
                                puan_verme_agaci.heading('ogr_no',text='Öğrenci No')
                                puan_verme_agaci.heading('ad',text='Öğrenci Adı')
                                puan_verme_agaci.heading('vize',text='Vize Notu')
                                puan_verme_agaci.heading('final',text='Final Notu')
                                puan_verme_agaci.heading('ort',text='Ortalama')
                                
                                puan_verme_agaci.column('no',width=35,anchor='center')
                                puan_verme_agaci.column('ogr_no',width=120,anchor='center')
                                puan_verme_agaci.column('ad',width=415,anchor='center')
                                puan_verme_agaci.column('vize',width=120,anchor='center')
                                puan_verme_agaci.column('final',width=120,anchor='center')
                                puan_verme_agaci.column('ort',width=120,anchor='center')

                                cr.execute(f"SELECT Ders_Id FROM Dersler where Ders_Ad='{row[2]}' AND Ders_Kodu='{row[1]}'")
                                sonuc_1=cr.fetchone()
                                print(sonuc_1)
                                cr.execute(f"SELECT Ogr_No,Vize_Puan,Final_Puan FROM Puan where Ders_Id={sonuc_1[0]}")
                                sonuc_2=cr.fetchall()
                                print(sonuc_2)

                                Ogrenci_Adlari=[]
                                

                                
                                for i in range(len(sonuc_2)):
                                    #cr.execute(f"CREATE VIEW sonuc_2 AS SELECT Ogr_Ad, Ogr_Soyad")
                                    cr.execute(f"SELECT Ogr_Ad, Ogr_Soyad FROM Ogrenciler WHERE Ogr_No={sonuc_2[i][0]}")
                                    sonuc_3=cr.fetchone()
                                    print(sonuc_3)
                                    Ogrenci_Adlari.append(sonuc_3[0] + " " + sonuc_3[1])
                                    #dersi_alan_ogrenciler = cr.fetchall()

                                    ders_bilgileri = []
                                    
                                    # Elemanları alt liste içine ekle
                                    ders_bilgileri.append(i + 1)  # Sıra numarası ekle
                                    ders_bilgileri.append(sonuc_2[i][0])  # ogr no
                                    ders_bilgileri.append(Ogrenci_Adlari[i])  # ogr ad
                                    if(sonuc_2[i][1]==None):
                                        ders_bilgileri.append("")  # vize
                                    else:
                                        ders_bilgileri.append(sonuc_2[i][1])  # vize

                                    if(sonuc_2[i][2]==None):
                                        ders_bilgileri.append("")  # final
                                    else:
                                        ders_bilgileri.append(sonuc_2[i][2])  # final
                                    try:
                                        ders_bilgileri.append(sonuc_2[i][1]*0.4+sonuc_2[i][2]*0.6)  # ort
                                    except:
                                        ders_bilgileri.append("")  # ort

                                    puan_verme_agaci.insert("", END, values=ders_bilgileri)
                                
                                


                                def puan_ekleme_sayfasi(event):
                                    cursor_row_1=puan_verme_agaci.focus()
                                    contents_1=puan_verme_agaci.item(cursor_row_1)
                                    row_1=contents_1['values']
                                    print("-----------------")
                                    print(row_1)
                                    print("-----------------")


                                    x, y, width, height = puan_verme_agaci.bbox(cursor_row_1)
                                    column = puan_verme_agaci.identify_column(event.x)
                                    print(x,y,width,height)
                                    print(column)
                                    

                                    if(int(column[1])==4):
                                        entry = Entry(puan_verme_agaci,justify='center')
                                        entry.place(x=754, y=y, width=181, height=height)
                                        entry.insert(0, row_1[3]) 
                                        def save_changes():
                                            new_value = entry.get()  
                                            puan_verme_agaci.set(cursor_row_1, column, new_value) 
                                            cr.execute(f"update  Puan set Vize_Puan='{int(entry.get().strip())}' where Ogr_No='{row_1[1]}' and Ders_Id='{sonuc_1[0]}'")
                                            db.commit()
                                            button.destroy()
                                            entry.destroy()
                                        button = Button(puan_verme_agaci, text="Kaydet", command=save_changes)
                                        button.place(x=820, y=y+height)

                                    elif(int(column[1])==5):
                                        entry = Entry(puan_verme_agaci,justify='center')
                                        entry.place(x=935, y=y, width=183, height=height)
                                        entry.insert(0, row_1[4])  
                                        def save_changes():
                                            new_value = entry.get()  
                                            puan_verme_agaci.set(cursor_row_1, column, new_value)
                                            cr.execute(f"update  Puan set Final_Puan='{int(entry.get().strip())}' where Ogr_No='{row_1[1]}' and Ders_Id='{sonuc_1[0]}'")
                                            db.commit()
                                            button.destroy()
                                            entry.destroy()
                                        button = Button(puan_verme_agaci, text="Kaydet", command=save_changes)
                                        button.place(x=1000, y=y+height)


                                    

                                puan_verme_agaci.bind("<ButtonRelease-1>",puan_ekleme_sayfasi)




                            ders_bilgileri_agaci.bind("<ButtonRelease-1>",puan_ekleme_fonk)


                            cr.execute(f"SELECT Ders_Id, Ders_Kodu, Ders_Ad from Dersler where Ogrt_No='{kul_adi.get().strip()}'")
                            ders_bilgi=cr.fetchall()


                            son_liste = []
                            for i in range(len(ders_bilgi)):
                                cr.execute(f"SELECT Ogr_no FROM Puan WHERE Ders_Id={ders_bilgi[i][0]}")
                                dersi_alan_ogrenciler = cr.fetchall()

                                ders_bilgileri = []
                                
                                # Elemanları alt liste içine ekle
                                ders_bilgileri.append(i + 1)  # Sıra numarası ekle
                                ders_bilgileri.append(ders_bilgi[i][1])  # Ders kodu ekle
                                ders_bilgileri.append(ders_bilgi[i][2])  # Ders adı ekle
                                ders_bilgileri.append(len(dersi_alan_ogrenciler))  # Ogrenci sayisi ekle
                                

                                # Oluşturulan alt listeyi 'son_liste' listesine ekle
                                son_liste.append(ders_bilgileri)
                                

                            if(len(son_liste)!=0):
                                for alt_liste in son_liste:
                                    ders_bilgileri_agaci.insert("", END, values=alt_liste)

                            
                            label_ogrenciler=Label(Akademisyen_sayfasi.frame_ders_bilgileri,
                            text='Dersi Alan Öğrencileri Görüntülemek Ve Puanlarının Vermek İçin Dersin Üzerine Tıklayınız',
                            bg='#DDE6ED',
                            fg='#526D82',
                            font=('calisto mt',18,'bold'))
                            label_ogrenciler.place(x=140,y=600)

                            
                        
                        def arama_islemleri_fonksiyonu():

                            try:
                                Akademisyen_sayfasi.frame_ders_bilgileri.destroy()
                            except:
                                pass

                            Akademisyen_sayfasi.arama_bilgileri_frame=Frame(frame_ust,bg='#9DB2BF')
                            Akademisyen_sayfasi.arama_bilgileri_frame.place(x=0,y=0,width=900,height=45)
                            
                            title_left63=Label(Akademisyen_sayfasi.arama_bilgileri_frame,
                            text='Öğrenci Arama',
                            bg='#526D82',
                            fg='#DDE6ED',
                            font=('calisto mt',15,'bold'))
                            title_left63.place(x=0,y=0,width=250,height=49)


                            search=StringVar()
                            i_search=StringVar()
                            i_search_yedek=StringVar()

                            combo_ogr_s=ttk.Combobox(Akademisyen_sayfasi.arama_bilgileri_frame,state='readonly',textvariable=search)
                            combo_ogr_s['value']=('Tüm Öğrenciler','Öğrenci No İle Arama','Öğrenci Adı İle Arama', 'Ders Adı İle Arama', 'Bölüm Adı İle Arama','Sınıf İle Arama')
                            combo_ogr_s.place(x=275,y=6,width=180,height=35)




                            def on_entry_click_arama(event):
                                if en_search.get() == "Arama":
                                    en_search.delete(0, END)
                                    en_search.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)

                            def on_entry_click_arama_yedek(event):
                                if en_search.get() == "Sınıf":
                                    en_search.delete(0, END)
                                    en_search.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)       
                        


                            en_search=Entry(Akademisyen_sayfasi.arama_bilgileri_frame,bd='2',fg='grey',justify='center',textvariable=i_search)
                            en_search.place(x=500,y=6,width=200,height=35)
                            en_search.insert(0, "Arama")
                            en_search.bind("<FocusIn>", on_entry_click_arama)

                            def update_buttons(*args):
                                        selected_option = search.get()
                                        print(f"Selected option: {selected_option}")    
                                        if selected_option == 'Sınıf İle Arama':
                                            Akademisyen_sayfasi.search_but.place(x=800, y=6, width=150, height=35)
                                            en_search.place(x=650, y=6, width=150, height=35)
                                            en_search.delete(0, END)
                                            en_search.insert(0, "Sınıf")
                                            en_search.bind("<FocusIn>", on_entry_click_arama_yedek)


                                            def on_entry_click_arama_asdfg(event):
                                                if update_buttons.en_search_1.get() == "Bölüm":
                                                    update_buttons.en_search_1.delete(0, END)
                                                    update_buttons.en_search_1.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)

                                            update_buttons.en_search_1=Entry(Akademisyen_sayfasi.arama_bilgileri_frame,bd='2',fg='grey',justify='center',textvariable=i_search_yedek)
                                            update_buttons.en_search_1.place(x=480,y=6,width=150,height=35)
                                            update_buttons.en_search_1.insert(0, "Bölüm")
                                            update_buttons.en_search_1.bind("<FocusIn>", on_entry_click_arama_asdfg)

                                        else:
                                            
                                            try:
                                                update_buttons.en_search_1.destroy()
                                                en_search.place(x=500,y=6,width=200,height=35)
                                                en_search.delete(0, END)
                                                en_search.insert(0, "Arama")
                                                en_search.bind("<FocusIn>", on_entry_click_arama)
                                            except:
                                                print("kkkkkkkkkkkkkkkkkkkkkkkk")
                                            arama_sayfasi()

                            combo_ogr_s.bind("<<ComboboxSelected>>", update_buttons)
                            



                            def arama_sayfasi():
                                if(search.get()=='Tüm Öğrenciler'):
                                    cr.execute("SELECT * FROM Ogrenciler")
                                    sonuc_arama_sayfasi=cr.fetchall()

                                    frame_arama_sayfasi=Frame(frame_orta,bg='#27374D')
                                    frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                    scrol_x_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=HORIZONTAL)
                                    scrol_y_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=VERTICAL)

                                    arama_sayfasi_table=ttk.Treeview(frame_arama_sayfasi,
                                                                    columns=('no','ogr_no','ad','tc','tarih','cinsiyet','tel','email','bolum','sinif'),
                                                                    xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                    yscrollcommand=scrol_y_arama_sayfasi.set,)
                                    
                                    arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                    scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                    scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                    scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                    scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                    arama_sayfasi_table['show']='headings'
                                    arama_sayfasi_table.heading('no',text='No')
                                    arama_sayfasi_table.heading('ogr_no',text='Öğrenci No')
                                    arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                    arama_sayfasi_table.heading('tc',text='TC')
                                    arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                    arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                    arama_sayfasi_table.heading('tel',text='Tel No')
                                    arama_sayfasi_table.heading('email',text='Email')
                                    arama_sayfasi_table.heading('bolum',text='Bölümü')
                                    arama_sayfasi_table.heading('sinif',text='Sınıfı')

                                    arama_sayfasi_table.column('no',width=25,anchor='center')
                                    arama_sayfasi_table.column('ogr_no',width=60,anchor='center')
                                    arama_sayfasi_table.column('ad',width=215,anchor='center')
                                    arama_sayfasi_table.column('tc',width=100,anchor='center')
                                    arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                    arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                    arama_sayfasi_table.column('tel',width=91,anchor='center')
                                    arama_sayfasi_table.column('email',width=230,anchor='center')
                                    arama_sayfasi_table.column('bolum',width=230,anchor='center')
                                    arama_sayfasi_table.column('sinif',width=45,anchor='center')

                                    
                                    
                                    if(len(sonuc_arama_sayfasi)!=0):
                                        arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                        arama_eklenecek_liste_son=[]
                                        for i in range(len(sonuc_arama_sayfasi)):


                                            arama_eklenecek_liste=[]
                                            arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2]+" "+sonuc_arama_sayfasi[i][3])  # Ad soyad
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # Cinsiyet
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # tel
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][7])  # Email

                                            cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Id={sonuc_arama_sayfasi[i][9]}")
                                            sonuc_arama_sayfasi_bolum_adlari=cr.fetchone()
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi_bolum_adlari[0])#bolum

                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][10]) # sinif

                                            arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                        for row in arama_eklenecek_liste_son:
                                            arama_sayfasi_table.insert("",END, value=row)


                                elif(search.get()=='Öğrenci No İle Arama' or ''):
                                    cr.execute(f"SELECT * FROM Ogrenciler where Ogr_No='{i_search.get().strip()}'")
                                    sonuc_arama_sayfasi=cr.fetchall()

                                    frame_arama_sayfasi=Frame(frame_orta,bg='#27374D')
                                    frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                    scrol_x_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=HORIZONTAL)
                                    scrol_y_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=VERTICAL)

                                    arama_sayfasi_table=ttk.Treeview(frame_arama_sayfasi,
                                                                    columns=('no','ogr_no','ad','tc','tarih','cinsiyet','tel','email','bolum','sinif'),
                                                                    xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                    yscrollcommand=scrol_y_arama_sayfasi.set,)
                                    
                                    arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                    scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                    scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                    scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                    scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                    arama_sayfasi_table['show']='headings'
                                    arama_sayfasi_table.heading('no',text='No')
                                    arama_sayfasi_table.heading('ogr_no',text='Öğrenci No')
                                    arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                    arama_sayfasi_table.heading('tc',text='TC')
                                    arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                    arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                    arama_sayfasi_table.heading('tel',text='Tel No')
                                    arama_sayfasi_table.heading('email',text='Email')
                                    arama_sayfasi_table.heading('bolum',text='Bölümü')
                                    arama_sayfasi_table.heading('sinif',text='Sınıfı')

                                    arama_sayfasi_table.column('no',width=25,anchor='center')
                                    arama_sayfasi_table.column('ogr_no',width=60,anchor='center')
                                    arama_sayfasi_table.column('ad',width=215,anchor='center')
                                    arama_sayfasi_table.column('tc',width=100,anchor='center')
                                    arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                    arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                    arama_sayfasi_table.column('tel',width=91,anchor='center')
                                    arama_sayfasi_table.column('email',width=230,anchor='center')
                                    arama_sayfasi_table.column('bolum',width=230,anchor='center')
                                    arama_sayfasi_table.column('sinif',width=45,anchor='center')

                                    

                                    if(len(sonuc_arama_sayfasi)!=0):
                                        arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                        arama_eklenecek_liste_son=[]
                                        for i in range(len(sonuc_arama_sayfasi)):


                                            arama_eklenecek_liste=[]
                                            arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2]+" "+sonuc_arama_sayfasi[i][3])  # Ad soyad
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # Cinsiyet
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # tel
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][7])  # Email

                                            cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Id={sonuc_arama_sayfasi[i][9]}")
                                            sonuc_arama_sayfasi_bolum_adlari=cr.fetchone()
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi_bolum_adlari[0])#bolum

                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][10]) # sinif

                                            arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                        for row in arama_eklenecek_liste_son:
                                            arama_sayfasi_table.insert("",END, value=row)


                                elif(search.get()=='Öğrenci Adı İle Arama'):
                                    '''cr.execute(f"SELECT Ogr_Id, Ogr_Ad, Ogr_Soyad FROM Ogrenciler")
                                    sonuc_0=cr.fetchall()

                                    sonuc_01=[]
                                    for row in sonuc_0:
                                        sonuc_02=[]
                                        sonuc_02.append(sonuc_0[row][0])
                                        sonuc_02.append(sonuc_0[row][1]+" "+sonuc_0[row][2])
                                        sonuc_01.append(sonuc_02)'''

                                    cr.execute(f"SELECT * FROM Ogrenciler where Ogr_ad LIKE '%{i_search.get().title().strip()}%'")
                                    sonuc_arama_sayfasi=cr.fetchall()

                                    frame_arama_sayfasi=Frame(frame_orta,bg='#27374D')
                                    frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                    scrol_x_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=HORIZONTAL)
                                    scrol_y_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=VERTICAL)

                                    arama_sayfasi_table=ttk.Treeview(frame_arama_sayfasi,
                                                                    columns=('no','ogr_no','ad','tc','tarih','cinsiyet','tel','email','bolum','sinif'),
                                                                    xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                    yscrollcommand=scrol_y_arama_sayfasi.set,)
                                    
                                    arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                    scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                    scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                    scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                    scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                    arama_sayfasi_table['show']='headings'
                                    arama_sayfasi_table.heading('no',text='No')
                                    arama_sayfasi_table.heading('ogr_no',text='Öğrenci No')
                                    arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                    arama_sayfasi_table.heading('tc',text='TC')
                                    arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                    arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                    arama_sayfasi_table.heading('tel',text='Tel No')
                                    arama_sayfasi_table.heading('email',text='Email')
                                    arama_sayfasi_table.heading('bolum',text='Bölümü')
                                    arama_sayfasi_table.heading('sinif',text='Sınıfı')

                                    arama_sayfasi_table.column('no',width=25,anchor='center')
                                    arama_sayfasi_table.column('ogr_no',width=60,anchor='center')
                                    arama_sayfasi_table.column('ad',width=215,anchor='center')
                                    arama_sayfasi_table.column('tc',width=100,anchor='center')
                                    arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                    arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                    arama_sayfasi_table.column('tel',width=91,anchor='center')
                                    arama_sayfasi_table.column('email',width=230,anchor='center')
                                    arama_sayfasi_table.column('bolum',width=230,anchor='center')
                                    arama_sayfasi_table.column('sinif',width=45,anchor='center')

                                    
                                    
                                    if(len(sonuc_arama_sayfasi)!=0):
                                        arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                        arama_eklenecek_liste_son=[]
                                        for i in range(len(sonuc_arama_sayfasi)):


                                            arama_eklenecek_liste=[]
                                            arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2]+" "+sonuc_arama_sayfasi[i][3])  # Ad soyad
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # Cinsiyet
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # tel
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][7])  # Email

                                            cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Id={sonuc_arama_sayfasi[i][9]}")
                                            sonuc_arama_sayfasi_bolum_adlari=cr.fetchone()
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi_bolum_adlari[0])#bolum

                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][10]) # sinif

                                            arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                        for row in arama_eklenecek_liste_son:
                                            arama_sayfasi_table.insert("",END, value=row)

                                elif(search.get()=='Ders Adı İle Arama'):
                                    cr.execute(f"SELECT Ders_Id FROM Dersler where Ders_Ad LIKE '%{i_search.get().strip()}%'")
                                    sonuc_1=cr.fetchone()
                                    print(sonuc_1)
                                    cr.execute(f"SELECT Ogr_no FROM Puan where Ders_Id={sonuc_1[0]}")
                                    sonuc_2=cr.fetchall()
                                    print(sonuc_2)


                                    sonuc_arama_sayfasi=[]
                                    for i in range(len(sonuc_2)):
                                        cr.execute(f"SELECT * FROM Ogrenciler where Ogr_No={sonuc_2[i][0]}")
                                        sonuc_3=cr.fetchall()
                                        sonuc_arama_sayfasi.append(sonuc_3)
                                    print(sonuc_arama_sayfasi)


                                    frame_arama_sayfasi=Frame(frame_orta,bg='#27374D')
                                    frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                    scrol_x_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=HORIZONTAL)
                                    scrol_y_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=VERTICAL)

                                    arama_sayfasi_table=ttk.Treeview(frame_arama_sayfasi,
                                                                    columns=('no','ogr_no','ad','tc','tarih','cinsiyet','tel','email','bolum','sinif'),
                                                                    xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                    yscrollcommand=scrol_y_arama_sayfasi.set,)
                                    
                                    arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                    scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                    scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                    scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                    scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                    arama_sayfasi_table['show']='headings'
                                    arama_sayfasi_table.heading('no',text='No')
                                    arama_sayfasi_table.heading('ogr_no',text='Öğrenci No')
                                    arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                    arama_sayfasi_table.heading('tc',text='TC')
                                    arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                    arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                    arama_sayfasi_table.heading('tel',text='Tel No')
                                    arama_sayfasi_table.heading('email',text='Email')
                                    arama_sayfasi_table.heading('bolum',text='Bölümü')
                                    arama_sayfasi_table.heading('sinif',text='Sınıfı')

                                    arama_sayfasi_table.column('no',width=25,anchor='center')
                                    arama_sayfasi_table.column('ogr_no',width=60,anchor='center')
                                    arama_sayfasi_table.column('ad',width=215,anchor='center')
                                    arama_sayfasi_table.column('tc',width=100,anchor='center')
                                    arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                    arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                    arama_sayfasi_table.column('tel',width=91,anchor='center')
                                    arama_sayfasi_table.column('email',width=230,anchor='center')
                                    arama_sayfasi_table.column('bolum',width=230,anchor='center')
                                    arama_sayfasi_table.column('sinif',width=45,anchor='center')

                                    
                                    cr.execute(f"SELECT Ders_Id FROM Dersler where Ders_Ad LIKE '%{i_search.get().strip()}%'")
                                    sonuc_1=cr.fetchone()
                                    if(len(sonuc_arama_sayfasi)!=0):
                                        arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                        arama_eklenecek_liste_son=[]
                                        for i in range(len(sonuc_arama_sayfasi)):


                                            arama_eklenecek_liste=[]
                                            arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][0])  # Ogrenci no
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][2]+" "+sonuc_arama_sayfasi[i][0][3])  # Ad soyad
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][1])  # TC
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][4])  # Dogum Tarihi
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][5])  # Cinsiyet
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][6])  # tel
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][7])  # Email

                                            cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Id={sonuc_arama_sayfasi[i][0][9]}")
                                            sonuc_arama_sayfasi_bolum_adlari=cr.fetchone()
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi_bolum_adlari[0])#bolum

                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][10]) # sinif

                                            arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                        for row in arama_eklenecek_liste_son:
                                            arama_sayfasi_table.insert("",END, value=row)

                                elif(search.get()=='Bölüm Adı İle Arama'):
                                    cr.execute(f"SELECT Bolum_Id FROM Bolumler where Bolum_Ad LIKE '%{i_search.get().strip()}%'")
                                    sonuc_1=cr.fetchone()
                                    print(sonuc_1)
                                    cr.execute(f"SELECT Ogr_no FROM Ogrenciler where Bolum_Id={sonuc_1[0]}")
                                    sonuc_2=cr.fetchall()
                                    print(sonuc_2)


                                    sonuc_arama_sayfasi=[]
                                    for i in range(len(sonuc_2)):
                                        cr.execute(f"SELECT * FROM Ogrenciler where Ogr_No={sonuc_2[i][0]}")
                                        sonuc_3=cr.fetchall()
                                        sonuc_arama_sayfasi.append(sonuc_3)
                                    print(sonuc_arama_sayfasi)


                                    frame_arama_sayfasi=Frame(frame_orta,bg='#27374D')
                                    frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                    scrol_x_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=HORIZONTAL)
                                    scrol_y_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=VERTICAL)

                                    arama_sayfasi_table=ttk.Treeview(frame_arama_sayfasi,
                                                                    columns=('no','ogr_no','ad','tc','tarih','cinsiyet','tel','email','bolum','sinif'),
                                                                    xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                    yscrollcommand=scrol_y_arama_sayfasi.set,)
                                    
                                    arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                    scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                    scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                    scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                    scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                    arama_sayfasi_table['show']='headings'
                                    arama_sayfasi_table.heading('no',text='No')
                                    arama_sayfasi_table.heading('ogr_no',text='Öğrenci No')
                                    arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                    arama_sayfasi_table.heading('tc',text='TC')
                                    arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                    arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                    arama_sayfasi_table.heading('tel',text='Tel No')
                                    arama_sayfasi_table.heading('email',text='Email')
                                    arama_sayfasi_table.heading('bolum',text='Bölümü')
                                    arama_sayfasi_table.heading('sinif',text='Sınıfı')

                                    arama_sayfasi_table.column('no',width=25,anchor='center')
                                    arama_sayfasi_table.column('ogr_no',width=60,anchor='center')
                                    arama_sayfasi_table.column('ad',width=215,anchor='center')
                                    arama_sayfasi_table.column('tc',width=100,anchor='center')
                                    arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                    arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                    arama_sayfasi_table.column('tel',width=91,anchor='center')
                                    arama_sayfasi_table.column('email',width=230,anchor='center')
                                    arama_sayfasi_table.column('bolum',width=230,anchor='center')
                                    arama_sayfasi_table.column('sinif',width=45,anchor='center')

                                    
                                 
                                    if(len(sonuc_arama_sayfasi)!=0):
                                        arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                        arama_eklenecek_liste_son=[]
                                        for i in range(len(sonuc_arama_sayfasi)):


                                            arama_eklenecek_liste=[]
                                            arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][0])  # Ogrenci no
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][2]+" "+sonuc_arama_sayfasi[i][0][3])  # Ad soyad
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][1])  # TC
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][4])  # Dogum Tarihi
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][5])  # Cinsiyet
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][6])  # tel
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][7])  # Email

                                            cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Id={sonuc_arama_sayfasi[i][0][9]}")
                                            sonuc_arama_sayfasi_bolum_adlari=cr.fetchone()
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi_bolum_adlari[0])#bolum

                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][10]) # sinif

                                            arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                        for row in arama_eklenecek_liste_son:
                                            arama_sayfasi_table.insert("",END, value=row)


                                elif(search.get()=='Ders Adı İle Arama'):
                                    cr.execute(f"SELECT Ders_Id FROM Dersler where Ders_Ad LIKE '%{i_search.get().strip()}%'")
                                    sonuc_1=cr.fetchone()
                                    print(sonuc_1)
                                    cr.execute(f"SELECT Ogr_no FROM Puan where Ders_Id={sonuc_1[0]}")
                                    sonuc_2=cr.fetchall()
                                    print(sonuc_2)


                                    sonuc_arama_sayfasi=[]
                                    for i in range(len(sonuc_2)):
                                        cr.execute(f"SELECT * FROM Ogrenciler where Ogr_No={sonuc_2[i][0]}")
                                        sonuc_3=cr.fetchall()
                                        sonuc_arama_sayfasi.append(sonuc_3)
                                    print(sonuc_arama_sayfasi)


                                    frame_arama_sayfasi=Frame(frame_orta,bg='#27374D')
                                    frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                    scrol_x_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=HORIZONTAL)
                                    scrol_y_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=VERTICAL)

                                    arama_sayfasi_table=ttk.Treeview(frame_arama_sayfasi,
                                                                    columns=('no','ogr_no','ad','tc','tarih','cinsiyet','tel','email','bolum','sinif'),
                                                                    xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                    yscrollcommand=scrol_y_arama_sayfasi.set,)
                                    
                                    arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                    scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                    scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                    scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                    scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                    arama_sayfasi_table['show']='headings'
                                    arama_sayfasi_table.heading('no',text='No')
                                    arama_sayfasi_table.heading('ogr_no',text='Öğrenci No')
                                    arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                    arama_sayfasi_table.heading('tc',text='TC')
                                    arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                    arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                    arama_sayfasi_table.heading('tel',text='Tel No')
                                    arama_sayfasi_table.heading('email',text='Email')
                                    arama_sayfasi_table.heading('bolum',text='Bölümü')
                                    arama_sayfasi_table.heading('sinif',text='Sınıfı')

                                    arama_sayfasi_table.column('no',width=25,anchor='center')
                                    arama_sayfasi_table.column('ogr_no',width=60,anchor='center')
                                    arama_sayfasi_table.column('ad',width=215,anchor='center')
                                    arama_sayfasi_table.column('tc',width=100,anchor='center')
                                    arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                    arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                    arama_sayfasi_table.column('tel',width=91,anchor='center')
                                    arama_sayfasi_table.column('email',width=230,anchor='center')
                                    arama_sayfasi_table.column('bolum',width=230,anchor='center')
                                    arama_sayfasi_table.column('sinif',width=45,anchor='center')

                                    
                                    
                                    if(len(sonuc_arama_sayfasi)!=0):
                                        arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                        arama_eklenecek_liste_son=[]
                                        for i in range(len(sonuc_arama_sayfasi)):


                                            arama_eklenecek_liste=[]
                                            arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][0])  # Ogrenci no
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][2]+" "+sonuc_arama_sayfasi[i][0][3])  # Ad soyad
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][1])  # TC
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][4])  # Dogum Tarihi
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][5])  # Cinsiyet
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][6])  # tel
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][7])  # Email

                                            cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Id={sonuc_arama_sayfasi[i][0][9]}")
                                            sonuc_arama_sayfasi_bolum_adlari=cr.fetchone()
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi_bolum_adlari[0])#bolum

                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][10]) # sinif

                                            arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                        for row in arama_eklenecek_liste_son:
                                            arama_sayfasi_table.insert("",END, value=row)

                                elif(search.get()=='Sınıf İle Arama'):

                                    cr.execute(f"SELECT Bolum_Id FROM Bolumler WHERE Bolum_Ad LIKE '%{i_search_yedek.get().strip()}%'")
                                    sonuc_0=cr.fetchone()

                                    cr.execute(f"SELECT * FROM Ogrenciler where Ogr_Sinif='{i_search.get().strip()}' AND Bolum_Id='{sonuc_0[0]}'")
                                    sonuc_arama_sayfasi=cr.fetchall()

                                    frame_arama_sayfasi=Frame(frame_orta,bg='#27374D')
                                    frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                    scrol_x_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=HORIZONTAL)
                                    scrol_y_arama_sayfasi=Scrollbar(frame_arama_sayfasi,orient=VERTICAL)

                                    arama_sayfasi_table=ttk.Treeview(frame_arama_sayfasi,
                                                                    columns=('no','ogr_no','ad','tc','tarih','cinsiyet','tel','email','bolum','sinif'),
                                                                    xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                    yscrollcommand=scrol_y_arama_sayfasi.set,)
                                    
                                    arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                    scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                    scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                    scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                    scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                    arama_sayfasi_table['show']='headings'
                                    arama_sayfasi_table.heading('no',text='No')
                                    arama_sayfasi_table.heading('ogr_no',text='Öğrenci No')
                                    arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                    arama_sayfasi_table.heading('tc',text='TC')
                                    arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                    arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                    arama_sayfasi_table.heading('tel',text='Tel No')
                                    arama_sayfasi_table.heading('email',text='Email')
                                    arama_sayfasi_table.heading('bolum',text='Bölümü')
                                    arama_sayfasi_table.heading('sinif',text='Sınıfı')

                                    arama_sayfasi_table.column('no',width=25,anchor='center')
                                    arama_sayfasi_table.column('ogr_no',width=60,anchor='center')
                                    arama_sayfasi_table.column('ad',width=215,anchor='center')
                                    arama_sayfasi_table.column('tc',width=100,anchor='center')
                                    arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                    arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                    arama_sayfasi_table.column('tel',width=91,anchor='center')
                                    arama_sayfasi_table.column('email',width=230,anchor='center')
                                    arama_sayfasi_table.column('bolum',width=230,anchor='center')
                                    arama_sayfasi_table.column('sinif',width=45,anchor='center')

                                    
                                   
                                    if(len(sonuc_arama_sayfasi)!=0):
                                        arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                        arama_eklenecek_liste_son=[]
                                        for i in range(len(sonuc_arama_sayfasi)):


                                            arama_eklenecek_liste=[]
                                            arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2]+" "+sonuc_arama_sayfasi[i][3])  # Ad soyad
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # Cinsiyet
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # tel
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][7])  # Email

                                            cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Id={sonuc_arama_sayfasi[i][9]}")
                                            sonuc_arama_sayfasi_bolum_adlari=cr.fetchone()
                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi_bolum_adlari[0])#bolum

                                            arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][10]) # sinif

                                            arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                        for row in arama_eklenecek_liste_son:
                                            arama_sayfasi_table.insert("",END, value=row)


                            Akademisyen_sayfasi.search_but=Button(Akademisyen_sayfasi.arama_bilgileri_frame,text='Ara',font=10,bg='#526D82',fg='#DDE6ED',command=arama_sayfasi)
                            Akademisyen_sayfasi.search_but.place(x=720,y=6,width=200,height=35)


                                




                        def kapatma():
                            try:
                                self.omer.destroy()
                            except:
                                pass
                        

                        def change_color_ders_bilgileri_btn1(event):
                            ders_bilgileri_btn.config(bg="#526D82", fg="#DDE6ED")  
                        def change_color_ders_bilgileri_btn2(event):
                            ders_bilgileri_btn.config(bg="#27374D", fg="#DDE6ED")
                        ders_bilgileri_btn=Button(frame_b,text='Ders Bilgileri',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0, command=ders_bilgileri_fonksiyonu)
                        ders_bilgileri_btn.place(x=5,y=50,width=207,height=40)
                        ders_bilgileri_btn.bind("<Enter>", change_color_ders_bilgileri_btn1)
                        ders_bilgileri_btn.bind("<Leave>", change_color_ders_bilgileri_btn2)

                        def change_color_Ders_programi_btn1(event):
                            Ders_programi_btn.config(bg="#526D82", fg="#DDE6ED")
                        def change_color_Ders_programi_btn2(event):
                            Ders_programi_btn.config(bg="#27374D", fg="#DDE6ED")
                        Ders_programi_btn=Button(frame_b,text='Arama İşlemleri',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0, command=arama_islemleri_fonksiyonu)
                        Ders_programi_btn.place(x=5,y=95,width=207,height=40)
                        Ders_programi_btn.bind("<Enter>", change_color_Ders_programi_btn1)
                        Ders_programi_btn.bind("<Leave>", change_color_Ders_programi_btn2)

                        def change_color_exit_btn1(event):
                            exit_btn.config(bg="#526D82", fg="#DDE6ED")  
                        def change_color_exit_btn2(event):
                            exit_btn.config(bg="#27374D", fg="#DDE6ED")
                        exit_btn=Button(frame_b,text='Programı Kapat',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=kapatma)
                        exit_btn.place(x=5,y=140,width=207,height=40)
                        exit_btn.bind("<Enter>", change_color_exit_btn1)  
                        exit_btn.bind("<Leave>", change_color_exit_btn2) 




                        cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad from Ogretmenler WHERE Ogrt_No='{kul_adi.get().strip()}'")
                        prof_ad_soyad=cr.fetchall()
                        def def_profil_sayfasi():
                            profil = Frame(self.omer,bg="blue")
                            profil.place(x=1150,y=80,width=380,height=360)

                            profil1 = Frame(profil,bg="#9DB2BF")
                            profil1.place(x=0,y=32,width=150,height=360)

                            profil_lbl_no=Label(profil1,text='Akademisyen No : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))         #no
                            profil_lbl_no.place(x=4,y=20)               
                            profil_lbl_ad_soyad=Label(profil1,text='Ad Soyad                : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))   #ad soyad
                            profil_lbl_ad_soyad.place(x=4,y=55)
                            profil_lbl_tc=Label(profil1,text='TC No                       : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))            #TC
                            profil_lbl_tc.place(x=4,y=90)
                            profil_lbl_dogum=Label(profil1,text='Doğum Tarihi        : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))  #Dogum
                            profil_lbl_dogum.place(x=4,y=125)
                            profil_lbl_tel=Label(profil1,text='Tel. No                    : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))         #Tel
                            profil_lbl_tel.place(x=4,y=160)
                            profil_lbl_eposta=Label(profil1,text='Eposta                     : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))       #Eposta
                            profil_lbl_eposta.place(x=4,y=195)
                            profil_lbl_cinsiyet=Label(profil1,text='Cinsiyet                  : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))   #Cinsiyet
                            profil_lbl_cinsiyet.place(x=4,y=230)


                            profil2 = Frame(profil,bg="#9DB2BF")
                            profil2.place(x=150,y=32,width=230,height=360)

                            cr.execute(f"SELECT Ogrt_Tc, Ogrt_DT, Ogrt_TelNo, Ogrt_Eposta, Ogrt_Cinsiyeti from Ogretmenler where Ogrt_No='{kul_adi.get()}'")
                            prof_db=cr.fetchall()

                            profil_db_no=Label(profil2,text=kul_adi.get().strip(),bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold")) #no
                            profil_db_no.place(x=4,y=20)
                            profil_db_ad_soyad=Label(profil2,text=prof_ad_soyad[0][0]+" "+ prof_ad_soyad[0][1],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))    #ad soyad
                            profil_db_ad_soyad.place(x=4,y=55)
                            profil_db_tc=Label(profil2,text=prof_db[0][0],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))         #TC
                            profil_db_tc.place(x=4,y=90)
                            profil_db_dogum=Label(profil2,text=prof_db[0][1],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))      #Dogum
                            profil_db_dogum.place(x=4,y=125)
                            profil_db_tel=Label(profil2,text=prof_db[0][2],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))        #Tel
                            profil_db_tel.place(x=4,y=160)
                            profil_db_eposta=Label(profil2,text=prof_db[0][3],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))     #Eposta
                            profil_db_eposta.place(x=4,y=195)
                            profil_db_cinsiyet=Label(profil2,text=prof_db[0][4],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))   #Cinsiyet
                            profil_db_cinsiyet.place(x=4,y=230)

                            def ana():
                                self.omer.destroy()
                                os.system("python Proje.py")
                                
                                


                            profil_cikis1=Button(profil,text="Çıkış", bg="#75163F",fg="#DDE6ED",font=40,command=ana)
                            profil_cikis1.place(x=130,y=300,width=120,height=45)



                            
                            kişisel_bligiler=Label(profil,text="Kişisel Bilgiler",bg='#526D82',fg='#DDE6ED',font=('Calibri',16,"bold"))
                            kişisel_bligiler.pack(fill=X)

                            def change_color_on_hover_enter(event):
                                profil_cikis.config(bg="red", fg="white")  # Fare butona yaklaştığında rengi değiştir

                            def change_color_on_hover_leave(event):
                                profil_cikis.config(bg="#526D82", fg="#DDE6ED")  # Fare butondan ayrıldığında orijinal rengine geri dön

                            profil_cikis=Button(profil,text="X", bg="#526D82",fg="#DDE6ED",font=30,command=profil.destroy, borderwidth=0, highlightthickness=0)
                            profil_cikis.place(x=345,y=2,width=32,height=28)

                            profil_cikis.bind("<Enter>", change_color_on_hover_enter)  # Fare butona geldiğinde rengi değiştir
                            profil_cikis.bind("<Leave>", change_color_on_hover_leave)  # Fare butondan ayrıldığında orijinal rengine geri dön

                            
 


                            
                        def change_color_1(event):
                            prof_btn.config(bg="#526D82", fg="#9DB2BF")  

                        def change_color_2(event):
                            prof_btn.config(bg="#9DB2BF", fg="#27374D")

                        prof_btn=Button(frame_ust,text=prof_ad_soyad[0][0]+ " "+ prof_ad_soyad[0][1] + " - " + kul_adi.get(),bg='#9DB2BF',fg='#27374D',font=20, borderwidth=0, highlightthickness=0,cursor='hand2',command=def_profil_sayfasi)
                        prof_btn.place(x=984,y=3,width=270,height=38)

                        prof_btn.bind("<Enter>", change_color_1)  
                        prof_btn.bind("<Leave>", change_color_2) 

                    else:
                        hata_lbl=Label(dogrulama_frame,text="Kullanıcı Adı Yada Şifre Yanlıştır",font=('Calibri',11),bg="#27374D",fg="red")
                        hata_lbl.place(x=107,y=235)
                        

                except:
                    hata_lbl=Label(dogrulama_frame,text="Kullanıcı Adı Yada Şifre Yanlıştır",font=('Calibri',11),bg="#27374D",fg="red")
                    hata_lbl.place(x=107,y=235)

                cr.commit()
                



            ake_bt = Button(dogrulama_frame, text="GİRİŞ", font=("Calibri", 18, "bold"), bg="#DDE6ED", fg="#27374D",command=giris_def)
            ake_bt.place(x=142,y=280, width=120,height=30)
            

            geri_bt=Button(dogrulama_frame,text="<", bg="#9DB2BF",fg="#27374D",font=20,command=dogrulama_frame.destroy)
            geri_bt.place(x=0,y=45,width=45,height=40)



        def Idari_sayfasi():
            dogrulama_frame=Frame(ilk_sayfa,bg="#27374D")
            dogrulama_frame.place(x=0,y=0,width=400,height=450)

            title_top68=Label(dogrulama_frame,text='Kimlik Doğrulama Sistemi',bg='#9DB2BF',fg='#27374D',font=('Calibri',23,"bold"))
            title_top68.pack(fill=X)

            kul_adi=StringVar()
            kul_sifre=StringVar()

            def on_entry_click(event):
                if entry_kul_adi.get() == "Kullanıcı Adı":
                    entry_kul_adi.delete(0, END)
                    entry_kul_adi.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)

            def on_sifre_click(event):
                if entry_sifre.get() == "Şifre":
                    entry_sifre.delete(0, END)
                    entry_sifre.config(show="*")  # İsteğe bağlı: Şifreyi gizleme karakterini ayarla
                    entry_sifre.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)

            entry_kul_adi = Entry(dogrulama_frame,justify="center",width=27,fg="#526D82",textvariable=kul_adi)
            entry_kul_adi.place(x=120, y=160,height=30)
            entry_kul_adi.insert(0, "Kullanıcı Adı")
            entry_kul_adi.bind("<FocusIn>", on_entry_click)

            entry_sifre = Entry(dogrulama_frame,justify="center",width=27,fg="#526D82",textvariable=kul_sifre)
            entry_sifre.place(x=120, y=200,height=30)
            entry_sifre.insert(0, "Şifre")
            entry_sifre.bind("<FocusIn>", on_sifre_click)

            def giris_def():
                db = pypyodbc.connect(
                'Driver={SQL Server};'
                'Server=YAZILIMCI\SQLEXPRESS01;'
                'Database=Proje;'
                'Trusted_Connection=True;')
                
                cr = db.cursor()

                try:
                    cr.execute(f"SELECT Admin_Sifre from Adminler where Admin_No='{kul_adi.get().strip()}'")
                    db_sifre=cr.fetchall()
                
                    if(db_sifre[0][0]==kul_sifre.get().strip()):
                        kul_adi1=kul_adi.get()
                        self.pro.destroy()
                        self.omer = Tk()
                        self.omer.geometry("{width}x{height}+0+0".format(width=self.omer.winfo_screenwidth(),height=self.omer.winfo_screenheight()))
                        self.omer.title("Öğrenci Bilgi Sistemi")
                        self.omer.config(bg="#27374D")

                        titl=Label(self.omer,text="Öğrenci Bilgi Sistemi",bg='#DDE6ED',fg='#27374D',font=('Calibri',16,"bold"))
                        titl.pack(fill=X)

                        #-------Frame_b--------#
                        frame_b=Frame(self.omer,bg='#9DB2BF')
                        frame_b.place(x=0,y=32,width=220,height=self.omer.winfo_screenheight())

                        title_top93=Label(frame_b,
                        text='Kontrol Paneli',
                        bg='#526D82',
                        fg='#DDE6ED',
                        font=('calisto mt',22,'bold'))
                        title_top93.place(x=0,y=0,width=220,height=45)


                        #--------frame_ust------#
                        frame_ust=Frame(self.omer,bg='#9DB2BF')
                        frame_ust.place(x=222,y=32,width=1310,height=45)
                        #-------------- orta Frame --------------#
                        orta_fremi=Frame(self.omer,bg="#27374D")
                        orta_fremi.place(x=222,y=80,width=1320,height=770)



                        #------frame_b button fremleri--------#
                            

                        
                        #--------Öğrenci button fremi---------#

                        
                        def ogr_btn_f():

                             #------öğrenci arama ekleme günceleme silme buttonları----#

                            def ogr_ara_bt():

                                try:
                                    Idari_sayfasi.ogrenci_f.destroy()
                                except:
                                    pass   
                                try:
                                    Idari_sayfasi.aram_tuşlar_fremi.destroy()
                                except:
                                    pass   
                                try:
                                    Idari_sayfasi.frame_arama_sayfasi.destroy()
                                except:
                                    pass   



                                Idari_sayfasi.aram_tuşlar_fremi=Frame(frame_ust,bg="#9DB2BF")
                                Idari_sayfasi.aram_tuşlar_fremi.place(x=0,y=0,width=970,height=45)

                                
                                
                                title_Öğrenci_arama_başlık=Label(Idari_sayfasi.aram_tuşlar_fremi,
                                text='Öğrenci Arama',
                                bg='#526D82',
                                fg='#DDE6ED',
                                font=('calisto mt',15,'bold'))
                                title_Öğrenci_arama_başlık.place(x=0,y=0,width=250,height=49)

                                arama_turu=StringVar()
                                i_search=StringVar()
                                i_search_yedek=StringVar()
                                


                                combo_ogr_arama_seçenekleri=ttk.Combobox(Idari_sayfasi.aram_tuşlar_fremi,state='readonly',textvariable=arama_turu)
                                combo_ogr_arama_seçenekleri['value']=('Tüm Öğrenciler','Öğrenci No İle Arama','Öğrenci Adı İle Arama', 'Ders Adı İle Arama', 'Bölüm Adı İle Arama','Sınıf İle Arama')
                                combo_ogr_arama_seçenekleri.place(x=275,y=6,width=180,height=35)


                                def on_entry_click_arama(event):
                                    if en_search.get() == "Arama" or "Sınıf":
                                        en_search.delete(0, END)
                                        en_search.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)     
    

                                en_search=Entry(Idari_sayfasi.aram_tuşlar_fremi,bd='2',fg='grey',justify='center',textvariable=i_search)
                                en_search.place(x=500,y=6,width=200,height=35)
                                en_search.insert(0, "Arama")
                                en_search.bind("<FocusIn>", on_entry_click_arama)


                                def update_buttons(*args):
                                    selected_option = arama_turu.get()
                                    if selected_option == 'Sınıf İle Arama':
                                        ara_but.place(x=800, y=6, width=150, height=35)
                                        en_search.place(x=650, y=6, width=150, height=35)
                                        en_search.delete(0, END)
                                        en_search.insert(0, "Sınıf")


                                        def on_entry_click_arama_asdfg(event):
                                            if update_buttons.en_search_1.get() == "Bölüm":
                                                update_buttons.en_search_1.delete(0, END)
                                                update_buttons.en_search_1.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)

                                        update_buttons.en_search_1=Entry(Idari_sayfasi.aram_tuşlar_fremi,bd='2',fg='grey',justify='center',textvariable=i_search_yedek)
                                        update_buttons.en_search_1.place(x=480,y=6,width=150,height=35)
                                        update_buttons.en_search_1.insert(0, "Bölüm")
                                        update_buttons.en_search_1.bind("<FocusIn>", on_entry_click_arama_asdfg)

                                    else:
                                        
                                        try:
                                            update_buttons.en_search_1.destroy()
                                            en_search.place(x=500,y=6,width=200,height=35)
                                            en_search.delete(0, END)
                                            en_search.insert(0, "Arama")
                                            en_search.bind("<FocusIn>", on_entry_click_arama)
                                        except:
                                            print("kkkkkkkkkkkkkkkkkkkkkkkk")
                                        Öğrenci_arama_işlemleri()

                                combo_ogr_arama_seçenekleri.bind("<<ComboboxSelected>>", update_buttons)


                                def Öğrenci_arama_işlemleri():
                                    if(arama_turu.get()=='Tüm Öğrenciler'):
                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        cr.execute("SELECT * FROM Ogrenciler")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                    
                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','ogr_no','ad','tc','tarih','cinsiyet','tel','email','bolum','sinif'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('ogr_no',text='Öğrenci No')
                                        arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                        arama_sayfasi_table.heading('tc',text='TC')
                                        arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                        arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                        arama_sayfasi_table.heading('tel',text='Tel No')
                                        arama_sayfasi_table.heading('email',text='Email')
                                        arama_sayfasi_table.heading('bolum',text='Bölümü')
                                        arama_sayfasi_table.heading('sinif',text='Sınıfı')

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('ogr_no',width=60,anchor='center')
                                        arama_sayfasi_table.column('ad',width=215,anchor='center')
                                        arama_sayfasi_table.column('tc',width=100,anchor='center')
                                        arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                        arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                        arama_sayfasi_table.column('tel',width=91,anchor='center')
                                        arama_sayfasi_table.column('email',width=230,anchor='center')
                                        arama_sayfasi_table.column('bolum',width=230,anchor='center')
                                        arama_sayfasi_table.column('sinif',width=45,anchor='center')


                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2]+" "+sonuc_arama_sayfasi[i][3])  # Ad soyad
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # Cinsiyet
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # tel
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][7])  # Email

                                                cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Id={sonuc_arama_sayfasi[i][9]}")
                                                sonuc_arama_sayfasi_bolum_adlari=cr.fetchone()
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi_bolum_adlari[0])#bolum

                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][10]) # sinif

                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)

                                    elif(arama_turu.get()=='Öğrenci No İle Arama' or ''):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass

                                        cr.execute(f"SELECT * FROM Ogrenciler where Ogr_No='{i_search.get().strip()}'")
                                        sonuc_arama_sayfasi=cr.fetchall()

                                        

                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','ogr_no','ad','tc','tarih','cinsiyet','tel','email','bolum','sinif'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('ogr_no',text='Öğrenci No')
                                        arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                        arama_sayfasi_table.heading('tc',text='TC')
                                        arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                        arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                        arama_sayfasi_table.heading('tel',text='Tel No')
                                        arama_sayfasi_table.heading('email',text='Email')
                                        arama_sayfasi_table.heading('bolum',text='Bölümü')
                                        arama_sayfasi_table.heading('sinif',text='Sınıfı')

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('ogr_no',width=60,anchor='center')
                                        arama_sayfasi_table.column('ad',width=215,anchor='center')
                                        arama_sayfasi_table.column('tc',width=100,anchor='center')
                                        arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                        arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                        arama_sayfasi_table.column('tel',width=91,anchor='center')
                                        arama_sayfasi_table.column('email',width=230,anchor='center')
                                        arama_sayfasi_table.column('bolum',width=230,anchor='center')
                                        arama_sayfasi_table.column('sinif',width=45,anchor='center')
                                       

                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2]+" "+sonuc_arama_sayfasi[i][3])  # Ad soyad
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # Cinsiyet
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # tel
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][7])  # Email

                                                cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Id={sonuc_arama_sayfasi[i][9]}")
                                                sonuc_arama_sayfasi_bolum_adlari=cr.fetchone()
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi_bolum_adlari[0])#bolum

                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][10]) # sinif

                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                        for row in arama_eklenecek_liste_son:
                                            arama_sayfasi_table.insert("",END, value=row)


                                    elif(arama_turu.get()=='Öğrenci Adı İle Arama'):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass

                                        cr.execute(f"SELECT * FROM Ogrenciler where Ogr_Ad LIKE '%{i_search.get().title().strip()}%'")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                   
                                        

                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','ogr_no','ad','tc','tarih','cinsiyet','tel','email','bolum','sinif'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('ogr_no',text='Öğrenci No')
                                        arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                        arama_sayfasi_table.heading('tc',text='TC')
                                        arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                        arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                        arama_sayfasi_table.heading('tel',text='Tel No')
                                        arama_sayfasi_table.heading('email',text='Email')
                                        arama_sayfasi_table.heading('bolum',text='Bölümü')
                                        arama_sayfasi_table.heading('sinif',text='Sınıfı')

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('ogr_no',width=60,anchor='center')
                                        arama_sayfasi_table.column('ad',width=215,anchor='center')
                                        arama_sayfasi_table.column('tc',width=100,anchor='center')
                                        arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                        arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                        arama_sayfasi_table.column('tel',width=91,anchor='center')
                                        arama_sayfasi_table.column('email',width=230,anchor='center')
                                        arama_sayfasi_table.column('bolum',width=230,anchor='center')
                                        arama_sayfasi_table.column('sinif',width=45,anchor='center')

                                        
                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2]+" "+sonuc_arama_sayfasi[i][3])  # Ad soyad
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # Cinsiyet
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # tel
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][7])  # Email

                                                cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Id={sonuc_arama_sayfasi[i][9]}")
                                                sonuc_arama_sayfasi_bolum_adlari=cr.fetchone()
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi_bolum_adlari[0])#bolum

                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][10]) # sinif

                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)


                                    elif(arama_turu.get()=='Ders Adı İle Arama'):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass

                                        cr.execute(f"SELECT Ders_Id FROM Dersler where Ders_Ad LIKE '%{i_search.get().strip()}%'")
                                        sonuc_1=cr.fetchone()
                                        print(sonuc_1)
                                        cr.execute(f"SELECT Ogr_no FROM Puan where Ders_Id={sonuc_1[0]}")
                                        sonuc_2=cr.fetchall()


                                        sonuc_arama_sayfasi=[]
                                        for i in range(len(sonuc_2)):
                                            cr.execute(f"SELECT * FROM Ogrenciler where Ogr_No={sonuc_2[i][0]}")
                                            sonuc_3=cr.fetchall()
                                            sonuc_arama_sayfasi.append(sonuc_3)

                                            
                                        
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','ogr_no','ad','tc','tarih','cinsiyet','tel','email','bolum','sinif'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('ogr_no',text='Öğrenci No')
                                        arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                        arama_sayfasi_table.heading('tc',text='TC')
                                        arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                        arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                        arama_sayfasi_table.heading('tel',text='Tel No')
                                        arama_sayfasi_table.heading('email',text='Email')
                                        arama_sayfasi_table.heading('bolum',text='Bölümü')
                                        arama_sayfasi_table.heading('sinif',text='Sınıfı')

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('ogr_no',width=60,anchor='center')
                                        arama_sayfasi_table.column('ad',width=215,anchor='center')
                                        arama_sayfasi_table.column('tc',width=100,anchor='center')
                                        arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                        arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                        arama_sayfasi_table.column('tel',width=91,anchor='center')
                                        arama_sayfasi_table.column('email',width=230,anchor='center')
                                        arama_sayfasi_table.column('bolum',width=230,anchor='center')
                                        arama_sayfasi_table.column('sinif',width=45,anchor='center')

                                        cr.execute(f"SELECT Ders_Id FROM Dersler where Ders_Ad LIKE '%{i_search.get().strip()}%'")
                                        sonuc_1=cr.fetchone()


                                        

                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][0])  # Ogrenci no
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][2]+" "+sonuc_arama_sayfasi[i][0][3])  # Ad soyad
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][1])  # TC
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][4])  # Dogum Tarihi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][5])  # Cinsiyet
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][6])  # tel
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][7])  # Email

                                                cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Id={sonuc_arama_sayfasi[i][0][9]}")
                                                sonuc_arama_sayfasi_bolum_adlari=cr.fetchone()
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi_bolum_adlari[0])#bolum

                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][10]) # sinif

                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)

                                    elif(arama_turu.get()=='Bölüm Adı İle Arama'):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass

                                        cr.execute(f"SELECT Bolum_Id FROM Bolumler where Bolum_Ad LIKE '%{i_search.get().strip()}%'")
                                        sonuc_1=cr.fetchone()
                                        print(sonuc_1)
                                        cr.execute(f"SELECT Ogr_no FROM Ogrenciler where Bolum_Id={sonuc_1[0]}")
                                        sonuc_2=cr.fetchall()
                                        print(sonuc_2)


                                        sonuc_arama_sayfasi=[]
                                        for i in range(len(sonuc_2)):
                                            cr.execute(f"SELECT * FROM Ogrenciler where Ogr_No={sonuc_2[i][0]}")
                                            sonuc_3=cr.fetchall()
                                            sonuc_arama_sayfasi.append(sonuc_3)
                                        print(sonuc_arama_sayfasi)
                                    

                                        
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','ogr_no','ad','tc','tarih','cinsiyet','tel','email','bolum','sinif'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('ogr_no',text='Öğrenci No')
                                        arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                        arama_sayfasi_table.heading('tc',text='TC')
                                        arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                        arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                        arama_sayfasi_table.heading('tel',text='Tel No')
                                        arama_sayfasi_table.heading('email',text='Email')
                                        arama_sayfasi_table.heading('bolum',text='Bölümü')
                                        arama_sayfasi_table.heading('sinif',text='Sınıfı')

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('ogr_no',width=60,anchor='center')
                                        arama_sayfasi_table.column('ad',width=215,anchor='center')
                                        arama_sayfasi_table.column('tc',width=100,anchor='center')
                                        arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                        arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                        arama_sayfasi_table.column('tel',width=91,anchor='center')
                                        arama_sayfasi_table.column('email',width=230,anchor='center')
                                        arama_sayfasi_table.column('bolum',width=230,anchor='center')
                                        arama_sayfasi_table.column('sinif',width=45,anchor='center')


                                        
                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][0])  # Ogrenci no
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][2]+" "+sonuc_arama_sayfasi[i][0][3])  # Ad soyad
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][1])  # TC
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][4])  # Dogum Tarihi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][5])  # Cinsiyet
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][6])  # tel
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][7])  # Email

                                                cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Id={sonuc_arama_sayfasi[i][0][9]}")
                                                sonuc_arama_sayfasi_bolum_adlari=cr.fetchone()
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi_bolum_adlari[0])#bolum

                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0][10]) # sinif

                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)


                                        

                                    elif(arama_turu.get()=='Sınıf İle Arama'):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass

                                        cr.execute(f"SELECT Bolum_Id FROM Bolumler WHERE Bolum_Ad LIKE '%{i_search_yedek.get().strip()}%'")
                                        sonuc_0=cr.fetchone()

                                        cr.execute(f"SELECT * FROM Ogrenciler where Ogr_Sinif='{i_search.get().strip()}' AND Bolum_Id='{sonuc_0[0]}'")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                    


                                        
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','ogr_no','ad','tc','tarih','cinsiyet','tel','email','bolum','sinif'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('ogr_no',text='Öğrenci No')
                                        arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                        arama_sayfasi_table.heading('tc',text='TC')
                                        arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                        arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                        arama_sayfasi_table.heading('tel',text='Tel No')
                                        arama_sayfasi_table.heading('email',text='Email')
                                        arama_sayfasi_table.heading('bolum',text='Bölümü')
                                        arama_sayfasi_table.heading('sinif',text='Sınıfı')

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('ogr_no',width=60,anchor='center')
                                        arama_sayfasi_table.column('ad',width=215,anchor='center')
                                        arama_sayfasi_table.column('tc',width=100,anchor='center')
                                        arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                        arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                        arama_sayfasi_table.column('tel',width=91,anchor='center')
                                        arama_sayfasi_table.column('email',width=230,anchor='center')
                                        arama_sayfasi_table.column('bolum',width=230,anchor='center')
                                        arama_sayfasi_table.column('sinif',width=45,anchor='center')


                                        
                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2]+" "+sonuc_arama_sayfasi[i][3])  # Ad soyad
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # Cinsiyet
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # tel
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][7])  # Email

                                                cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Id={sonuc_arama_sayfasi[i][9]}")
                                                sonuc_arama_sayfasi_bolum_adlari=cr.fetchone()
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi_bolum_adlari[0])#bolum

                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][10]) # sinif

                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)



                                ara_but=Button(Idari_sayfasi.aram_tuşlar_fremi,text='Ara',font=10,bg='#526D82',fg='#DDE6ED',command=Öğrenci_arama_işlemleri)#,command=arama_sayfasi
                                ara_but.place(x=720,y=6,width=200,height=35)

                            def ogr_ekle_bt():
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x500+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=500)

                                title_top68=Label(ilk_sayfa,
                                text='Öğrenci Ekleme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)



                                fr1 = Frame(pro1, width=400, height=450, bg="#27374D")
                                fr1.pack(pady=45)

                                lbl = Label(fr1, text="Tc", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=15)
                                lbl = Label(fr1, text="Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=55)
                                lbl = Label(fr1, text="Soyadı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=95)
                                lbl = Label(fr1, text="Doğum Tarihi", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=135)
                                lbl = Label(fr1, text="Cinsiyet", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=175)
                                lbl = Label(fr1, text="Tel No", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=215)
                                lbl = Label(fr1, text="E-Posta", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=255)
                                lbl = Label(fr1, text="Bölüm Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=295)
                                lbl = Label(fr1, text="Sınıf", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=335)
                                lbl = Label(fr1, text="Şifre", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=375)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=15)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=55)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=95)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=135)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=175)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=215)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=255)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=295)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=335)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=375)

                                entry_tc = Entry(fr1)
                                entry_tc.place(x=200, y=20)
                                entry_ad = Entry(fr1)
                                entry_ad.place(x=200, y=60)
                                entry_soyad = Entry(fr1)
                                entry_soyad.place(x=200, y=100)
                                entry_dogum_tarihi = Entry(fr1)
                                entry_dogum_tarihi.place(x=200, y=140)
                                entry_cinsiyet = Entry(fr1)
                                entry_cinsiyet.place(x=200, y=180)
                                entry_telno = Entry(fr1)
                                entry_telno.place(x=200, y=220)
                                entry_eposta = Entry(fr1)
                                entry_eposta.place(x=200, y=260)
                                entry_bolumad = Entry(fr1)
                                entry_bolumad.place(x=200, y=300)
                                entry_sinif = Entry(fr1)
                                entry_sinif.place(x=200, y=340)
                                entry_sifre = Entry(fr1)
                                entry_sifre.place(x=200, y=380)

                                def tamamla():
                                

                                    tc = entry_tc.get()
                                    ad = entry_ad.get()
                                    soyad = entry_soyad.get()
                                    dogum_tarihi = entry_dogum_tarihi.get()
                                    cinsiyet = entry_cinsiyet.get()
                                    telno = entry_telno.get()
                                    eposta = entry_eposta.get()
                                    bolumad = entry_bolumad.get()
                                    sinif = entry_sinif.get()
                                    sifre = entry_sifre.get()

                                    cr.execute(f"INSERT INTO Ogrenciler (Ogr_Tc, Ogr_Ad, Ogr_Soyad, Ogr_DT, Ogr_Cinsiyeti, Ogr_TelNo, Ogr_Eposta, Ogr_Sifre,  Ogr_Sinif) VALUES ('{tc}','{ad}','{soyad}','{dogum_tarihi}','{cinsiyet}','{telno}','{eposta}','{sinif}','{sifre}')")
                                    cr.commit()

                                    cr.execute(f"SELECT Bolum_Id FROM Bolumler WHERE Bolum_Ad LIKE '%{bolumad}%'")
                                    bolumid = cr.fetchone()
                                    print(bolumid)
                                    
                                    cr.execute(f"UPDATE Ogrenciler SET Bolum_Id = '{bolumid[0]}' WHERE Ogr_Tc='{tc}' AND Ogr_Ad='{ad}' AND Ogr_Soyad='{soyad}'")

                                    cr.commit()

                                def bitir():
                                    tamamla()
                                    pro1.destroy()

                                btn_cik = Button(self.pro1, text="KAYDET", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_cik.place(x=120, y=460)


                            def ogr_sil_btn():
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x250+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=250)

                                title_top68=Label(ilk_sayfa,
                                text='Öğrenci Silme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)

                                
                                fr1 = Frame(pro1, width=400, height=200, bg="#27374D")
                                fr1.pack(pady=50)

                                lbl = Label(fr1, text="Öğrenci No", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=20)
                                lbl = Label(fr1, text="Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=65)
                                lbl = Label(fr1, text="Soyadı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=110)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=20)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=65)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=110)

                                entry_no = Entry(fr1)
                                entry_no.place(x=200, y=25)
                                entry_ad = Entry(fr1)
                                entry_ad.place(x=200, y=70)
                                entry_soyad = Entry(fr1)
                                entry_soyad.place(x=200, y=115)

                                def tamamla():
                                

                                    no = entry_no.get()
                                    ad = entry_ad.get()
                                    soyad = entry_soyad.get()

                                    cr.execute(f"SELECT Ogr_Ad,Ogr_Soyad FROM Ogrenciler WHERE Ogr_No= '{no}'")
                                    kontrol = cr.fetchall()
                                    print(no)
                                    print(ad)
                                    print(soyad)
                                    print(kontrol)

                                    if(len(kontrol)>0):
                                        if(ad==kontrol[0][0]):
                                            if(soyad==kontrol[0][1]):
                                                cr.execute(f"DELETE FROM Puan WHERE Ogr_No='{no}'")
                                                cr.execute(f"DELETE FROM Ogrenciler WHERE Ogr_No='{no}' AND Ogr_Ad='{ad}' AND Ogr_Soyad='{soyad}'")
                                                cr.commit()
                                                print("1")
                                            else:
                                                messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                        else:
                                            messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                    else:
                                        messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                        

                                def bitir():
                                    tamamla()
                                    pro1.destroy()

                                btn_cik = Button(self.pro1, text="SİL", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_cik.place(x=120, y=200)

                            def ogr_guncelle_btn():
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x500+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=500)

                                title_top68=Label(ilk_sayfa,
                                text='Bilgi Güncelleme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)

                                fr2 = Frame(pro1, width=400, height=450, bg="#27374D")
                                fr2.pack(pady=100)

                                

                                

                                
                                lbl_u_ogr_no=Label(fr2,text='No: ', font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")         ####### ogr no ########
                                lbl_u_ogr_no.place(x=30,y=35)
                                en_u_ogr_no=Entry(fr2,bd=2,justify='center')
                                en_u_ogr_no.place(x=200,y=40)

                                lbl_u_ogr_ad=Label(fr2,text='Ad: ', font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")         ####### ogr ad ########
                                lbl_u_ogr_ad.place(x=30,y=80)
                                en_ogr_ad=Entry(fr2,bd=2,justify='center')
                                en_ogr_ad.place(x=200,y=85)
                                lbl_u_ogr_soyad=Label(fr2,text='Soyad: ', font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")         ####### ogr ad ########
                                lbl_u_ogr_soyad.place(x=30,y=125)
                                en_ogr_soyad=Entry(fr2,bd=2,justify='center')
                                en_ogr_soyad.place(x=200,y=130)
                                
                                no=en_u_ogr_no.get()


                                def musab():
                                    cr.execute(f"SELECT Ogr_Ad, Ogr_Soyad FROM Ogrenciler WHERE Ogr_No='{en_u_ogr_no.get()}'")
                                    kontrol = cr.fetchall()

                                    if(len(kontrol)>0):
                                        if(en_ogr_ad.get()==kontrol[0][0]):
                                            if(en_ogr_soyad.get()==kontrol[0][1]):

                                       
                                                no=en_u_ogr_no.get()
                                                no_1=no
                                                fr2.destroy()
                                                fr1 = Frame(pro1, width=400, height=500, bg="#27374D")
                                                #fr1.pack(pady=45)
                                                fr1.place(x=0, y=0, width=400, height=500)

                                                

                                                lbl = Label(fr1, text="Tc", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=15)
                                                lbl = Label(fr1, text="Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=55)
                                                lbl = Label(fr1, text="Soyadı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                                lbl.place(x=30, y=95)
                                                lbl = Label(fr1, text="Doğum Tarihi", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                                lbl.place(x=30, y=135)
                                                lbl = Label(fr1, text="Cinsiyet", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=175)
                                                lbl = Label(fr1, text="Tel No", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                                lbl.place(x=30, y=215)
                                                lbl = Label(fr1, text="E-Posta", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                                lbl.place(x=30, y=255)
                                                lbl = Label(fr1, text="Bölüm Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=295)
                                                lbl = Label(fr1, text="Sınıf", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=335)
                                                lbl = Label(fr1, text="Şifre", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=375)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=15)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=55)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=95)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=135)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=175)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=215)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=255)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=295)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=335)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=375)

                                                entry_tc = Entry(fr1)
                                                entry_tc.place(x=200, y=20)
                                                entry_ad = Entry(fr1)
                                                entry_ad.place(x=200, y=60)
                                                entry_soyad = Entry(fr1)
                                                entry_soyad.place(x=200, y=100)
                                                entry_dogum_tarihi = Entry(fr1)
                                                entry_dogum_tarihi.place(x=200, y=140)
                                                entry_cinsiyet = Entry(fr1)
                                                entry_cinsiyet.place(x=200, y=180)
                                                entry_telno = Entry(fr1)
                                                entry_telno.place(x=200, y=220)
                                                entry_eposta = Entry(fr1)
                                                entry_eposta.place(x=200, y=260)
                                                entry_bolumad = Entry(fr1)
                                                entry_bolumad.place(x=200, y=300)
                                                entry_sinif = Entry(fr1)
                                                entry_sinif.place(x=200, y=340)
                                                entry_sifre = Entry(fr1)
                                                entry_sifre.place(x=200, y=380)

                                                def f_save_btn():
                                                    
                                                    
                                                    cr.execute(f"UPDATE Ogrenciler SET Ogr_Sinif='{entry_sinif.get().strip()}', Ogr_Tc='{entry_tc.get().strip()}', Ogr_Ad='{entry_ad.get().strip().title()}',Ogr_Soyad='{entry_soyad.get().strip().title()}', Ogr_DT='{entry_dogum_tarihi.get().strip()}', Ogr_TelNo='{entry_telno.get().strip()}', Ogr_Eposta='{entry_eposta.get().strip()}', Ogr_Sifre='{entry_sifre.get().strip()}', Ogr_Cinsiyeti='{entry_cinsiyet.get()}' WHERE Ogr_No='{no_1}'")
                                                    db.commit()

                                                    cr.execute(f"SELECT Bolum_Id FROM Bolumler WHERE Bolum_Ad LIKE '%{entry_bolumad.get()}%'")
                                                    bolumid = cr.fetchone()
                                                    print(bolumid)
                                                    
                                                    cr.execute(f"UPDATE Ogrenciler SET Bolum_Id = '{bolumid[0]}' WHERE Ogr_Tc='{entry_tc.get()}' AND Ogr_Ad='{entry_ad.get()}' AND Ogr_Soyad='{entry_soyad.get()}'")

                                                    cr.commit()
                                                
                                                    self.pro1.destroy()

                                                def f_add_close_btn():
                                                    self.pro1.destroy()


                                                save_btn=Button(fr1,text='Güncelle', font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=10,command=f_save_btn)
                                                save_btn.place(x=75,y=430)

                                                add_close_btn=Button(fr1,text='Kapat', font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=10,command=f_add_close_btn)
                                                add_close_btn.place(x=225,y=430)
                                            else:
                                                messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                                self.pro1.destroy()
                                        else:
                                            messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                            self.pro1.destroy()
                                    else:
                                        messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                        self.pro1.destroy()
                                
                                def bitir():
                                    musab()
                                    
                                btn_ara = Button(fr2, text="ARA", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_ara.place(x=120,y=200)




                            #----------- diğer fremleri kapat----------# 
                            try:
                                Idari_sayfasi.Bölüm_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.Akademisyen_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.idari_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.Ders_f.destroy()
                            except:
                                pass     







                            Idari_sayfasi.ogrenci_f=Frame(frame_b,bg='#9DB2BF')
                            Idari_sayfasi.ogrenci_f.place(x=5,y=300,width=200,height=190)

                            başlık=Label(Idari_sayfasi.ogrenci_f,
                            text='Öğrenci İşlemleri',
                            bg='#526D82',
                            fg='#DDE6ED',
                            font=('calisto mt',15,'bold'))
                            başlık.place(x=0,y=0,width=200,height=35)


                            def change_color_Ara_btn1(event):
                                Ara_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Ara_btn2(event):
                                Ara_btn.config(bg="#27374D", fg="#DDE6ED")
                            Ara_btn=Button(Idari_sayfasi.ogrenci_f,text='Öğrenci Ara',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=ogr_ara_bt)
                            Ara_btn.place(x=5,y=40,width=190,height=30)
                            Ara_btn.bind("<Enter>", change_color_Ara_btn1)  
                            Ara_btn.bind("<Leave>", change_color_Ara_btn2) 

        

                            def change_color_Ekle_btn1(event):
                                Ekle_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Ekle_btn2(event):
                                Ekle_btn.config(bg="#27374D", fg="#DDE6ED")
                            Ekle_btn=Button(Idari_sayfasi.ogrenci_f,text='Öğrenci Ekle',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=ogr_ekle_bt)
                            Ekle_btn.place(x=5,y=75,width=190,height=30)
                            Ekle_btn.bind("<Enter>", change_color_Ekle_btn1)  
                            Ekle_btn.bind("<Leave>", change_color_Ekle_btn2) 
                            

                            def change_color_Sil_btn1(event):
                                Sil_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Sil_btn2(event):
                                Sil_btn.config(bg="#27374D", fg="#DDE6ED")
                            Sil_btn=Button(Idari_sayfasi.ogrenci_f,text='Öğrenci Sil',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=ogr_sil_btn)
                            Sil_btn.place(x=5,y=110,width=190,height=30)
                            Sil_btn.bind("<Enter>", change_color_Sil_btn1)  
                            Sil_btn.bind("<Leave>", change_color_Sil_btn2) 


                            def change_color_Güncelle_btn1(event):
                                Güncelle_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Güncelle_btn2(event):
                                Güncelle_btn.config(bg="#27374D", fg="#DDE6ED")
                            Güncelle_btn=Button(Idari_sayfasi.ogrenci_f,text='Öğrenci Güncelle',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=ogr_guncelle_btn)
                            Güncelle_btn.place(x=5,y=145,width=190,height=30)
                            Güncelle_btn.bind("<Enter>", change_color_Güncelle_btn1)  
                            Güncelle_btn.bind("<Leave>", change_color_Güncelle_btn2) 



                        #--------Akademisyen button fremi---------#


                        def Akademisyen_btn_f():

                            #------Akademisyen arama ekleme günceleme silme buttonları----#

                            def Akademisyen_ara_btn():

                                try:
                                    Idari_sayfasi.Akademisyen_f.destroy()
                                except:
                                    pass   
                                try:
                                    Idari_sayfasi.aram_tuşlar_fremi.destroy()
                                except:
                                    pass   
                                try:
                                    Idari_sayfasi.frame_arama_sayfasi.destroy()
                                except:
                                    pass   



                                Idari_sayfasi.aram_tuşlar_fremi=Frame(frame_ust,bg="#9DB2BF")
                                Idari_sayfasi.aram_tuşlar_fremi.place(x=0,y=0,width=970,height=45)

                                
                                
                                title_Akademisyen_arama_başlık=Label(Idari_sayfasi.aram_tuşlar_fremi,
                                text='Akademisyen Arama',
                                bg='#526D82',
                                fg='#DDE6ED',
                                font=('calisto mt',15,'bold'))
                                title_Akademisyen_arama_başlık.place(x=0,y=0,width=250,height=49)

                                arama_turu=StringVar()
                                i_search=StringVar()
                                


                                combo_ogrt_arama_seçenekleri=ttk.Combobox(Idari_sayfasi.aram_tuşlar_fremi,state='readonly',textvariable=arama_turu)
                                combo_ogrt_arama_seçenekleri['value']=('Tüm Akademisyenler','Akademisyen No İle Arama','Akademisyen Adı İle Arama', 'Ders Adı İle Arama')
                                combo_ogrt_arama_seçenekleri.place(x=275,y=6,width=180,height=35)


                                def on_entry_click_arama(event):
                                    if en_search.get() == "Arama":
                                        en_search.delete(0, END)
                                        en_search.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)
    

                                en_search=Entry(Idari_sayfasi.aram_tuşlar_fremi,bd='2',fg='grey',justify='center',textvariable=i_search)
                                en_search.place(x=500,y=6,width=200,height=35)
                                en_search.insert(0, "Arama")
                                en_search.bind("<FocusIn>", on_entry_click_arama)


                                def Akademisyen_arama_işlemleri():
                                    if(arama_turu.get()=='Tüm Akademisyenler'):
                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass

                                        cr.execute("SELECT * FROM Ogretmenler")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                        

                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','ogrt_no','ad','tc','tarih','cinsiyet','tel','email'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('ogrt_no',text='Akademisyen No')
                                        arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                        arama_sayfasi_table.heading('tc',text='TC')
                                        arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                        arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                        arama_sayfasi_table.heading('tel',text='Tel No')
                                        arama_sayfasi_table.heading('email',text='Email')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('ogrt_no',width=60,anchor='center')
                                        arama_sayfasi_table.column('ad',width=215,anchor='center')
                                        arama_sayfasi_table.column('tc',width=100,anchor='center')
                                        arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                        arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                        arama_sayfasi_table.column('tel',width=91,anchor='center')
                                        arama_sayfasi_table.column('email',width=230,anchor='center')
                                        
                                        
                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2]+" "+sonuc_arama_sayfasi[i][3])  # Ad soyad
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][8])  # Cinsiyet
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # tel
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # Email

                                             

                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)

                                    elif(arama_turu.get()=='Akademisyen No İle Arama' or ''):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass

                                        cr.execute(f"SELECT * FROM Ogretmenler where Ogrt_No='{i_search.get().strip()}'")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                        

                                        

                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','ogrt_no','ad','tc','tarih','cinsiyet','tel','email'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('ogrt_no',text='Akademisyen No')
                                        arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                        arama_sayfasi_table.heading('tc',text='TC')
                                        arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                        arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                        arama_sayfasi_table.heading('tel',text='Tel No')
                                        arama_sayfasi_table.heading('email',text='Email')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('ogrt_no',width=60,anchor='center')
                                        arama_sayfasi_table.column('ad',width=215,anchor='center')
                                        arama_sayfasi_table.column('tc',width=100,anchor='center')
                                        arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                        arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                        arama_sayfasi_table.column('tel',width=91,anchor='center')
                                        arama_sayfasi_table.column('email',width=230,anchor='center')


                                        
                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2]+" "+sonuc_arama_sayfasi[i][3])  # Ad soyad
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][8])  # Cinsiyet
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # tel
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # Email

                                               

                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                        for row in arama_eklenecek_liste_son:
                                            arama_sayfasi_table.insert("",END, value=row)

                                        
                                    
                                    elif(arama_turu.get()=='Akademisyen Adı İle Arama'):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass

                                        try:
                                            cr.execute(f"DROP VIEW ogretmen_adlari")
                                        except:
                                            print(" view silinmedi")

                                        cr.execute(f"Create VIEW ogretmen_adlari AS SELECT CONCAT(Ogrt_Ad,' ', Ogrt_Soyad) AS FULL_NAME, Ogrt_No From Ogretmenler")

                                        cr.execute(f"SELECT Ogrt_No FROM ogretmen_adlari WHERE FULL_NAME LIKE '%{i_search.get().title().strip()}%'")
                                        ogrt_no=cr.fetchall()

                                        if(len(ogrt_no)==1):
                                            cr.execute(f"SELECT * FROM Ogretmenler where Ogrt_No='{ogrt_no[0][0]}'")
                                            sonuc_arama_sayfasi=cr.fetchall()
                                        else:
                                            messagebox.showinfo('Hata','Akademisyen Adı Yanlıştır..!')
                                            return
                                            
                                        
                                        
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','ogrt_no','ad','tc','tarih','cinsiyet','tel','email'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('ogrt_no',text='Akademisyen No')
                                        arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                        arama_sayfasi_table.heading('tc',text='TC')
                                        arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                        arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                        arama_sayfasi_table.heading('tel',text='Tel No')
                                        arama_sayfasi_table.heading('email',text='Email')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('ogrt_no',width=60,anchor='center')
                                        arama_sayfasi_table.column('ad',width=215,anchor='center')
                                        arama_sayfasi_table.column('tc',width=100,anchor='center')
                                        arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                        arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                        arama_sayfasi_table.column('tel',width=91,anchor='center')
                                        arama_sayfasi_table.column('email',width=230,anchor='center')


                                       
                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2]+" "+sonuc_arama_sayfasi[i][3])  # Ad soyad
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][8])  # Cinsiyet
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # tel
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # Email

                                               

                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)

                                    elif(arama_turu.get()=='Ders Adı İle Arama'):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass


                                        cr.execute(f"SELECT Ogrt_No FROM Dersler where Ders_Ad LIKE '%{i_search.get().strip()}%'")
                                        sonuc_1=cr.fetchone()
                                        cr.execute(f"SELECT * FROM Ogretmenler where Ogrt_No='{sonuc_1[0]}'")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                        


                                        
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','ogrt_no','ad','tc','tarih','cinsiyet','tel','email'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('ogrt_no',text='Akademisyen No')
                                        arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                        arama_sayfasi_table.heading('tc',text='TC')
                                        arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                        arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                        arama_sayfasi_table.heading('tel',text='Tel No')
                                        arama_sayfasi_table.heading('email',text='Email')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('ogrt_no',width=60,anchor='center')
                                        arama_sayfasi_table.column('ad',width=215,anchor='center')
                                        arama_sayfasi_table.column('tc',width=100,anchor='center')
                                        arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                        arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                        arama_sayfasi_table.column('tel',width=91,anchor='center')
                                        arama_sayfasi_table.column('email',width=230,anchor='center')
                                        
                                    

                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2]+" "+sonuc_arama_sayfasi[i][3])  # Ad soyad
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][8])  # Cinsiyet
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # tel
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # Email


                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)
                                    

                                ara_but=Button(Idari_sayfasi.aram_tuşlar_fremi,text='Ara',font=10,bg='#526D82',fg='#DDE6ED',command=Akademisyen_arama_işlemleri)#,command=arama_sayfasi
                                ara_but.place(x=720,y=6,width=200,height=35)

                            def Akademisyen_ekle_btn():
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x500+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=500)

                                title_top68=Label(ilk_sayfa,
                                text='Akademisyen Ekleme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)



                                fr1 = Frame(pro1, width=400, height=450, bg="#27374D")
                                fr1.pack(pady=70)

                                lbl = Label(fr1, text="Tc", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=15)
                                lbl = Label(fr1, text="Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=55)
                                lbl = Label(fr1, text="Soyadı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=95)
                                lbl = Label(fr1, text="Doğum Tarihi", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=135)
                                lbl = Label(fr1, text="Cinsiyet", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=175)
                                lbl = Label(fr1, text="Tel No", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=215)
                                lbl = Label(fr1, text="E-Posta", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=255)
                                lbl = Label(fr1, text="Şifre", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=295)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=15)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=55)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=95)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=135)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=175)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=215)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=255)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=295)


                                entry_tc = Entry(fr1)
                                entry_tc.place(x=200, y=20)
                                entry_ad = Entry(fr1)
                                entry_ad.place(x=200, y=60)
                                entry_soyad = Entry(fr1)
                                entry_soyad.place(x=200, y=100)
                                entry_dogum_tarihi = Entry(fr1)
                                entry_dogum_tarihi.place(x=200, y=140)
                                entry_telno = Entry(fr1)
                                entry_telno.place(x=200, y=220)
                                entry_eposta = Entry(fr1)
                                entry_eposta.place(x=200, y=260)
                                entry_sifre = Entry(fr1)
                                entry_sifre.place(x=200, y=300)
                                entry_cinsiyet = Entry(fr1)
                                entry_cinsiyet.place(x=200, y=180)

                                def tamamla():
                                

                                    tc = entry_tc.get()
                                    ad = entry_ad.get()
                                    soyad = entry_soyad.get()
                                    dogum_tarihi = entry_dogum_tarihi.get()
                                    telno = entry_telno.get()
                                    eposta = entry_eposta.get()
                                    sifre = entry_sifre.get()
                                    cinsiyet = entry_cinsiyet.get()


                                    cr.execute(f"INSERT INTO Ogretmenler (Ogrt_Tc, Ogrt_Ad, Ogrt_Soyad, Ogrt_DT, Ogrt_TelNo, Ogrt_Eposta, Ogrt_Sifre, Ogrt_Cinsiyeti) VALUES ('{tc}','{ad}','{soyad}','{dogum_tarihi}','{telno}','{eposta}','{sifre}','{cinsiyet}')")
                                    cr.commit()


                                def bitir():
                                    tamamla()
                                    pro1.destroy()

                                btn_cik = Button(self.pro1, text="KAYDET", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_cik.place(x=120, y=420)


                            def Akademisyen_sil_btn():
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x250+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=250)

                                title_top68=Label(ilk_sayfa,
                                text='Akademisyen Silme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)

                                
                                fr1 = Frame(pro1, width=400, height=200, bg="#27374D")
                                fr1.pack(pady=50)

                                lbl = Label(fr1, text="No", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=20)
                                lbl = Label(fr1, text="Ad", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=65)
                                lbl = Label(fr1, text="Soyad", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=110)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=20)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=65)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=110)

                                entry_no = Entry(fr1)
                                entry_no.place(x=200, y=25)
                                entry_ad = Entry(fr1)
                                entry_ad.place(x=200, y=70)
                                entry_soyad = Entry(fr1)
                                entry_soyad.place(x=200, y=115)

                                def tamamla():
                                

                                    no = entry_no.get()
                                    ad = entry_ad.get()
                                    soyad = entry_soyad.get()

                                    cr.execute(f"SELECT Ogrt_Ad,Ogrt_Soyad FROM Ogretmenler WHERE Ogrt_No= '{no}'")
                                    kontrol = cr.fetchall()


                                    if(len(kontrol)>0):
                                        if(ad==kontrol[0][0]):
                                            if(soyad==kontrol[0][1]):
                                                cr.execute(f"DELETE FROM Ogretmenler WHERE Ogrt_No='{no}' AND Ogrt_Ad='{ad}' AND Ogrt_Soyad='{soyad}'")
                                                cr.commit()
                                            else:
                                                messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                        else:
                                            messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                    else:
                                        messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')

                                def bitir():
                                    tamamla()
                                    pro1.destroy()

                                btn_cik = Button(self.pro1, text="SİL", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_cik.place(x=120,y=200)

                            
                            def Akademisyen_guncelle_btn():
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x500+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=500)

                                title_top68=Label(ilk_sayfa,
                                text='Bilgi Güncelleme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)

                                fr2 = Frame(pro1, width=400, height=450, bg="#27374D")
                                fr2.pack(pady=100)

                                

                                

                                
                                lbl_u_ogr_no=Label(fr2,text='No: ', font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")         ####### ogr no ########
                                lbl_u_ogr_no.place(x=30,y=35)
                                en_u_ogr_no=Entry(fr2,bd=2,justify='center')
                                en_u_ogr_no.place(x=200,y=40)

                                lbl_u_ogr_ad=Label(fr2,text='Ad: ', font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")         ####### ogr ad ########
                                lbl_u_ogr_ad.place(x=30,y=80)
                                en_ogr_ad=Entry(fr2,bd=2,justify='center')
                                en_ogr_ad.place(x=200,y=85)
                                lbl_u_ogr_soyad=Label(fr2,text='Soyad: ', font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")         ####### ogr ad ########
                                lbl_u_ogr_soyad.place(x=30,y=125)
                                en_ogr_soyad=Entry(fr2,bd=2,justify='center')
                                en_ogr_soyad.place(x=200,y=130)
                                
                                no=en_u_ogr_no.get()


                                def musab():
                                    cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad FROM Ogretmenler WHERE Ogrt_No='{en_u_ogr_no.get()}'")
                                    kontrol = cr.fetchall()

                                    if(len(kontrol)>0):
                                        if(en_ogr_ad.get()==kontrol[0][0]):
                                            if(en_ogr_soyad.get()==kontrol[0][1]):

                                       
                                                no=en_u_ogr_no.get()
                                                no_1=no
                                                fr2.destroy()
                                                fr1 = Frame(pro1, width=400, height=450, bg="#27374D")
                                                fr1.pack(pady=45)

                                                

                                                lbl = Label(fr1, text="Tc", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=15)
                                                lbl = Label(fr1, text="Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=55)
                                                lbl = Label(fr1, text="Soyadı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                                lbl.place(x=30, y=95)
                                                lbl = Label(fr1, text="Doğum Tarihi", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                                lbl.place(x=30, y=135)
                                                lbl = Label(fr1, text="Cinsiyet", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=175)
                                                lbl = Label(fr1, text="Tel No", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                                lbl.place(x=30, y=215)
                                                lbl = Label(fr1, text="E-Posta", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                                lbl.place(x=30, y=255)
                                                lbl = Label(fr1, text="Şifre", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=295)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=15)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=55)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=95)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=135)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=175)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=215)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=255)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=295)

                                                entry_tc = Entry(fr1)
                                                entry_tc.place(x=200, y=20)
                                                entry_ad = Entry(fr1)
                                                entry_ad.place(x=200, y=60)
                                                entry_soyad = Entry(fr1)
                                                entry_soyad.place(x=200, y=100)
                                                entry_dogum_tarihi = Entry(fr1)
                                                entry_dogum_tarihi.place(x=200, y=140)
                                                entry_cinsiyet = Entry(fr1)
                                                entry_cinsiyet.place(x=200, y=180)
                                                entry_telno = Entry(fr1)
                                                entry_telno.place(x=200, y=220)
                                                entry_eposta = Entry(fr1)
                                                entry_eposta.place(x=200, y=260)
                                                entry_sifre = Entry(fr1)
                                                entry_sifre.place(x=200, y=300)

                                                def f_save_btn():
                                                    
                                                    
                                                    cr.execute(f"UPDATE Ogretmenler SET Ogrt_Tc='{entry_tc.get().strip()}', Ogrt_Ad='{entry_ad.get().strip().title()}',Ogrt_Soyad='{entry_soyad.get().strip().title()}', Ogrt_DT='{entry_dogum_tarihi.get().strip()}', Ogrt_TelNo='{entry_telno.get().strip()}', Ogrt_Eposta='{entry_eposta.get().strip()}',Ogrt_Sifre='{entry_sifre.get().strip()}', Ogrt_Cinsiyeti='{entry_cinsiyet.get()}' WHERE Ogrt_No='{no_1}'")
                                                    db.commit()
                                                
                                                    self.pro1.destroy()

                                                def f_add_close_btn():
                                                    self.pro1.destroy()


                                                save_btn=Button(fr1,text='Güncelle', font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=10,command=f_save_btn)
                                                save_btn.place(x=85,y=350)

                                                add_close_btn=Button(fr1,text='Kapat', font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=10,command=f_add_close_btn)
                                                add_close_btn.place(x=215,y=350)
                                            else:
                                                messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                                self.pro1.destroy()
                                        else:
                                            messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                            self.pro1.destroy()
                                    else:
                                        messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                        self.pro1.destroy()
                                
                                def bitir():
                                    musab()
                                    
                                btn_ara = Button(fr2, text="ARA", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_ara.place(x=120,y=200)




                            #----------- diğer fremleri kapat----------# 
                            try:
                                Idari_sayfasi.Bölüm_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.ogrenci_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.idari_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.Ders_f.destroy()
                            except:
                                pass 


                            Idari_sayfasi.Akademisyen_f=Frame(frame_b,bg='#9DB2BF')
                            Idari_sayfasi.Akademisyen_f.place(x=5,y=300,width=200,height=190)

                            başlık=Label(Idari_sayfasi.Akademisyen_f,
                            text='Akademisyen İşlemleri',
                            bg='#526D82',
                            fg='#DDE6ED',
                            font=('calisto mt',13,'bold'))
                            başlık.place(x=0,y=0,width=200,height=35)


                            def change_color_Ara_btn1(event):
                                Ara_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Ara_btn2(event):
                                Ara_btn.config(bg="#27374D", fg="#DDE6ED")
                            Ara_btn=Button(Idari_sayfasi.Akademisyen_f,text='Akademisyen Ara',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Akademisyen_ara_btn)
                            Ara_btn.place(x=5,y=40,width=190,height=30)
                            Ara_btn.bind("<Enter>", change_color_Ara_btn1)  
                            Ara_btn.bind("<Leave>", change_color_Ara_btn2) 

                            def change_color_Ekle_btn1(event):
                                Ekle_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Ekle_btn2(event):
                                Ekle_btn.config(bg="#27374D", fg="#DDE6ED")
                            Ekle_btn=Button(Idari_sayfasi.Akademisyen_f,text='Akademisyen Ekle',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Akademisyen_ekle_btn)
                            Ekle_btn.place(x=5,y=75,width=190,height=30)
                            Ekle_btn.bind("<Enter>", change_color_Ekle_btn1)  
                            Ekle_btn.bind("<Leave>", change_color_Ekle_btn2) 
                            

                            def change_color_Sil_btn1(event):
                                Sil_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Sil_btn2(event):
                                Sil_btn.config(bg="#27374D", fg="#DDE6ED")
                            Sil_btn=Button(Idari_sayfasi.Akademisyen_f,text='Akademisyen Sil',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Akademisyen_sil_btn)
                            Sil_btn.place(x=5,y=110,width=190,height=30)
                            Sil_btn.bind("<Enter>", change_color_Sil_btn1)  
                            Sil_btn.bind("<Leave>", change_color_Sil_btn2) 


                            def change_color_Güncelle_btn1(event):
                                Güncelle_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Güncelle_btn2(event):
                                Güncelle_btn.config(bg="#27374D", fg="#DDE6ED")
                            Güncelle_btn=Button(Idari_sayfasi.Akademisyen_f,text='Akademisyen Güncelle',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Akademisyen_guncelle_btn)
                            Güncelle_btn.place(x=5,y=145,width=190,height=30)
                            Güncelle_btn.bind("<Enter>", change_color_Güncelle_btn1)  
                            Güncelle_btn.bind("<Leave>", change_color_Güncelle_btn2) 


        
                        #--------İdari button fremi---------#


                        def İdari_btn_f():


                            #------İdari arama ekleme günceleme silme buttonları----#

                            def İdari_ara_btn():

                                try:
                                    Idari_sayfasi.idari_f.destroy()
                                except:
                                    pass   
                                try:
                                    Idari_sayfasi.aram_tuşlar_fremi.destroy()
                                except:
                                    pass   
                                try:
                                    Idari_sayfasi.frame_arama_sayfasi.destroy()
                                except:
                                    pass   



                                Idari_sayfasi.aram_tuşlar_fremi=Frame(frame_ust,bg="#9DB2BF")
                                Idari_sayfasi.aram_tuşlar_fremi.place(x=0,y=0,width=970,height=45)

                                
                                
                                title_İdari_arama_başlık=Label(Idari_sayfasi.aram_tuşlar_fremi,
                                text='İdari Arama',
                                bg='#526D82',
                                fg='#DDE6ED',
                                font=('calisto mt',15,'bold'))
                                title_İdari_arama_başlık.place(x=0,y=0,width=250,height=49)

                                arama_turu=StringVar()
                                i_search=StringVar()
                                


                                combo_İdari_arama_seçenekleri=ttk.Combobox(Idari_sayfasi.aram_tuşlar_fremi,state='readonly',textvariable=arama_turu)
                                combo_İdari_arama_seçenekleri['value']=('Tüm İdariler','İdari No İle Arama','İdari Adı İle Arama')
                                combo_İdari_arama_seçenekleri.place(x=275,y=6,width=180,height=35)


                                def on_entry_click_arama(event):
                                    if en_search.get() == "Arama":
                                        en_search.delete(0, END)
                                        en_search.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)
    

                                en_search=Entry(Idari_sayfasi.aram_tuşlar_fremi,bd='2',fg='grey',justify='center',textvariable=i_search)
                                en_search.place(x=500,y=6,width=200,height=35)
                                en_search.insert(0, "Arama")
                                en_search.bind("<FocusIn>", on_entry_click_arama)


                                def İdari_arama_işlemleri():
                                    if(arama_turu.get()=='Tüm İdariler'):
                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        cr.execute("SELECT * FROM Adminler")
                                        sonuc_arama_sayfasi=cr.fetchall()

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','İdari_no','ad','tc','tarih','cinsiyet','tel','email'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('İdari_no',text='İdari No')
                                        arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                        arama_sayfasi_table.heading('tc',text='TC')
                                        arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                        arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                        arama_sayfasi_table.heading('tel',text='Tel No')
                                        arama_sayfasi_table.heading('email',text='Email')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('İdari_no',width=60,anchor='center')
                                        arama_sayfasi_table.column('ad',width=215,anchor='center')
                                        arama_sayfasi_table.column('tc',width=100,anchor='center')
                                        arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                        arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                        arama_sayfasi_table.column('tel',width=91,anchor='center')
                                        arama_sayfasi_table.column('email',width=230,anchor='center')

                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                                arama_eklenecek_liste.append(str(sonuc_arama_sayfasi[i][2])+" "+str(sonuc_arama_sayfasi[i][3]))  # Ad soyad
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][8])  # Cinsiyet
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # tel
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # Email

                                              
                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)
                                        
                                    

                                    elif(arama_turu.get()=='İdari No İle Arama' or ''):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass

                                        cr.execute(f"SELECT * FROM Adminler where Admin_No='{i_search.get().strip()}'")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                        

                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','İdari_no','ad','tc','tarih','cinsiyet','tel','email'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('İdari_no',text='İdari No')
                                        arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                        arama_sayfasi_table.heading('tc',text='TC')
                                        arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                        arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                        arama_sayfasi_table.heading('tel',text='Tel No')
                                        arama_sayfasi_table.heading('email',text='Email')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('İdari_no',width=60,anchor='center')
                                        arama_sayfasi_table.column('ad',width=215,anchor='center')
                                        arama_sayfasi_table.column('tc',width=100,anchor='center')
                                        arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                        arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                        arama_sayfasi_table.column('tel',width=91,anchor='center')
                                        arama_sayfasi_table.column('email',width=230,anchor='center')

                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                                arama_eklenecek_liste.append(str(sonuc_arama_sayfasi[i][2])+" "+str(sonuc_arama_sayfasi[i][3]))  # Ad soyad
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][8])  # Cinsiyet
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # tel
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # Email

                                               
                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                        for row in arama_eklenecek_liste_son:
                                            arama_sayfasi_table.insert("",END, value=row)
                                        
                                    
                                    elif(arama_turu.get()=='İdari Adı İle Arama'):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass


                                        cr.execute(f"SELECT * FROM Adminler where Admin_Ad LIKE '%{i_search.get().title().strip()}%'")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                        
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','İdari_no','ad','tc','tarih','cinsiyet','tel','email'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('İdari_no',text='İdari No')
                                        arama_sayfasi_table.heading('ad',text='Ad Soyad')
                                        arama_sayfasi_table.heading('tc',text='TC')
                                        arama_sayfasi_table.heading('tarih',text='Doğum Tarihi')
                                        arama_sayfasi_table.heading('cinsiyet',text='Cinsiyeti')
                                        arama_sayfasi_table.heading('tel',text='Tel No')
                                        arama_sayfasi_table.heading('email',text='Email')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('İdari_no',width=60,anchor='center')
                                        arama_sayfasi_table.column('ad',width=215,anchor='center')
                                        arama_sayfasi_table.column('tc',width=100,anchor='center')
                                        arama_sayfasi_table.column('tarih',width=100,anchor='center')
                                        arama_sayfasi_table.column('cinsiyet',width=55,anchor='center')
                                        arama_sayfasi_table.column('tel',width=91,anchor='center')
                                        arama_sayfasi_table.column('email',width=230,anchor='center')


                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Ogrenci no
                                                arama_eklenecek_liste.append(str(sonuc_arama_sayfasi[i][2])+" "+str(sonuc_arama_sayfasi[i][3]))  # Ad soyad
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # TC
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # Dogum Tarihi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][8])  # Cinsiyet
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # tel
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # Email
                                               

                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)

                           

                                ara_but=Button(Idari_sayfasi.aram_tuşlar_fremi,text='Ara',font=10,bg='#526D82',fg='#DDE6ED',command=İdari_arama_işlemleri)#,command=arama_sayfasi
                                ara_but.place(x=720,y=6,width=200,height=35)

                            def İdari_ekle_btn():
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x500+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=500)

                                title_top68=Label(ilk_sayfa,
                                text='İdari Personel Ekleme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)



                                fr1 = Frame(pro1, width=400, height=450, bg="#27374D")
                                fr1.pack(pady=70)

                                lbl = Label(fr1, text="Tc", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=15)
                                lbl = Label(fr1, text="Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=55)
                                lbl = Label(fr1, text="Soyadı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=95)
                                lbl = Label(fr1, text="Doğum Tarihi", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=135)
                                lbl = Label(fr1, text="Cinsiyet", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=175)
                                lbl = Label(fr1, text="Tel No", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=215)
                                lbl = Label(fr1, text="E-Posta", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=255)
                                lbl = Label(fr1, text="Şifre", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=295)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=15)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=55)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=95)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=135)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=175)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=215)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=255)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=295)


                                entry_tc = Entry(fr1)
                                entry_tc.place(x=200, y=20)
                                entry_ad = Entry(fr1)
                                entry_ad.place(x=200, y=60)
                                entry_soyad = Entry(fr1)
                                entry_soyad.place(x=200, y=100)
                                entry_dogum_tarihi = Entry(fr1)
                                entry_dogum_tarihi.place(x=200, y=140)
                                entry_telno = Entry(fr1)
                                entry_telno.place(x=200, y=220)
                                entry_eposta = Entry(fr1)
                                entry_eposta.place(x=200, y=260)
                                entry_sifre = Entry(fr1)
                                entry_sifre.place(x=200, y=300)
                                entry_cinsiyet = Entry(fr1)
                                entry_cinsiyet.place(x=200, y=180)

                                def tamamla():
                                

                                    tc = entry_tc.get()
                                    ad = entry_ad.get()
                                    soyad = entry_soyad.get()
                                    dogum_tarihi = entry_dogum_tarihi.get()
                                    telno = entry_telno.get()
                                    eposta = entry_eposta.get()
                                    sifre = entry_sifre.get()
                                    cinsiyet = entry_cinsiyet.get()


                                    cr.execute(f"INSERT INTO Adminler (Admin_Tc, Admin_Ad, Admin_Soyad, Admin_DT, Admin_TelNo, Admin_Eposta, Admin_Sifre, Admin_Cinsiyeti) VALUES ('{tc}','{ad}','{soyad}','{dogum_tarihi}','{telno}','{eposta}','{sifre}','{cinsiyet}')")
                                    cr.commit()


                                def bitir():
                                    tamamla()
                                    pro1.destroy()

                                btn_cik = Button(self.pro1, text="KAYDET", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_cik.place(x=120, y=420)



                            def Idari_sil_btn():
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x250+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=250)

                                title_top68=Label(ilk_sayfa,
                                text='İdari Silme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)

                                
                                fr1 = Frame(pro1, width=400, height=200, bg="#27374D")
                                fr1.pack(pady=50)

                                lbl = Label(fr1, text="İdari No", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=20)
                                lbl = Label(fr1, text="Ad", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=65)
                                lbl = Label(fr1, text="Soyad", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=110)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=20)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=65)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=110)

                                entry_no = Entry(fr1)
                                entry_no.place(x=200, y=25)
                                entry_ad = Entry(fr1)
                                entry_ad.place(x=200, y=70)
                                entry_soyad = Entry(fr1)
                                entry_soyad.place(x=200, y=115)

                                def tamamla():
                                

                                    no = entry_no.get()
                                    ad = entry_ad.get()
                                    soyad = entry_soyad.get()

                                    cr.execute(f"SELECT Admin_Ad,Admin_Soyad FROM Adminler WHERE Admin_No= '{no}'")
                                    kontrol = cr.fetchall()


                                    if(len(kontrol)>0):
                                        if(ad==kontrol[0][0]):
                                            if(soyad==kontrol[0][1]):
                                                cr.execute(f"DELETE FROM Adminler WHERE Admin_No='{no}' AND Admin_Ad='{ad}' AND Admin_Soyad='{soyad}'")
                                                cr.commit()
                                            else:
                                                messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                        else:
                                            messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                    else:
                                        messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')

                                def bitir():
                                    tamamla()
                                    pro1.destroy()

                                btn_cik = Button(self.pro1, text="SİL", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_cik.place(x=120, y=200)


                            def Idari_guncelle_btn():
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x500+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=500)

                                title_top68=Label(ilk_sayfa,
                                text='Bilgi Güncelleme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)

                                fr2 = Frame(pro1, width=400, height=450, bg="#27374D")
                                fr2.pack(pady=100)

                                

                                lbl_u_ogr_no=Label(fr2,text='İdari No: ', font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")         ####### ogr no ########
                                lbl_u_ogr_no.place(x=30,y=35)
                                en_u_ogr_no=Entry(fr2,bd=2,justify='center')
                                en_u_ogr_no.place(x=200,y=40)

                                lbl_u_ogr_ad=Label(fr2,text='İdari Ad: ', font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")         ####### ogr ad ########
                                lbl_u_ogr_ad.place(x=30,y=80)
                                en_ogr_ad=Entry(fr2,bd=2,justify='center')
                                en_ogr_ad.place(x=200,y=85)
                                lbl_u_ogr_soyad=Label(fr2,text='İdari Soyad: ', font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")         ####### ogr ad ########
                                lbl_u_ogr_soyad.place(x=30,y=125)
                                en_ogr_soyad=Entry(fr2,bd=2,justify='center')
                                en_ogr_soyad.place(x=200,y=130)
                                
                                no=en_u_ogr_no.get()


                                def musab():
                                    cr.execute(f"SELECT Admin_Ad, Admin_Soyad FROM Adminler WHERE Admin_No= '{en_u_ogr_no.get()}'")
                                    kontrol = cr.fetchall()

                                    if(len(kontrol)>0):
                                        if(en_ogr_ad.get()==kontrol[0][0]):
                                            if(en_ogr_soyad.get()==kontrol[0][1]):

                                       
                                                no=en_u_ogr_no.get()
                                                no_1=no
                                                fr2.destroy()
                                                fr1 = Frame(pro1, width=400, height=450, bg="#27374D")
                                                fr1.pack(pady=45)

                                                

                                                lbl = Label(fr1, text="Tc", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=15)
                                                lbl = Label(fr1, text="Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=55)
                                                lbl = Label(fr1, text="Soyadı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                                lbl.place(x=30, y=95)
                                                lbl = Label(fr1, text="Doğum Tarihi", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                                lbl.place(x=30, y=135)
                                                lbl = Label(fr1, text="Cinsiyet", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=175)
                                                lbl = Label(fr1, text="Tel No", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                                lbl.place(x=30, y=215)
                                                lbl = Label(fr1, text="E-Posta", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                                lbl.place(x=30, y=255)
                                                lbl = Label(fr1, text="Şifre", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                                lbl.place(x=30, y=295)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=15)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=55)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=95)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=135)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=175)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=215)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=255)
                                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                                lbl.place(x=175,y=295)

                                                entry_tc = Entry(fr1)
                                                entry_tc.place(x=200, y=20)
                                                entry_ad = Entry(fr1)
                                                entry_ad.place(x=200, y=60)
                                                entry_soyad = Entry(fr1)
                                                entry_soyad.place(x=200, y=100)
                                                entry_dogum_tarihi = Entry(fr1)
                                                entry_dogum_tarihi.place(x=200, y=140)
                                                entry_cinsiyet = Entry(fr1)
                                                entry_cinsiyet.place(x=200, y=180)
                                                entry_telno = Entry(fr1)
                                                entry_telno.place(x=200, y=220)
                                                entry_eposta = Entry(fr1)
                                                entry_eposta.place(x=200, y=260)
                                                entry_sifre = Entry(fr1)
                                                entry_sifre.place(x=200, y=300)

                                                def f_save_btn():
                                                    
                                                    
                                                    cr.execute(f"UPDATE Adminler SET Admin_Tc='{entry_tc.get().strip()}', Admin_Ad='{entry_ad.get().strip().title()}',Admin_Soyad='{entry_soyad.get().strip().title()}', Admin_DT='{entry_dogum_tarihi.get().strip()}', Admin_TelNo='{entry_telno.get().strip()}', Admin_Eposta='{entry_eposta.get().strip()}',Admin_Sifre='{entry_sifre.get().strip()}', Admin_Cinsiyeti='{entry_cinsiyet.get()}' WHERE Admin_No='{no_1}'")
                                                    db.commit()
                                                
                                                    self.pro1.destroy()

                                                def f_add_close_btn():
                                                    self.pro1.destroy()


                                                save_btn=Button(fr1,text='Güncelle', font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=10,command=f_save_btn)
                                                save_btn.place(x=85,y=350)

                                                add_close_btn=Button(fr1,text='Kapat', font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=10,command=f_add_close_btn)
                                                add_close_btn.place(x=215,y=350)
                                            else:
                                                messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                                self.pro1.destroy()
                                        else:
                                            messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                            self.pro1.destroy()
                                    else:
                                        messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                        self.pro1.destroy()
                                
                                def bitir():
                                    musab()
                                    
                                btn_ara = Button(fr2, text="ARA", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_ara.place(x=120,y=200)


                                
                           
                            #----------- diğer fremleri kapat----------# 
                            try:
                                Idari_sayfasi.Bölüm_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.ogrenci_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.Akademisyen_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.Ders_f.destroy()
                            except:
                                pass
                           
                            Idari_sayfasi.idari_f=Frame(frame_b,bg='#9DB2BF')
                            Idari_sayfasi.idari_f.place(x=5,y=300,width=200,height=190)
                           
                            başlık=Label(Idari_sayfasi.idari_f,
                            text='İdari İşlemleri',
                            bg='#526D82',
                            fg='#DDE6ED',
                            font=('calisto mt',15,'bold'))
                            başlık.place(x=0,y=0,width=200,height=35)

                            def change_color_Ara_btn1(event):
                                Ara_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Ara_btn2(event):
                                Ara_btn.config(bg="#27374D", fg="#DDE6ED")
                            Ara_btn=Button(Idari_sayfasi.idari_f,text='İdari Ara',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=İdari_ara_btn)
                            Ara_btn.place(x=5,y=40,width=190,height=30)
                            Ara_btn.bind("<Enter>", change_color_Ara_btn1)  
                            Ara_btn.bind("<Leave>", change_color_Ara_btn2) 

                            def change_color_Ekle_btn1(event):
                                Ekle_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Ekle_btn2(event):
                                Ekle_btn.config(bg="#27374D", fg="#DDE6ED")
                            Ekle_btn=Button(Idari_sayfasi.idari_f,text='İdari Ekle',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=İdari_ekle_btn)
                            Ekle_btn.place(x=5,y=75,width=190,height=30)
                            Ekle_btn.bind("<Enter>", change_color_Ekle_btn1)  
                            Ekle_btn.bind("<Leave>", change_color_Ekle_btn2) 
                            

                            def change_color_Sil_btn1(event):
                                Sil_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Sil_btn2(event):
                                Sil_btn.config(bg="#27374D", fg="#DDE6ED")
                            Sil_btn=Button(Idari_sayfasi.idari_f,text='İdari Sil',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Idari_sil_btn)
                            Sil_btn.place(x=5,y=110,width=190,height=30)
                            Sil_btn.bind("<Enter>", change_color_Sil_btn1)  
                            Sil_btn.bind("<Leave>", change_color_Sil_btn2) 


                            def change_color_Güncelle_btn1(event):
                                Güncelle_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Güncelle_btn2(event):
                                Güncelle_btn.config(bg="#27374D", fg="#DDE6ED")
                            Güncelle_btn=Button(Idari_sayfasi.idari_f,text='İdari Güncelle',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Idari_guncelle_btn)
                            Güncelle_btn.place(x=5,y=145,width=190,height=30)
                            Güncelle_btn.bind("<Enter>", change_color_Güncelle_btn1)  
                            Güncelle_btn.bind("<Leave>", change_color_Güncelle_btn2) 


                        



                        
                         #--------Bölüm button fremi---------#


                        #--------Bölüm button fremi---------#

                        def Bölüm_btn_f():

                            #------Bölüm arama ekleme günceleme silme buttonları----#

                            def Bolum_ara_btn():
                                
                                Idari_sayfasi.aram_tuşlar_fremi=Frame(frame_ust,bg="#9DB2BF")
                                Idari_sayfasi.aram_tuşlar_fremi.place(x=0,y=0,width=970,height=45)

                                
                                
                                title_bolum_arama_başlık=Label(Idari_sayfasi.aram_tuşlar_fremi,
                                text='Bölüm Arama',
                                bg='#526D82',
                                fg='#DDE6ED',
                                font=('calisto mt',15,'bold'))
                                title_bolum_arama_başlık.place(x=0,y=0,width=250,height=49)

                                arama_turu=StringVar()
                                i_search=StringVar()
                                


                                combo_bolum_arama_seçenekleri=ttk.Combobox(Idari_sayfasi.aram_tuşlar_fremi,state='readonly',textvariable=arama_turu)
                                combo_bolum_arama_seçenekleri['value']=('Tüm Bölümler','Bölüm Kodu İle Arama','Bölüm Adı İle Arama')
                                combo_bolum_arama_seçenekleri.place(x=275,y=6,width=180,height=35)


                                def on_entry_click_arama(event):
                                    if en_search.get() == "Arama":
                                        en_search.delete(0, END)
                                        en_search.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)
    

                                en_search=Entry(Idari_sayfasi.aram_tuşlar_fremi,bd='2',fg='grey',justify='center',textvariable=i_search)
                                en_search.place(x=500,y=6,width=200,height=35)
                                en_search.insert(0, "Arama")
                                en_search.bind("<FocusIn>", on_entry_click_arama)


                                def bolum_arama_işlemleri():
                                    if(arama_turu.get()=='Tüm Bölümler'):
                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        cr.execute("SELECT * FROM Bolumler")
                                        sonuc_arama_sayfasi=cr.fetchall()

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','Bölüm_ID','Bölüm_Kodu','Bölüm_Adı'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('Bölüm_ID',text='Bölüm ID')
                                        arama_sayfasi_table.heading('Bölüm_Kodu',text='Bölüm Kodu')
                                        arama_sayfasi_table.heading('Bölüm_Adı',text='Bölüm Adı')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('Bölüm_ID',width=50,anchor='center')
                                        arama_sayfasi_table.column('Bölüm_Kodu',width=100,anchor='center')
                                        arama_sayfasi_table.column('Bölüm_Adı',width=200,anchor='center')
                                        

                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Bolum Id
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # Bolum Kodu
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2])  # Bolum Ad
                                              
                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)
                                        
                                    

                                    elif(arama_turu.get()=='Bölüm Kodu İle Arama'):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass

                                        cr.execute(f"SELECT * FROM Bolumler where Bolum_Kodu='{i_search.get().strip()}'")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                        

                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','Bölüm_ID','Bölüm_Kodu','Bölüm_Adı'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('Bölüm_ID',text='Bölüm ID')
                                        arama_sayfasi_table.heading('Bölüm_Kodu',text='Bölüm Kodu')
                                        arama_sayfasi_table.heading('Bölüm_Adı',text='Bölüm Adı')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('Bölüm_ID',width=50,anchor='center')
                                        arama_sayfasi_table.column('Bölüm_Kodu',width=100,anchor='center')
                                        arama_sayfasi_table.column('Bölüm_Adı',width=200,anchor='center')

                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Bolum Id
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # Bolum Kodu
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2])  # Bolum Ad

                                               
                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                        for row in arama_eklenecek_liste_son:
                                            arama_sayfasi_table.insert("",END, value=row)
                                        
                                    
                                    elif(arama_turu.get()=='Bölüm Adı İle Arama'):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass


                                        cr.execute(f"SELECT * FROM Bolumler where Bolum_Ad LIKE '%{i_search.get().title().strip()}%'")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                        
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','Bölüm_ID','Bölüm_Kodu','Bölüm_Adı'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('Bölüm_ID',text='Bölüm ID')
                                        arama_sayfasi_table.heading('Bölüm_Kodu',text='Bölüm Kodu')
                                        arama_sayfasi_table.heading('Bölüm_Adı',text='Bölüm Adı')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('Bölüm_ID',width=50,anchor='center')
                                        arama_sayfasi_table.column('Bölüm_Kodu',width=100,anchor='center')
                                        arama_sayfasi_table.column('Bölüm_Adı',width=200,anchor='center')


                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][0])  # Bolum Id
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # Bolum Kodu
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2])  # Bolum Ad
                                               

                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)

                           

                                ara_but=Button(Idari_sayfasi.aram_tuşlar_fremi,text='Ara',font=10,bg='#526D82',fg='#DDE6ED',command=bolum_arama_işlemleri)#,command=arama_sayfasi
                                ara_but.place(x=720,y=6,width=200,height=35)

                            def Bolum_ekle_btn():
                                pro1 = Tk()
                                self.pro1 = pro1
                                self.pro1.geometry("400x250+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=250)

                                title_top68=Label(ilk_sayfa,
                                text='Bölüm Ekleme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)



                                fr1 = Frame(pro1, width=400, height=250, bg="#27374D")
                                fr1.place(x=0,y=70,width=400,height=180)

                                lbl = Label(fr1, text="Bölüm Kodu", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=15)
                                lbl = Label(fr1, text="Bölüm Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=55)
                                
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=15)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=55)
                                

                                entry_bolum_kodu = Entry(fr1)
                                entry_bolum_kodu.place(x=200, y=20)
                                entry_bolum_adi = Entry(fr1)
                                entry_bolum_adi.place(x=200, y=60)
                                

                                def tamamla():
                                

                                    bolum_kodu = entry_bolum_kodu.get().strip()
                                    bolum_adi = entry_bolum_adi.get().strip().capitalize()


                                    cr.execute(f"INSERT INTO Bolumler (Bolum_Kodu, Bolum_Ad) VALUES ('{bolum_kodu}','{bolum_adi}')")
                                    cr.commit()


                                def bitir():
                                    tamamla()
                                    pro1.destroy()

                                btn_cik = Button(self.pro1, text="KAYDET", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_cik.place(x=120, y=190)

                            def Bolum_sil_btn():
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x250+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=250)

                                title_top68=Label(ilk_sayfa,
                                text='Bölüm  Silme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)

                                
                                fr1 = Frame(pro1, width=400, height=200, bg="#27374D")
                                fr1.pack(pady=50)

                                lbl = Label(fr1, text="Bölüm Kodu", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=20)
                                lbl = Label(fr1, text="Bölüm Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=65)
                                
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=20)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=65)

                                entry_bolum_kodu = Entry(fr1)
                                entry_bolum_kodu.place(x=200, y=25)
                                entry_bolum_adi = Entry(fr1)
                                entry_bolum_adi.place(x=200, y=70)

                                def tamamla():
                                

                                    bolum_kodu = entry_bolum_kodu.get().strip()
                                    bolum_adi = entry_bolum_adi.get().strip().capitalize()

                                    cr.execute(f"SELECT Bolum_Ad, Bolum_Id FROM Bolumler WHERE Bolum_Kodu= '{bolum_kodu}'")
                                    kontrol = cr.fetchone()
                                    print(kontrol)


                                    if(len(kontrol)>0):
                                        if(bolum_adi==kontrol[0]):
                                            cr.execute(f"DELETE FROM Bolumler WHERE Bolum_Id='{kontrol[1]}'")
                                            cr.commit()
                                        else:
                                            messagebox.showinfo('Hata','Böyle bir Bölüm bulunmamaktadır..!')
                                    else:
                                        messagebox.showinfo('Hata','Böyle bir Bölüm bulunmamaktadır..!')

                                def bitir():
                                    tamamla()
                                    pro1.destroy()

                                btn_cik = Button(self.pro1, text="SİL", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_cik.place(x=120,y=200)

                            def Bolum_guncelle_btn():
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x500+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=500)

                                title_top68=Label(ilk_sayfa,
                                text='Bilgi Güncelleme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)

                                fr2 = Frame(pro1, bg="#27374D")
                                fr2.place(x=0,y=50,width=400,height=450)

                                

                                lbl=Label(fr2,text='Bölüm Kodu: ', font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")         ####### ogr no ########
                                lbl.place(x=30,y=35)
                                en_bolum_kod=Entry(fr2,bd=2,justify='center')
                                en_bolum_kod.place(x=200,y=40)

                                lbl=Label(fr2,text='Bölüm Adı: ', font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")         ####### ogr ad ########
                                lbl.place(x=30,y=80)
                                en_bolum_ad=Entry(fr2,bd=2,justify='center')
                                en_bolum_ad.place(x=200,y=85)


                                def musab():
                                    cr.execute(f"SELECT Bolum_Ad FROM Bolumler WHERE Bolum_Kodu= '{en_bolum_kod.get().strip()}'")
                                    kontrol = cr.fetchall()

                                    if(len(kontrol)==1):
                                        if(en_bolum_ad.get().strip().title()==kontrol[0][0]):
                                       
                                            kod=en_bolum_kod.get().strip()
                                            fr2.destroy()
                                            fr1 = Frame(pro1, bg="#27374D")
                                            fr1.place(x=0,y=50,width=400,height=450)

                                            lbl = Label(fr1, text="Bölüm Kodu", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                            lbl.place(x=30, y=15)
                                            lbl = Label(fr1, text="Bölüm Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                            lbl.place(x=30, y=55)
                                            
                                            lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                            lbl.place(x=175,y=15)
                                            lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                            lbl.place(x=175,y=55)
                                            

                                            entry_bolum_kodu = Entry(fr1)
                                            entry_bolum_kodu.place(x=200, y=20)
                                            entry_bolum_adi = Entry(fr1)
                                            entry_bolum_adi.place(x=200, y=60)


                                            def f_save_btn():
                                                
                                                
                                                cr.execute(f"UPDATE Bolumler SET Bolum_Kodu='{entry_bolum_kodu.get().strip()}', Bolum_Ad='{entry_bolum_adi.get().strip().title()}' WHERE Bolum_Kodu='{kod}'")
                                                db.commit()
                                            
                                                self.pro1.destroy()

                                            def f_add_close_btn():
                                                self.pro1.destroy()


                                            save_btn=Button(fr1,text='Güncelle', font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=10,command=f_save_btn)
                                            save_btn.place(x=85,y=350)

                                            add_close_btn=Button(fr1,text='Kapat', font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=10,command=f_add_close_btn)
                                            add_close_btn.place(x=215,y=350)
                                            
                                        else:
                                            messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                            self.pro1.destroy()
                                    else:
                                        messagebox.showinfo('Hata','Böyle bir kullanıcı bulunmamaktadır..!')
                                        self.pro1.destroy()
                                
                                def bitir():
                                    musab()
                                    
                                btn_ara = Button(fr2, text="ARA", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_ara.place(x=120,y=200)

                            #----------- diğer fremleri kapat----------#         

                            try:
                                Idari_sayfasi.ogrenci_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.Akademisyen_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.idari_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.Ders_f.destroy()
                            except:
                                pass     

                            Idari_sayfasi.Bölüm_f=Frame(frame_b,bg='#9DB2BF')
                            Idari_sayfasi.Bölüm_f.place(x=5,y=300,width=200,height=190)

                            başlık=Label(Idari_sayfasi.Bölüm_f,
                            text='Bölüm İşlemleri',
                            bg='#526D82',
                            fg='#DDE6ED',
                            font=('calisto mt',15,'bold'))
                            başlık.place(x=0,y=0,width=200,height=35)

                            def change_color_ara_btn1(event):
                                Ara_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_ara_btn2(event):
                                Ara_btn.config(bg="#27374D", fg="#DDE6ED")
                            Ara_btn=Button(Idari_sayfasi.Bölüm_f,text='Bölüm Ara',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Bolum_ara_btn)
                            Ara_btn.place(x=5,y=40,width=190,height=30)
                            Ara_btn.bind("<Enter>", change_color_ara_btn1)  
                            Ara_btn.bind("<Leave>", change_color_ara_btn2) 

                            def change_color_Ekle_btn1(event):
                                Ekle_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Ekle_btn2(event):
                                Ekle_btn.config(bg="#27374D", fg="#DDE6ED")
                            Ekle_btn=Button(Idari_sayfasi.Bölüm_f,text='Bölüm Ekle',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Bolum_ekle_btn)
                            Ekle_btn.place(x=5,y=75,width=190,height=30)
                            Ekle_btn.bind("<Enter>", change_color_Ekle_btn1)  
                            Ekle_btn.bind("<Leave>", change_color_Ekle_btn2) 
                            

                            def change_color_Sil_btn1(event):
                                Sil_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Sil_btn2(event):
                                Sil_btn.config(bg="#27374D", fg="#DDE6ED")
                            Sil_btn=Button(Idari_sayfasi.Bölüm_f,text='Bölüm Sil',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Bolum_sil_btn)
                            Sil_btn.place(x=5,y=110,width=190,height=30)
                            Sil_btn.bind("<Enter>", change_color_Sil_btn1)  
                            Sil_btn.bind("<Leave>", change_color_Sil_btn2) 


                            def change_color_Güncelle_btn1(event):
                                Güncelle_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Güncelle_btn2(event):
                                Güncelle_btn.config(bg="#27374D", fg="#DDE6ED")
                            Güncelle_btn=Button(Idari_sayfasi.Bölüm_f,text='Bölüm Güncelle',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Bolum_guncelle_btn)
                            Güncelle_btn.place(x=5,y=145,width=190,height=30)
                            Güncelle_btn.bind("<Enter>", change_color_Güncelle_btn1)  
                            Güncelle_btn.bind("<Leave>", change_color_Güncelle_btn2) 


                        #--------Ders button fremi---------#


                        def Ders_btn_f():


                            #------Ders arama ekleme günceleme silme buttonları----#

                            def Ders_ara_btn():
                                Idari_sayfasi.aram_tuşlar_fremi=Frame(frame_ust,bg="#9DB2BF")
                                Idari_sayfasi.aram_tuşlar_fremi.place(x=0,y=0,width=970,height=45)

                                
                                
                                title_ders_arama_başlık=Label(Idari_sayfasi.aram_tuşlar_fremi,
                                text='Ders Arama',
                                bg='#526D82',
                                fg='#DDE6ED',
                                font=('calisto mt',15,'bold'))
                                title_ders_arama_başlık.place(x=0,y=0,width=250,height=49)

                                arama_turu=StringVar()
                                i_search=StringVar()
                                


                                combo_ders_arama_seçenekleri=ttk.Combobox(Idari_sayfasi.aram_tuşlar_fremi,state='readonly',textvariable=arama_turu)
                                combo_ders_arama_seçenekleri['value']=('Tüm Dersler','Ders Kodu İle Arama','Ders Adı İle Arama', 'Akademisyen Adı İle Arama', 'Bölüm Adı İle Arama')
                                combo_ders_arama_seçenekleri.place(x=275,y=6,width=180,height=35)


                                def on_entry_click_arama(event):
                                    if en_search.get() == "Arama":
                                        en_search.delete(0, END)
                                        en_search.config(fg='#27374D')  # Yazı rengini değiştirme (isteğe bağlı)
    

                                en_search=Entry(Idari_sayfasi.aram_tuşlar_fremi,bd='2',fg='grey',justify='center',textvariable=i_search)
                                en_search.place(x=500,y=6,width=200,height=35)
                                en_search.insert(0, "Arama")
                                en_search.bind("<FocusIn>", on_entry_click_arama)


                                def ders_arama_işlemleri():
                                    if(arama_turu.get()=='Tüm Dersler'):
                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        cr.execute("SELECT * FROM Dersler Order BY Ogr_Sinif, Donem")
                                        sonuc_arama_sayfasi=cr.fetchall()

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','Ders_Kodu','Ders_Adi', 'Akademisyen', 'Bolum' ,'Sinif' , 'Donem' ,'AKTS', 'Kredi', 'Teori', 'Uygulama'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('Ders_Kodu',text='Ders Kodu')
                                        arama_sayfasi_table.heading('Ders_Adi',text='Ders Adı')
                                        arama_sayfasi_table.heading('Akademisyen',text='Akademisyen')
                                        arama_sayfasi_table.heading('Bolum',text='Bolum')
                                        arama_sayfasi_table.heading('Sinif',text='Sinif')
                                        arama_sayfasi_table.heading('Donem',text='Donem')
                                        arama_sayfasi_table.heading('AKTS',text='AKTS')
                                        arama_sayfasi_table.heading('Kredi',text='Kredi')
                                        arama_sayfasi_table.heading('Teori',text='Teori')
                                        arama_sayfasi_table.heading('Uygulama',text='Uygulama')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('Ders_Kodu',width=75,anchor='center')
                                        arama_sayfasi_table.column('Ders_Adi',width=275,anchor='center')
                                        arama_sayfasi_table.column('Akademisyen',width=175,anchor='center')
                                        arama_sayfasi_table.column('Bolum',width=200,anchor='center')
                                        arama_sayfasi_table.column('Sinif',width=50,anchor='center')
                                        arama_sayfasi_table.column('Donem',width=50,anchor='center')
                                        arama_sayfasi_table.column('AKTS',width=50,anchor='center')
                                        arama_sayfasi_table.column('Kredi',width=50,anchor='center')
                                        arama_sayfasi_table.column('Teori',width=50,anchor='center')
                                        arama_sayfasi_table.column('Uygulama',width=50,anchor='center')
                                        

                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # Ders kodu
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2])  # Ders Adi

                                                cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad FROM Ogretmenler Where Ogrt_No={sonuc_arama_sayfasi[i][7]}")
                                                ogretmen_adi=cr.fetchone()
                                                cr.execute(f"SELECT Bolum_Ad FROM Bolumler Where Bolum_Id={sonuc_arama_sayfasi[i][8]}")
                                                bolum_adi=cr.fetchone()

                                                arama_eklenecek_liste.append(ogretmen_adi[0] + " " + ogretmen_adi[1])  # akademisyen
                                                arama_eklenecek_liste.append(bolum_adi[0])  # bolum
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][9])  # sinif
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][10])  # donem
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # akts
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][3])  # kredi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # teori
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # uygulama
                                              
                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)
                                        
                                    

                                    elif(arama_turu.get()=='Ders Kodu İle Arama'):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass

                                        cr.execute(f"SELECT * FROM Dersler where Ders_Kodu='{i_search.get().strip()}' Order BY Ogr_Sinif, Donem")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                        

                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','Ders_Kodu','Ders_Adi', 'Akademisyen', 'Bolum' ,'Sinif' , 'Donem' ,'AKTS', 'Kredi', 'Teori', 'Uygulama'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('Ders_Kodu',text='Ders Kodu')
                                        arama_sayfasi_table.heading('Ders_Adi',text='Ders Adı')
                                        arama_sayfasi_table.heading('Akademisyen',text='Akademisyen')
                                        arama_sayfasi_table.heading('Bolum',text='Bolum')
                                        arama_sayfasi_table.heading('Sinif',text='Sinif')
                                        arama_sayfasi_table.heading('Donem',text='Donem')
                                        arama_sayfasi_table.heading('AKTS',text='AKTS')
                                        arama_sayfasi_table.heading('Kredi',text='Kredi')
                                        arama_sayfasi_table.heading('Teori',text='Teori')
                                        arama_sayfasi_table.heading('Uygulama',text='Uygulama')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('Ders_Kodu',width=75,anchor='center')
                                        arama_sayfasi_table.column('Ders_Adi',width=275,anchor='center')
                                        arama_sayfasi_table.column('Akademisyen',width=175,anchor='center')
                                        arama_sayfasi_table.column('Bolum',width=200,anchor='center')
                                        arama_sayfasi_table.column('Sinif',width=50,anchor='center')
                                        arama_sayfasi_table.column('Donem',width=50,anchor='center')
                                        arama_sayfasi_table.column('AKTS',width=50,anchor='center')
                                        arama_sayfasi_table.column('Kredi',width=50,anchor='center')
                                        arama_sayfasi_table.column('Teori',width=50,anchor='center')
                                        arama_sayfasi_table.column('Uygulama',width=50,anchor='center')
                                        

                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # Ders kodu
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2])  # Ders Adi

                                                cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad FROM Ogretmenler Where Ogrt_No={sonuc_arama_sayfasi[i][7]}")
                                                ogretmen_adi=cr.fetchone()
                                                cr.execute(f"SELECT Bolum_Ad FROM Bolumler Where Bolum_Id={sonuc_arama_sayfasi[i][8]}")
                                                bolum_adi=cr.fetchone()

                                                arama_eklenecek_liste.append(ogretmen_adi[0] + " " + ogretmen_adi[1])  # akademisyen
                                                arama_eklenecek_liste.append(bolum_adi[0])  # bolum
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][9])  # sinif
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][10])  # donem
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # akts
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][3])  # kredi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # teori
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # uygulama
                                              
                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)
                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)
                                        
                                    
                                    elif(arama_turu.get()=='Ders Adı İle Arama'):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass


                                        cr.execute(f"SELECT * FROM Dersler where Ders_Ad LIKE '%{i_search.get().title().strip()}%' Order BY Ogr_Sinif, Donem")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                        
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','Ders_Kodu','Ders_Adi', 'Akademisyen', 'Bolum' ,'Sinif' , 'Donem' ,'AKTS', 'Kredi', 'Teori', 'Uygulama'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('Ders_Kodu',text='Ders Kodu')
                                        arama_sayfasi_table.heading('Ders_Adi',text='Ders Adı')
                                        arama_sayfasi_table.heading('Akademisyen',text='Akademisyen')
                                        arama_sayfasi_table.heading('Bolum',text='Bolum')
                                        arama_sayfasi_table.heading('Sinif',text='Sinif')
                                        arama_sayfasi_table.heading('Donem',text='Donem')
                                        arama_sayfasi_table.heading('AKTS',text='AKTS')
                                        arama_sayfasi_table.heading('Kredi',text='Kredi')
                                        arama_sayfasi_table.heading('Teori',text='Teori')
                                        arama_sayfasi_table.heading('Uygulama',text='Uygulama')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('Ders_Kodu',width=75,anchor='center')
                                        arama_sayfasi_table.column('Ders_Adi',width=275,anchor='center')
                                        arama_sayfasi_table.column('Akademisyen',width=175,anchor='center')
                                        arama_sayfasi_table.column('Bolum',width=200,anchor='center')
                                        arama_sayfasi_table.column('Sinif',width=50,anchor='center')
                                        arama_sayfasi_table.column('Donem',width=50,anchor='center')
                                        arama_sayfasi_table.column('AKTS',width=50,anchor='center')
                                        arama_sayfasi_table.column('Kredi',width=50,anchor='center')
                                        arama_sayfasi_table.column('Teori',width=50,anchor='center')
                                        arama_sayfasi_table.column('Uygulama',width=50,anchor='center')
                                        

                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # Ders kodu
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2])  # Ders Adi

                                                cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad FROM Ogretmenler Where Ogrt_No={sonuc_arama_sayfasi[i][7]}")
                                                ogretmen_adi=cr.fetchone()
                                                cr.execute(f"SELECT Bolum_Ad FROM Bolumler Where Bolum_Id={sonuc_arama_sayfasi[i][8]}")
                                                bolum_adi=cr.fetchone()

                                                arama_eklenecek_liste.append(ogretmen_adi[0] + " " + ogretmen_adi[1])  # akademisyen
                                                arama_eklenecek_liste.append(bolum_adi[0])  # bolum
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][9])  # sinif
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][10])  # donem
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # akts
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][3])  # kredi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # teori
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # uygulama
                                              
                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)
                                              

                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)


                                    elif(arama_turu.get()=='Akademisyen Adı İle Arama'):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass
                                        try:
                                            cr.execute(f"DROP VIEW ogretmen_adlari")
                                        except:
                                            print(" view silinmedi")

                                        cr.execute(f"Create VIEW ogretmen_adlari AS SELECT CONCAT(Ogrt_Ad,' ', Ogrt_Soyad) AS FULL_NAME, Ogrt_No From Ogretmenler")
                                        #ogretmenler_ad_soyad_no=cr.fetchall()

                                        #for row in ogretmenler_ad_soyad_no:
                                            #print(f"Name: {row[0]}, Number: {row[1]}")


                                        cr.execute(f"SELECT DISTINCT * FROM Dersler where Ogrt_No = (SELECT Ogrt_No FROM ogretmen_adlari Where FULL_NAME LIKE '%{i_search.get().title().strip()}%')")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                        print(sonuc_arama_sayfasi)
                                        print(len(sonuc_arama_sayfasi))
                                        
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','Ders_Kodu','Ders_Adi', 'Akademisyen', 'Bolum' ,'Sinif' , 'Donem' ,'AKTS', 'Kredi', 'Teori', 'Uygulama'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('Ders_Kodu',text='Ders Kodu')
                                        arama_sayfasi_table.heading('Ders_Adi',text='Ders Adı')
                                        arama_sayfasi_table.heading('Akademisyen',text='Akademisyen')
                                        arama_sayfasi_table.heading('Bolum',text='Bolum')
                                        arama_sayfasi_table.heading('Sinif',text='Sinif')
                                        arama_sayfasi_table.heading('Donem',text='Donem')
                                        arama_sayfasi_table.heading('AKTS',text='AKTS')
                                        arama_sayfasi_table.heading('Kredi',text='Kredi')
                                        arama_sayfasi_table.heading('Teori',text='Teori')
                                        arama_sayfasi_table.heading('Uygulama',text='Uygulama')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('Ders_Kodu',width=75,anchor='center')
                                        arama_sayfasi_table.column('Ders_Adi',width=275,anchor='center')
                                        arama_sayfasi_table.column('Akademisyen',width=175,anchor='center')
                                        arama_sayfasi_table.column('Bolum',width=200,anchor='center')
                                        arama_sayfasi_table.column('Sinif',width=50,anchor='center')
                                        arama_sayfasi_table.column('Donem',width=50,anchor='center')
                                        arama_sayfasi_table.column('AKTS',width=50,anchor='center')
                                        arama_sayfasi_table.column('Kredi',width=50,anchor='center')
                                        arama_sayfasi_table.column('Teori',width=50,anchor='center')
                                        arama_sayfasi_table.column('Uygulama',width=50,anchor='center')
                                        

                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # Ders kodu
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2])  # Ders Adi

                                                cr.execute(f"SELECT FULL_NAME FROM ogretmen_adlari Where Ogrt_No={sonuc_arama_sayfasi[i][7]}")
                                                ogretmen_adi=cr.fetchone()

                                                cr.execute(f"SELECT Bolum_Ad FROM Bolumler Where Bolum_Id={sonuc_arama_sayfasi[i][8]}")
                                                bolum_adi=cr.fetchone()

                                                arama_eklenecek_liste.append(ogretmen_adi[0])  # akademisyen
                                                arama_eklenecek_liste.append(bolum_adi[0])  # bolum
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][9])  # sinif
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][10])  # donem
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # akts
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][3])  # kredi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # teori
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # uygulama
                                              
                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)
                                              
                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)

                                        cr.execute(f"DROP VIEW ogretmen_adlari")
                                    elif(arama_turu.get()=='Bölüm Adı İle Arama'):

                                        try:
                                            Idari_sayfasi.frame_arama_sayfasi.destroy()
                                        except:
                                            pass
                                        try:
                                            cr.execute(f"DROP VIEW ogretmen_adlari")
                                        except:
                                            print(" view silinmedi")

                                    
                                        cr.execute(f"SELECT DISTINCT * FROM Dersler where Bolum_Id = (SELECT Bolum_Id FROM Bolumler Where Bolum_Ad LIKE '%{i_search.get().title().strip()}%')")
                                        sonuc_arama_sayfasi=cr.fetchall()
                                        print(sonuc_arama_sayfasi)
                                        print(len(sonuc_arama_sayfasi))
                                        
                                        Idari_sayfasi.frame_arama_sayfasi=Frame(orta_fremi,bg='#27374D')
                                        Idari_sayfasi.frame_arama_sayfasi.place(x=0,y=0,width=1312,height=self.omer.winfo_screenheight()-148)

                                        scrol_x_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=HORIZONTAL)
                                        scrol_y_arama_sayfasi=Scrollbar(Idari_sayfasi.frame_arama_sayfasi,orient=VERTICAL)

                                        arama_sayfasi_table=ttk.Treeview(Idari_sayfasi.frame_arama_sayfasi,
                                                                        columns=('no','Ders_Kodu','Ders_Adi', 'Akademisyen', 'Bolum' ,'Sinif' , 'Donem' ,'AKTS', 'Kredi', 'Teori', 'Uygulama'),
                                                                        xscrollcommand=scrol_x_arama_sayfasi.set,
                                                                        yscrollcommand=scrol_y_arama_sayfasi.set,)
                                        
                                        arama_sayfasi_table.place(x=0,y=0,width=1295,height=700)
                                        scrol_x_arama_sayfasi.pack(side=BOTTOM,fill=X)
                                        scrol_y_arama_sayfasi.pack(side=RIGHT,fill=Y)
                                        scrol_x_arama_sayfasi.config(command=arama_sayfasi_table.xview)
                                        scrol_y_arama_sayfasi.config(command=arama_sayfasi_table.yview)

                                        arama_sayfasi_table['show']='headings'
                                        arama_sayfasi_table.heading('no',text='No')
                                        arama_sayfasi_table.heading('Ders_Kodu',text='Ders Kodu')
                                        arama_sayfasi_table.heading('Ders_Adi',text='Ders Adı')
                                        arama_sayfasi_table.heading('Akademisyen',text='Akademisyen')
                                        arama_sayfasi_table.heading('Bolum',text='Bolum')
                                        arama_sayfasi_table.heading('Sinif',text='Sinif')
                                        arama_sayfasi_table.heading('Donem',text='Donem')
                                        arama_sayfasi_table.heading('AKTS',text='AKTS')
                                        arama_sayfasi_table.heading('Kredi',text='Kredi')
                                        arama_sayfasi_table.heading('Teori',text='Teori')
                                        arama_sayfasi_table.heading('Uygulama',text='Uygulama')
                                        
                                        

                                        arama_sayfasi_table.column('no',width=25,anchor='center')
                                        arama_sayfasi_table.column('Ders_Kodu',width=75,anchor='center')
                                        arama_sayfasi_table.column('Ders_Adi',width=275,anchor='center')
                                        arama_sayfasi_table.column('Akademisyen',width=175,anchor='center')
                                        arama_sayfasi_table.column('Bolum',width=200,anchor='center')
                                        arama_sayfasi_table.column('Sinif',width=50,anchor='center')
                                        arama_sayfasi_table.column('Donem',width=50,anchor='center')
                                        arama_sayfasi_table.column('AKTS',width=50,anchor='center')
                                        arama_sayfasi_table.column('Kredi',width=50,anchor='center')
                                        arama_sayfasi_table.column('Teori',width=50,anchor='center')
                                        arama_sayfasi_table.column('Uygulama',width=50,anchor='center')
                                        

                                        if(len(sonuc_arama_sayfasi)!=0):
                                            arama_sayfasi_table.delete(*arama_sayfasi_table.get_children())
                                            arama_eklenecek_liste_son=[]
                                            for i in range(len(sonuc_arama_sayfasi)):


                                                arama_eklenecek_liste=[]
                                                arama_eklenecek_liste.append(i + 1)  # Sıra numarası ekle
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][1])  # Ders kodu
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][2])  # Ders Adi

                                                cr.execute(f"SELECT Bolum_Ad FROM Bolumler Where Bolum_Id={sonuc_arama_sayfasi[i][8]}")
                                                bolum_adi=cr.fetchone()

                                                cr.execute(f"SELECT Ogrt_Ad, Ogrt_Soyad FROM Ogretmenler Where Ogrt_No={sonuc_arama_sayfasi[i][7]}")
                                                ogretmen_adi=cr.fetchone()

                                                arama_eklenecek_liste.append(ogretmen_adi[0] + " " + ogretmen_adi[1])  # akademisyen
                                                arama_eklenecek_liste.append(bolum_adi[0])  # bolum

                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][9])  # sinif
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][10])  # donem
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][4])  # akts
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][3])  # kredi
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][5])  # teori
                                                arama_eklenecek_liste.append(sonuc_arama_sayfasi[i][6])  # uygulama
                                              
                                                arama_eklenecek_liste_son.append(arama_eklenecek_liste)
                                              
                                            for row in arama_eklenecek_liste_son:
                                                arama_sayfasi_table.insert("",END, value=row)

                                        cr.execute(f"DROP VIEW ogretmen_adlari")

                           

                                ara_but=Button(Idari_sayfasi.aram_tuşlar_fremi,text='Ara',font=10,bg='#526D82',fg='#DDE6ED',command=ders_arama_işlemleri)#,command=arama_sayfasi
                                ara_but.place(x=720,y=6,width=200,height=35)

                            def Ders_ekle_btn():
                                try:
                                        cr.execute("DROP VIEW ogretmen_adlari")
                                except:
                                    print("view silinmedi")
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x500+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=500)

                                title_top68=Label(ilk_sayfa,
                                text='Ders Ekleme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)



                                fr1 = Frame(pro1, bg="#27374D")
                                fr1.place(x=0,y=40,width=400,height=460)

                                lbl = Label(fr1, text="Ders Kodu", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=15)
                                lbl = Label(fr1, text="Ders Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=55)
                                lbl = Label(fr1, text="Kredi", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=95)
                                lbl = Label(fr1, text="AKTS", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=135)
                                lbl = Label(fr1, text="Teori", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=175)
                                lbl = Label(fr1, text="Uygulama", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=215)
                                lbl = Label(fr1, text="Akademisyen Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                lbl.place(x=30, y=255)
                                lbl = Label(fr1, text="Bölüm", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=295)
                                lbl = Label(fr1, text="Sınıf", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=335)
                                lbl = Label(fr1, text="Dönem", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=375)


                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=200,y=15)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=200,y=55)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=200,y=95)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=200,y=135)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=200,y=175)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=200,y=215)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=200,y=255)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=200,y=295)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=200,y=335)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=200,y=375)


                                entry_ders_kodu = Entry(fr1)
                                entry_ders_kodu.place(x=220, y=20)
                                entry_ders_adi = Entry(fr1)
                                entry_ders_adi.place(x=220, y=60)
                                entry_kredi = Entry(fr1)
                                entry_kredi.place(x=220, y=100)
                                entry_akts = Entry(fr1)
                                entry_akts.place(x=220, y=140)
                                entry_teori = Entry(fr1)
                                entry_teori.place(x=220, y=180)
                                entry_uyg = Entry(fr1)
                                entry_uyg.place(x=220, y=220)
                                entry_akdemisyen = Entry(fr1)
                                entry_akdemisyen.place(x=220, y=260)
                                entry_bolum = Entry(fr1)
                                entry_bolum.place(x=220, y=300)
                                entry_sinif = Entry(fr1)
                                entry_sinif.place(x=220, y=340)
                                entry_donem = Entry(fr1)
                                entry_donem.place(x=220, y=380)

                                def tamamla():
                                

                                    '''ders_kodu = entry_ders_kodu.get().strip()
                                    ders_adi = entry_ders_adi.get().strip().upper()
                                    kredi = entry_kredi.get().strip()
                                    akts = entry_akts.get().strip()
                                    teori = entry_teori.get().strip()
                                    uyg = entry_uyg.get().strip()
                                    sinif = entry_sinif.get().strip()
                                    donem = entry_donem.get().strip()'''

                                    cr.execute(f"CREATE VIEW ogretmen_adlari AS SELECT CONCAT(Ogrt_Ad,' ', Ogrt_Soyad) AS FULL_NAME, Ogrt_No From Ogretmenler")
                                    cr.execute(f"SELECT Ogrt_No FROM ogretmen_adlari where FULL_NAME LIKE '%{entry_akdemisyen.get().strip().title()}%'")
                                    akdemisyen = cr.fetchall()

                                    cr.execute(f"SELECT Bolum_Id FROM Bolumler where Bolum_Ad LIKE '%{entry_bolum.get().strip().title()}%'")
                                    bolum = cr.fetchall()

                                    

                                    if(len(akdemisyen)==1 and len(bolum)==1):
                                        cr.execute(f"INSERT INTO Dersler (Ders_Kodu, Ders_Ad, Kredi, Akts, Teori, Uygulama, Ogrt_No, Bolum_Id, Ogr_Sinif, Donem) VALUES ('{entry_ders_kodu.get().strip()}','{entry_ders_adi.get().strip().upper()}','{entry_kredi.get().strip()}','{entry_akts.get().strip()}','{entry_teori.get().strip()}','{entry_uyg.get().strip()}','{akdemisyen[0][0]}','{bolum[0][0]}','{entry_sinif.get().strip()}','{entry_donem.get().strip()}')")
                                        cr.commit()
                                    else:
                                        messagebox.showinfo('Hata','Akademisyen Adı Yada Bölüm Adı Yanlıştır..!')


                                def bitir():
                                    tamamla()
                                    try:
                                        cr.execute("DROP VIEW ogretmen_adlari")
                                    except:
                                        print("view silinmedi")
                                    pro1.destroy()

                                btn_cik = Button(self.pro1, text="KAYDET", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_cik.place(x=120, y=450)

                            def Ders_sil_btn():
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x250+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=250)

                                title_top68=Label(ilk_sayfa,
                                text='Ders  Silme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)

                                
                                fr1 = Frame(pro1, width=400, height=200, bg="#27374D")
                                fr1.pack(pady=50)

                                lbl = Label(fr1, text="Ders Kodu", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=20)
                                lbl = Label(fr1, text="Ders Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                lbl.place(x=30, y=65)
                                
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=20)
                                lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                lbl.place(x=175,y=65)

                                entry_ders_kodu = Entry(fr1)
                                entry_ders_kodu.place(x=200, y=25)
                                entry_ders_adi = Entry(fr1)
                                entry_ders_adi.place(x=200, y=70)

                                def tamamla():
                                

                                    ders_kodu = entry_ders_kodu.get().strip()
                                    ders_adi = entry_ders_adi.get().strip().capitalize()

                                    cr.execute(f"SELECT Ders_Ad, Ders_Id FROM Dersler WHERE Ders_Kodu= '{ders_kodu}'")
                                    kontrol = cr.fetchone()
                                    print(kontrol)


                                    if(len(kontrol)>0):
                                        if(ders_adi==kontrol[0]):
                                            cr.execute(f"DELETE FROM Dersler WHERE Ders_Id='{kontrol[1]}'")
                                            cr.commit()
                                        else:
                                            messagebox.showinfo('Hata','Böyle bir Ders bulunmamaktadır..!')
                                    else:
                                        messagebox.showinfo('Hata','Böyle bir Ders bulunmamaktadır..!')

                                def bitir():
                                    tamamla()
                                    pro1.destroy()

                                btn_cik = Button(self.pro1, text="SİL", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_cik.place(x=120,y=200)

                            def Ders_güncelle_btn():
                                pro1 = Tk()
                            
                                self.pro1 = pro1
                                self.pro1.geometry("400x500+568+207")
                                #self.pro.geometry("400x450+775+200")
                                self.pro1.resizable(False, False)
                                self.pro1.title("Öğrenci Bilgi Sistemi")
                                self.pro1.config(bg="red")
                                #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

                                ilk_sayfa=Frame(self.pro1,bg="#27374D")
                                ilk_sayfa.place(x=0,y=0,width=400,height=500)

                                title_top68=Label(ilk_sayfa,
                                text='Bilgi Güncelleme',
                                bg='#9DB2BF',
                                fg='#27374D',
                                font=('Calibri',23,"bold"))
                                title_top68.pack(fill=X)

                                fr2 = Frame(pro1, bg="#27374D")
                                fr2.place(x=0,y=50,width=400,height=450)

                                

                                lbl=Label(fr2,text='Ders Kodu: ', font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")         ####### ogr no ########
                                lbl.place(x=30,y=35)
                                en_ders_kod=Entry(fr2,bd=2,justify='center')
                                en_ders_kod.place(x=200,y=40)

                                lbl=Label(fr2,text='Ders Adı: ', font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")         ####### ogr ad ########
                                lbl.place(x=30,y=80)
                                en_ders_ad=Entry(fr2,bd=2,justify='center')
                                en_ders_ad.place(x=200,y=85)


                                def musab():
                                    cr.execute(f"SELECT Ders_Ad FROM Dersler WHERE Ders_Kodu= '{en_ders_kod.get().strip()}'")
                                    kontrol = cr.fetchall()

                                    if(len(kontrol)==1):
                                        if(en_ders_ad.get().strip().title()==kontrol[0][0]):

                                            try:
                                                    cr.execute("DROP VIEW ogretmen_adlari")
                                            except:
                                                print("view silinmedi")
                                       
                                            kod=en_ders_kod.get().strip()
                                            fr2.destroy()
                                            fr1 = Frame(pro1, bg="#27374D")
                                            fr1.place(x=0,y=50,width=400,height=450)


                                            lbl = Label(fr1, text="Ders Kodu", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                            lbl.place(x=30, y=15)
                                            lbl = Label(fr1, text="Ders Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                            lbl.place(x=30, y=55)
                                            lbl = Label(fr1, text="Kredi", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                            lbl.place(x=30, y=95)
                                            lbl = Label(fr1, text="AKTS", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                            lbl.place(x=30, y=135)
                                            lbl = Label(fr1, text="Teori", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                            lbl.place(x=30, y=175)
                                            lbl = Label(fr1, text="Uygulama", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                            lbl.place(x=30, y=215)
                                            lbl = Label(fr1, text="Akademisyen Adı", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED", justify="left")
                                            lbl.place(x=30, y=255)
                                            lbl = Label(fr1, text="Bölüm", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                            lbl.place(x=30, y=295)
                                            lbl = Label(fr1, text="Sınıf", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                            lbl.place(x=30, y=335)
                                            lbl = Label(fr1, text="Dönem", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED",justify="left")
                                            lbl.place(x=30, y=375)


                                            lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                            lbl.place(x=200,y=15)
                                            lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                            lbl.place(x=200,y=55)
                                            lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                            lbl.place(x=200,y=95)
                                            lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                            lbl.place(x=200,y=135)
                                            lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                            lbl.place(x=200,y=175)
                                            lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                            lbl.place(x=200,y=215)
                                            lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                            lbl.place(x=200,y=255)
                                            lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                            lbl.place(x=200,y=295)
                                            lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                            lbl.place(x=200,y=335)
                                            lbl= Label(fr1, text=":", font=("Aftesto", 15, "bold"), bg="#27374D", fg="#DDE6ED")
                                            lbl.place(x=200,y=375)


                                            entry_ders_kodu = Entry(fr1)
                                            entry_ders_kodu.place(x=220, y=20)
                                            entry_ders_adi = Entry(fr1)
                                            entry_ders_adi.place(x=220, y=60)
                                            entry_kredi = Entry(fr1)
                                            entry_kredi.place(x=220, y=100)
                                            entry_akts = Entry(fr1)
                                            entry_akts.place(x=220, y=140)
                                            entry_teori = Entry(fr1)
                                            entry_teori.place(x=220, y=180)
                                            entry_uyg = Entry(fr1)
                                            entry_uyg.place(x=220, y=220)
                                            entry_akdemisyen = Entry(fr1)
                                            entry_akdemisyen.place(x=220, y=260)
                                            entry_bolum = Entry(fr1)
                                            entry_bolum.place(x=220, y=300)
                                            entry_sinif = Entry(fr1)
                                            entry_sinif.place(x=220, y=340)
                                            entry_donem = Entry(fr1)
                                            entry_donem.place(x=220, y=380)


                                            def f_save_btn():

                                                cr.execute(f"CREATE VIEW ogretmen_adlari AS SELECT CONCAT(Ogrt_Ad,' ', Ogrt_Soyad) AS FULL_NAME, Ogrt_No From Ogretmenler")
                                                cr.execute(f"SELECT Ogrt_No FROM ogretmen_adlari where FULL_NAME LIKE '%{entry_akdemisyen.get().strip().title()}%'")
                                                akdemisyen = cr.fetchall()

                                                cr.execute(f"SELECT Bolum_Id FROM Bolumler where Bolum_Ad LIKE '%{entry_bolum.get().strip().title()}%'")
                                                bolum = cr.fetchall()

                                                

                                                if(len(akdemisyen)==1 and len(bolum)==1):
                                                    cr.execute(f"UPDATE Dersler SET Ders_Kodu='{entry_ders_kodu.get().strip()}', Ders_Ad='{entry_ders_adi.get().strip().upper()}', Kredi='{entry_kredi.get().strip()}', Akts='{entry_akts.get().strip()}', Teori='{entry_teori.get().strip()}', Uygulama='{entry_uyg.get().strip()}', Ogrt_No='{akdemisyen[0][0]}', Bolum_Id='{bolum[0][0]}', Ogr_Sinif='{entry_sinif.get().strip()}', Donem='{entry_donem.get().strip()}' WHERE Ders_Kodu='{kod}'")
                                                    cr.commit()
                                                else:
                                                    messagebox.showinfo('Hata','Akademisyen Adı Yada Bölüm Adı Yanlıştır..!')
                                                #------------------------
                                                self.pro1.destroy()

                                            def bitir():
                                                f_save_btn()
                                                try:
                                                    cr.execute("DROP VIEW ogretmen_adlari")
                                                except:
                                                    print("view silinmedi")
                                                pro1.destroy()

                                            def f_add_close_btn():
                                                self.pro1.destroy()


                                            save_btn=Button(fr1,text='Güncelle', font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=10,command=bitir)
                                            save_btn.place(x=85,y=420)

                                            add_close_btn=Button(fr1,text='Kapat', font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=10,command=f_add_close_btn)
                                            add_close_btn.place(x=215,y=420)
                                            
                                        else:
                                            messagebox.showinfo('Hata','Böyle bir Ders bulunmamaktadır..!')
                                            self.pro1.destroy()
                                    else:
                                        messagebox.showinfo('Hata','Böyle bir Ders bulunmamaktadır..!')
                                        self.pro1.destroy()
                                
                                def bitir():
                                    musab()
                                    
                                btn_ara = Button(fr2, text="ARA", font=("Aftesto", 12, "bold"), bg="#526D82", fg="#DDE6ED", width=15,command=bitir)
                                btn_ara.place(x=120,y=200)


                            #----------- diğer fremleri kapat----------# 
                            try:
                                Idari_sayfasi.Bölüm_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.ogrenci_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.Akademisyen_f.destroy()
                            except:
                                pass     
                            try:
                                Idari_sayfasi.idari_f.destroy()
                            except:
                                pass 
                            

                            Idari_sayfasi.Ders_f=Frame(frame_b,bg='#9DB2BF')
                            Idari_sayfasi.Ders_f.place(x=5,y=300,width=200,height=190)

                            başlık=Label(Idari_sayfasi.Ders_f,
                            text='Ders İşlemleri',
                            bg='#526D82',
                            fg='#DDE6ED',
                            font=('calisto mt',15,'bold'))
                            başlık.place(x=0,y=0,width=200,height=35)


                            def change_color_ara_btn1(event):
                                Ara_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_ara_btn2(event):
                                Ara_btn.config(bg="#27374D", fg="#DDE6ED")
                            Ara_btn=Button(Idari_sayfasi.Ders_f,text='Ders Ara',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Ders_ara_btn)
                            Ara_btn.place(x=5,y=40,width=190,height=30)
                            Ara_btn.bind("<Enter>", change_color_ara_btn1)  
                            Ara_btn.bind("<Leave>", change_color_ara_btn2) 


                            def change_color_Ekle_btn1(event):
                                Ekle_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Ekle_btn2(event):
                                Ekle_btn.config(bg="#27374D", fg="#DDE6ED")
                            Ekle_btn=Button(Idari_sayfasi.Ders_f,text='Ders Ekle',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Ders_ekle_btn)
                            Ekle_btn.place(x=5,y=75,width=190,height=30)
                            Ekle_btn.bind("<Enter>", change_color_Ekle_btn1)  
                            Ekle_btn.bind("<Leave>", change_color_Ekle_btn2) 
                            

                            def change_color_Sil_btn1(event):
                                Sil_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Sil_btn2(event):
                                Sil_btn.config(bg="#27374D", fg="#DDE6ED")
                            Sil_btn=Button(Idari_sayfasi.Ders_f,text='Ders Sil',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Ders_sil_btn)
                            Sil_btn.place(x=5,y=110,width=190,height=30)
                            Sil_btn.bind("<Enter>", change_color_Sil_btn1)  
                            Sil_btn.bind("<Leave>", change_color_Sil_btn2) 


                            def change_color_Güncelle_btn1(event):
                                Güncelle_btn.config(bg="#526D82", fg="#DDE6ED")  
                            def change_color_Güncelle_btn2(event):
                                Güncelle_btn.config(bg="#27374D", fg="#DDE6ED")
                            Güncelle_btn=Button(Idari_sayfasi.Ders_f,text='Ders Güncelle',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Ders_güncelle_btn)
                            Güncelle_btn.place(x=5,y=145,width=190,height=30)
                            Güncelle_btn.bind("<Enter>", change_color_Güncelle_btn1)  
                            Güncelle_btn.bind("<Leave>", change_color_Güncelle_btn2) 


                        def change_color_ogrenci_btn1(event):
                            ogrenci_btn.config(bg="#526D82", fg="#DDE6ED")  
                        def change_color_ogrenci_btn2(event):
                            ogrenci_btn.config(bg="#27374D", fg="#DDE6ED")
                        ogrenci_btn=Button(frame_b,text='Öğrenci İşlemleri',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=ogr_btn_f)
                        ogrenci_btn.place(x=5,y=55,width=207,height=40)
                        ogrenci_btn.bind("<Enter>", change_color_ogrenci_btn1)  
                        ogrenci_btn.bind("<Leave>", change_color_ogrenci_btn2) 

                        def change_color_Akademisyen_btn1(event):
                            Akademisyen_btn.config(bg="#526D82", fg="#DDE6ED")  
                        def change_color_Akademisyen_btn2(event):
                            Akademisyen_btn.config(bg="#27374D", fg="#DDE6ED")
                        Akademisyen_btn=Button(frame_b,text='Akademisyen İşlemleri',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Akademisyen_btn_f)
                        Akademisyen_btn.place(x=5,y=100,width=207,height=40)
                        Akademisyen_btn.bind("<Enter>", change_color_Akademisyen_btn1)  
                        Akademisyen_btn.bind("<Leave>", change_color_Akademisyen_btn2) 

                        def change_color_İdari_btn1(event):
                            İdari_btn.config(bg="#526D82", fg="#DDE6ED")  
                        def change_color_İdari_btn2(event):
                            İdari_btn.config(bg="#27374D", fg="#DDE6ED")
                        İdari_btn=Button(frame_b,text='İdari Personel İşlemleri ',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=İdari_btn_f)
                        İdari_btn.place(x=5,y=145,width=207,height=40)
                        İdari_btn.bind("<Enter>", change_color_İdari_btn1)  
                        İdari_btn.bind("<Leave>", change_color_İdari_btn2) 

                        def change_color_Bölüm_btn1(event):
                            Bölüm_btn.config(bg="#526D82", fg="#DDE6ED")  
                        def change_color_Bölüm_btn2(event):
                            Bölüm_btn.config(bg="#27374D", fg="#DDE6ED")
                        Bölüm_btn=Button(frame_b,text='Bölüm İşlemler',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Bölüm_btn_f)
                        Bölüm_btn.place(x=5,y=190,width=207,height=40)
                        Bölüm_btn.bind("<Enter>", change_color_Bölüm_btn1)  
                        Bölüm_btn.bind("<Leave>", change_color_Bölüm_btn2) 

                        def change_color_Ders_btn1(event):
                            Ders_btn.config(bg="#526D82", fg="#DDE6ED")  
                        def change_color_Ders_btn2(event):
                            Ders_btn.config(bg="#27374D", fg="#DDE6ED")
                        Ders_btn=Button(frame_b,text='Ders İşlemleri',font=10,bg='#27374D',fg='#DDE6ED', borderwidth=0, highlightthickness=0,command=Ders_btn_f)
                        Ders_btn.place(x=5,y=235,width=207,height=40)
                        Ders_btn.bind("<Enter>", change_color_Ders_btn1)  
                        Ders_btn.bind("<Leave>", change_color_Ders_btn2) 


                        cr.execute(f"SELECT Admin_Ad, Admin_Soyad from Adminler WHERE Admin_No='{kul_adi.get().strip()}'")
                        prof_ad_soyad=cr.fetchall()
                        def def_profil_sayfasi():
                            profil = Frame(self.omer,bg="blue")
                            profil.place(x=1150,y=80,width=380,height=360)

                            profil1 = Frame(profil,bg="#9DB2BF")
                            profil1.place(x=0,y=32,width=150,height=360)

                            profil_lbl_no=Label(profil1,text='İdari No                  : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))         #no
                            profil_lbl_no.place(x=4,y=20)               
                            profil_lbl_ad_soyad=Label(profil1,text='Ad Soyad                : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))   #ad soyad
                            profil_lbl_ad_soyad.place(x=4,y=55)
                            profil_lbl_tc=Label(profil1,text='TC No                       : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))            #TC
                            profil_lbl_tc.place(x=4,y=90)
                            profil_lbl_dogum=Label(profil1,text='Doğum Tarihi        : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))  #Dogum
                            profil_lbl_dogum.place(x=4,y=125)
                            profil_lbl_tel=Label(profil1,text='Tel. No                    : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))         #Tel
                            profil_lbl_tel.place(x=4,y=160)
                            profil_lbl_eposta=Label(profil1,text='Eposta                     : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))       #Eposta
                            profil_lbl_eposta.place(x=4,y=195)
                            profil_lbl_cinsiyet=Label(profil1,text='Cinsiyet                  : ',bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))   #Cinsiyet
                            profil_lbl_cinsiyet.place(x=4,y=230)


                            profil2 = Frame(profil,bg="#9DB2BF")
                            profil2.place(x=150,y=32,width=230,height=360)

                            cr.execute(f"SELECT Admin_Tc, Admin_DT, Admin_TelNo, Admin_Eposta, Admin_Cinsiyeti from Adminler where Admin_No='{kul_adi.get()}'")
                            prof_db=cr.fetchall()

                            profil_db_no=Label(profil2,text=kul_adi.get().strip(),bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold")) #no
                            profil_db_no.place(x=4,y=20)
                            profil_db_ad_soyad=Label(profil2,text=prof_ad_soyad[0][0]+" "+ prof_ad_soyad[0][1],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))    #ad soyad
                            profil_db_ad_soyad.place(x=4,y=55)
                            profil_db_tc=Label(profil2,text=prof_db[0][0],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))         #TC
                            profil_db_tc.place(x=4,y=90)
                            profil_db_dogum=Label(profil2,text=prof_db[0][1],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))      #Dogum
                            profil_db_dogum.place(x=4,y=125)
                            profil_db_tel=Label(profil2,text=prof_db[0][2],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))        #Tel
                            profil_db_tel.place(x=4,y=160)
                            profil_db_eposta=Label(profil2,text=prof_db[0][3],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))     #Eposta
                            profil_db_eposta.place(x=4,y=195)
                            profil_db_cinsiyet=Label(profil2,text=prof_db[0][4],bg='#9DB2BF',fg="#27374D",font=('Calibri',14,"bold"))   #Cinsiyet
                            profil_db_cinsiyet.place(x=4,y=230)

                            def ana():
                                self.omer.destroy()
                                os.system("python Proje.py")
                                
                                


                            profil_cikis1=Button(profil,text="Çıkış", bg="#75163F",fg="#DDE6ED",font=40,command=ana)
                            profil_cikis1.place(x=130,y=300,width=120,height=45)



                            
                            kişisel_bligiler=Label(profil,text="Kişisel Bilgiler",bg='#526D82',fg='#DDE6ED',font=('Calibri',16,"bold"))
                            kişisel_bligiler.pack(fill=X)

                            def change_color_on_hover_enter(event):
                                profil_cikis.config(bg="red", fg="white")  # Fare butona yaklaştığında rengi değiştir

                            def change_color_on_hover_leave(event):
                                profil_cikis.config(bg="#526D82", fg="#DDE6ED")  # Fare butondan ayrıldığında orijinal rengine geri dön

                            profil_cikis=Button(profil,text="X", bg="#526D82",fg="#DDE6ED",font=30,command=profil.destroy, borderwidth=0, highlightthickness=0)
                            profil_cikis.place(x=345,y=2,width=32,height=28)

                            profil_cikis.bind("<Enter>", change_color_on_hover_enter)  # Fare butona geldiğinde rengi değiştir
                            profil_cikis.bind("<Leave>", change_color_on_hover_leave)  # Fare butondan ayrıldığında orijinal rengine geri dön

                            
 


                            
                        def change_color_1(event):
                            prof_btn.config(bg="#526D82", fg="#9DB2BF")  

                        def change_color_2(event):
                            prof_btn.config(bg="#9DB2BF", fg="#27374D")

                        prof_btn=Button(frame_ust,text=prof_ad_soyad[0][0]+ " "+ prof_ad_soyad[0][1] + " - " + kul_adi.get(),bg='#9DB2BF',fg='#27374D',font=20, borderwidth=0, highlightthickness=0,cursor='hand2',command=def_profil_sayfasi)
                        prof_btn.place(x=984,y=3,width=270,height=38)

                        prof_btn.bind("<Enter>", change_color_1)  
                        prof_btn.bind("<Leave>", change_color_2) 



                    else:
                        hata_lbl=Label(dogrulama_frame,text="Kullanıcı Adı Yada Şifre Yanlıştır",font=('Calibri',11),bg="#27374D",fg="red")
                        hata_lbl.place(x=107,y=235)
                        

                except:
                    hata_lbl=Label(dogrulama_frame,text="Kullanıcı Adı Yada Şifre Yanlıştır",font=('Calibri',11),bg="#27374D",fg="red")
                    hata_lbl.place(x=107,y=235)

                cr.commit()


            ake_bt = Button(dogrulama_frame, text="GİRİŞ", font=("Calibri", 18, "bold"), bg="#DDE6ED", fg="#27374D",command=giris_def)
            ake_bt.place(x=142,y=280, width=120,height=30)
            

            geri_bt=Button(dogrulama_frame,text="<", bg="#9DB2BF",fg="#27374D",font=20,command=dogrulama_frame.destroy)
            geri_bt.place(x=0,y=45,width=45,height=40)


        self.pro = pro
        self.pro.geometry("400x450+568+207")
        #self.pro.geometry("400x450+775+200")
        self.pro.resizable(False, False)
        self.pro.title("Öğrenci Bilgi Sistemi")
        self.pro.config(bg="red")
        #self.pro.iconbitmap("C:\\Users\\Lenov\\Downloads\\MySpace.ico")

        ilk_sayfa=Frame(self.pro,bg="#27374D")
        ilk_sayfa.place(x=0,y=0,width=400,height=450)

        title_top68=Label(ilk_sayfa,
        text='Öğrenci Bilgi Sistemi',
        bg='#9DB2BF',
        fg='#27374D',
        font=('Calibri',23,"bold"))
        title_top68.pack(fill=X)



        ogr_bt = Button(ilk_sayfa, text="Öğrenci Girişi", font=("Calibri", 15, "bold"), bg="#DDE6ED", fg="#27374D", width=18,command=ogrenci_sayfasi)
        ogr_bt.place(x=105, y=140)
        ogrt_bt = Button(ilk_sayfa, text="Akademisyen Girişi", font=("Calibri", 15, "bold"), bg="#DDE6ED", fg="#27374D", width=18,command=Akademisyen_sayfasi)
        ogrt_bt.place(x=105, y=200)
        ake_bt = Button(ilk_sayfa, text="İdari Personel Girişi", font=("Calibri", 15, "bold"), bg="#DDE6ED", fg="#27374D", width=18,command=Idari_sayfasi)
        ake_bt.place(x=105,y=260)

    





pro = Tk()
ob = Student(pro)
pro.mainloop()