import tkinter as tk

def getboard(arr):
    
    window = tk.Tk()
    for i in range(9):
        for j in range(9):
            #if (i)%3==0: padyvar = 300
            #else: padyvar=100
            #if (j)%3==0: padxvar = 300
            #else: padxvar=100
            frame = tk.Frame(
                bg="white",
                master=window,
                #relief=tk.RAISED,
                borderwidth=2
            )
            frame.grid(row=i, column=j, padx=5, pady=5)
            label = tk.Label(master=frame, text=arr[i,j])
            #label.place(relx=padyvar, rely=padxvar)
            label.pack()

    window.mainloop()
