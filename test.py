from customtkinter import *
from outdated_files.start import start
from outdated_files.stop import stop
from outdated_files.reload import reload

root = CTk()
root.geometry("500x500")
root.configure(fg_color="grey30")

for i in range(3):root.rowconfigure(weight=i, index=3)
for r in range(3):root.columnconfigure(weight=r, index=3)

start_btn = CTkButton(root, text="START", fg_color="#276d30", text_color="#C5C2C2", command=start)
start_btn.grid(row=3, column=0)

stop_btn = CTkButton(root, text="STOP", fg_color="#ac1616", text_color="#C5C2C2", command=stop)
stop_btn.grid(row=3, column=1)

reload_btn = CTkButton(root, text="RELOAD", fg_color="#bdb21d", text_color="#C5C2C2", command=reload)
reload_btn.grid(row=3, column=2)


root.mainloop()