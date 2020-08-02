#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Justin Ma
"""
from tkinter import *
from InstagramLoader import InstagramLoader

'''Creates a global account variable for efficient Login'''
account = InstagramLoader(None,None)


class App:
    
    '''Constructor that runs when App is run'''
    def __init__(self):
        
        '''Function for checking Login information'''
        def login():
            username = userentry.get()
            password = passentry.get()
            #Attempts to login with given information
            try:
                account = InstagramLoader(username, password)
                LoginScreen.destroy()
                self.mainmenu()
            #Displays Login error if Login is incorrect
            except Exception as e: 
                Label(LoginScreen, text=e).grid(row=3, column = 1)
        
        
        '''GUI Code for displaying the Login screen'''
        LoginScreen = Tk()
        LoginScreen.title("Login Screen")
        Label(LoginScreen, text="username:").grid(row=0, column=0)
        Label(LoginScreen, text="password:").grid(row=1, column=0)
        userentry = Entry(LoginScreen, width=20, bg="white")
        userentry.grid(row=0, column=1)
        passentry = Entry(LoginScreen, width=20, bg="white")
        passentry.grid(row=1, column=1)
        Button(LoginScreen, text="Login", width=6, command = login).grid(row=3, column =0)
        LoginScreen.mainloop()
        
    ''''GUI For Main Menu'''
    def mainmenu(self):
        
        '''Displays the Window that shows appropriate users depending on the type'''
        def see_users(Type):
            resultwindow = Toplevel(menu)
            resultwindow.title(Type)
            row_count = 0
            col_count = 0
        
            #Checks to see what button has been clicked
            if Type == "Followers":
                users = account.get_follower_usernames()
            elif Type == "Following":
                users = account.get_following_usernames()
            elif Type == "Fans":
                users = account.get_fan_usernames()
            elif Type == "Fakes":
                users = account.get_fake_usernames()
            elif Type == "Ghosts":
                users = account.get_ghost_usernames()
        
            '''Creates a label for each user and puts it on the resultwindow.'''
            for i in users:
                Label(resultwindow, text = i).grid(row = row_count, column=col_count)
                col_count += 1
                if col_count == 5:
                    col_count = 0
                    row_count += 1
        '''Create the Menu window and add buttons'''
        menu = Tk()
        menu.title("Menu")
        Button(menu, text="See Followers", width = 15, command = lambda:see_users("Followers")).grid(row=0, column =0)
        Button(menu, text="See Following", width = 15, command = lambda:see_users("Following")).grid(row=1, column =0)
        Button(menu, text="See Fans", width = 15, command = lambda:see_users("Fans")).grid(row=2, column =0)
        Button(menu, text="See Fakes", width = 15, command = lambda:see_users("Fakes")).grid(row=3, column =0) 
        Button(menu, text="See Ghosts", width = 15, command = lambda:see_users("Ghosts")).grid(row=4, column =0)
        menu.mainloop()
        
        
        
                
        
        
    '''For Testing Purposes
    def see_followers(self):
        print(account.get_follower_usernames())
    
    def see_following(self):
        print(account.get_following_usernames())
        
    def see_fans(self):
        print(account.get_fan_usernames())
        
    def see_fakes(self):
        print(account.get_fake_usernames())
        
    def see_ghosts(self):
        print(account.get_ghost_usernames())
        '''

'''Run the App'''
App()