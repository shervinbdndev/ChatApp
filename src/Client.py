try:
    import os
    import sv_ttk
    import socket
    import tkinter
    import ntkutils
    import threading
    import webbrowser
    import darkdetect
    from typing_extensions import Self
    from tkinter.ttk import (Notebook , Frame)
    from tkinter.__init__ import (Text , StringVar)
    from customtkinter.widgets.customtkinter_entry import CTkEntry
    from customtkinter.widgets.customtkinter_button import CTkButton
    
    from Management import Materials
    
except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Run') from None
    
finally:
    ...
    
    



class Client:
    def __init__(self : Self) -> None:
        super(Client , self).__init__()
        self.root = tkinter.Tk()
        self.root.title(string=f'Client : {socket.gethostbyname(socket.gethostname())}')
        self.root.geometry(newGeometry='500x700')
        self.root.resizable(width=False , height=False)
        self.root.iconbitmap(bitmap=os.path.join(os.path.abspath(path=os.path.dirname(p=__file__)) , r'images/icon.ico'))
        self.tabControl = Notebook(master=self.root)
        self.tabChat = Frame(master=self.tabControl)
        self.tabLang = Frame(master=self.tabControl)
        self.tabAbout = Frame(master=self.tabControl)
        self.tabControl.add(child=self.tabChat , text='Chat')
        self.tabControl.add(child=self.tabLang , text='Language')
        self.tabControl.add(child=self.tabAbout , text='About')
        self.tabControl.pack(expand=1 , fill=Materials.Alignments.both)
        self.enMessage = StringVar(master=self.tabChat)
        self.clientSocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        self.clientSocket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
        self.port: int = 8000
        self.hostIP: str = '127.0.0.1'
        self.clientSocket.connect((self.hostIP , self.port))
        
        def setBySystemTheme() -> None:
            if (darkdetect.isLight()):
                sv_ttk.set_theme(theme=Materials.Themes.LIGHT)
                self.textChat.configure(foreground=Materials.Colors.black)
                self.btnSend.configure(bg_color=Materials.Colors.white)
                self.btnPA.configure(bg_color=Materials.Colors.white)
                self.btnEN.configure(bg_color=Materials.Colors.white)
                self.btnGithub.configure(bg_color=Materials.Colors.white)
                self.root.update_idletasks()
            if (darkdetect.isDark()):
                sv_ttk.set_theme(theme=Materials.Themes.DARK)
                ntkutils.dark_title_bar(window=self.root)
                self.textChat.configure(foreground=Materials.Colors.white)
                self.btnSend.configure(bg_color=Materials.Colors.dark)
                self.btnPA.configure(bg_color=Materials.Colors.dark)
                self.btnEN.configure(bg_color=Materials.Colors.dark)
                self.btnGithub.configure(bg_color=Materials.Colors.dark)
                self.root.update_idletasks()
                
        def changeAppLanguage(arg : str) -> None:
            if (arg == 'PA'):
                self.root.title(string=f'دستگاه : {socket.gethostbyname(socket.gethostname())}')
                self.tabControl.add(child=self.tabChat , text='چت')
                self.tabControl.add(child=self.tabLang , text='زبان')
                self.tabControl.add(child=self.tabAbout , text='درباره')
                self.btnSend.configure(text='ارسال')
                self.btnPA.configure(text='پارسی')
                self.btnEN.configure(text='انگلیسی')
                self.btnGithub.configure(text='گیتهاب')
                if (self.enMessage.get() == ''):
                    pass
                else:
                    self.enMessage.set(value='پیام خود را وارد کنید')
            elif (arg == 'EN'):
                self.root.title(string=f'Client : {socket.gethostbyname(socket.gethostname())}')
                self.tabControl.add(child=self.tabChat , text='Chat')
                self.tabControl.add(child=self.tabLang , text='Language')
                self.tabControl.add(child=self.tabAbout , text='About')
                self.btnSend.configure(text='Send')
                self.btnPA.configure(text='Persian')
                self.btnEN.configure(text='English')
                self.btnGithub.configure(text='Github')
                if (self.enMessage.get() == ''):
                    pass
                else:
                    self.enMessage.set(value='Type Your Message Here')
            
        def aboutMeClickEvent() -> None:
            webbrowser.open(url='https://github.com/shervinbdndev')
                
        def sendMessage() -> None:
            msg = self.enMessage.get()
            self.textChat.insert(index=tkinter.END , chars=f"\n You: {msg}")
            self.clientSocket.send(msg.encode(encoding='utf-8'))
                
        def receiveMessage() -> None:
            while True:
                serverMessage = self.clientSocket.recv(1024).decode(encoding='utf-8')
                self.textChat.insert(index=tkinter.END , chars=f"\n {serverMessage}")
                
        def startRecieveing() -> None:
            recv = threading.Thread(target=receiveMessage)
            recv.daemon = True
            recv.start()
        
        self.textChat = Text(
            master=self.tabChat ,
            width=53 ,
            height=31 ,
            bd=1 ,
            border=1 ,
            borderwidth=1 ,
            font=(Materials.Fonts.pop , 12 , Materials.FontWeight.bold) ,
            relief=Materials.Reliefs.groove ,
            highlightcolor=Materials.Colors.medPurple ,
            highlightbackground=Materials.Colors.medPurple ,
            highlightthickness=1 ,
        )
        
        self.textChat.place(relx=0.5 , rely=0.46 , anchor=Materials.Alignments.center)
        
        self.entryMessage = CTkEntry(
            master=self.tabChat ,
            textvariable=self.enMessage ,
            corner_radius=5 ,
            width=363 ,
            height=40 ,
            text_color=Materials.Colors.medPurple ,
            text_font=(Materials.FontWeight.bold) ,
            cursor=Materials.Cursors.hand ,
            justify=Materials.Alignments.left ,
            border_color=Materials.Colors.medPurple ,
            state=Materials.State.normal ,
        )
        
        self.enMessage.set(value='Type Your Message Here')
        
        self.entryMessage.place(relx=0.377 , rely=0.95452 , anchor=Materials.Alignments.center)
        
        self.btnSend = CTkButton(
            master=self.tabChat ,
            text='Send' ,
            corner_radius=5 ,
            width=100 ,
            height=40 ,
            text_color=Materials.Colors.white ,
            text_font=(Materials.FontWeight.bold) ,
            fg_color=Materials.Colors.medPurple ,
            cursor=Materials.Cursors.hand ,
            state=Materials.State.normal ,
            command=sendMessage,
        )
        
        self.btnSend.place(relx=0.882 , rely=0.95452 , anchor=Materials.Alignments.center)
        
        self.btnPA = CTkButton(
            master=self.tabLang ,
            text='Persian' ,
            corner_radius=5 ,
            width=200 ,
            height=60 ,
            text_color=Materials.Colors.white ,
            text_font=(Materials.FontWeight.bold) ,
            fg_color=Materials.Colors.medPurple ,
            cursor=Materials.Cursors.hand ,
            state=Materials.State.normal ,
            command=lambda:changeAppLanguage(arg='PA'),
        )
        
        self.btnPA.place(relx=0.25 , rely=0.5 , anchor=Materials.Alignments.center)
        
        self.btnEN = CTkButton(
            master=self.tabLang ,
            text='English' ,
            corner_radius=5 ,
            width=200 ,
            height=60 ,
            text_color=Materials.Colors.white ,
            text_font=(Materials.FontWeight.bold) ,
            fg_color=Materials.Colors.medPurple ,
            cursor=Materials.Cursors.hand ,
            state=Materials.State.normal ,
            command=lambda:changeAppLanguage(arg='EN'),
        )
        
        self.btnEN.place(relx=0.75 , rely=0.5 , anchor=Materials.Alignments.center)
        
        self.btnGithub = CTkButton(
            master=self.tabAbout ,
            text='Github' ,
            corner_radius=5 ,
            width=200 ,
            height=60 ,
            text_color=Materials.Colors.white ,
            text_font=(Materials.FontWeight.bold) ,
            fg_color=Materials.Colors.medPurple ,
            cursor=Materials.Cursors.hand ,
            state=Materials.State.normal ,
            command=aboutMeClickEvent,
        )
        
        self.btnGithub.place(relx=0.5 , rely=0.5 , anchor=Materials.Alignments.center)
        
        setBySystemTheme()
        startRecieveing()
        
        self.root.mainloop()
        
        
        
        
        


def main() -> None:
    Client()





if (__name__ == '__main__' and __package__ is None):
    main()