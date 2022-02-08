#Exercise¶
#Implement a small download program, using https://hackernews.com as a test URL:

#Create a cli program to take 2 arguments: url (required) and destination_file (optional)
#Create a description of what the program does
#Implement the download part
#If no destination file was specified, save the file in default_file.dat
#Improve the code: if no destination file was specified, use the last subset of the URL as the name for the file
#Improve the code: if no destination file was specified, use the MIME-type of the HTTP header to guess the file extension

import argparse
from posixpath import split
from modules import webget

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take a URL and destination_file')
    parser.add_argument('URL', help='URL to process')
    parser.add_argument('-d','--destination',help='Name of the file to store the url')
    args = parser.parse_args()

    if not args.destination:
        list = args.URL.split('/')
        print(list)
        if list[-1]:
            args.destination = "my_files/week2/files/"+ list[-1]
        else:
            args.destination = "my_files/week2/files/"+ list[-2]
    else :
        args.destination = "my_files/week2/files/" + args.destination

    print(f"downloading: {args.URL} To: {args.destination}")
    webget.download(args.URL,args.destination)


    

