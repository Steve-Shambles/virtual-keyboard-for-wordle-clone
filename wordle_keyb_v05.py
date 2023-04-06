""" virtual keyboard V0.5 Steve Shambles april 2023
    for a Wordle game, or something similar.

    V0.5: better colours, mostly non-hard-coded,
    used grid for all geom managers, previously used
    pack and grid but it started to get confusing.

requirements: None

todo:
Make buttons look better.
"""
import tkinter as tk

c_font = ('calibri', 10, 'bold')
bg_col = 'darkcyan'

root = tk.Tk()
root.title("Virtual Keyboard V0.5")
root.configure(bg=bg_col)


def key_pressed(event):
    """ Detect when a button on the virtual keyboard is clicked
        and store the letter of the pressed key in string 'clicked_key'. """
    clicked_key = event.widget['text']
    print(clicked_key)

# keys colours
kb_bg_col='black'
kb_fg_col='white'

# Create the main keyboard frame.
keyb_frame = tk.Frame(root, bg=bg_col)
keyb_frame.grid(row=0, column=0, padx=10, pady=10)

# Create QWERTYUIOP top row frame.
qwerty_frame = tk.Frame(keyb_frame, bg=bg_col)
qwerty_frame.grid(row=0, column=0, columnspan=10, padx=2, pady=2)

# Populate buttons with letters.
for i, char in enumerate("QWERTYUIOP"):
    qwerty_btn = tk.Button(qwerty_frame, font=c_font,
                           text=char, width=5, height=2,
                           bg=kb_bg_col, fg=kb_fg_col)
    qwerty_btn.bind('<Button-1>', key_pressed)
    qwerty_btn.grid(row=0, column=i, padx=2, pady=2)

# Create ASDFGHJKL second row.
asd_frame = tk.Frame(keyb_frame, bg=bg_col)
asd_frame.grid(row=1, column=0, columnspan=10, padx=2, pady=2)

# Populate buttons with letters.
for i, char in enumerate("ASDFGHJKL"):
    asd_btn = tk.Button(asd_frame, font=c_font,
                        text=char, width=5, height=2,
                        bg=kb_bg_col, fg=kb_fg_col)
    asd_btn.bind('<Button-1>', key_pressed)
    asd_btn.grid(row=0, column=i, padx=2, pady=2)

# Create ZXCVBNM third row.
zxc_frame = tk.Frame(keyb_frame, bg=bg_col)
zxc_frame.grid(row=2, column=0, columnspan=10, padx=2, pady=2)

zxc_left = tk.Frame(zxc_frame, bg=bg_col)
zxc_left.grid(row=0, column=0, padx=2, pady=2)

zxc_right = tk.Frame(zxc_frame, bg=bg_col)
zxc_right.grid(row=0, column=1, columnspan=9, padx=2, pady=2)

# Add "*" button to the left frame, represents delete key.
star_btn = tk.Button(zxc_left, font=c_font, text="Del",
                     fg=kb_fg_col, width=5, height=2,
                     bg='indianred')
star_btn.bind('<Button-1>', key_pressed)
star_btn.grid(row=0, column=0, padx=2, pady=2)

for i, char in enumerate("ZXCVBNM"):
    zxc_btn = tk.Button(zxc_right, font=c_font, text=char,
                        bg=kb_bg_col, fg=kb_fg_col,
                        width=5, height=2)
    zxc_btn.bind('<Button-1>', key_pressed)
    zxc_btn.grid(row=0, column=i, padx=2, pady=2)

# Add "=" button to the right frame, represents the enter button.
button_enter = tk.Button(zxc_right, font=c_font,
                         text="Ent", fg=kb_fg_col,
                         width=5, height=2, bg='seagreen')
button_enter.bind('<Button-1>', key_pressed)
button_enter.grid(row=0, column=9, padx=6,pady=2)

# Add both frames to the main frame
zxc_left.grid(row=0, column=0, padx=2, pady=2)
zxc_right.grid(row=0, column=1, padx=2, pady=2)
zxc_frame.grid(row=2, column=0, columnspan=10, padx=2, pady=2)


root.mainloop()
