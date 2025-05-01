# Virus-total-scanner


## Objective

The objective for this project was to utlize the public api from Virus Total and parse any information you recieve reagaring the hash. Either is the hash is malicious or not, virus total cross references this hash on various platform. However for this project we only needed to check the results it presented on Fortinets platform.

## How To Use This Tool

#### Step 1:
>Before you use this tool, ensure that all the files are in the same directory
Ensure you have pip working on this machine, to verify you can just type in pip
If that resulted in an error then we can install pip using the following command

```sudo apt install python3-pip```

*if you are presented with a prompt enter 'y' for yes*

### Step 2:
>Now we want to install all the dependencies to do this enter the following command

```pip install -r requirements.txt```

***make sure you are in the directory where you downloaded all the files***

### Step 3:
>Now we can run the file, to run the file we can enter the following command

```python3 Virus-Total-Fortinet.py -f <hash.txt-file>```

***for demo I have included a sample file called sample_hash_input.txt***

To try the sample file we can write the following command on terminal

```python3 Virus-Total-Fortinet.py -f sample_hash_input.txt```

*The results will be stored in the current directory under __results.txt__*

### Installation Summary

```
git clone https://github.com/mayfled/Virus-total-scanner.git
cd Virus-total-scanner
pip install -r requirements.txt
python3 Virus-Total-Fortinet.py -f <hash.txt>
```

### Usage Options

```
usage: Virus-Total-Fortinet.py [-h] -f FILE

Verify if hash is malicious on Fortinet's Platform using Virus Total The results will be stored in the results.txt file in the current directory The results will be displayed once all hashes are scanned

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The text file you want to scan
```

## Summary of Code

>This code consists of 3 functions. The first function initializes the command line interface for the user.
The second function parses the file provided by the user. The third function fetches from the virus-total database for results of each hash.
In this function we have an if statement to check if the hash exists in the database. If it does then it will parse through the json, collect the results and append it to a file and a table. However if the hash doesn't exist in the database this will tell the user that this hash has never been checked on the virus totals database. Once all the hashes have been check it will output to a text file called 'results.txt'


## Required dependencies

>The following were the dependencies that are required in order for this code to execute:

- tqdm==4.60.0
- requests==2.25.1
- prettytable==0.7.2

***These dependencies must be installed prior to executing the code***











