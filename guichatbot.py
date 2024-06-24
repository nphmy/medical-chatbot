#Creating GUI with tkinter

from tkinter import *


def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
 

root = tk.Tk()
root.title("CHAT WITH MEDICARE")
root.geometry("1000x600+50+50")
root.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(root, bd=0, bg="green", height="1000", width="580", font="Helvetica 13",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(root, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(root, font='Helvetica 13 bold', text="SEND", width="12", height=3,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Create the send box to enter message
EntryBox = Text (root, bd=0,fg='Green', bg="white",width="29", height="5", font="Helvetica")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=978,y=15, height=450)
ChatLog.place(x=6,y=6, height=472, width=1000)
EntryBox.place(x=40, y=500, height=80, width=800)
SendButton.place(y= 500, x=841, height=80)

root.mainloop()
