#Joseph Taylor
#15/06/17 - Initial commit.
#01/10/17 - Code completed.
#An AI that always wins or draws at 'Naughts and Crosses'.
 
import tkinter as tk
import random as rand
import time
 
whoGoesFirst = rand.randint(0,1)
toggle = rand.randint(0,1)
loopnum = 0
 
window = tk.Tk()                        #Main window now called 'window' as variable name
window.title("Naughts and Crosses")     #Give window a name
window.attributes('-fullscreen',True)   #Make auto-fullscreen
window.configure(background='floral white')
 
window.update()                 #Updating the window refreshes it so changes are visualised. Without this the window will never, visually, change.
height = window.winfo_height()  #Get height of monitor being used.
width = window.winfo_width()    #Get width of monitor being used.
 
framed = round(height / 5)                              ##Making some monitor-specific
gap1 = round(framed / 5)                                ##variables so that the layout
gap2 = round((width - (3*(framed)) - (2*(gap1)))/2)     ##is scaled and works perfectly
gap3 = round((height - (3*(framed)) - (2*(gap1)))/2)    ##on every monitor.
 
def fill(ButNum):           #Function that gets called when buttons are pressed by user.
    global toggle1          #toggle1 tries to be local if this line not included.
    global whoGoesFirst     #whoGoesFirst tries to be local of this line not included.
    if toggle1 == 0 and toggle2 == 0:        #The point of toggle1: Buttons will not do anything when toggle1 is 0
        if ButNum['font'] == ("{Times New Roman} 50"):  #Test if button is empty. Button fonts are only changed to size 50 when nought or cross is placed.
            return                                      #In this case, button isn't empty, so don't try to change it. toggle1 is still 0 so PC cannot play.
        else:                                           #If the button IS empty...
            ButNum['text'] = letter2                    #Change button text to user's symbol, either a nought or a cross due to random generation.
            ButNum['font'] = ("Times New Roman", 50)    #Change font size to 50 so that nought/cross takes up entire button.
            whoGoesFirst = 0                            #Toggling this means the computer can play.
    return                                              #End function
 
def smartPlay():                #Function that gets called on the computers 2nd, 3rd, and all subsequent turns.
    global gridRay              ##These variables
    global gridNo               ##try to be local if these lines
    global whoGoesFirst         ##aren't included.
    array = [0,0,0,0,0,0,0,0,0] #initialising an array of length 9, one for each button.
    for x in range(0,9):                        ##This section of the code essentially
        if gridRay[x]['text'] == '':            ##allocates a number to each button.
            array[x] = 0                        ##Any button that is empty is assigned
        elif gridRay[x]['text'] == letter:      ##the value '0', and button that contains
            array[x] = 1                        ##the symbol the computer is playing is
        elif gridRay[x]['text'] == letter2:     ##assigned the value '1', and any button
            array[x] = 5                        ##that contains the symbol the player is using is assinged the value '5'.
 
    topRow = array[0] + array[1] + array[2]     ##Now we calculate the value
    midRow = array[3] + array[4] + array[5]     ##of each row, column and the
    botRow = array[6] + array[7] + array[8]     ##diagonals based in the above
    leftCol = array[0] + array[3] + array[6]    ##allocations of 0, 1 and 5.
    midCol = array[1] + array[4] + array[7]     ##This allows us to refer to an
    rightCol = array[2] + array[5] + array[8]   ##entire row as being equal to, for
    diag1 = array[0] + array[4] + array[8]      ##examlple, 10, which must mean it
    diag2 = array[2] + array[4] + array[6]      ##contains 2 of the players symbols, and a blank space.
 
    if topRow == 2:                                             ##A very repetitive section of the code.
        for x in range(0,3):                                    ##This part of 'smartPlay' is checking
            if gridRay[x]['text'] == "":                        ##each row, column and diagonal to see
                gridRay[x]['text'] = letter                     ##if any are equal to '2', which would
                gridRay[x]['font'] = ("Times New Roman", 50)    ##represent a blank space, and 2 of the
    elif midRow == 2:                                           ##computer's symbols. If any are equal to
        for x in range(3,6):                                    ##2, the computer can win by then checking
            if gridRay[x]['text'] == "":                        ##each button in that row/column/diagonal to
                gridRay[x]['text'] = letter                     ##see which one is empty, and will play
                gridRay[x]['font'] = ("Times New Roman", 50)    ##in that space.
    elif botRow == 2:
        for x in range(6,9):
            if gridRay[x]['text'] == "":
                gridRay[x]['text'] = letter
                gridRay[x]['font'] = ("Times New Roman", 50)
    elif leftCol == 2:
        for x in range(0,7,3):
            if gridRay[x]['text'] == "":
                gridRay[x]['text'] = letter
                gridRay[x]['font'] = ("Times New Roman", 50)
    elif midCol == 2:
        for x in range(1,8,3):
            if gridRay[x]['text'] == "":
                gridRay[x]['text'] = letter
                gridRay[x]['font'] = ("Times New Roman", 50)
    elif rightCol == 2:
        for x in range(2,9,3):
            if gridRay[x]['text'] == "":
                gridRay[x]['text'] = letter
                gridRay[x]['font'] = ("Times New Roman", 50)
    elif diag1 == 2:
        for x in range(0,9,4):
            if gridRay[x]['text'] == "":
                gridRay[x]['text'] = letter
                gridRay[x]['font'] = ("Times New Roman", 50)
    elif diag2 == 2:
        for x in range(2,7,2):
            if gridRay[x]['text'] == "":
                gridRay[x]['text'] = letter
                gridRay[x]['font'] = ("Times New Roman", 50)
    elif topRow == 10:                                          ##In this section the value chages to 10.
        for x in range(0,3):                                    ##(if topRow == 10, instead of == 2.)
            if gridRay[x]['text'] == "":                        ##At this stage, the computer has checked
                gridRay[x]['text'] = letter                     ##and found that it can't win yet, so it
                gridRay[x]['font'] = ("Times New Roman", 50)    ##now checks to see if the player can win.
    elif midRow == 10:                                          ##If they can, the value of the row/column/
        for x in range(3,6):                                    ##diagonal will be 10, as remember, the player's
            if gridRay[x]['text'] == "":                        ##symbol is represented by a value of 5.
                gridRay[x]['text'] = letter                     ##Once again, if it finds that the player
                gridRay[x]['font'] = ("Times New Roman", 50)    ##can win, it will stop them from winning
    elif botRow == 10:                                          ##by finding the blank space, and playing in
        for x in range(6,9):                                    ##it.
            if gridRay[x]['text'] == "":
                gridRay[x]['text'] = letter
                gridRay[x]['font'] = ("Times New Roman", 50)
    elif leftCol == 10:
        for x in range(0,7,3):
            if gridRay[x]['text'] == "":
                gridRay[x]['text'] = letter
                gridRay[x]['font'] = ("Times New Roman", 50)
    elif midCol == 10:
        for x in range(1,8,3):
            if gridRay[x]['text'] == "":
                gridRay[x]['text'] = letter
                gridRay[x]['font'] = ("Times New Roman", 50)
    elif rightCol == 10:
        for x in range(2,9,3):
            if gridRay[x]['text'] == "":
                gridRay[x]['text'] = letter
                gridRay[x]['font'] = ("Times New Roman", 50)
    elif diag1 == 10:
        for x in range(0,9,4):
            if gridRay[x]['text'] == "":
                gridRay[x]['text'] = letter
                gridRay[x]['font'] = ("Times New Roman", 50)
    elif diag2 == 10:
        for x in range(2,7,2):
            if gridRay[x]['text'] == "":
                gridRay[x]['text'] = letter
                gridRay[x]['font'] = ("Times New Roman", 50)
    elif (gridRay[0]['text'] or gridRay[1]['text'] or gridRay[2]['text'] or gridRay[3]['text'] or gridRay[5]['text'] or gridRay[6]['text'] or gridRay[7]['text'] or gridRay[8]['text']) == letter2 and gridRay[4]['text'] == '':
                gridRay[4]['text'] = letter
                gridRay[4]['font'] = ("Times New Roman", 50)
    elif diag1 == 11 and (topRow == 5 and botRow == 5 and leftCol == 5 and rightCol == 5):      ##This section of code blocks a very specific
        side = True                                                                             ##scenario where the player can win. In the PCs
        while side == True:                                                                     ##Initial turn, if the player goes first and plays
            gridNo = rand.choice([1, 3, 5, 7])                                                  ##anywhere but the middle, the computer will play in
            #Chooses one of the 4 sides to play                                                 ##in the middle. The player can utilise this by playing
            but = gridRay[gridNo]                                                               ##in 2 opposite corners, either side of the middle,
            #'but' is the name of the button currently being changed                            ##to which the computer would play in one of the other
            if but['font'] == ("{Times New Roman} 50"):                                         ##2 corners. This section of code stops the computer
                side = True                                                                     ##playing in the corners in that specific scenario.
            else:
                but['text'] = letter
                but['font'] = ("Times New Roman", 50)
                side = False
    elif diag1 == 11 and (midRow == 5 and midCol == 5 and diag2 == 5):          ##This section of code blocks a very specific
        side = True                                                             ##scenario where the player can win. In the PCs
        while side == True:                                                     ##Initial turn, if the player goes first and plays
            gridNo = rand.choice([0, 2, 6, 8])                                  ##in the middle, the computer will play in
            #Chooses one of the 4 sides to play                                 ##in a random corner. The player can utilise this by playing
            but = gridRay[gridNo]                                               ##in the opposite corner, and the PC would sometimes
            #'but' is the name of the button currently being changed            ##proceed to play on one of the edges. If this happened,
            if but['font'] == ("{Times New Roman} 50"):                         ##the player could win. If the PC played in the corner
                side = True                                                     ##instead, it would end in a draw. This makes it play
            else:                                                               ##in the corner every time.
                but['text'] = letter
                but['font'] = ("Times New Roman", 50)
                side = False
    elif diag2 == 11 and (topRow == 5 and botRow == 5 and leftCol == 5 and rightCol == 5):     
        side = True                                                             
        while side == True:                                                     
            gridNo = rand.choice([1, 3, 5, 7])                                  
            #Chooses one of the 4 sides to play                                 
            but = gridRay[gridNo]                                               
            #'but' is the name of the button currently being changed
            if but['font'] == ("{Times New Roman} 50"):
                side = True
            else:
                but['text'] = letter
                but['font'] = ("Times New Roman", 50)
                side = False
    elif diag2 == 11 and (midRow == 5 and midCol == 5 and diag1 == 5):
        side = True                                                             
        while side == True:                                                     
            gridNo = rand.choice([0, 2, 6, 8])                                  
            #Chooses one of the 4 sides to play                                 
            but = gridRay[gridNo]                                               
            #'but' is the name of the button currently being changed
            if but['font'] == ("{Times New Roman} 50"):
                side = True
            else:
                but['text'] = letter
                but['font'] = ("Times New Roman", 50)
                side = False
    else:                                                                       ##The computer's default move. If the computer doesn't
        y = 0                                                                   ##win, or block the player, and does not detect the
        for x in range(0,9):                                                    ##situation explained in the previous paragraph, it does
            if gridRay[x]['text'] != '':                                        ##this by default: Picks a corner at random, and plays in it.
                y = y + 1                                                       ##If there are no corners to play in, it will detect this, and
        if y == 9:                                                              ##play on the side or in the middle instead.
            return()                                                            ##The for loop at the start of this section is to detect if the
        else:                                                                   ##board is actually already full, so as not get caught in a
            corn = True                                                         ##loop forever. The 'corn' variable means 'corners', as that's
            x1 = 0                                                              ##the default playing position. x1, x2, x3 and x4 are to test
            x2 = 0                                                              ##for if the computer has tried, and failed, to play a corner.
            x3 = 0                                                              ##once all these variables are equal to 1 and not 0, the computer
            x4 = 0                                                              ##will start to try playing in the sides and middle instead. But
            while corn == True:                                                 ##while any of them are still 0, it will keep testing the corners.
                if (x1 == 0 or x2 == 0 or x3 == 0 or x4 == 0):
                    #In other words, if not all of the corners have been tested yet
                    gridNo = rand.choice([0, 2, 6, 8])
                    #Choose one of the 4 corners to play
                    but = gridRay[gridNo]
                    #'but' is the name of the button currently being changed
                    if gridNo == 0:
                        x1 = 1 #Changes if the top left corner has been tested.
                    elif gridNo == 2:
                        x2 = 1 #Changes if the top right corner has been tested.
                    elif gridNo == 6:
                        x3 = 1 #Changes if the bottom left corner has been tested.
                    else:
                        x4 = 1 #Changes if the bottom right corner has been tested.
                else: #If all the corners have been tested, and failed
                    gridNo = rand.choice([1, 3, 4, 5, 7])
                    #Choose anything but one of the 4 corners to play
                    but = gridRay[gridNo]
                    #'but' is the name of the button currently being changed
                if but['font'] == ("{Times New Roman} 50"):
                    corn = True
                    #If the button already has a symbol in it, go round again and generate a different button
                else:
                    but['text'] = letter                    ##Changes the button text to the value the
                    but['font'] = ("Times New Roman", 50)   ##computer is using.
                    corn = False
    whoGoesFirst = 1                ##Here at the very end of the function, whoGoesFirst is set to 1 so that
    toggle1 = 0                     ##the computer can't play twice in a row. This gets set back to 0 after
    return()                        ##the user clicks on any empty button.
 
def hasWon():                       ##Function that tests if all the symbols in a given row, column or diagonal
    global gridRay                  ##are the same. Called once just before the computer plays, and again just
    global Title                    ##after the computer plays.
    global toggle2
    for x in range(0,9,3):
        if (gridRay[x]['text'] == letter and gridRay[x+1]['text'] == letter and gridRay[x+2]['text'] == letter):        ##in this first for loop, x takes on the values
            Title['text'] = ("Computer wins!")                                                                          ##of 0, 3 and 6, which are the numerical equivalent
            Reset['text'] = ("Play again?")                                                                             ##values of the first buttons of each row. Then, the
            toggle1 = 1                                                                                                 ##buttons of value x, x+1 and x+2 (being the 3 buttons
            toggle2 = 1                                                                                                 ##
            return(1)                                                                                                   ##in a given row) will be tested, and if they all match
        elif (gridRay[x]['text'] == letter2 and gridRay[x+1]['text'] == letter2 and gridRay[x+2]['text'] == letter2):   ##then the game will end. Returning a value of 1
            Title['text'] = ("Player wins!")                                                                            ##breaks main program's while loop, and setting
            Reset['text'] = ("Play again?")                                                                             ##toggle1 equal to 1 will stop the user from clicking
            toggle1 = 1                                                                                                 ##any more buttons.
            toggle2 = 1
            return(1)
    for x in range(0,3):
        if (gridRay[x]['text'] == letter and gridRay[x+3]['text'] == letter and gridRay[x+6]['text'] == letter):        ##The maths and methods for these other 2 loops are
            Title['text'] = ("Computer wins!")                                                                          ##very similar and hopefully can be figured out from the
            Reset['text'] = ("Play again?")                                                                             ##context of the first paragraph, some maths skills and
            toggle1 = 1                                                                                                 ##some common sense.
            toggle2 = 1
            return(1)
        elif (gridRay[x]['text'] == letter2 and gridRay[x+3]['text'] == letter2 and gridRay[x+6]['text'] == letter2):
            Title['text'] = ("Player wins!")
            Reset['text'] = ("Play again?")
            toggle1 = 1
            toggle2 = 1
            return(1)
    for x in range(0,3,2):
        if (gridRay[x]['text'] == letter and gridRay[4]['text'] == letter and gridRay[8-x]['text'] == letter):
            Title['text'] = ("Computer wins!")
            Reset['text'] = ("Play again?")
            toggle1 = 1
            toggle2 = 1
            return(1)
        elif (gridRay[x]['text'] == letter2 and gridRay[4]['text'] == letter2 and gridRay[8-x]['text'] == letter2):
            Title['text'] = ("Player wins!")
            Reset['text'] = ("Play again?")
            toggle1 = 1
            toggle2 = 1
            return(1)
    return(0)
 
def reset():
    global gridRay
    global toggle1
    global toggle2
    global whoGoesFirst
    for x in range(0,9):
        gridRay[x]['text'] = ''
        gridRay[x]['font'] = ("{Times New Roman} 15")
        Title['text'] = "Naughts and Crosses"
        Reset['text'] = "Reset"
        whoGoesFirst = rand.randint(0,1)
        if whoGoesFirst == 1:
            toggle1 = 0
            toggle2 = 0
 
def quitGame():
    window.destroy()
    exit()
     
         
f = tk.Frame(window, height=framed, width=framed)   #Create a frame to put a button in
f.pack_propagate(0)                                 #The frame will try to fit to the smallest space possible, unless this line is involved.
f.grid(row=1, column=1, padx=(gap2,0), pady=(0,0))  #Position in the grid. First row, first column, for this is button number 1.
 
f2 = tk.Frame(window, height=framed, width=framed)
f2.pack_propagate(0) 
f2.grid(row=1, column=2, padx=(gap1,0), pady=(0,0))
 
f3 = tk.Frame(window, height=framed, width=framed)
f3.pack_propagate(0) 
f3.grid(row=1, column=3, padx=(gap1,0), pady=(0,0))
 
f4 = tk.Frame(window, height=framed, width=framed) 
f4.pack_propagate(0) 
f4.grid(row=2, column=1, padx=(gap2,0), pady=(gap1,0))
 
f5 = tk.Frame(window, height=framed, width=framed) 
f5.pack_propagate(0) 
f5.grid(row=2, column=2, padx=(gap1,0), pady=(gap1,0))
 
f6 = tk.Frame(window, height=framed, width=framed) 
f6.pack_propagate(0) 
f6.grid(row=2, column=3, padx=(gap1,0), pady=(gap1,0))
 
f7 = tk.Frame(window, height=framed, width=framed) 
f7.pack_propagate(0) 
f7.grid(row=3, column=1, padx=(gap2,0), pady=(gap1,0))
 
f8 = tk.Frame(window, height=framed, width=framed)
f8.pack_propagate(0)
f8.grid(row=3, column=2, padx=(gap1,0), pady=(gap1,0))
 
f9 = tk.Frame(window, height=framed, width=framed)
f9.pack_propagate(0)
f9.grid(row=3, column=3, padx=(gap1,0), pady=(gap1,0))
 
fTitle = tk.Frame(window, height=(gap3), width=(gap3 + gap1))           ##Those monitor-specific variables initialised at the start of
fTitle.pack_propagate(0)                                                ##the program are used for determining the height, width and
fTitle.grid(row=0, column=2, columnspan=1, padx=(gap1,0), pady=(0,0))   ##padding on the buttons. This is one of the more complicated
                                                                        ##buttons.
fReset = tk.Frame(window, height=(gap3 - (2*gap1)), width=(gap3 - gap1))
fReset.pack_propagate(0)
fReset.grid(row=4, column=1, columnspan=1, padx=(gap2,0), pady=(gap1,0))
 
fQuit = tk.Frame(window, height=(gap3 - (2*gap1)), width=(gap3 - gap1))
fQuit.pack_propagate(0)
fQuit.grid(row=4, column=3, columnspan=1, padx=(gap1,0), pady=(gap1,0))
 
Grid1 = tk.Button(f, command=lambda: fill(Grid1), bg='light cyan')  #Create a plain, blank button and place it in the specified frame (in this case, frame 'f')
Grid1.pack(fill=tk.BOTH, expand=1)                              #This line means the button fills the whole of the space of the frame it is in.
 
Grid2 = tk.Button(f2, command=lambda: fill(Grid2), bg='light cyan')     ##Command=lambda: fill(Grid2) means that when the button is pressed, call a function, and that
Grid2.pack(fill=tk.BOTH, expand=1)                                      ##function is 'fill' from the top of the document. Each button passes itself into the function.
 
Grid3 = tk.Button(f3, command=lambda: fill(Grid3), bg='light cyan') 
Grid3.pack(fill=tk.BOTH, expand=1)  
 
Grid4 = tk.Button(f4, command=lambda: fill(Grid4), bg='light cyan')  
Grid4.pack(fill=tk.BOTH, expand=1) 
 
Grid5 = tk.Button(f5, command=lambda: fill(Grid5), bg='light cyan') 
Grid5.pack(fill=tk.BOTH, expand=1) 
 
Grid6 = tk.Button(f6, command=lambda: fill(Grid6), bg='light cyan')  
Grid6.pack(fill=tk.BOTH, expand=1) 
 
Grid7 = tk.Button(f7, command=lambda: fill(Grid7), bg='light cyan')  
Grid7.pack(fill=tk.BOTH, expand=1)  
 
Grid8 = tk.Button(f8, command=lambda: fill(Grid8), bg='light cyan')  
Grid8.pack(fill=tk.BOTH, expand=1)  
 
Grid9 = tk.Button(f9, command=lambda: fill(Grid9), bg='light cyan')
Grid9.pack(fill=tk.BOTH, expand=1)
 
Title = tk.Label(fTitle, text="Naughts and Crosses", font=("Times new roman", 15),bg='floral white')        ##The title and reset buttons some unique feature like text and font
Title.pack(fill=tk.BOTH, expand=1)                                                                          ##size, and the lack of a command, so that clicking the title does
                                                                                                            ##nothing, as intended.
Reset = tk.Button(fReset, command=lambda: reset(), text="Reset", font=("Times new roman", 15), bg='light goldenrod')
Reset.pack(fill=tk.BOTH, expand=1)
 
Quit = tk.Button(fQuit, command=lambda: quitGame(), text="Quit", font=("Times new roman", 15), bg='light goldenrod')
Quit.pack(fill=tk.BOTH, expand=1)
 
if toggle == 1:         ##Random generation.
    letter = 'X'        ##The user can be
    letter2 = 'O'       ##noughts or crosses,
else:                   ##as with the computer,
    letter = 'O'        ##and it's random as
    letter2 = 'X'       ##to which thakes the
                        ##first go.
if whoGoesFirst == 0:
    toggle1 = 1
else:
    toggle1 = 0
 
toggle2 = 0
 
while True:
    #Play the game until the loop is broken (which will happen when the computer detects either a winner or a draw)
    while True:
        gridRay = [Grid1, Grid2, Grid3, Grid4, Grid5, Grid6, Grid7, Grid8, Grid9]
        #Array can be referenced to refer to any button
        gridNo = 0
        #Initialising Array index
        window.update()
        #Window must be updated every loop
        time.sleep(0.05)
        #Creating a small delay
 
        breakOrNot = hasWon()
        if breakOrNot == 1:
            break
 
        if whoGoesFirst == 0 and toggle2 == 0:
            loopnum = loopnum + 1
            #Determines how many times this part of the code has been executed
            if loopnum == 1:
                if (gridRay[0]['text'] or gridRay[1]['text'] or gridRay[2]['text'] or gridRay[3]['text'] or gridRay[5]['text'] or gridRay[6]['text'] or gridRay[7]['text'] or gridRay[8]['text']) == letter2:
                    gridRay[4]['text'] = letter
                    gridRay[4]['font'] = ("Times New Roman", 50)
                    whoGoesFirst = 1
                    toggle1 = 0
                else:
                    gridNo = rand.choice([0, 2, 6, 8])
                    #Chooses one of the 4 corners as first play
                    but = gridRay[gridNo]
                    #'but' is the name of the button currently being changed
                    if but['font'] == ("{Times New Roman} 50"):
                        whoGoesFirst = 0
                        #Loop again if space is taken already, and play in a different corner
                    else:
                        but['text'] = letter
                        but['font'] = ("Times New Roman", 50)
                        whoGoesFirst = 1
                        toggle1 = 0
            elif loopnum >= 1:
                smartPlay()
 
        breakOrNot = hasWon()
        if breakOrNot == 1:
            break
                   
        y = 0
        for x in range(0,9):
            if gridRay[x]['text'] != '':
                y = y + 1
            if y == 9:
                Title['text'] = ("Draw!")
                Reset['text'] = ("Play again?")
                break
 
window.mainloop()