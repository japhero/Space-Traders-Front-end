import customtkinter as ck

app = ck.CTk()
app.geometry("800x800")

app.rowconfigure([0, 1, 2, 3], minsize=25)
app.columnconfigure([0, 1, 2], minsize=100)

scrollable_frame = ck.CTkScrollableFrame(app, label_text="CTkScrollableFrame")
scrollable_frame.grid(row=1, column=8, padx=(20, 0), pady=(20, 0), sticky="nsew")
scrollable_frame_switches = []
for i in range(10):
    switch = ck.CTkSwitch(master=scrollable_frame, text=f"active")

    label = ck.CTkLabel(scrollable_frame, text=f"shipNum: {i + 1}", )

    label.grid(row=i, column=0, padx=10, pady=(0, 20))
    switch.grid(row=i, column=4, padx=10, pady=(0, 20))

app.mainloop()
