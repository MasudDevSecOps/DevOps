from datetime import datetime
import calendar
import boto3
from pandas import *
import csv

client = boto3.client('ses')


def send_greetings():
    email_list = get_email_list()
    current_day = get_current_day()

    # if current day is sunday, send student a greeting
    # current_day = 'Sunday' - True or False
    if current_day == 'Sunday':
        send_email_by_ses()
    else:
        print("Sorry! Email can not be sent, today is " + current_day)


def get_email_list():
    email_address_list = ['mr2chow@uwaterloo.ca', 'email2masudur@gmail.com', 'jahidul2543@gmail.com,'
                      'm.mhudn@gmail.com', 'mdmasudur.rahman@yorkmail.cuny.edu',
                      'foysal.minhaz@gmail.com', 'mperven0@gmail.com']
    return email_address_list

# # To read from csv file
# def csv_reader():
#     data = read_csv('emaildata.csv')
#     name = data['name'].tolist()
#     email = data['email'].tolist()

def get_current_day():
    dt = datetime.now()  # get the current date time
    print('Datetime is:', dt)

    # get day name
    current_day = calendar.day_name[dt.weekday()]
    print('Weekday name is: ', current_day)
    return current_day


def send_email_by_ses():
    email_address_list = get_email_list()
    # data = read_csv("emaildata2.csv")
    # email_address_list = data['email'].tolist()
    # email_address_list = get_email_list()

    for emails_container in email_address_list[0:1]:
        user_name = emails_container.split('@')[0] # rahmanmdm16, gmail.com
        message = (f'Assalamualaikum Mr. {user_name}, Whoever can guarantee (the chastity of) what is between his two '
                   f'jaw-bones and what is between his two legs (i.e. his tongue and his private parts), '
                   f'I guarantee Paradise for him."')
        ses_send(emails_container, message)



def ses_send(email, message):
    response = client.send_email(
        Source='rahmanmdm16@gmail.com',
        Destination={
        'ToAddresses': ['mailtomaasud@gmail.com']
            },
        Message={
        'Subject': {
            'Data': 'Hadith of the day!',
        },
        'Body': {
            'Text': {
                'Data': message
            },
        }
    },
    ReplyToAddresses=['rahmanmdm16@gmail.com',
                      ],
    )

send_greetings()

