# import from library
import hashlib
import os
import random
import string
import tkinter as tk
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

# import from other program
from db.data import search_db
from db.image import get_image_from_db, upload_image_to_db
from db.params import user_table, art_table, exchange_table, backup_user_table, backup_coll1, \
    backup_coll2
from style.button import DefaultButton, DefaultCheckbutton
from style.field import DefaultTextField
from style.inputbox import InputBoxWithPlaceholder
from style.params import main_color, main_fg_color, main_title_font, button_width, log_out_button_width, \
    info_detail_font, error_field_fg_colour, error_field_font, inputReplaceEntryColor

# Library requirement
# Python version 3.8.10 or higher
# Library requirement
# Tkinter, pip command: pip install tk
# Pillow, pip command: pip install Pillow
# pymongo, pip command: pip install pymongo
# dnspython, pip command: pip install dnspython
# certifi, pip command: pip install certifi

# Account
# default username: Anson
# default password: Aa123456
#
# admin username: Admin
# admin password: Admin123

# Global constant
C_VERSION = "v0.0.8"
ShowPage = 0
current_user = ""
buy_digital_art_id = 1


# User Interface and Interface creation
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Declare the interface
        tk.Tk.__init__(self, *args, **kwargs)
        # Set the size and location
        self.geometry("300x400+810+340")
        # Title of the window
        self.title("CSS Project")
        # Window resizeable
        self.resizable(0, 0)
        # Create the frame
        win = tk.Frame(self)
        self.win = win
        win.pack()
        # Set the grid value
        win.grid_columnconfigure(0, minsize=300)
        win.grid_rowconfigure(0, minsize=400)

        self.frames = {}
        # Init all the page
        for F in (MainPage, RegisterPage, changePassword, AfterLogin):
            frame = F(win, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.config(bg=main_color)
        # show the first page
        self.show_frame(MainPage)

    # change to frame
    def show_frame(self, page):
        frame = self.frames[page]
        frame.update()
        frame.tkraise()

    # refresh the frame
    def load_frame(self, page):
        frame = page(self.win, self)
        self.frames[page] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        frame.config(bg=main_color)


#######################################################################

# Main page or login page
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        global user_input_box, pwd_input_box, error_msg_field
        # change the frame use
        self.controller = controller
        # init the frame
        tk.Frame.__init__(self, parent)

        # image size reset and load the image
        img = get_image_from_db("homepage.jpg", 240, 150)

        # variable for determine the checkbutton on or off
        self.var = tk.IntVar()
        # checkbutton for show the password or show in * form
        show_pwd_btn = DefaultCheckbutton(self, "Show password", variable=self.var, command=self.show_password_action)
        show_pwd_btn.place(x=200, y=280, anchor=tk.E)

        # show the image
        image_field = DefaultTextField(self, image=img, bg=main_fg_color)
        image_field.image = img
        image_field.place(x=150, y=10, anchor=tk.N)
        # input bar Username
        user_input_box = InputBoxWithPlaceholder(self, "Username")
        # Place the bar to interface
        user_input_box.place(x=150, y=205, anchor=tk.CENTER)

        # input bar Password
        pwd_input_box = InputBoxWithPlaceholder(self, "Password", input_value_with_star=True)
        # Place the bar to interface
        pwd_input_box.place(x=150, y=250, anchor=tk.CENTER)

        # button login
        login_btn = DefaultButton(self, "Login", command=self.pwd_check, height=1)
        login_btn.place(x=205, y=310, anchor=tk.CENTER)

        # error message
        error_msg_field = DefaultTextField(self,font=error_field_font)
        error_msg_field.place(x=150, y=180, anchor=tk.CENTER)

        # register button
        register_btn = DefaultButton(self, "Register", command=self.go_to_register_page)
        register_btn.place(x=95, y=310, anchor=tk.CENTER)

        # bottom right version
        version_field = DefaultTextField(self, C_VERSION)
        version_field.place(x=290, y=390, anchor=tk.SE)

    def pwd_check(self):
        # remove the cursor from the input box
        self.focus()
        if user_input_box["fg"] == inputReplaceEntryColor or user_input_box.get() == "":
            error_msg_field.config(text="Please enter username.", fg=error_field_fg_colour)
            return
        # empty password input
        elif pwd_input_box["fg"] == inputReplaceEntryColor or pwd_input_box.get() == "":
            error_msg_field.config(text="Please enter a password.", fg=error_field_fg_colour)
            return
        # Find the username in database
        username = search_db(user_table, user_input_box.get())
        # if no sure username found in the database
        if not username:
            self.empty_input_action()
            error_msg_field.config(text="Invalid username or password. Please try again.", fg=error_field_fg_colour)
            return
        else:# username found, get the salting and hashed password
            random_num = username["salting"]
            password = username["password"]
        # calculate the hashed password with salting and user input password
        pwd_from_user = "" + random_num + pwd_input_box.get()
        hash_user_pwd = (hashlib.sha256(pwd_from_user.encode()))
        
        # compare the user input hashed passowrd and database stored hashed password
        if hash_user_pwd.hexdigest() == password:
            global current_user
            current_user = user_input_box.get()
            self.empty_input_action()
            self.controller.load_frame(AfterLogin)
            self.controller.show_frame(AfterLogin)
        else:
            # wrong input
            error_msg_field.config(text="Invalid username or password. Please try again.", fg=error_field_fg_colour)

    # change to the register page
    def go_to_register_page(self):
        self.empty_input_action()
        self.controller.show_frame(RegisterPage)

    # remove all the input from the user
    @staticmethod
    def empty_input_action():
        user_input_box.reset()
        pwd_input_box.reset()
        error_msg_field.config(text="")

    def show_password_action(self):
        # show password button is chosen
        if self.var.get() == 1:
            pwd_input_box["show"] = ""  # show the password without replacement
            pwd_input_box.inputValueWithStar = False  # stop the auto replacement
        # show password button is not chosen
        if self.var.get() == 0:
            pwd_input_box.inputValueWithStar = True  # resume the auto replacement
            if pwd_input_box["fg"] == pwd_input_box.default_fg_color:
                pwd_input_box["show"] = "*"  # show the password with replacement
        return

# Exchange Page
class AfterLogin(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        # Title of the page
        title_field = DefaultTextField(self, "NFT Exchange", font=main_title_font)
        title_field.grid(column=0, row=0, columnspan=3, rowspan=1, sticky=tk.W)

        # count the number of page to be shown
        total_page = 0
        number = art_table.find({})
        if number is None:
            return
        for i in number:
            total_page += 1
        self.totalPage = total_page

        ############################## Loop the picture on one page
        # Next row to be add
        row_extra = 0
        # the last divider row position
        end_row = 0
        # get 2 data information for one page
        for i in range(2):
            # control the page. i.e if number of picture is 5, it will stop the program to generate pic. 6
            if ShowPage + i >= total_page:
                row_extra = 5
                continue
            # Change the end row
            end_row = 10
            # Each picture use 4 rows, add 4 if it is second picture
            row_extra = i * 4
            # Get the picture from database
            searched_art = search_db(art_table, ShowPage + i)
            # Get the information of the art
            art_id = searched_art["_id"]
            cost = searched_art["cost"]
            temp = searched_art["artname"]
            # If the artname is too large, use "..." to show the remaining
            if len(temp)>8:
                temp=temp[0:8]
                temp+="..."
            # replace the name with modified one
            art_name = temp
            owner = searched_art["owner"]
            filename = searched_art["filename"]
            
            # image divider
            line = DefaultTextField(self, text="------------------------------------------------------------")
            rows = row_extra + 1
            line.grid(column=0, row=rows, columnspan=3, rowspan=1, sticky=tk.N)

            # transfer the information which had got to a string
            art_name_text = tk.StringVar()
            art_name_text.set("Art Name: " + art_name)
            id_text = tk.StringVar()
            id_text.set("ID: " + str(art_id).zfill(5))
            cost_text = tk.StringVar()
            cost_text.set("Price: $" + cost)
            owner_name_text = tk.StringVar()
            owner_name_text.set("Owned by " + owner)

            # place the information in the GUI
            art_id_field = DefaultTextField(self, textvariable=id_text, font=info_detail_font)
            rows = 2 + row_extra
            art_id_field.grid(column=0, row=rows, columnspan=1, rowspan=1, sticky=tk.W)

            # art name
            art_name_field = DefaultTextField(self, textvariable=art_name_text, font=info_detail_font)
            rows = 3 + row_extra
            art_name_field.grid(column=0, row=rows, columnspan=1, rowspan=1, sticky=tk.W)
            # cost 
            cost_field = DefaultTextField(self, textvariable=cost_text, font=info_detail_font)
            rows = 4 + row_extra
            cost_field.grid(column=0, row=rows, columnspan=1, rowspan=1, sticky=tk.W)


            # place the image in the GUI
            img = get_image_from_db(filename, 60, 60)
            image_field = DefaultButton(self, image=img, bg=main_fg_color)

            # Choose first page or second page
            if i % 2 == 1:
                self.id1 = art_id
                image_field.config(command=lambda: self.buy_btn_action(self.id1))
            else:
                self.id2 = art_id
                image_field.config(command=lambda: self.buy_btn_action(self.id2))

            # set the image to the button
            image_field.image = img
            rows = 2 + row_extra

            # Grid the button on interface
            image_field.grid(column=2, row=rows, columnspan=1, rowspan=2, stick=tk.W + tk.N,padx=10)
        ################################## End looping

        # Last divider
        split_line_field = DefaultTextField(self, text="------------------------------------------------------------")
        split_line_field.grid(column=0, row=end_row, columnspan=3, rowspan=1, sticky=tk.N)

        # place Logout button
        logout_btn = DefaultButton(self, "Logout", command=self.logout, width=log_out_button_width)
        logout_btn.place(x=290, y=15, anchor=tk.E)

        # place previousPage button and control the previousPage button
        previous_page_btn = DefaultButton(self, "Previous Page", command=lambda: self.next(-2))
        # Check if there is previous page to be shown
        if ShowPage == 0:
            previous_page_btn.config(state=tk.DISABLED)# disable the button
        else:
            previous_page_btn.config(state=tk.NORMAL)# enable the button
        previous_page_btn.place(anchor=tk.W, x=10, y=300)

        # place change password button
        change_pwd_btn = DefaultButton(self, "Change Password", command=self.change_pwd_btn_action)
        change_pwd_btn.place(anchor=tk.W, x=10, y=340)

        # place next_page_btn button and control the next_page_btn button
        next_page_btn = DefaultButton(self, "Next Page", command=lambda: self.next(2))

        # Check if there is last page
        if ShowPage + 2 >= self.totalPage:
            next_page_btn.config(state=tk.DISABLED) # disable the button
        else:
            next_page_btn.config(state=tk.NORMAL)# enable the button
        next_page_btn.place(anchor=tk.E, x=290, y=300)

        # place upload button
        upload_btn = DefaultButton(self, "Upload", command=self.upload)
        upload_btn.place(anchor=tk.E, x=290, y=340)

    # change page function, with page to be shown
    def next(self, page):
        global ShowPage
        ShowPage += page
        self.controller.load_frame(AfterLogin)
        self.controller.show_frame(AfterLogin)

    # upload function
    def upload(self):
        # file dialog
        doc_name = filedialog.askopenfilename(filetypes=[("JPG Picture", ".jpg")])
        if doc_name is None or doc_name == "": # if user click cancel
            messagebox.showwarning("Cancelled", "The upload action is cancelled.")
            return
        # if file size exceed 1MB
        if os.path.getsize(doc_name) > 1048576:
            messagebox.showwarning("Warning", "The upload picture should not exceed 1MB.")
            return
        # Check if the it is a image
        try:
            Image.open(doc_name)
        # filename not an image file
        except IOError:
            messagebox.showwarning("Warning", "The upload file is not a picture")
            return
        # get the file name
        name = upload_image_to_db(doc_name)
        # check the file name exceed 25 chars or not
        if len(name)>25:
            messagebox.showerror("Error!","File name should be exceed 25 character(s).\n Please change the file name and try again.")
            return
        # Pop window to let user for selecting the art price
        price = simpledialog.askstring(title="CSS Project", prompt="What is the price?")
        # Empty input
        if price is None or price == "" :
            messagebox.showwarning("Cancelled", "The upload action is cancelled.")
            return
        # Not positive integer
        if not price.isdigit() or int(price) < 1:
            messagebox.showwarning("Failed", "Please input correct price.")
            return
        # Count all the art in the database
        digital_db_count = 0
        digital = art_table.find({})
        if digital is None:
            return
        for i in digital:
            digital_db_count = digital_db_count + 1
        # Store all the information into list
        post = {"_id": digital_db_count, "artname": name[:-4], "owner": current_user, "cost": price,
                "Author": current_user, "filename": name, "available": 1}
        # upload the list into two database
        art_table.insert_one(post)
        backup_coll1.insert_one(post)
        # Message box for inform user success uploading the image
        messagebox.showinfo("Success!","You have upload a digit art to our platform!")
        # Refresh the page
        self.controller.load_frame(AfterLogin)
        self.controller.show_frame(AfterLogin)

    # function after press change password(change_pwd_btn) button
    def change_pwd_btn_action(self):
        #self.empty_input_action()
        self.controller.show_frame(changePassword)
        return

    # function after press the iamge
    def buy_btn_action(self, art_id):
        global buy_digital_art_id
        buy_digital_art_id = art_id
        self.controller.load_frame(BuyPage)
        self.controller.show_frame(BuyPage)

    # function after press logout(logout_btn) button
    def logout(self):
        #self.empty_input_action()
        self.controller.show_frame(MainPage)

# show the page after press the image
# Buy page or confirm buy
class BuyPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        # get the information of the specific id which have pressed the specific button from database
        searched_art = search_db(art_table, buy_digital_art_id)
        # if no that id
        if searched_art is None:
            return
        else:# get all id from database
            art_id = searched_art["_id"]
            file = searched_art["filename"]
            art_name = searched_art["artname"]
            owner = searched_art["owner"]
            cost = searched_art["cost"]
            author = searched_art["Author"]
            available = searched_art["available"]

        # place the image
        img = get_image_from_db(file, 150, 150)
        imageLabel = DefaultTextField(self, image=img, bg=main_fg_color)
        imageLabel.image = img
        imageLabel.place(x=150, y=10, anchor=tk.N)

        # transfer the information which had got to a string
        # art name
        inside_artname = tk.StringVar()
        inside_artname.set("Art Name: " + art_name)
        # id
        inside_id = tk.StringVar()
        inside_id.set("Art Number: " + str(art_id).zfill(5))
        # cost
        inside_cost = tk.StringVar()
        inside_cost.set("Cost: $" + cost)
        # author name
        inside_Author = tk.StringVar()
        inside_Author.set("Author by " + author)
        inside_ownername = tk.StringVar()
        # save the owername for check later
        self.ownername = owner
        # owner name
        inside_ownername.set("Owned by " + owner)
        inside_available = tk.StringVar()

        # Status here
        if available == 1:# normal
            inside_available.set("Status: Available")
        elif available == 2:# banned by admin
            inside_available.set("Status: Unavailable (Banned by Admin)")
        else:# closed by owner
            inside_available.set("Status: Unavailable")

        # place the information to the GUI
        # id
        number_art = DefaultTextField(self, textvariable=inside_id)
        number_art.place(x=20, y=190, anchor=tk.W)
        # art name
        art = DefaultTextField(self, textvariable=inside_artname)
        art.place(x=20, y=215, anchor=tk.W)
        # author name
        author = DefaultTextField(self, textvariable=inside_Author)
        author.place(x=20, y=240, anchor=tk.W)
        # cost
        cost = DefaultTextField(self, textvariable=inside_cost)
        cost.place(x=20, y=265, anchor=tk.W)
        # owner name
        owner = DefaultTextField(self, textvariable=inside_ownername)
        owner.place(x=20, y=290, anchor=tk.W)
        # status above
        availableLabel = DefaultTextField(self, textvariable=inside_available)
        availableLabel.place(x=20, y=315, anchor=tk.W)

        # place the buy button
        Buy = DefaultButton(self, "Buy", command=self.buy, width=button_width)
        Buy.place(x=10, y=350, anchor=tk.W)

        # place the back button
        backButton = DefaultButton(self, "Back", command=self.back, width=button_width)
        backButton.place(x=290, y=350, anchor=tk.E)

        # place the Available button
        global availablebutton
        # button for owner or admin to close or open the digit art for public
        if available == 1:# Stop the art from buying
            availablebutton = DefaultButton(self, "Close for public", command=self.ChangeAvailability)
        elif available == 2: # reopen the art for buying (Admin Only)
            availablebutton = DefaultButton(self, "Unban this art", command=self.ChangeAvailability)
        else: # Open for public to buy the art
            availablebutton = DefaultButton(self, "Open for public", command=self.ChangeAvailability)
        # If not ban from admin and user is the owner of the art, or user is admin, can use the button
        if (self.ownername == current_user and available != 2) or current_user == "Admin":
            availablebutton.config(state=tk.NORMAL)
        else:# else cannot use the button
            availablebutton.config(state=tk.DISABLED)
        availablebutton.place(x=150, y=350, anchor=tk.CENTER)

    # function of the Available button which can control the object can be bought or not
    def ChangeAvailability(self):
        # get the information of the specific object
        global availablebutton # get the available button above
        # search the art from database
        selected_art = search_db(art_table, buy_digital_art_id)
        if selected_art is None:
            return
        else:
            selected_art_id = selected_art["_id"]
            available = selected_art["available"]

        # update the available in the database when pressed the button

        # condition: Open for public , owner. Result: close for public
        if available == 1 and current_user == self.ownername:
            art_table.update_one({"_id": selected_art_id}, {"$set": {"available": 0}})
            backup_coll1.update_one({"_id": selected_art_id}, {"$set": {"available": 0}})
            self.controller.load_frame(BuyPage)

        # condition: Close for public , owner. Result: Open for public
        elif available == 0 and current_user == self.ownername:
            art_table.update_one({"_id": selected_art_id}, {"$set": {"available": 1}})
            backup_coll1.update_one({"_id": selected_art_id}, {"$set": {"available": 1}})
            self.controller.load_frame(BuyPage)

        # condition: Open for public , Admin. Result: ban the art (Owner cannot open, other cannot buy it)
        elif available == 1 and current_user == "Admin":
            art_table.update_one({"_id": selected_art_id}, {"$set": {"available": 2}})
            backup_coll1.update_one({"_id": selected_art_id}, {"$set": {"available": 2}})
            self.controller.load_frame(BuyPage)

        # condition: ban the art , Admin. Result: unban the art (Owner cannot open, other cannot buy it)
        elif available == 2 and current_user == "Admin":
            art_table.update_one({"_id": selected_art_id}, {"$set": {"available": 0}})
            backup_coll1.update_one({"_id": selected_art_id}, {"$set": {"available": 0}})
            self.controller.load_frame(BuyPage)
        # inform the user the change have done
        messagebox.showinfo(title="Success!", message="You have change the available.")

    # back function
    def back(self):
        self.controller.load_frame(AfterLogin)
        self.controller.show_frame(AfterLogin)

    # buy function where user click the buy button
    def buy(self):
        # create the blockchain for the exchange record
        class NeuralCoinBlock:
            def __init__(self, previous_block_hash, transaction_list):
                self.previous_block_hash = previous_block_hash
                self.transaction_list = transaction_list

                self.block_data = "".join(transaction_list) + "-" + previous_block_hash
                self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

        # get the information of the specific object
        detailed_information = search_db(art_table, buy_digital_art_id)
        if detailed_information is None:
            return
        else:
            id = detailed_information["_id"]
            artname = detailed_information["artname"]
            owner = detailed_information["owner"]
            cost = detailed_information["cost"]
            available = detailed_information["available"]

        # check the current user, if same as the owner ,then can't buy the object
        if current_user == owner:
            messagebox.showerror("Error!", "You cannot buy your own digit art!")
            return
        # check the availability of the object
        if available != 1: # not available
            messagebox.showinfo(title="Error!", message="Sorry, this art is not available to buy.")
            return

        # count the exchange database object
        ex_db_count = 0
        exchange = exchange_table.find({})
        if exchange is None:
            return
        for i in exchange:
            ex_db_count = ex_db_count + 1
        ex_db_count = ex_db_count - 1

        # get the previous hash for the current hash
        exchange1 = search_db(exchange_table, ex_db_count)
        if not exchange1:
            return
        else:
            block_h = exchange1["block"]

        # transfer the data to a string format
        p_text = "{}".format(block_h)
        transaction = "{} paid ${} to {} to buy {}(id={})".format(current_user, cost, owner, artname, id)

        # pass the string to a blockchain function
        initial_block = NeuralCoinBlock(p_text, transaction)

        # add the hash and the block data to the database(exchange)
        post = {"_id": ex_db_count + 1, "block_data": initial_block.block_data, "block": initial_block.block_hash}
        # add the hash
        exchange_table.insert_one(post)
        backup_coll2.insert_one(post)
        # change the owner in database
        art_table.update_one({"_id": id}, {"$set": {"owner": current_user}})
        backup_coll1.update_one({"_id": id}, {"$set": {"owner": current_user}})
        # refresh the frame
        self.controller.load_frame(BuyPage)

        # show the Success messagebox
        messagebox.showinfo(title="Success!", message="You have bought this art!")
        self.back()


# Change the user password
class changePassword(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        global da, db, dc, dd
        # variable name: function
        # da: username
        # db: first password input
        # dc: second password input
        # dd: error message
        # de: checkbutton for showing password

        # original Password
        da = InputBoxWithPlaceholder(self, "Original password", input_value_with_star=True)
        da.place(x=150, y=140, anchor=tk.CENTER)

        # first password input
        db = InputBoxWithPlaceholder(self, "New Password", input_value_with_star=True)
        db.place(x=150, y=190, anchor=tk.CENTER)

        # second password input
        dc = InputBoxWithPlaceholder(self, "Confirm password", input_value_with_star=True)
        dc.place(x=150, y=240, anchor=tk.CENTER)

        # error message
        dd = DefaultTextField(self)
        dd.place(x=150, y=100, anchor=tk.CENTER)

        ## variable for determine the checkbutton on or off
        self.var = tk.IntVar()
        # checkbutton for show the password or show in * form
        de = DefaultCheckbutton(self, "Show password", variable=self.var, command=self.showPassword)
        de.place(x=200, y=265, anchor=tk.E)

        # register button
        df = DefaultButton(self, "Confirm", command=self.checkPWD)
        df.place(x=205, y=295, anchor=tk.CENTER)

        # return to main page
        dg = DefaultButton(self, "Back", command=self.back)
        dg.place(x=75, y=295, anchor=tk.W)

    def checkPWD(self):
        # get the user password, id and salting
        user = search_db(user_table, current_user)
        salting = user["salting"]
        password = user["password"]
        id = user["_id"]
        # Hash the old password
        oldPW = "" + salting + da.get()
        HashedPW = hashlib.sha256(oldPW.encode())
        # check if user enter the origianl password
        if (da['fg']==inputReplaceEntryColor or da.get() == ""):
            dd.config(text="Please enter the origianl password.", fg=error_field_fg_colour)
            return
        # check if user enter a password
        if (db['fg']==inputReplaceEntryColor or db.get() == ""):
            dd.config(text="Please enter a password.", fg=error_field_fg_colour)
            return
        # check if user confirm the password
        if (dc['fg']==inputReplaceEntryColor or dc.get() == ""):
            dd.config(text="Please confirm the password.", fg=error_field_fg_colour)
            return
        # check for old password is match
        if (HashedPW.hexdigest() != password):
            dd.config(text="The original did not match. Please try again.", fg=error_field_fg_colour)
            return
        # check the characters are more than 8
        if (len(db.get()) < 8):
            dd.config(text="Use 8 characters or more for your password", fg=error_field_fg_colour)
            return
        # password do not match
        if (db.get() != dc.get()):
            cd.config(text="Those passwords didn’t match. Please try again.", fg=error_field_fg_colour)
            return
        # no integer in the password
        if not any(char.isdigit() for char in db.get()):
            dd.config(text="Password should have at least one numeral", fg=error_field_fg_colour)
            return
        # no Uppercase letter in the password
        if not any(char.isupper() for char in db.get()):
            dd.config(text="Password should have at least one uppercase letter", fg=error_field_fg_colour)
            return
        # no Lowercase letter in the password
        if not any(char.islower() for char in db.get()):
            dd.config(text="Password should have at least one lowercase letter", fg=error_field_fg_colour)
            return
        # hash the new password
        newPW = "" + salting + db.get()
        HashedPW = hashlib.sha256(newPW.encode())
        # update the password to the database
        user_table.update_one({"_id": id}, {"$set": {"password": HashedPW.hexdigest()}})
        backup_user_table.update_one({"_id": id}, {"$set": {"password": HashedPW.hexdigest()}})
        self.back()

    # return to exchange page
    def back(self):
        self.emptyInput()
        self.controller.load_frame(AfterLogin)
        self.controller.show_frame(AfterLogin)

    def emptyInput(self):
        # empty all the input from the user
        da.reset()
        db.reset()
        dc.reset()
        dd.config(text="")

    def showPassword(self):
        # show password button is chosen
        if (self.var.get() == 1):
            da["show"] = ""  # show the password without replacement
            da.inputValueWithStar = False  # stop the auto replacement
            db["show"] = ""  # show the password without replacement
            db.inputValueWithStar = False  # stop the auto replacement
            dc["show"] = ""  # show the password without replacement
            dc.inputValueWithStar = False  # stop the auto replacement
        # show password button is not chosen
        if (self.var.get() == 0):
            db.inputValueWithStar = True  # resume the auto replacement
            dc.inputValueWithStar = True  # resume the auto replacement
            da.inputValueWithStar = True  # resume the auto replacement
            if (db["fg"] == db.default_fg_color):
                db["show"] = "*"  # show the password with replacement
            if (dc["fg"] == dc.default_fg_color):
                dc["show"] = "*"  # show the password with replacement
            if (da["fg"] == da.default_fg_color):
                da["show"] = "*"  # show the password with replacement
        return

# Register a new account
class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        global ca, cb, cc, cd
        self.controller = controller
        tk.Frame.__init__(self, parent)
        # variable name: function
        # ca: username
        # cb: first password input
        # cc: second password input
        # cd: error message
        # ce: checkbutton for showing password
        # cf: register button
        # cg: back button

        # username input
        ca = InputBoxWithPlaceholder(self, "Username")
        ca.place(x=150, y=140, anchor=tk.CENTER)

        # first password input
        cb = InputBoxWithPlaceholder(self, "Password", input_value_with_star=True)
        cb.place(x=150, y=190, anchor=tk.CENTER)

        # second password input
        cc = InputBoxWithPlaceholder(self, "Confirm password", input_value_with_star=True)
        cc.place(x=150, y=240, anchor=tk.CENTER)

        # error message
        cd = DefaultTextField(self, font=error_field_font)
        cd.place(x=150, y=100, anchor=tk.CENTER)

        # variable for determine the checkbutton on or off
        self.var = tk.IntVar()
        # checkbutton for show the password or show in * form
        ce = DefaultCheckbutton(self, "Show password", variable=self.var, command=self.showPassword)
        ce.place(x=200, y=265, anchor=tk.E)

        # register button
        cf = DefaultButton(self, "Register", command=self.checkPWD)
        cf.place(x=205, y=295, anchor=tk.CENTER)

        cg = DefaultButton(self, "Back", command=self.back)
        cg.place(x=75, y=295, anchor=tk.W)

    # return to main page
    def back(self):
        self.emptyInput()
        self.controller.show_frame(MainPage)

    def checkPWD(self):
        self.focus()
        # empty username
        if (ca["fg"] == inputReplaceEntryColor or ca.get() == ""):
            cd.config(text="Please input username first.", fg=error_field_fg_colour)
            return
        # empty the password
        if (cb["fg"] == inputReplaceEntryColor or cb.get() == ""):
            cd.config(text="Please enter a password", fg=error_field_fg_colour)
            return
        # empty the confirmation password
        if (cc["fg"] == inputReplaceEntryColor or cc.get() == ""):
            cd.config(text="Please confirm your password", fg=error_field_fg_colour)
            return
        # length does not more than 8 char
        if (len(cb.get()) < 8):
            cd.config(text="Use 8 characters or more for your password", fg=error_field_fg_colour)
            return
        # password do not match
        if (cb.get() != cc.get()):
            cd.config(text="Those passwords didn’t match. Please try again.", fg=error_field_fg_colour)
            return
        # no integer in the password
        if not any(char.isdigit() for char in cb.get()):
            cd.config(text="Password should have at least one numeral", fg=error_field_fg_colour)
            return
        # no Uppercase letter in the password
        if not any(char.isupper() for char in cb.get()):
            cd.config(text="Password should have at least one uppercase letter", fg=error_field_fg_colour)
            return
        # no Lowercase letter in the password
        if not any(char.islower() for char in cb.get()):
            cd.config(text="Password should have at least one lowercase letter", fg=error_field_fg_colour)
            return
        # salt of password, random six character string
        salting = "".join(random.choices(string.ascii_letters + string.digits, k=6))
        # combine the salt and original password together
        newpd = salting + cb.get()
        # hash the password
        hash = (hashlib.sha256(newpd.encode()))
        hashedPassword = hash.hexdigest()
        # get the username
        username = ca.get()

        # database register
        RepeatedUserName = user_table.find_one({"username": username})
        if (RepeatedUserName != None):
            cd.config(text="That username is taken. Try another.", fg=error_field_fg_colour)
            return

        # count all the existing account number
        dbcount = 0
        for xyz in user_table.find({}):
            dbcount += 1
        dbcount += 1

        # create the account by storing the data into database
        user_table.insert_one(
            {"_id": dbcount, "username": username, "password": hashedPassword, "salting": salting, "balance": 0})
        backup_user_table.insert_one(
            {"_id": dbcount, "username": username, "password": hashedPassword, "salting": salting, "balance": 0})

        # back to main page
        self.back()

    def emptyInput(self):
        # empty all input from user
        ca.reset()
        cb.reset()
        cc.reset()
        cd.config(text="")

    def showPassword(self):
        # show password button is chosen
        if (self.var.get() == 1):
            cb["show"] = ""  # show the password without replacement
            cb.inputValueWithStar = False  # stop the auto replacement
            cc["show"] = ""  # show the password without replacement
            cc.inputValueWithStar = False  # stop the auto replacement
        # show password button is not chosen
        if (self.var.get() == 0):
            cb.inputValueWithStar = True  # resume the auto replacement
            cc.inputValueWithStar = True  # resume the auto replacement
            if (cb["fg"] == cb.default_fg_color):
                cb["show"] = "*"  # show the password with replacement
            if (cc["fg"] == cc.default_fg_color):
                cc["show"] = "*"  # show the password with replacement
        return


# loop the interface
app = Application()
app.mainloop()
