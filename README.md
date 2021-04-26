# Virus-total-scanner


## Objective

The objective for this project was to utlize the public api from Virus Total and parse any information you recieve reagaring the hash. Either is the hash is malicious or not, virus total cross references this hash on various platform. However for this project we only needed to check the results it presented on Fortinets platform.

## How-To-Use-This-Tool

###### Step 1:
>Before you use this tool, ensure that all the files are in the same directory
Ensure you have pip working on this machine, to verify you can just type in pip
If that resulted in an error then we can install pip using the following command

```sudo apt install python3-pip```

***if you are presented with a prompt enter 'y' for yes***

Step 2:
-------
Now we want to install all the dependencies to do this enter the following command

pip install -r requirements.txt

*make sure you are in the directory where you downloaded all the files*

Step 3:
-------
Now we can run the file, to run the file we can enter the following command

python3 Virus-Total-Fortinet.py -f <hash.txt-file>

*for demo I have included a sample file called 'sample_hash_input.txt' *

To try the sample file we can write the following command on terminal

python3 Virus-Total-Fortinet.py -f sample_hash_input.txt

*The results will be stored in the current directory under 'results.txt' *

*--Summary-of-Code--*

This code consists of 3 functions. The first function initializes the command line interface for the user.
The second function parses the file provided by the user. The third function fetches from the virus-total database for results of each hash.
In this function we have an if statement to check if the hash exists in the database. If it does then it will parse through the json, collect the results and append it to a file and a table. However if the hash doesn't exist in the database this will tell the user that this hash has never been checked on the virus totals database. Once all the hashes have been check it will output to a text file called 'results.txt'


*--Technology-Used--*

To complete this project I utlized various technologies including Linux,python,MySQL and Flask


Linux:
------
Linux was used to ensure that the command line interface was working accordingly

Python:
-------
Python was used to create this tool

MySQL, Flask, Django: 
---------------------
MySQL and Flask were used to create a web interface for this tool. Currently I'm working on the web interface for this tool. I'm utilizing https://pythonanywhere.com 
to deploy this tool on to the web. I had used this tool before since I have experience working with Flask, the web interface will allow users to upload a text file
where after it will execute the code and print the results back to the user also allowing them to download a copy of the results. 


*--Required-dependencies--*

The following were the dependencies that are required in order for this code to execute:

tqdm==4.60.0
requests==2.25.1
prettytable

*These dependencies must be installed prior to executing the code*


*--Issues-Encounterd--*

This was a very exciting project for me to work on. I have learned quite a lot while trying to complete this project. Althought it wasn't easy as I have encountered many problems. 

One of the many problems I encounred was, I wasn't able to scan multiple hashes at the same time since there was a rate limit for a public api user. My code would first start and after the first 4 hashes it would come to a stop. When investigating on the Virus Total website, I have come to learn that it can scan only 4 per minute. To over come this I put a sleep timer on my for loop to delay each iteration by 30 seconds so the code wouldn't come to a halt.

Another Issue I had encountered was the max daily quota. Again since I was using a free api I was only allowed to go a total of 500 request per day. Since building a code it would require various testing and 500 quota wouldn't be enough. I had to make multiple accounts to recieve new api keys so I can start with a fresh number of quota.

Checking if the hash was found was another issue I faced. I had to ensure that the hash was located in the database, to verify I got the response code it presented to me with at each hash. When the response code came in as 0, it would mean the hash wasn't found in their database. Where as 1 would mean it was found.

Finally working on the web interface, the current issue I am facing is how to take the output results from my python code and dynamically make a table on html. This task was proven rather difficult for me as my knowledge in Django is limited. Currently I have to figure out a way to process thorugh all the hashes and output the results to the webpage without having pythonanywhere break on me.








