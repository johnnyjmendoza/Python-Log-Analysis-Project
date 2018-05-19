# Log Analysis Project

**Overview**

This project is part of UDACITY'S Full Stack Web Developer Program. The goal is to create a reporting tool in Python/PostgreSQL that prints out reports based on data in a database. The program will query the news database and return three different sets of data:

1. The three most popular articles. 
2. The most popular authors. 
3. On which days more than 1% of the requests lead to errors. 

**Python Version Information**

This program uses Python3 and as such, you must use the Python3 command within the Vagrant shell in order to run this program without any problems. 

**Files**

1. LogAnalysis.py - Python Program
2. output.py - Text file that displays the output of running the Python program.

**Running the Program**

Running the program requires the following:

1. Install GIT Bash program.
2. Install VirtualBox program.
3. Install Vagrant program.
4. Launch GIT BASH
5. CD to vagrant directory to find the Vagrantfile program 
    (example: cd documents, cd Vagrant, cd fsnd-virtual-machine, cd FSND-Virtual-Machine, cd vagrant)
6. Once you locate the Vagrantfile program and are inside the same directory: 
    start FSND Virtual Machine using Vagrant Up command to launch UBUNTU Linux.
7. With Vagrant running, run Vagrant SSH to enter the shell.
8. Change directory to Vagrant by using CD /Vagrant command.
9. Ensure that the Python file LogAnalysis.py is in the vagrant directory.
10. Run LogAnalysis.py with the command "Python3 LogAnalysis.py"
11. The database query may take a few minutes. 
12. After a few minutes, the database will return the 3 different sets of data.

**Vagrant Reminders**

For those unfamiliar with the Vagrant system, it can cause some headaches. The Vagrant Up command must be run in the proper directory. If you attempt to run it in a directory that does not have the main "vagrantfile" file. 

1. After installing Vagrant, make sure you navigate to the proper directory where you installed it. An example if you had installed it in the Documents folder would be to CD to the full path of the Vagrantfile file: /documents/Vagrant/fsnd-virtual-machine/FSND-Virtual-Machine/vagrant
2. Once you are in the vagrant directory you can type in "vagrant up" and the system will load up the Linux build. 
3. After a few minutes, the system will display the familiar Linux command line and you can begin working. Note: If Vagrant is already running, then run Vagrant SSH to enter the shell. 

**License**

This program was written by Johnny Mendoza and is free to use for non-commercial use. 

Contact Johnnymendoza@gmail.com for more information on this program. 
