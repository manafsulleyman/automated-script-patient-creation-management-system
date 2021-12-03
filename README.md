 
# mPharma-Patient-management-system

# Installation

To run the automated script, you first have to get the application running locally. Follow the **Appliccation installation** below to run Application locally.

Once you have the Application running, follow the Automated test script repo instruction to get the script running. 

# Application installation
These instructions will get you a copy of the project up and running on your local machine.

The first step to running this repo locally is downloading the code by cloning the repository

1. Clone the app repo git clone https://github.com/mPharma/qa-take-home-test.git

2. After cloning, cd qa-take-home-test if you are not in the folder already.
3. npm install
4. npm start

NB: You need Nodejs/NPM on your local machine for this project to work

# Automated test script repo 

These instructions will get you on how to get the automated test script on your machine and start the test. 

1. Clone the app repo git clone https://github.com/manafsulleyman/automated-script-Patient-mgmnt-system.git

2. After cloning, cd mPharmaTest

3. You need to install the following packages using the commands below
4.      pip install selenium
5.      pip install webdriver-manager
6.      pip install xlrd
7.      pip install behave

7. Copy the **Url** from the **qa-take-home-test Application** running on your localhost. eg:localhost:3000/

8. Open the **helper_base.py** file in the Helper folder and replace the value of the **base_url** on line 8 with it. 

9. Open the terminal and type the word **behave** and hit enter. 
