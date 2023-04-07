Instructions for running this program are as follows:

I have not provided you with the database. You will have to load it on your own.* Follow these instructions:

1. Run 'databasecreate.py'. This will create the database, including all the necessary tables.
2. Run 'databaseload.py'. This will load the data into the database, using the data in the data folder.

After this, run 'runningthedatabase.py'. This runs the interface, despite it being called 'runningthedatabase'.

To run the interface, you must install an app called Flask, otherwise it will not work. You may have this already, but if you don't, the instructions for this are
below:

1. Create a virtual environment for the program using Python 3.9. Make sure to activate the virtual environment. 
Please don't use Python 3.7. It won't work.
2. Open the terminal in PyCharm or use your computer terminal.
3. Use the command 'pip install Flask'
4. Make a flask app by typing set FLASK_APP=databaseapp
5. Run the file either in PyCharm or by using the command 'python databaseapp.py'
Then go to the address http://localhost:5000/. This should run the program.

The folder marked 'database13' contains the required files to run this program. Please do not delete any of
these files. I will cry if you do.

Mercurial is available with this project if you follow these instructions to run it.
1. Open a command prompt
2. Select the drive which this project is stored on by typing the name of the drive (e.g E) with a colon into 
the command prompt
3. Type cd database13 into the command prompt
4. Type hg log into the command prompt

ChatGPT was not used for this project, since it doesn't work for me. However, I used several websites, which are below:
https://www.w3schools.com/tags/att_option_selected.asp
https://ttl255.com/jinja2-tutorial-part-2-loops-and-conditionals/#cond-tests
https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number

Unfortunately I don't have any more records of websites I used, if any, please forgive me.

This folder also contains several test programs created to test the class functions. Feel free to look at them. They are in the top level, not the 'test' folder.

*this is because my testing messed up the database and I didn't want to reload it myself. 