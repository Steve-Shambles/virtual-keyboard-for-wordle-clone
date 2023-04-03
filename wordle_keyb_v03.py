""" Wordle keyboard by Steve Shambles, April 2023.
    I wrote this for a Wordle clone I'm
    going to write soon. The '*' button is
    for delete and '=' for enter."""

import tkinter as tk

c_font = ('calibri', 10, 'bold')
bg_col = 'steelblue'

root = tk.Tk()
root.title("Wordle Keyboard")
root.configure(bg=bg_col)


def key_pressed(event):
    """ Detect when a button on the virtual keyboard is clicked
        and store the letter of the pressed key in string 'clicked_key'. """
    clicked_key = event.widget['text']
    print(clicked_key)


# Create main keyboard frame.
keyb_frame = tk.Frame(root, bg=bg_col)
keyb_frame.pack(padx=10, pady=10)

# Create QWERTYUIOP top row.
qwerty_frame = tk.Frame(keyb_frame, bg=bg_col)
qwerty_frame.grid(row=0, column=0, columnspan=10, padx=2, pady=2)

# Populate buttons with letters.
for i, char in enumerate("QWERTYUIOP"):
    qwerty_btn = tk.Button(qwerty_frame, font=c_font,
                           text=char, width=5, height=2)
    qwerty_btn.bind('<Button-1>', key_pressed)
    qwerty_btn.grid(row=0, column=i, padx=2, pady=2)

# Create ASDFGHJKL second row.
asd_frame = tk.Frame(keyb_frame, bg=bg_col)
asd_frame.grid(row=1, column=0, columnspan=10, padx=2, pady=2)

# Populate buttons with letters.
for i, char in enumerate("ASDFGHJKL"):
    asd_btn = tk.Button(asd_frame, font=c_font,
                        text=char, width=5, height=2)
    asd_btn.bind('<Button-1>', key_pressed)
    asd_btn.grid(row=0, column=i, padx=2, pady=2)

# Create ZXCVBNM third row.
zxc_frame = tk.Frame(keyb_frame, bg=bg_col)
zxc_left = tk.Frame(zxc_frame, bg=bg_col)
zxc_right = tk.Frame(zxc_frame, bg=bg_col)

# Add "*" button to the left frame, represents delete key.
star_btn = tk.Button(zxc_left, font=c_font, text="*",
                     width=5, height=2, bg='indianred')
star_btn.bind('<Button-1>', key_pressed)
star_btn.pack(side=tk.LEFT, padx=2, pady=2)

for i, char in enumerate("ZXCVBNM"):
    zxc_btn = tk.Button(zxc_right, font=c_font, text=char, width=5, height=2)
    zxc_btn.bind('<Button-1>', key_pressed)
    zxc_btn.pack(side=tk.LEFT, padx=2, pady=2)

# Add "=" button to the right frame, represents the enter button.
button_enter = tk.Button(zxc_right, font=c_font, text="=",
                         width=5, height=2, bg='lightgreen')
button_enter.bind('<Button-1>', key_pressed)
button_enter.pack(side=tk.RIGHT, padx=2, pady=2)

# Add both frames to the main frame
zxc_left.pack(side=tk.LEFT)
zxc_right.pack(side=tk.LEFT)
zxc_frame.grid(row=2, column=0, columnspan=10, padx=2, pady=2)


root.mainloop()
