# Description: Code that helps you take a break by reminding you to set aside
#              time after 1 hour for some light fun. Simple Python
# Author     : Harikrishnan G Nair
# Copyright New York University. All rights reserved

import time
import webbrowser
import Tkinter as tk
import tkMessageBox


#Dialogue box to show the "Take a break" message
def callback():
	root = tk.Tk()
	root.withdraw()
	root.update()
	tkMessageBox.showinfo('Break Time', 'Time for a short break')
	root.update()
	return

#main function
def main():
	total_breaks = 3
	break_count = 0
	print("This program started on "+time.ctime()); #display current time
	while(break_count < total_breaks):
	    #webbrowser.open("https://www.youtube.com/watch?v=_dK2tDK9grQ") #open browser and play "Shape of You"
	    callback()
	    time.sleep(6)
	    break_count += 1

if __name__ == "__main__":
    main()
