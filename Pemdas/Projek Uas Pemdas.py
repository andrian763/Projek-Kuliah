from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image, ImageTk
import random

class KasirCafe:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1270x690+0+0')
        self.root.resizable(0, 0)
        self.root.title('Kasir Kafe Barokah')

        self.create_top_frame()
        self.create_menu_bar()
        self.hide_indicators()
        self.variable()
        self.frame_jumlahharga()
        self.layarstruk()
        self.bayar_uangpelanggan()

    def create_top_frame(self):
        self.topFrame=Frame(self.root,bd=10,relief=RIDGE)
        self.topFrame.pack(side=TOP)
        self.labelTitle=Label(self.topFrame,text='Kasir Kafe Barokah',font=('ariel',30,'bold'),fg='yellow',bd=10,bg='blue4',width=52)
        self.labelTitle.grid(row=0,column=0)
        
        self.original_image = Image.open('e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\cafebg.png')
        
        self.new_width = 1275
        self.new_height = 600
        self.resized_image = self.original_image.resize((self.new_width, self.new_height),Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(self.resized_image)

        self.label_background= Label(self.root,image=self.background_image)
        self.label_background.place(x=5,y=88)

    def create_menu_bar(self):
        self.menu_bar = Frame(height=450,width=230,bg='grey')
        self.menu_bar.place(x=0,y=88)
        

        self.foods = Button(self.menu_bar,height=2,width=20,fg='black',text='MAKANAN',
              font=('helvetica',10,'bold'),bg='yellow',command=self.show_page1)
        self.foods.place(x=25,y=70)
        self.foods_indicate = Label(self.menu_bar,text='',bg='green')
        self.foods_indicate.place(x=6,y=70,width=5,height=42)

        self.drinks = Button(self.menu_bar,height=2,width=20,fg='black',text='MINUMAN',
                font=('helvetica',10,'bold'),bg='yellow',command=self.show_page2)
        self.drinks.place(x=25,y=205)
        self.drinks_indicate = Label(self.menu_bar,text='',bg='green')
        self.drinks_indicate.place(x=6,y=205,width=5,height=42)

        self.cakes = Button(self.menu_bar,height=2,width=20,fg='black',text='CAMILAN',
               font=('helvetica',10,'bold'),bg='yellow',command= self.show_page3)
        self.cakes.place(x=25,y=335)
        self.cakes_indicate = Label(self.menu_bar,text='',bg='green')
        self.cakes_indicate.place(x=6,y=335,width=5,height=42)

    def show_page1(self):
        self.menufoods()
        self.indicate(self.foods_indicate)

    def show_page2(self):
        self.menudrinks()
        self.indicate(self.drinks_indicate)

    def show_page3(self):
        self.menucakes()
        self.indicate(self.cakes_indicate)

    def hide_page1(self):
        self.menufoods_fram.destroy()  # Destroy the frame when hiding the page
        self.reset_indicate(self.foods_indicate)  # Atur warna kembali ke warna default

    def hide_page2(self):
        self.menudrinks_fram.destroy()  # Destroy the frame when hiding the page
        self.reset_indicate(self.drinks_indicate)  # Atur warna kembali ke warna default

    def hide_page3(self):
        self.menucakes_fram.destroy()  # Destroy the frame when hiding the page
        self.reset_indicate(self.cakes_indicate)  # Atur warna kembali ke warna default
        
    def indicate(self,lb):
        self.hide_indicators()
        lb.config(bg='#158aff')

    def reset_indicate(self, lb):
        lb.config(bg='grey')  # Atur warna kembali ke warna default

    def hide_indicators(self):
        self.foods_indicate.config(bg='grey')
        self.drinks_indicate.config(bg='grey')
        self.cakes_indicate.config(bg='grey')
        
    def variable(self):
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()
        self.var10 = IntVar()
        self.var11 = IntVar()
        self.var12 = IntVar()
        self.var13 = IntVar()
        self.var14 = IntVar()
        self.var15 = IntVar()
        self.var16 = IntVar()
        self.var17 = IntVar()
        self.var18 = IntVar()
        self.var19 = IntVar()
        self.var20 = IntVar()
        self.var21 = IntVar()
        self.var22 = IntVar()
        self.var23 = IntVar()
        self.var24 = IntVar()
        self.var25 = IntVar()
        self.var26 = IntVar()
        self.var27 = IntVar()

        self.e_roti=StringVar()
        self.e_ayamgoreng=StringVar()
        self.e_nasigoreng=StringVar()
        self.e_telurdadar=StringVar()
        self.e_bakso=StringVar()
        self.e_mieayam=StringVar()
        self.e_nasicampur=StringVar()
        self.e_miegoreng =StringVar()
        self.e_miepangsit=StringVar()

        self.e_esteh=StringVar()
        self.e_kopi=StringVar()
        self.e_jusjeruk=StringVar()
        self.e_kolak=StringVar()
        self.e_bandrek=StringVar()
        self.e_esdawet=StringVar()
        self.e_escendol=StringVar()
        self.e_lemontea=StringVar()
        self.e_esdurian=StringVar()

        self.e_bikaambon=StringVar()
        self.e_donat=StringVar()
        self.e_bengbeng=StringVar()
        self.e_sariroti=StringVar()
        self.e_pancake=StringVar()
        self.e_klepon=StringVar()
        self.e_ondeonde=StringVar()
        self.e_lemper=StringVar()
        self.e_dadargulung=StringVar()

        self.e_roti.set('0')
        self.e_ayamgoreng.set('0')
        self.e_nasigoreng.set('0')
        self.e_telurdadar.set('0')
        self.e_bakso.set('0')
        self.e_mieayam.set('0')
        self.e_nasicampur.set('0')
        self.e_miegoreng.set('0')
        self.e_miepangsit.set('0')

        self.e_esteh.set('0')
        self.e_kopi.set('0')
        self.e_jusjeruk.set('0')
        self.e_kolak.set('0')
        self.e_bandrek.set('0')
        self.e_esdawet.set('0')
        self.e_escendol.set('0')
        self.e_lemontea.set('0')
        self.e_esdurian.set('0')

        self.e_bikaambon.set('0')
        self.e_donat.set('0')
        self.e_bengbeng.set('0')
        self.e_sariroti.set('0')
        self.e_pancake.set('0')
        self.e_klepon.set('0')
        self.e_ondeonde.set('0')
        self.e_lemper.set('0')
        self.e_dadargulung.set('0')

        self.costoffoodsvar=StringVar()
        self.costofdrinksvar=StringVar()
        self.costofcakesvar=StringVar()
        self.subtotalvar=StringVar()
        self.servicetaxvar=StringVar()
        self.totalcostvar=StringVar()
        self.kembalianvar = StringVar()


    def menufoods(self):
        self.menufoods_fram = Frame(height=600,width=750, bg='brown')
        self.menufoods_fram.place(x=200,y=88)

        canvas1 = Canvas(self.menufoods_fram, bg='brown', highlightthickness=0, height=450, width=630)
        scrollbar1 = Scrollbar(self.menufoods_fram, orient='vertical', command=canvas1.yview)
        scrollable_frame1 = Frame(canvas1, bg='brown')

        canvas1.pack(side='left', fill='both', expand=True,padx=0, pady=0)
        scrollbar1.pack(side='right', fill='y')
        # Mengaitkan scrollbar dengan canvas
        canvas1.configure(yscrollcommand=scrollbar1.set)
        canvas1.create_window((0, 0), window=scrollable_frame1, anchor='nw')

        canvas1.bind_all("<MouseWheel>", lambda event: canvas1.yview_scroll(int(-1 * (event.delta / 120)), "units"))
        scrollable_frame1.bind('<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox('all')))

        close_button = Button(self.menufoods_fram, text="X", font=('arial',10,'bold'), command=self.hide_page1, bg='red', fg='black', width=3)
        close_button.pack()

        def roti():
            if self.var1.get()==1:
                self.textroti.config(state=NORMAL)
                self.textroti.delete(0,END)
                self.textroti.focus()
            else:
                self.textroti.config(state=DISABLED)
                self.e_roti.set('0')
        # Tambahkan path gambar sesuai dengan lokasi gambar Anda
        roti_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\roti.png'
        image = PhotoImage(file=roti_image)
        label_image = Label(scrollable_frame1, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=0, column=2,pady=10, columnspan=2)

        roti = Checkbutton(scrollable_frame1,text='Roti',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var1,command=roti)
        roti.grid(row=1,column=2,sticky=W,padx=(0,50))
        self.textroti=Entry(scrollable_frame1,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_roti)
        self.textroti.grid(row=1,column=2,padx=(50,0))

        roti_spasi = Label(scrollable_frame1, text="",bg='brown',font=('arial', '18', 'bold'))
        roti_spasi.grid(row=2, column=2, pady=20)

        def ayamgoreng():
            if self.var2.get()==1:
                self.textayamgoreng.config(state=NORMAL)
                self.textayamgoreng.delete(0,END)
                self.textayamgoreng.focus()
            else:
                self.textayamgoreng.config(state=DISABLED)
                self.e_ayamgoreng.set('0')
        ayamgoreng_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\ayamgoreng.png'
        image = PhotoImage(file=ayamgoreng_image)
        label_image = Label(scrollable_frame1, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=3, column=2,pady=10, columnspan=2)

        ayamgoreng=Checkbutton(scrollable_frame1,text='Ayam\ngoreng',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var2,command=ayamgoreng)
        ayamgoreng.grid(row=4,column=2,sticky=W,padx=(0,70))
        self.textayamgoreng=Entry(scrollable_frame1,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_ayamgoreng)
        self.textayamgoreng.grid(row=4,column=2,padx=(70,0))
        
        ayamgoreng_spasi = Label(scrollable_frame1, text="",bg='brown',font=('arial', '18', 'bold'))
        ayamgoreng_spasi.grid(row=6, column=2, pady=20)

        def nasigoreng():
            if self.var3.get()==1:
                self.textnasigoreng.config(state=NORMAL)
                self.textnasigoreng.delete(0,END)
                self.textnasigoreng.focus()
            else:
                self.textnasigoreng.config(state=DISABLED)
                self.e_nasigoreng.set('0')
        nasgor_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\nasgor.png'
        image = PhotoImage(file=nasgor_image)
        label_image = Label(scrollable_frame1, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=7, column=2,pady=10)

        nasigoreng=Checkbutton(scrollable_frame1,text='Nasi\ngoreng',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var3,command=nasigoreng)
        nasigoreng.grid(row=8,column=2,sticky=W,padx=(0,70))
        self.textnasigoreng=Entry(scrollable_frame1,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_nasigoreng)
        self.textnasigoreng.grid(row=8,column=2,padx=(70,0))

        nasigoreng_spasi = Label(scrollable_frame1, text="",bg='brown', font=('arial', '18', 'bold'))
        nasigoreng_spasi.grid(row=10, column=2, pady=50)

        def telurdadar():
            if self.var4.get()==1:
                self.texttelurdadar.config(state=NORMAL)
                self.texttelurdadar.delete(0,END)
                self.texttelurdadar.focus()
            else:
                self.texttelurdadar.config(state=DISABLED)
                self.e_telurdadar.set('0')
        telurdadar_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\telurdadar.png'
        image = PhotoImage(file=telurdadar_image)
        label_image = Label(scrollable_frame1, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=11, column=2,pady=10)

        telurdadar=Checkbutton(scrollable_frame1,text='Telur\nDadar',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var4,command=telurdadar)
        telurdadar.grid(row=12,column=2,sticky=W,padx=(0,70))
        self.texttelurdadar=Entry(scrollable_frame1,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_telurdadar)
        self.texttelurdadar.grid(row=12,column=2,padx=(70,0))

        telurdadar_spasi = Label(scrollable_frame1, text="",bg='brown', font=('arial', '18', 'bold'))
        telurdadar_spasi.grid(row=14, column=2, pady=50)

        def bakso():
            if self.var5.get()==1:
                self.textbakso.config(state=NORMAL)
                self.textbakso.delete(0,END)
                self.textbakso.focus()
            else:
                self.textbakso.config(state=DISABLED)
                self.e_bakso.set('0')
        bakso_image = 'e:\\KULIAH\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\bakso.png'
        image = PhotoImage(file=bakso_image)
        label_image = Label(scrollable_frame1, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=15, column=2,pady=10)

        bakso=Checkbutton(scrollable_frame1,text='Bakso',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var5,command=bakso)
        bakso.grid(row=16,column=2,sticky=W,padx=(0,50))
        self.textbakso=Entry(scrollable_frame1,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_bakso)
        self.textbakso.grid(row=16,column=2,padx=(50,0))

        bakso_spasi = Label(scrollable_frame1, text="",bg='brown', font=('arial', '18', 'bold'))
        bakso_spasi.grid(row=17, column=2, pady=50)

        def mieayam():
            if self.var6.get()==1:
                self.textmieayam.config(state=NORMAL)
                self.textmieayam.delete(0,END)
                self.textmieayam.focus()
            else:
                self.textmieayam.config(state=DISABLED)
                self.e_mieayam.set('0')
        mieayam_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\mieayam.png'
        image = PhotoImage(file=mieayam_image)
        label_image = Label(scrollable_frame1, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=18, column=2,pady=10)

        mieayam=Checkbutton(scrollable_frame1,text='Mie\nAyam',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var6,command=mieayam)
        mieayam.grid(row=19,column=2,sticky=W,padx=(0,50))
        self.textmieayam=Entry(scrollable_frame1,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_mieayam)
        self.textmieayam.grid(row=19,column=2,padx=(50,0))
    
        mieayam_spasi = Label(scrollable_frame1, text="",bg='brown', font=('arial', '18', 'bold'))
        mieayam_spasi.grid(row=21, column=2, pady=50)

        def nasicampur():
            if self.var7.get()==1:
                self.textnasicampur.config(state=NORMAL)
                self.textnasicampur.delete(0,END)
                self.textnasicampur.focus()
            else:
                self.textnasicampur.config(state=DISABLED)
                self.e_nasicampur.set('0')
        nasicampur_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\nasi campur.png'
        image = PhotoImage(file=nasicampur_image)
        label_image = Label(scrollable_frame1, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=22, column=2,pady=10)

        nasicampur=Checkbutton(scrollable_frame1,text='Nasi\nCampur',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var7, command=nasicampur)
        nasicampur.grid(row=23,column=2,sticky=W,padx=(0,70))
        self.textnasicampur=Entry(scrollable_frame1,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_nasicampur)
        self.textnasicampur.grid(row=23,column=2,padx=(70,0))

        nasicampur_spasi = Label(scrollable_frame1, text="",bg='brown', font=('arial', '18', 'bold'))
        nasicampur_spasi.grid(row=25, column=2, pady=50)

        def miegoreng():
            if self.var8.get()==1:
                self.textmiegoreng.config(state=NORMAL)
                self.textmiegoreng.delete(0,END)
                self.textmiegoreng.focus()
            else:
                self.textmiegoreng.config(state=DISABLED)
                self.e_miegoreng.set('0')
        miegoreng_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\miegoreng.png'
        image = PhotoImage(file=miegoreng_image)
        label_image = Label(scrollable_frame1, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=26, column=2,pady=10)

        miegoreng=Checkbutton(scrollable_frame1,text='Mie\nGoreng',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var8,command=miegoreng)
        miegoreng.grid(row=27,column=2,sticky=W,padx=(0,70))
        self.textmiegoreng=Entry(scrollable_frame1,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_miegoreng)
        self.textmiegoreng.grid(row=27,column=2,padx=(70,0))

        miegoreng_spasi = Label(scrollable_frame1, text="",bg='brown', font=('arial', '18', 'bold'))
        miegoreng_spasi.grid(row=29, column=2, pady=50)

        def miepangsit():
            if self.var9.get()==1:
                self.textmiepangsit.config(state=NORMAL)
                self.textmiepangsit.delete(0,END)
                self.textmiepangsit.focus()
            else:
                self.textmiepangsit.config(state=DISABLED)
                self.e_miepangsit.set('0')
        miepangsit_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\miepangsit.png'
        image = PhotoImage(file=miepangsit_image)
        label_image = Label(scrollable_frame1, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=31, column=2,pady=10)

        miepangsit=Checkbutton(scrollable_frame1,text='Mie\nPangsit',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var9,command=miepangsit)
        miepangsit.grid(row=32,column=2,sticky=W,padx=(0,70))
        self.textmiepangsit=Entry(scrollable_frame1,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_miepangsit)
        self.textmiepangsit.grid(row=32,column=2,padx=(70,0))

        miepangsit_spasi = Label(scrollable_frame1, text="",bg='brown',font=('arial', '18', 'bold'))
        miepangsit_spasi.grid(row=33, column=2, pady=50)


    def menudrinks(self):
        self.menudrinks_fram = Frame(height=600,width=750,bg='brown')
        self.menudrinks_fram.place(x=200,y=88)

        canvas2 = Canvas(self.menudrinks_fram, bg='brown', highlightthickness=0, height=450, width=630)
        scrollbar2 = Scrollbar(self.menudrinks_fram, orient='vertical', command=canvas2.yview)
        scrollable_frame2 = Frame(canvas2, bg='brown')

        canvas2.pack(side='left', fill='both', expand=True)
        scrollbar2.pack(side='right', fill='y')
        # Mengaitkan scrollbar dengan canvas
        canvas2.configure(yscrollcommand=scrollbar2.set)
        canvas2.create_window((0, 0), window=scrollable_frame2, anchor='nw')

        canvas2.bind_all("<MouseWheel>", lambda event: canvas2.yview_scroll(int(-1 * (event.delta / 120)), "units"))
        scrollable_frame2.bind('<Configure>', lambda e: canvas2.configure(scrollregion=canvas2.bbox('all')))

        close_button = Button(self.menudrinks_fram, text="X", font=('arial',10,'bold'), command=self.hide_page2, bg='red', fg='black', width=3)
        close_button.pack()

        def esteh():
            if self.var10.get()==1:
                self.textesteh.config(state=NORMAL)
                self.textesteh.delete(0,END)
                self.textesteh.focus()
            else:
                self.textesteh.config(state=DISABLED)
                self.e_esteh.set('0')
        esteh_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\esteh.png'
        image = PhotoImage(file=esteh_image)
        label_image = Label(scrollable_frame2, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=0, column=2,pady=10)

        esteh=Checkbutton(scrollable_frame2,text='Es Teh',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var10,command=esteh)
        esteh.grid(row=1,column=2,sticky=W,padx=(0,70))
        self.textesteh=Entry(scrollable_frame2,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_esteh)
        self.textesteh.grid(row=1,column=2,padx=(70,0))

        esteh_spasi = Label(scrollable_frame2, text="",bg='brown',font=('arial', '18', 'bold'))
        esteh_spasi.grid(row=2, column=2, pady=20)

        def kopi():
            if self.var11.get()==1:
                self.textkopi.config(state=NORMAL)
                self.textkopi.delete(0,END)
                self.textkopi.focus()
            else:
                self.textkopi.config(state=DISABLED)
                self.e_kopi.set('0')
        kopi_image = 'e:\\KULIAH\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\kopi.png'
        image = PhotoImage(file=kopi_image)
        label_image = Label(scrollable_frame2, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=3, column=2,pady=10)

        kopi=Checkbutton(scrollable_frame2,text='Kopi',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var11,command=kopi)
        kopi.grid(row=4,column=2,sticky=W,padx=(0,50))
        self.textkopi=Entry(scrollable_frame2,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_kopi)
        self.textkopi.grid(row=4,column=2,padx=(50,0))

        kopi_spasi = Label(scrollable_frame2, text="",bg='brown',font=('arial', '18', 'bold'))
        kopi_spasi.grid(row=5, column=2, pady=20)

        def jusjeruk():
            if self.var12.get()==1:
                self.textjusjeruk.config(state=NORMAL)
                self.textjusjeruk.delete(0,END)
                self.textjusjeruk.focus()
            else:
                self.textjusjeruk.config(state=DISABLED)
                self.e_jusjeruk.set('0')
        jusjeruk_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\jusjeruk.png'
        image = PhotoImage(file=jusjeruk_image)
        label_image = Label(scrollable_frame2, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=6, column=2,pady=10)

        jusjeruk=Checkbutton(scrollable_frame2,text='Jus\nJeruk',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var12,command=jusjeruk)
        jusjeruk.grid(row=7,column=2,sticky=W,padx=(0,50))
        self.textjusjeruk=Entry(scrollable_frame2,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_jusjeruk)
        self.textjusjeruk.grid(row=7,column=2,padx=(50,0))

        jusjeruk_spasi = Label(scrollable_frame2, text="",bg='brown',font=('arial', '18', 'bold'))
        jusjeruk_spasi.grid(row=9, column=2, pady=20)

        def kolak():
            if self.var13.get()==1:
                self.textkolak.config(state=NORMAL)
                self.textkolak.delete(0,END)
                self.textkolak.focus()
            else:
                self.textkolak.config(state=DISABLED)
                self.e_kolak.set('0')
        kolak_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\kolak.png'
        image = PhotoImage(file=kolak_image)
        label_image = Label(scrollable_frame2, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=10, column=2,pady=10)

        kolak=Checkbutton(scrollable_frame2,text='Kolak',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var13,command=kolak)
        kolak.grid(row=11,column=2,sticky=W,padx=(0,50))
        self.textkolak=Entry(scrollable_frame2,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_kolak)
        self.textkolak.grid(row=11,column=2,padx=(50,0))

        kolak_spasi = Label(scrollable_frame2, text="",bg='brown',font=('arial', '18', 'bold'))
        kolak_spasi.grid(row=12, column=0, pady=20)

        def bandrek():
            if self.var14.get()==1:
                self.textbandrek.config(state=NORMAL)
                self.textbandrek.delete(0,END)
                self.textbandrek.focus()
            else:
                self.textbandrek.config(state=DISABLED)
                self.e_bandrek.set('0')
        bandrek_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\bandrek.png'
        image = PhotoImage(file=bandrek_image)
        label_image = Label(scrollable_frame2, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=13, column=2,pady=10)

        bandrek=Checkbutton(scrollable_frame2,text='Bandrek',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var14,command=bandrek)
        bandrek.grid(row=14,column=2,sticky=W,padx=(0,70))
        self.textbandrek=Entry(scrollable_frame2,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_bandrek)
        self.textbandrek.grid(row=14,column=2,padx=(70,0))

        bandrek_spasi = Label(scrollable_frame2, text="",bg='brown',font=('arial', '18', 'bold'))
        bandrek_spasi.grid(row=15, column=2, pady=20)

        def esdawet():
            if self.var15.get()==1:
                self.textesdawet.config(state=NORMAL)
                self.textesdawet.delete(0,END)
                self.textesdawet.focus()
            else:
                self.textesdawet.config(state=DISABLED)
                self.e_esdawet.set('0')
        esdawet_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\esdawet.png'
        image = PhotoImage(file=esdawet_image)
        label_image = Label(scrollable_frame2, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=16, column=2,pady=10)

        esdawet=Checkbutton(scrollable_frame2,text='Es\nDawet',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var15,command=esdawet)
        esdawet.grid(row=17,column=2,sticky=W,padx=(0,70))
        self.textesdawet=Entry(scrollable_frame2,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_esdawet)
        self.textesdawet.grid(row=17,column=2,padx=(70,0))

        esdawet_spasi = Label(scrollable_frame2, text="",bg='brown',font=('arial', '18', 'bold'))
        esdawet_spasi.grid(row=19, column=2, pady=20)

        def escendol():
            if self.var16.get()==1:
                self.textescendol.config(state=NORMAL)
                self.textescendol.delete(0,END)
                self.textescendol.focus()
            else:
                self.textescendol.config(state=DISABLED)
                self.e_escendol.set('0')
        escendol_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\escendol.png'
        image = PhotoImage(file=escendol_image)
        label_image = Label(scrollable_frame2, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=20, column=2,pady=10)

        escendol=Checkbutton(scrollable_frame2,text='Es\nCendol',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var16,command=escendol)
        escendol.grid(row=21,column=2,sticky=W,padx=(0,70))
        self.textescendol=Entry(scrollable_frame2,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_escendol)
        self.textescendol.grid(row=21,column=2,padx=(70,0))
    
        escendol_spasi = Label(scrollable_frame2, text="",bg='brown',font=('arial', '18', 'bold'))
        escendol_spasi.grid(row=23, column=2, pady=20)

        def lemontea():
            if self.var17.get()==1:
                self.textlemontea.config(state=NORMAL)
                self.textlemontea.delete(0,END)
                self.textlemontea.focus()
            else:
                self.textlemontea.config(state=DISABLED)
                self.e_lemontea.set('0')
        lemontea_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\lemontea.png'
        image = PhotoImage(file=lemontea_image)
        label_image = Label(scrollable_frame2, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=24, column=2,pady=10)

        lemontea=Checkbutton(scrollable_frame2,text='Lemon\nTea',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var17,command=lemontea)
        lemontea.grid(row=25,column=2,sticky=W,padx=(0,70))
        self.textlemontea=Entry(scrollable_frame2,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_lemontea)
        self.textlemontea.grid(row=25,column=2,padx=(70,0))
        
        lemontea_spasi = Label(scrollable_frame2, text="",bg='brown',font=('arial', '18', 'bold'))
        lemontea_spasi.grid(row=27, column=2, pady=20)
    
        def esdurian():
            if self.var18.get()==1:
                self.textesdurian.config(state=NORMAL)
                self.textesdurian.delete(0,END)
                self.textesdurian.focus()
            else:
                self.textesdurian.config(state=DISABLED)
                self.e_esdurian.set('0')
        esdurian_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\esdurian.png'
        image = PhotoImage(file=esdurian_image)
        label_image = Label(scrollable_frame2, image=image, bg='brown')
        label_image.image = image
        label_image.grid(row=28, column=2,pady=10)

        esdurian=Checkbutton(scrollable_frame2,text='Es\nDurian',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var18,command=esdurian)
        esdurian.grid(row=29,column=2,sticky=W,padx=(0,70))
        self.textesdurian=Entry(scrollable_frame2,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=self.e_esdurian)
        self.textesdurian.grid(row=29,column=2,padx=(70,0))

        esdurian_spasi = Label(scrollable_frame2, text="",bg='brown',font=('arial', '18', 'bold'))
        esdurian_spasi.grid(row=31, column=2, pady=20)


    def menucakes(self):
        self.menucakes_fram = Frame(height=600,width=750,bg='brown')
        self.menucakes_fram.place(x=200,y=88)

        canvas3 = Canvas(self.menucakes_fram, bg='brown', highlightthickness=0, height=450, width=630)
        scrollbar3 = Scrollbar(self.menucakes_fram, orient='vertical', command=canvas3.yview)
        scrollable_frame3 = Frame(canvas3, bg='brown')

        canvas3.pack(side='left', fill='both', expand=True)
        scrollbar3.pack(side='right', fill='y')
        # Mengaitkan scrollbar dengan canvas
        canvas3.configure(yscrollcommand=scrollbar3.set)
        canvas3.create_window((0, 0), window=scrollable_frame3, anchor='nw')

        canvas3.bind_all("<MouseWheel>", lambda event: canvas3.yview_scroll(int(-1 * (event.delta / 120)), "units"))
        scrollable_frame3.bind('<Configure>', lambda e: canvas3.configure(scrollregion=canvas3.bbox('all')))

        close_button = Button(self.menucakes_fram, text="X",font=('arial',10,'bold'), command=self.hide_page3, bg='red', fg='black', width=3)
        close_button.pack()

        def bikaambon():
            if self.var19.get()==1:
                self.textbikaambon.config(state=NORMAL)
                self.textbikaambon.delete(0,END)
                self.textbikaambon.focus()
            else:
                self.textbikaambon.config(state=DISABLED)
                self.e_bikaambon.set('0')
        bikaambon_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\bikaambon.png'
        image = PhotoImage(file=bikaambon_image)
        label_image = Label(scrollable_frame3, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=0, column=2,pady=10)

        bikaambon=Checkbutton(scrollable_frame3,text='Bika\nAmbon',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var19,command=bikaambon)
        bikaambon.grid(row=1,column=2,sticky=W,padx=(0,70))
        self.textbikaambon=Entry(scrollable_frame3,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable= self.e_bikaambon)
        self.textbikaambon.grid(row=1,column=2,padx=(70,0))

        bikaambon_spasi = Label(scrollable_frame3, text="",bg='brown',font=('arial', '18', 'bold'))
        bikaambon_spasi.grid(row=3, column=2, pady=20)

        def donat():
            if self.var20.get()==1:
                self.textdonat.config(state=NORMAL)
                self.textdonat.delete(0,END)
                self.textdonat.focus()
            else:
                self.textdonat.config(state=DISABLED)
                self.e_donat.set('0')
        donat_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\donat.png'
        image = PhotoImage(file=donat_image)
        label_image = Label(scrollable_frame3, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=4, column=2,pady=10)

        donat=Checkbutton(scrollable_frame3,text='Donat',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var20,command=donat)
        donat.grid(row=5,column=2,sticky=W,padx=(0,50))
        self.textdonat=Entry(scrollable_frame3,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable= self.e_donat)
        self.textdonat.grid(row=5,column=2,padx=(50,0))

        donat_spasi = Label(scrollable_frame3, text="",bg='brown',font=('arial', '18', 'bold'))
        donat_spasi.grid(row=6, column=2, pady=20)

        def bengbeng():
            if self.var21.get()==1:
                self.textbengbeng.config(state=NORMAL)
                self.textbengbeng.delete(0,END)
                self.textbengbeng.focus()
            else:
                self.textbengbeng.config(state=DISABLED)
                self.e_bengbeng.set('0')
        bengbeng_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\bengbeng.png'
        image = PhotoImage(file=bengbeng_image)
        label_image = Label(scrollable_frame3, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=7, column=2,pady=10)

        bengbeng=Checkbutton(scrollable_frame3,text='Bengbeng',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var21,command=bengbeng)
        bengbeng.grid(row=8,column=2,sticky=W,padx=(0,120))
        self.textbengbeng=Entry(scrollable_frame3,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable= self.e_bengbeng)
        self.textbengbeng.grid(row=8,column=2,padx=(120,0))

        bengbeng_spasi = Label(scrollable_frame3, text="",bg='brown',font=('arial', '18', 'bold'))
        bengbeng_spasi.grid(row=9, column=2, pady=20)

        def sariroti():
            if self.var22.get()==1:
                self.textsariroti.config(state=NORMAL)
                self.textsariroti.delete(0,END)
                self.textsariroti.focus()
            else:
                self.textsariroti.config(state=DISABLED)
                self.e_sariroti.set('0')
        sariroti_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\sariroti.png'
        image = PhotoImage(file=sariroti_image)
        label_image = Label(scrollable_frame3, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=10, column=2,pady=10)

        sariroti=Checkbutton(scrollable_frame3,text='Sari Roti',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var22,command=sariroti)
        sariroti.grid(row=11,column=2,sticky=W,padx=(0,80))
        self.textsariroti=Entry(scrollable_frame3,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable= self.e_sariroti)
        self.textsariroti.grid(row=11,column=2,padx=(80,0))

        sariroti_spasi = Label(scrollable_frame3, text="",bg='brown',font=('arial', '18', 'bold'))
        sariroti_spasi.grid(row=12, column=2, pady=20)

        def pancake():
            if self.var23.get()==1:
                self.textpancake.config(state=NORMAL)
                self.textpancake.delete(0,END)
                self.textpancake.focus()
            else:
                self.textpancake.config(state=DISABLED)
                self.e_pancake.set('0')
        pancake_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\pancake.png'
        image = PhotoImage(file=pancake_image)
        label_image = Label(scrollable_frame3, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=13, column=2,pady=10)

        pancake=Checkbutton(scrollable_frame3,text='PanCake',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var23,command=pancake)
        pancake.grid(row=14,column=2,sticky=W,padx=(0,70))
        self.textpancake=Entry(scrollable_frame3,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable= self.e_pancake)
        self.textpancake.grid(row=14,column=2,padx=(70,0))

        pancake_spasi = Label(scrollable_frame3, text="",bg='brown',font=('arial', '18', 'bold'))
        pancake_spasi.grid(row=15, column=2, pady=20)

        def klepon():
            if self.var24.get()==1:
                self.textklepon.config(state=NORMAL)
                self.textklepon.delete(0,END)
                self.textklepon.focus()
            else:
                self.textklepon.config(state=DISABLED)
                self.e_klepon.set('0')
        klepon_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\klepon.png'
        image = PhotoImage(file=klepon_image)
        label_image = Label(scrollable_frame3, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=16, column=2,pady=10)

        klepon=Checkbutton(scrollable_frame3,text='Klepon',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var24,command=klepon)
        klepon.grid(row=17,column=2,sticky=W,padx=(0,50))
        self.textklepon=Entry(scrollable_frame3,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable= self.e_klepon)
        self.textklepon.grid(row=17,column=2,padx=(50,0))

        klepon_spasi = Label(scrollable_frame3, text="",bg='brown',font=('arial', '18', 'bold'))
        klepon_spasi.grid(row=18, column=2, pady=20)

        def ondeonde():
            if self.var25.get()==1:
                self.textondeonde.config(state=NORMAL)
                self.textondeonde.delete(0,END)
                self.textondeonde.focus()
            else:
                self.textondeonde.config(state=DISABLED)
                self.e_ondeonde.set('0')
        ondeonde_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\ondeonde.png'
        image = PhotoImage(file=ondeonde_image)
        label_image = Label(scrollable_frame3, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=19, column=2,pady=10)

        ondeonde=Checkbutton(scrollable_frame3,text='Onde\nOnde',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var25,command=ondeonde)
        ondeonde.grid(row=20,column=2,sticky=W,padx=(0,50))
        self.textondeonde=Entry(scrollable_frame3,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable= self.e_ondeonde)
        self.textondeonde.grid(row=20,column=2,padx=(50,0))

        ondeonde_spasi = Label(scrollable_frame3, text="",bg='brown',font=('arial', '18', 'bold'))
        ondeonde_spasi.grid(row=22, column=2, pady=20)

        def lemper():
            if self.var26.get()==1:
                self.textlemper.config(state=NORMAL)
                self.textlemper.delete(0,END)
                self.textlemper.focus()
            else:
                self.textlemper.config(state=DISABLED)
                self.e_lemper.set('0')
        lemper_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\lemper.png'
        image = PhotoImage(file=lemper_image)
        label_image = Label(scrollable_frame3, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=23, column=2,pady=10)

        lemper=Checkbutton(scrollable_frame3,text='Lemper',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var26,command=lemper)
        lemper.grid(row=24,column=2,sticky=W,padx=(0,70))
        self.textlemper=Entry(scrollable_frame3,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable= self.e_lemper)
        self.textlemper.grid(row=24,column=2,padx=(70,0))

        lemper_spasi = Label(scrollable_frame3, text="",bg='brown',font=('arial', '18', 'bold'))
        lemper_spasi.grid(row=25, column=2, pady=20)

        def dadargulung():
            if self.var27.get()==1:
                self.textdadargulung.config(state=NORMAL)
                self.textdadargulung.delete(0,END)
                self.textdadargulung.focus()
            else:
                self.textdadargulung.config(state=DISABLED)
                self.e_dadargulung.set('0')
        dadargulung_image = 'e:\\KULIAH\\SEMESTER 1\\PEMROGRAMAN DASAR\\TUGAS\\dadargulung.png'
        image = PhotoImage(file=dadargulung_image)
        label_image = Label(scrollable_frame3, image=image, bg='blue')
        label_image.image = image
        label_image.grid(row=26, column=2,pady=10)

        dadargulung=Checkbutton(scrollable_frame3,text='Dadar\nGulung',font=('arial','18','bold'), onvalue=1, offvalue=0, variable=self.var27,command=dadargulung)
        dadargulung.grid(row=27,column=2,sticky=W,padx=(0,70))
        self.textdadargulung=Entry(scrollable_frame3,font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable= self.e_dadargulung)
        self.textdadargulung.grid(row=27,column=2,padx=(70,0))

        dadargulung_spasi = Label(scrollable_frame3, text="",bg='brown',font=('arial', '18', 'bold'))
        dadargulung_spasi.grid(row=28, column=2, pady=20)

    def frame_jumlahharga(self):
        self.costFrame=Frame(bd=4, relief=RIDGE, bg='blue', pady=10)
        self.costFrame.place(x=45, y=550)

        labelCostofFoods=Label(self.costFrame,text='Cost of Foods',font=('arial',16, 'bold'), bg = 'blue', fg ='white')
        labelCostofFoods.grid(row=0,column=0)
        textCostofFoods= Entry(self.costFrame, font=('arial',16,'bold'), bd=6, width=14,
                                        state= 'readonly',textvariable=self.costoffoodsvar )
        textCostofFoods.grid(row=0, column=1,padx= 41) 

        labelCostofDrinks=Label(self.costFrame,text='Cost of Drinks',font=('arial',16, 'bold'), bg = 'blue', fg ='white')
        labelCostofDrinks.grid(row=1,column=0)
        textCostofDrinks= Entry(self.costFrame, font=('arial',16,'bold'), bd=6, width=14,state= 'readonly',textvariable=self.costofdrinksvar )
        textCostofDrinks.grid(row=1, column=1,padx= 41) 

        labelCostofCakes=Label(self.costFrame,text='Cost of Cakes',font=('arial',16, 'bold'), bg = 'blue', fg ='white')
        labelCostofCakes.grid(row=2,column=0)
        textCostofCakes= Entry(self.costFrame, font=('arial',16,'bold'), bd=6, width=14,state= 'readonly',textvariable=self.costofcakesvar )
        textCostofCakes.grid(row=2, column=1,padx= 41) 

        labelSubTotal=Label(self.costFrame,text='Sub Total',font=('arial',16, 'bold'), bg = 'blue', fg ='white')
        labelSubTotal.grid(row=0,column=2)
        textSubtotal= Entry(self.costFrame, font=('arial',16,'bold'), bd=6, width=14,state= 'readonly',textvariable=self.subtotalvar )
        textSubtotal.grid(row=0, column=3,padx= 41) 

        labelServiceTax=Label(self.costFrame,text='Service Tax',font=('arial',16, 'bold'), bg = 'blue', fg ='white')
        labelServiceTax.grid(row=1,column=2)
        textServiceTax= Entry(self.costFrame, font=('arial',16,'bold'), bd=6, width=14,state= 'readonly',textvariable=self.servicetaxvar )
        textServiceTax.grid(row=1, column=3,padx= 41) 

        labelTotalCost=Label(self.costFrame,text='Total Cost',font=('arial',16, 'bold'), bg = 'blue', fg ='white')
        labelTotalCost.grid(row=2,column=2)
        textTotalCost= Entry(self.costFrame, font=('arial',16,'bold'), bd=6, width=14,state= 'readonly',textvariable=self.totalcostvar )
        textTotalCost.grid(row=2, column=3, padx= 41) 
    
    def layarstruk(self):
        self.rightFrame=Frame(bd=15,relief=RIDGE)
        self.rightFrame.pack(side=RIGHT)
        # Membuat layar struk
        self.recieptFrame= Frame(self.rightFrame,bd=4,relief=RIDGE)
        self.recieptFrame.pack()
        self.textReceipt= Text(self.recieptFrame,font=('arial',12,'bold'), bd=3,width=37,height=14)
        self.textReceipt.grid(row=0,column=0)
        # Membuat frame tombol
        self.buttonFrame= Frame(self.rightFrame,bd=4,relief=RIDGE)
        self.buttonFrame.pack()
        
        def reset():
            self.textReceipt.delete(1.0,END)
            self.e_roti.set('0')
            self.e_ayamgoreng.set('0')
            self.e_nasigoreng.set('0')
            self.e_telurdadar.set('0')
            self.e_bakso.set('0')
            self.e_mieayam.set('0')
            self.e_nasicampur.set('0')
            self.e_miegoreng.set('0')
            self.e_miepangsit.set('0')

            self.e_esteh.set('0')
            self.e_kopi.set('0')
            self.e_jusjeruk.set('0')
            self.e_kolak.set('0')
            self.e_bandrek.set('0')
            self.e_esdawet.set('0')
            self.e_escendol.set('0')
            self.e_lemontea.set('0')
            self.e_esdurian.set('0')

            self.e_bikaambon.set('0')
            self.e_donat.set('0')
            self.e_bengbeng.set('0')
            self.e_sariroti.set('0')
            self.e_pancake.set('0')
            self.e_klepon.set('0')
            self.e_ondeonde.set('0')
            self.e_lemper.set('0')
            self.e_dadargulung.set('0')

            self.textroti.config(state=DISABLED)
            self.textayamgoreng.config(state=DISABLED)
            self.textnasigoreng.config(state=DISABLED)
            self.texttelurdadar.config(state=DISABLED)
            self.textbakso.config(state=DISABLED)
            self.textmieayam.config(state=DISABLED)
            self.textnasicampur.config(state=DISABLED)
            self.textmiegoreng.config(state=DISABLED)
            self.textmiepangsit.config(state=DISABLED)

            self.textesteh.config(state=DISABLED)
            self.textkopi.config(state=DISABLED)
            self.textjusjeruk.config(state=DISABLED)
            self.textkolak.config(state=DISABLED)
            self.textbandrek.config(state=DISABLED)
            self.textesdawet.config(state=DISABLED)
            self.textescendol.config(state=DISABLED)
            self.textlemontea.config(state=DISABLED)
            self.textesdurian.config(state=DISABLED)

            self.textbikaambon.config(state=DISABLED)
            self.textdonat.config(state=DISABLED)
            self.textbengbeng.config(state=DISABLED)
            self.textsariroti.config(state=DISABLED)
            self.textpancake.config(state=DISABLED)
            self.textklepon.config(state=DISABLED)
            self.textondeonde.config(state=DISABLED)
            self.textlemper.config(state=DISABLED)
            self.textdadargulung.config(state=DISABLED)

            self.var1.set(0)
            self.var2.set(0)
            self.var3.set(0)
            self.var4.set(0)
            self.var5.set(0)
            self.var6.set(0)
            self.var7.set(0)
            self.var8.set(0)
            self.var9.set(0)
            self.var10.set(0)
            self.var11.set(0)
            self.var12.set(0)
            self.var13.set(0)
            self.var14.set(0)
            self.var15.set(0)
            self.var16.set(0)
            self.var17.set(0)
            self.var18.set(0)
            self.var19.set(0)
            self.var20.set(0)
            self.var21.set(0)
            self.var22.set(0)
            self.var23.set(0)
            self.var24.set(0)
            self.var25.set(0)
            self.var26.set(0)
            self.var27.set(0)

            self.costofdrinksvar.set('')
            self.costoffoodsvar.set('')
            self.costofcakesvar.set('')
            self.subtotalvar.set('')
            self.servicetaxvar.set('')
            self.totalcostvar.set('')

        buttonReset= Button(self.buttonFrame,text='Reset',font=('arial',12,'bold'),fg='white',bg='blue',bd=3,padx=3,
                    command=reset)
        buttonReset.grid(row=0,column=4)

        def save():
            if self.textReceipt.get(1.0, END)=='\n':
                pass
            else:
                url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
                if url== None:
                    pass
                else:
                    bill_data=self.textReceipt.get(1.0,END)
                    url.write(bill_data)
                    url.close()
                    messagebox.showinfo('Information','your Bill is Successfully Saved')

        buttonSave= Button(self.buttonFrame,text='Save',font=('arial',12,'bold'),fg='white',bg='blue',bd=3,padx=3,
                   command=save)
        buttonSave.grid(row=0,column=2)

        def receipt():
            global billnumber
            if self.costoffoodsvar.get() != '' or self.costofcakesvar.get() != '' or self.costofdrinksvar.get() !='' :
                self.textReceipt.delete(1.0,END)
                x=random.randint(100,10000)
                billnumber='BILL'+str(x)
                self.textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\n')
                self.textReceipt.insert(END,'***************************************************'+'\n')
                self.textReceipt.insert(END,'Items: \t\t Cost Of Items(Rp)'+'\n')
                self.textReceipt.insert(END,'***************************************************'+'\n')
                if self.e_roti.get()!='0':
                    self.textReceipt.insert(END,f'Roti\t\t\t{int(self.e_roti.get())*6000}\n\n')
                if self.e_ayamgoreng.get()!='0':
                    self.textReceipt.insert(END,f'Ayam Goreng\t\t\t{int(self.e_ayamgoreng.get())*9000}\n\n')
                if self.e_nasigoreng.get()!='0':
                    self.textReceipt.insert(END,f'Nasi Goreng\t\t\t{int(self.e_nasigoreng.get())*15000}\n\n')
                if self.e_telurdadar.get()!='0':
                    self.textReceipt.insert(END,f'Telur Dadar\t\t\t{int(self.e_telurdadar.get())*8000}\n\n')
                if self.e_bakso.get()!='0':
                    self.textReceipt.insert(END,f'Bakso\t\t\t{int(self.e_bakso.get())*12000}\n\n')
                if self.e_mieayam.get()!='0':
                    self.textReceipt.insert(END,f'Mie Ayam\t\t\t{int(self.e_mieayam.get())*13000}\n\n')
                if self.e_nasicampur.get()!='0':
                    self.textReceipt.insert(END,f'Nasi Campur\t\t\t{int(self.e_nasicampur.get())*16000}\n\n')
                if self.e_miegoreng.get()!='0':
                    self.textReceipt.insert(END,f'Mie Goreng\t\t\t{int(self.e_miegoreng.get())*20000}\n\n')
                if self.e_miepangsit.get()!='0':
                    self.textReceipt.insert(END,f'Mie Pangsit\t\t\t{int(self.e_miepangsit.get())*22000}\n\n')

                if self.e_esteh.get()!='0':
                    self.textReceipt.insert(END,f'Es Teh\t\t\t{int(self.e_esteh.get())*6000}\n\n')
                if self.e_kopi.get()!='0':
                    self.textReceipt.insert(END,f'Kopi\t\t\t{int(self.e_kopi.get())*8000}\n\n')
                if self.e_jusjeruk.get()!='0':
                    self.textReceipt.insert(END,f'Jus Jeruk\t\t\t{int(self.e_jusjeruk.get())*9000}\n\n')
                if self.e_kolak.get()!='0':
                    self.textReceipt.insert(END,f'Kolak\t\t\t{int(self.e_kolak.get())*10000}\n\n')
                if self.e_bandrek.get()!='0':
                    self.textReceipt.insert(END,f'Bandrek\t\t\t{int(self.e_bandrek.get())*12000}\n\n')
                if self.e_esdawet.get()!='0':
                    self.textReceipt.insert(END,f'Es Dawet\t\t\t{int(self.e_esdawet.get())*12000}\n\n')
                if self.e_escendol.get()!='0':
                    self.textReceipt.insert(END,f'Es Cendol\t\t\t{int(self.e_escendol.get())*14000}\n\n')
                if self.e_lemontea.get()!='0':
                    self.textReceipt.insert(END,f'Lemon Tea\t\t\t{int(self.e_lemontea.get())*13000}\n\n')
                if self.e_esdurian.get()!='0':
                    self.textReceipt.insert(END,f'Es Durian\t\t\t{int(self.e_esdurian.get())*15000}\n\n')

                if self.e_bikaambon.get()!='0':
                    self.textReceipt.insert(END,f'Bika Ambon\t\t\t{int(self.e_bikaambon.get())*5000}\n\n')
                if self.e_donat.get()!='0':
                    self.textReceipt.insert(END,f'Donat\t\t\t{int(self.e_donat.get())*6000}\n\n')
                if self.e_bengbeng.get()!='0':
                    self.textReceipt.insert(END,f'Bengbeng\t\t\t{int(self.e_bengbeng.get())*7000}\n\n')
                if self.e_sariroti.get()!='0':
                    self.textReceipt.insert(END,f'Sari Roti\t\t\t{int(self.e_sariroti.get())*8000}\n\n')
                if self.e_pancake.get()!='0':
                    self.textReceipt.insert(END,f'Pancake\t\t\t{int(self.e_pancake.get())*9000}\n\n')
                if self.e_klepon.get()!='0':
                    self.textReceipt.insert(END,f'Klepon\t\t\t{int(self.e_klepon.get())*10000}\n\n')
                if self.e_ondeonde.get()!='0':
                    self.textReceipt.insert(END,f'Onde Onde\t\t\t{int(self.e_ondeonde.get())*11000}\n\n')
                if self.e_lemper.get()!='0':
                    self.textReceipt.insert(END,f'Lemper\t\t\t{int(self.e_lemper.get())*12000}\n\n')
                if self.e_dadargulung.get()!='0':
                    self.textReceipt.insert(END,f'Dadar Gulung\t\t\t{int(self.e_dadargulung.get())*13000}\n\n')
        
                self.textReceipt.insert(END,'***************************************************************\n')
                if self.costoffoodsvar.get()!='Rp.0':
                    self.textReceipt.insert(END,f'Cost Of Foods\t\t\tRp.{priceofFoods}\n\n')
                if self.costofdrinksvar.get()!='Rp.0':
                    self.textReceipt.insert(END,f'Cost Of Drinks\t\t\tRp.{priceofDrinks}\n\n')
                if self.costofcakesvar.get()!='Rp.0':
                    self.textReceipt.insert(END,f'Cost Of Cakes\t\t\tRp.{priceofCakes}\n\n')
        
                self.textReceipt.insert(END,f'Sub Total\t\t\tRp.{subtotalofItems}\n\n')
                self.textReceipt.insert(END,f'Service Tax\t\t\tRp.{2000}\n\n')
                self.textReceipt.insert(END,f'Total Cost\t\t\tRp.{subtotalofItems+2000}\n\n')                    
                self.textReceipt.insert(END,'***************************************************************\n')
                self.textReceipt.insert(END, f'Bayar\t\t\tRp.{uang_pelanggan}\n')
                self.textReceipt.insert(END, f'Kembali\t\t\tRp.{kembalian}\n')             

            else: 
                messagebox.showerror('Error','Tidak ada Item yang dipilih')

        buttonReceipt= Button(self.buttonFrame,text='Receipt',font=('arial',12,'bold'),fg='white',bg='blue',bd=3,padx=3,command=receipt)
        buttonReceipt.grid(row=0,column=1)

        def totalcost():
            global priceofFoods,priceofDrinks,priceofCakes,subtotalofItems,totalcost#,uang_pelanggan,kembalian
            if self.var1.get() != 0 or self.var2.get() != 0 or self.var3.get() != 0 or self.var4.get() != 0 or self.var5.get() != 0 or \
                self.var6.get() != 0 or self.var7.get() != 0 or self.var8.get() != 0 or self.var9.get() != 0 or self.var10.get() != 0 or \
                self.var11.get() != 0 or self.var12.get() != 0 or self.var13.get() != 0 or self.var14.get() != 0 or self.var15.get() != 0 or \
                self.var16.get() != 0 or self.var17.get() != 0 or self.var18.get() != 0 or self.var19.get() != 0 or self.var20.get() != 0 or \
                self.var21.get() != 0 or self.var22.get() != 0 or self.var23.get() != 0 or self.var24.get() != 0 or self.var25.get() != 0 or \
                self.var26.get() !=0 or self.var27.get() != 0:
        
                item1=int(self.e_roti.get())
                item2=int(self.e_ayamgoreng.get())
                item3=int(self.e_nasigoreng.get())
                item4=int(self.e_telurdadar.get())
                item5=int(self.e_bakso.get())
                item6=int(self.e_mieayam.get())
                item7=int(self.e_nasicampur.get())
                item8=int(self.e_miegoreng.get())
                item9=int(self.e_miepangsit.get())

                item10=int(self.e_esteh.get())
                item11=int(self.e_kopi.get())
                item12=int(self.e_jusjeruk.get())
                item13=int(self.e_kolak.get())
                item14=int(self.e_bandrek.get())
                item15=int(self.e_esdawet.get())
                item16=int(self.e_escendol.get())
                item17=int(self.e_lemontea.get())
                item18=int(self.e_esdurian.get())

                item19=int(self.e_bikaambon.get())
                item20=int(self.e_donat.get())
                item21=int(self.e_bengbeng.get())
                item22=int(self.e_sariroti.get())
                item23=int(self.e_pancake.get())
                item24=int(self.e_klepon.get())
                item25=int(self.e_ondeonde.get())
                item26=int(self.e_lemper.get())
                item27=int(self.e_dadargulung.get())

                priceofFoods=(item1*6000)+(item2*9000)+(item3*15000)+(item4*8000)+(item5*12000)+(item6*13000)+(item7*16000)+(item8*20000)+(item9*22000)

                priceofDrinks=(item10*6000)+(item11*8000)+(item12*9000)+(item13*10000)+(item14*12000)+(item15*12000)+(item16*14000)+(item17*13000)+(item18*15000)

                priceofCakes=(item19*5000)+(item20*6000)+(item21*7000)+(item22*8000)+(item23*9000)+(item24*10000)+(item25*11000)+(item26*12000)+(item27*13000)

                self.costoffoodsvar.set('Rp.' + str(priceofFoods))
                self.costofdrinksvar.set('Rp.' +str(priceofDrinks))
                self.costofcakesvar.set('Rp.' +str(priceofCakes))

                subtotalofItems=priceofFoods+priceofDrinks+priceofCakes
                self.subtotalvar.set('Rp.'+ str(subtotalofItems))

                self.servicetaxvar.set("Rp.2000")

                totalcost=subtotalofItems+2000
                self.totalcostvar.set('Rp.'+str (totalcost))

            else: 
                messagebox.showerror('Error','Tidak ada Item yang dipilih')

        buttonTotal= Button(self.buttonFrame,text='Total',font=('arial',12,'bold'),fg='white',bg='blue',bd=3, padx=3,command=totalcost)
        buttonTotal.grid(row=0,column=0)

    def bayar_uangpelanggan(self):
        self.frame_uangpelanggan=Frame(bd=4, relief=RIDGE, bg='blue', pady=10)
        self.frame_uangpelanggan.place(x=950, y=580)

        label_uangpelanggan=Label(self.frame_uangpelanggan,text='Uang Pembayaran',font=('arial',16, 'bold'), bg = 'blue', fg ='white')
        label_uangpelanggan.grid(row=0,column=1)
        self.text_uangpelanggan= Entry(self.frame_uangpelanggan, font=('arial',16,'bold'), bd=6, width=14)
        self.text_uangpelanggan.grid(row=1, column=1) 

        def hasil_perhitungan():
            global uang_pelanggan,kembalian
            try:
                uang_pelanggan = int(self.text_uangpelanggan.get())
                kembalian = uang_pelanggan - totalcost
                self.kembalianvar.set('Rp.' + str(kembalian))
            except ValueError:
                kembalian = 0
                self.kembalianvar.set('Rp.' + str(kembalian))
                messagebox.showwarning('Error', 'Masukkan jumlah uang pembayaran dengan benar!')

        button_pembayaran= Button(self.frame_uangpelanggan,text='SEND',font=('Heltavica',12,'bold'),fg='black',bg='white',bd=3, padx=3,command=hasil_perhitungan)
        button_pembayaran.grid(row=1,column=2)


if __name__ == "__main__":
    root = Tk()
    kasir_cafe = KasirCafe(root)
    root.mainloop()

# Class Kalkulator
import tkinter as tk
from tkinter import Entry, Button, END

class CalculatorApp:
    def __init__(self, root):
        self.operator = ''
        self.root = root
        self.root.title("Calculator")
        
        # Calculator Frame
        self.calculator_frame = tk.Frame(root, bd=1, relief=tk.RIDGE)
        self.calculator_frame.pack()

        # Calculator Field
        self.calculator_field = tk.Entry(self.calculator_frame, font=('arial', 12, 'bold'), width=32, bd=4)
        self.calculator_field.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'Ans', 'Clear', '0', '/'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.calculator_frame, text=button, padx=20, pady=20, font=('arial', 16, 'bold'),
                      command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, numbers):
        if numbers == 'Clear':
            self.clear()
        elif numbers == 'Ans':
            try:
                result = str(eval(self.operator))
                self.calculator_field.delete(0, END)
                self.calculator_field.insert(0, result)
                self.operator = ''
            except Exception as e:
                self.calculator_field.delete(0, END)
                self.calculator_field.insert(0, 'Error')
        else:
            self.operator += numbers
            self.calculator_field.delete(0, END)
            self.calculator_field.insert(END, self.operator)

    def clear(self):
        self.operator = ''
        self.calculator_field.delete(0, END)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
