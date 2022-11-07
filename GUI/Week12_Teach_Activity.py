import tkinter as tk
import number_entry as nent

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    main_frame = tk.Frame(root)
    main_frame.master.title("Heart Rate")
    main_frame.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(main_frame)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


def populate_main_window(main_frame):

    """Create a label that displays the 'Age' """
    label_age = tk.Label(main_frame, text = "Age:")

    """Create an integer entry box where the user will enter her age"""
    enter_age = nent.IntEntry(main_frame, 12, 90, width=5)

    """Create a label that displays rates"""
    label_rate = tk.Label(main_frame, text= "Rates:")

    """Create labels that will display the results"""
    label_slow = tk.Label(main_frame, width= 4)
    label_fast = tk.Label(main_frame, width= 4)

    """Create a clear button"""
    btn_clear = tk.Button(main_frame, text= "Clear")

    """layout all the labels, entry boxes, and buttons in a grid"""
    label_age.grid(row=0, column=0, padx=3, pady=3)
    enter_age.grid(row=0, column=1, padx=3, pady=3)
    label_rate.grid(row=0, column=2, padx=(30,3), pady=3)
    label_slow.grid(row=0, column=3, padx=3, pady=3)
    label_fast.grid(row=0, column=4, padx=3, pady=3)
    btn_clear.grid(row=1, column=3, padx=3, pady=3, columnspan=5, sticky="w")

    def calculate(event):
        """Compute and display the user's slowest 
        and fastest beneficial heart rates."""
        try:
            #Get the user's age.
            age = enter_age.get()

            #Compute the user's maximum heart rate.
            max_rate = 220 - age

            #compute the user's slowest and 
            #fastest beneficial heart rate
            slow = max_rate * 0.65
            fast = max_rate * 0.85

            #Display the slowest and fastest beneficial 
            #heart rates for the user to see.
            label_slow.config(text = f"{slow: .0f}")
            label_fast.config(text = f"{fast:.0f}")

        except ValueError:
            #When the user deletes all the digits in the age
            #entry box, clear the slowest and fastest labels.
            label_slow.config(text="")
            label_fast.config(text="")


        """This function will be called each time
        the user presses the clear button"""
    def clear():
        #Clear all the inputs and outputs
        enter_age.delete(0, tk.END)
        label_slow.config(text="")
        label_fast.config(text="")
        enter_age.focus()

        #Bind the calculate fucntion to the age entry box
        #so that the calculate function will be called when
        #the user changes the text in the entry box.
        enter_age.bind("<KeyRelease>", calculate)


        #Bind the clear function to the clear button so
        #that the clear function will be called when the 
        #user clicks the clear button.
        btn_clear.config(command=clear)

        #Give the keybaord focus to the age entry box
        enter_age.focus()

if __name__ == "__main__":
    main()

