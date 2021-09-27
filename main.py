from tkinter import Tk, Label, Frame, LabelFrame, Button, PhotoImage,Message, messagebox, Grid, Entry, StringVar, Canvas
import math

class Base():
    def __init__(self):

        self.frames = {}    # Dictionary to hold the frames that we are going to show

    def load_frames(self, *args):
        for F in args:

            frame = F(self) # Create objects from the classes listed above in the F loop

            self.frames[F] = frame # Save the created objects to our dictionary

            frame.grid(row=0, column=0, sticky="nsew")  # Load the frame objects into a grid stacking them on top of each other
            #frame.pack(expand=True, fill='both')
    def show_frame(self, frame_to_show):
        """ 
            Receives a class and look for it in our frames dictionary,
            if we found it then show it as the top screen

            Parameters
            ----------
            frame_to_show: Class type that we want to show 
        """
        frame = self.frames[frame_to_show]  # Look for the class in our dictionary
        self.current_frame = frame  # Set the frame as our current frame variable
        frame.tkraise() # Raise the frame to the top

class App(Base,Tk):
    """
        A class that inherits from the main tkinter class
        and some functions from the Base class
        It is the top object that holds the whole interface
        ...

        Attributes
        ----------
        None
        
        Methods
        -------
        None
    """

    def __init__(self, *args, **kwargs):
        """ 
            Parameters
            ---------
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        Base.__init__(self)
        Tk.__init__(self, *args, **kwargs) # Inherit from the main tkinter class
        

        # Set the weight to 0
        Grid.rowconfigure(self, 0, weight=1)     
        Grid.columnconfigure(self, 0, weight=1)

        self.title("Connect 4")
        #self.attributes("-fullscreen", True) # For final build this should be ativated
        self.geometry('852x516') # Size of screen
        
        
        
        #self.photo_logo = PhotoImage(file= "Jogbox Tester\icons\its-logo-short.png").subsample(10,10)
        #self.iconphoto(True, self.photo_logo)   # Icon that shows on the left corner of the screen

        self.load_frames(StartPage, Game, EasterEgg)

        self.show_frame(EasterEgg)  # Frame object to show at the top screen


class StartPage(Frame):
    """
        A class that holds the start - main page of the interface
        It inherits from the Frame class of tkinter
        ...

        Attributes
        ----------
        parent : tk class 
            object that is to hold the StartPage object
        
        Methods
        -------
        None
    """

    def __init__(self, parent):
        """
            Parameters
            ----------
            parent : tk class 
                object that is to hold the StartPage object
        """
        
        Frame.__init__(self, parent,bg="#e6e600")

        self.parent = parent

       
        #self.container = Frame(self,bg="gray",padx=135)
        #self.container.pack()

        self.title = Label(self, text="CONNECT 4",borderwidth=2,bg="#e6e600",fg="red",font=("Robot", 55,"bold"))
        self.title.pack(fill='x',expand=True)

        self.container_players = Frame(self,bg="#e6e600")
        self.container_players.pack()

        self.text_temp_1 = StringVar()
        Label(self.container_players, text="P1:",borderwidth=2,bg="#e6e600",fg="black",font=("Robot", 25,"bold")).grid(row=0, column=0,padx=10)
        self.player_1 = Entry(self.container_players,relief='flat',bg="#ffff33",fg="black",font=("Robot", 25,"bold"),textvariable=self.text_temp_1)
        self.player_1.grid(row=0, column=1)
        self.player_1.bind("<KeyRelease>", self.caps)

        self.text_temp_2 = StringVar()
        Label(self.container_players, text="P2:",borderwidth=2,bg="#e6e600",fg="black",font=("Robot", 25,"bold")).grid(row=1, column=0,padx=10)
        self.player_2 = Entry(self.container_players,relief='flat',bg="#ffff33",fg="black",font=("Robot", 25,"bold"),textvariable=self.text_temp_2)
        self.player_2.grid(row=1, column=1)
        self.player_2.bind("<KeyRelease>", self.caps)

        self.naming_note = Label(self.container_players, text="Please use less than 10 digits",borderwidth=2,bg="#e6e600",fg="#e6e600",font=("Robot", 15,"bold"))
        self.naming_note.grid(row=2, column=0,columnspan=2,padx=10)

       
        #self.photo_123 = PhotoImage(file= "Jogbox Tester\icons\ico_123.png").subsample(2,2)
        self.btn_start = Button(self,text= "START",bg="red", fg = "white", font = ("Robot",30,"bold"),
                        command=lambda: [self.parent.show_frame(Game),self.parent.frames[Game].set_players(self.player_1.get(),self.player_2.get())])
        self.btn_start.pack(fill='none',expand=True)

    def caps(self, event):
        self.text_temp_1.set(self.text_temp_1.get().upper())
        self.text_temp_2.set(self.text_temp_2.get().upper())
        
        if len(self.text_temp_1.get()) > 10 or len(self.text_temp_2.get()) > 10:
            self.text_temp_1.set(self.text_temp_1.get()[:10])
            self.text_temp_2.set(self.text_temp_2.get()[:10])
            self.naming_note['fg']= 'red'
        else:
            self.naming_note['fg']= '#e6e600'


class EasterEgg(Frame):
    """
        A class that holds the start - main page of the interface
        It inherits from the Frame class of tkinter
        ...

        Attributes
        ----------
        parent : tk class 
            object that is to hold the StartPage object
        
        Methods
        -------
        None
    """

    def __init__(self, parent):
        """
            Parameters
            ----------
            parent : tk class 
                object that is to hold the StartPage object
        """
        
        Frame.__init__(self, parent,bg="#e6e600")

        self.parent = parent

        Label(self, text="Developed by Alwurts",borderwidth=2,fg="black",font=("Robot", 25,"bold")).grid(row=0, column=0)

        self.canvas = Canvas(self,width=852, height=516, bg='white')

        # pack the canvas into a frame/form
        self.canvas.grid(row=0,column=0)

        # load the .gif image file
        self.logo = PhotoImage(file='logo-large.png').subsample(2)

        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        self.logo_canvas = self.canvas.create_image(1, 10, image=self.logo, anchor='nw')

        #self.canvas.move(self.logo_canvas, 100, 0)
        

        #print(self.canvas.coords(self.logo_canvas))
        self.heading = 45

        #self.holder_move_loop = self.parent.after(1000, self.move_loop)

        self.container_text = Frame(self,bg='black',padx=30,pady=30)
        self.container_text.grid(row=0,column=0)
        Label(self.container_text, text="Developed by Alwurts",borderwidth=2,bg='black',fg="white",font=("Robot", 25,"bold")).pack()
        Label(self.container_text, text="alejandrowurts.com",borderwidth=2,bg='black',fg="white",font=("Robot", 25,"bold")).pack()

        self.btn_goback = Button(self.container_text,text= "GO BACK",bg="black", fg = "white",relief='flat', font = ("Robot",15,"bold"),pady=10,
                        command=lambda: [self.parent.show_frame(StartPage),self.parent.after_cancel(self.holder_move_loop)])
        self.btn_goback.pack(expand=True)


    def move_loop(self):
        print("moving")
        x,y = self.canvas.coords(self.logo_canvas)

        move = 8
        angle = math.radians(self.heading)

        move_x =int( move * math.cos(angle))
        move_y =int( move * math.sin(angle))

        self.canvas.move(self.logo_canvas, move_x, move_y)

        self.holder_move_loop = self.parent.after(10, self.move_loop)

        x,y = self.canvas.coords(self.logo_canvas)
        #print(x,y)

        if x >= 700 or x <= -60 or y >= 380 or y <= -70:
            self.heading=self.heading + 270
            


    

class Game(Frame):
    """
        A class that holds the start - main page of the interface
        It inherits from the Frame class of tkinter
        ...

        Attributes
        ----------
        parent : tk class 
            object that is to hold the StartPage object
        
        Methods
        -------
        None
    """

    def __init__(self, parent):
        """
            Parameters
            ----------
            parent : tk class 
                object that is to hold the StartPage object
        """
        
        Frame.__init__(self, parent,bg="#e6e600")

        self.parent = parent

        self.turn = 1 # 1 : Player one, 2 : Player two

        self.container = Frame(self)
        self.container.pack(side='left')

        #self.photo_square_empty = PhotoImage(file= "square_empty.png")
        self.square_list = []
        for column in range(7):
            temp_list = []
            for row in range(6):
                temp_object = Square(self.container, self, column, row)
                #self.title.image = self.photo_square_empty
                #temp_object.grid(column= column, row= row)
                temp_list.append(temp_object)
            
            self.square_list.append(temp_list)

        self.container_actions = Frame(self,bg="#e6e600")
        self.container_actions.pack(side='left', expand=True)

        self.lbl_player_1 = Label(self.container_actions, text="",borderwidth=2,bg="#e6e600",fg="black",font=("Robot", 25,"bold"))
        self.lbl_player_1.grid(row=0, column=0)
        Label(self.container_actions, text="vs",borderwidth=2,bg="#e6e600",fg="black",font=("Robot", 25,"bold")).grid(row=1, column=0)
        self.lbl_player_2 = Label(self.container_actions, text="",borderwidth=2,bg="#e6e600",fg="black",font=("Robot", 25,"bold"))
        self.lbl_player_2.grid(row=2, column=0)

        self.lbl_player_turn = SquareLarge(self.container_actions,self,0,3)

        self.btn_reset = Button(self.container_actions,text= "RESET",bg="red", fg = "white", font = ("Robot",20,"bold"),
                        command=lambda: self.clear_all())
        self.btn_reset.grid(row= 4, column=0)

        self.btn_back = Button(self.container_actions,text= "EXIT",bg="red", fg = "white", font = ("Robot",20,"bold"),
                        command=lambda: [self.parent.show_frame(StartPage),self.clear_all()])
        self.btn_back.grid(row= 5, column=0)

    def set_players (self,name_1, name_2):
        #print(name_1 + name_2)
        self.player_1 = name_1
        self.lbl_player_1['text']= name_1

        self.player_2 = name_2
        self.lbl_player_2['text']= name_2

    def get_turn(self):
        return self.turn

    def set_turn(self,turn):
        self.turn = turn
        if turn == 1: self.lbl_player_turn.set_player_1()
        if turn == 2: self.lbl_player_turn.set_player_2()

    def clear_all (self):
        for column in self.square_list:
            for square in column:
                square.set_white()
        self.lbl_player_turn.set_player_1()

        self.turn = 1

    def which_column (self,incoming_square):
        for square in reversed(self.square_list[incoming_square.column]):
            if square.get_status() == 0:
                square.activate()
                self.check_win(square)
                #print(square)
                break

    def check_win (self,square):
    
        turn = square.get_status()
        column, row = square.get_coordinates()

        print("column: ", end="")
        print(column)
        print("row: ", end="")
        print(row)

        # Check vertical down
        count = 1
        for i in range(1,6-row):
            if self.square_list[column][row + i].get_status() == turn:
                count += 1
                #print ("it match")
            else:
                break
        if count >= 4:
            print("WIN!!!!!!!!  Player: ", end="")
            print(turn)
            messagebox.showinfo("WIN", "Player " + str(turn) + " WINS!!!!!!") 
            self.clear_all()

        # Check horizontal to the right
        count = 1
        for i in range(1,7-column):
            if self.square_list[column + i][row].get_status() == turn:
                count += 1
                #print ("it match")
            else:
                break
        if count >= 4:
            print("WIN!!!!!!!!  Player: ", end="")
            print(turn)
            messagebox.showinfo("WIN", "Player " + str(turn) + " WINS!!!!!!") 
            self.clear_all()

        # Check horizontal to the left
        count = 1
        for i in range(1,column+1):
            
            if self.square_list[column - i][row].get_status() == turn:
                count += 1
                #print ("it match")
            else:
                break
        if count >= 4:
            print("WIN left!!!!!!!!  Player: ", end="")
            print(turn)
            messagebox.showinfo("WIN", "Player " + str(turn) + " WINS!!!!!!") 
            self.clear_all()

        # Check vertical down right
        count = 1
        for i,j in zip(range(1,6-row), range(1,7-column)):
            #print(i, end=" ")
            #print(j)
            if self.square_list[column + j][row + i].get_status() == turn:
                count += 1
                #print ("it match")
            else:
                break
        if count >= 4:
            print("WIN down right!!!!!!!!  Player: ", end="")
            print(turn)
            messagebox.showinfo("WIN", "Player " + str(turn) + " WINS!!!!!!") 
            self.clear_all()

        
        # Check vertical down left
        count = 1
        for i,j in zip(range(1,6-row), range(1,column+1)):
            
            #print(i, end=" ")
            #print(j)
            if self.square_list[column - j][row + i].get_status() == turn:
                count += 1
                #print ("it match")
            else:
                break
        if count >= 4:
            print("WIN down left!!!!!!!!  Player: ", end="")
            print(turn)
            messagebox.showinfo("WIN", "Player " + str(turn) + " WINS!!!!!!") 
            self.clear_all()

        
        # Check vertical up right
        count = 1
        for i,j in zip(range(1,row + 1), range(1,7-column)):
            
            #print(i, end=" ")
            #print(j)
            if self.square_list[column + j][row - i].get_status() == turn:
                count += 1
                #print ("it match")
            else:
                break
        if count >= 4:
            print("WIN!!!!!!!!  Player: ", end="")
            print(turn)
            messagebox.showinfo("WIN", "Player " + str(turn) + " WINS!!!!!!") 
            self.clear_all()
        

        # Check vertical up left
        count = 1
        for i,j in zip(range(1,row + 1), range(1,column + 1)):
            #print(i, end=" ")
            #print(j)
            if self.square_list[column - j][row - i].get_status() == turn:
                count += 1
                #print ("it match")
            else:
                break
        if count >= 4:
            print("WIN!!!!!!!!  Player: ", end="")
            print(turn)
            messagebox.showinfo("WIN", "Player " + str(turn) + " WINS!!!!!!") 
            self.clear_all()
   

        
        


       
class Square(Button):

    # Class Variable
    #photo_square_empty = PhotoImage(file= "square_empty.png")

    def __init__(self, parent_container, parent_game,column,row):

        self.parent_game = parent_game
        self.column = column
        self.row = row

        self.photo_square_empty = PhotoImage(file= "square_empty.png")
        
        Button.__init__(self, parent_container, image= self.photo_square_empty,borderwidth=0, relief='flat',overrelief='flat',takefocus="off",width=84,height=84,
                        command=lambda: self.parent_game.which_column(self))
        self.image = self.photo_square_empty
        self.grid(row=row,column=column)

        self.set_white()

    def activate (self):
        if self.status == 0:

            if self.parent_game.get_turn() == 1:
                self.set_p1()
                self.parent_game.set_turn(2)
            elif self.parent_game.get_turn() == 2:
                self.set_p2()
                self.parent_game.set_turn(1)

    def get_status(self):
        return self.status

    def get_coordinates(self):
        return self.column, self.row

    def set_white (self):
        self.status = 0
        self['bg'] = 'white'
    
    def set_p1 (self):
        self.status = 1
        self['bg'] = 'red'

    def set_p2 (self):
        self.status = 2
        self['bg'] = 'blue'


class SquareLarge(Label):

    # Class Variable
    #photo_square_empty = PhotoImage(file= "square_empty.png")

    def __init__(self, parent_container, parent_game,column,row):

        self.parent_game = parent_game
        

        self.photo_square_empty = PhotoImage(file= "square_empty_large.png")
        
        Label.__init__(self, parent_container, image= self.photo_square_empty,fg='white',font = ("Robot",30,"bold"),borderwidth=0,height=118,width=118, relief='flat',takefocus="off",compound='center')
        self.image = self.photo_square_empty
        self.grid(row=row,column=column)

        self.set_player_1()

    def set_player_1(self):
        self['bg']= 'red'
        self['text'] = 'P1'

    def set_player_2(self):
        self['bg']= 'blue'
        self['text'] = 'P2'



if __name__ == "__main__":
    app = App()
    
    app.mainloop()
