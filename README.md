# About Contact Book

This contact book application uses the Trie (or Prefix Tree) data structure to arrange contact names in an alphabetical order and allows the user to search for specific individuals depending on the prefix they entered in the search field. The core functionality of this app (add, remove, and search) has also been tested using **unittest** module. 

Furthermore, this app's graphical user interface is built using **Tkinter** and the database component is powered by **MongoDB** to store user information, and their list of contacts. 

![image](https://i.imgur.com/n1Vuxr6.png)

Demonstration of this application can be viewed here: https://www.youtube.com/watch?v=t3IHILH7UZs

# Requirements

This application requires these following dependencies to run:
- Tkinter 
- Pymongo

Furthermore, you'll need a MongoDB connection uri in order to launch this application. This string will need to be used inside database.py file, or the application will not function. 

# Future Plans

Currently the application has all the basic important functionality implemented. But in the future, I plan to add the following features to improve the app:

- Continue improving the design of the UI, including more user verification checks. 
- Be able to edit an existing contact
- Figure out a way to have contacts with same name, but have different information such as phone number.
