from tkinter import *
import tkinter.messagebox
from tkcalendar import DateEntry
import MiniProject_Backend

class Movie:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Movie Ticket Booking System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="black")

        Movie_Name = StringVar()
        Movie_ID = StringVar()
        Release_Date = StringVar()
        Director = StringVar()
        Cast = StringVar()
        Budget = StringVar()
        Duration = StringVar()
        Rating = StringVar()

        def iExit():
            iExit = tkinter.messagebox.askyesno("Online Movie Ticket Booking System", "Are you sure you want to exit?")
            if iExit > 0:
                root.destroy()

        def clcdata():
            Movie_ID.set("")
            Movie_Name.set("")
            Release_Date.set("")
            Director.set("")
            Cast.set("")
            Budget.set("")
            Duration.set("")
            Rating.set("")

            self.txtMovie_ID.delete(0, END)
            self.txtMovie_Name.delete(0, END)
            self.txtDirector.delete(0, END)
            self.txtCast.delete(0, END)
            self.txtBudget.delete(0, END)
            self.txtDuration.delete(0, END)
            self.txtRating.delete(0, END)
            self.txtRelease_Date.set_date('')

        def adddata():
            if len(Movie_ID.get()) != 0:
                MiniProject_Backend.AddMovieRec(Movie_ID.get(), Movie_Name.get(), self.txtRelease_Date.get(),
                                                Director.get(), Cast.get(), Budget.get(), Duration.get(), Rating.get())
                MovieList.delete(0, END)
                MovieList.insert(END, (Movie_ID.get(), Movie_Name.get(), self.txtRelease_Date.get(),
                                       Director.get(), Cast.get(), Budget.get(), Duration.get(), Rating.get()))

        def disdata():
            MovieList.delete(0, END)
            for row in MiniProject_Backend.ViewMovieData():
                MovieList.insert(END, row, str(""))

        def movierec(event):
            global sd
            searchmovie = MovieList.curselection()[0]
            sd = MovieList.get(searchmovie)
            self.txtMovie_ID.delete(0, END)
            self.txtMovie_ID.insert(END, sd[1])
            self.txtMovie_Name.delete(0, END)
            self.txtMovie_Name.insert(END, sd[2])
            self.txtRelease_Date.set_date(sd[3])
            self.txtDirector.delete(0, END)
            self.txtDirector.insert(END, sd[4])
            self.txtCast.delete(0, END)
            self.txtCast.insert(END, sd[5])
            self.txtBudget.delete(0, END)
            self.txtBudget.insert(END, sd[6])
            self.txtDuration.delete(0, END)
            self.txtDuration.insert(END, sd[7])
            self.txtRating.delete(0, END)
            self.txtRating.insert(END, sd[8])

        def deldata():
            if len(Movie_ID.get()) != 0:
                MiniProject_Backend.DeleteMovieRec(sd[0])
                clcdata()
                disdata()

        def searchdb():
            MovieList.delete(0, END)
            for row in MiniProject_Backend.SearchMovieData(Movie_ID.get(), Movie_Name.get(),
                                                           self.txtRelease_Date.get(), Director.get(),
                                                           Cast.get(), Budget.get(), Duration.get(), Rating.get()):
                MovieList.insert(END, row, str(""))

        def updata():
            if len(Movie_ID.get()) != 0:
                MiniProject_Backend.UpdateMovieData(sd[0], Movie_ID.get(), Movie_Name.get(),
                                                    self.txtRelease_Date.get(), Director.get(), Cast.get(),
                                                    Budget.get(), Duration.get(), Rating.get())
                disdata()

        MainFrame = Frame(self.root, bg="black")
        MainFrame.grid()

        TFrame = Frame(MainFrame, bd=5, padx=54, pady=8, bg="black", relief=RIDGE)
        TFrame.pack(side=TOP)
        self.TFrame = Label(TFrame, font=('Arial', 40, 'bold'), text="ONLINE MOVIE TICKET BOOKING SYSTEM",
                            bg="black", fg="orange")
        self.TFrame.grid()

        BFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
        BFrame.pack(side=BOTTOM)

        DFrame = Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="black", relief=RIDGE)
        DFrame.pack(side=BOTTOM)

        DFrameL = LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="black", relief=RIDGE,
                             font=('Arial', 20, 'bold'), text="Movie Info_", fg="white")
        DFrameL.pack(side=LEFT)

        DFrameR = LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="black", relief=RIDGE,
                             font=('Arial', 20, 'bold'), text="Movie Details_", fg="white")
        DFrameR.pack(side=RIGHT)

        def on_focus_in(entry):
            entry.config(highlightbackground="orange", highlightcolor="orange", highlightthickness=2)

        def on_focus_out(entry):
            entry.config(highlightthickness=0)

        self.txtMovie_ID = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Movie_ID, width=39, bg="black", fg="white")
        self.txtMovie_Name = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Movie_Name, width=39, bg="black", fg="white")
        self.txtRelease_Date = DateEntry(DFrameL, font=('Arial', 18, 'bold'), width=37, background="orange", foreground="black", date_pattern='yyyy-mm-dd')
        self.txtDirector = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Director, width=39, bg="black", fg="white")
        self.txtCast = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Cast, width=39, bg="black", fg="white")
        self.txtBudget = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Budget, width=39, bg="black", fg="white")
        self.txtDuration = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Duration, width=39, bg="black", fg="white")
        self.txtRating = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Rating, width=39, bg="black", fg="white")

        entries = [self.txtMovie_ID, self.txtMovie_Name, self.txtDirector, self.txtCast,
                   self.txtBudget, self.txtDuration, self.txtRating]
        for e in entries:
            e.bind("<FocusIn>", lambda event, entry=e: on_focus_in(entry))
            e.bind("<FocusOut>", lambda event, entry=e: on_focus_out(entry))

        labels = ["Movie ID:", "Movie Name:", "Release Date:", "Director:", "Cast:",
                  "Budget (Crores INR):", "Duration (Hrs):", "Rating (Out of 5):"]
        widgets = [self.txtMovie_ID, self.txtMovie_Name, self.txtRelease_Date, self.txtDirector,
                   self.txtCast, self.txtBudget, self.txtDuration, self.txtRating]
        for i in range(len(labels)):
            Label(DFrameL, font=('Arial', 18, 'bold'), text=labels[i], bg="black", fg="orange").grid(row=i, column=0, sticky=W)
            widgets[i].grid(row=i, column=1)

        sb = Scrollbar(DFrameR)
        sb.grid(row=0, column=1, sticky='ns')
        MovieList = Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'),
                            bg="black", fg="white", yscrollcommand=sb.set)
        MovieList.bind('<<ListboxSelect>>', movierec)
        MovieList.grid(row=0, column=0, padx=8)
        sb.config(command=MovieList.yview)

        buttons = [
            ("Add New", adddata),
            ("Display", disdata),
            ("Clear", clcdata),
            ("Search", searchdb),
            ("Delete", deldata),
            ("Update", updata),
            ("Exit", iExit)
        ]

        for i, (text, cmd) in enumerate(buttons):
            Button(BFrame, text=text, font=('Arial', 20, 'bold'), width=10, height=1, bd=4,
                   bg="orange", command=cmd).grid(row=0, column=i)

if __name__ == '__main__':
    MiniProject_Backend.MovieData()
    root = Tk()
    app = Movie(root)
    root.mainloop()
