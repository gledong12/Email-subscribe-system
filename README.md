# Email Subscribe System
<div align="center">
  <img src="https://images.velog.io/images/eagle5424/post/120b7f03-79f8-4362-b2fe-0d8cee329bc3/Email%20(1).png"><br>
</div>



----------
## What is it?
**Email Subscribe System API** is a system that receives subscription data along with name, email, and subscription category and sends mail to subscribers according to each category.

## Project Structure
```
├── Email
├── user
├── data
│   └── data.sql
├── subscribe_email
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── wait-for-it.sh
```
* `Email`: Include API function code related to supscription and send mail
    * `SubscribeView` : The functions to accepts mail supscription requests that only the logged-in user receives a name, email or category
    * `UnsubscribeView` : The functions to accepts mail unsupscription requests that only the logged-in user 
    * `CheckingSubscriberView` : The function is that show full or subscription category userlist.
    * `SendingMailView` : The function is sending mail to all subscribed users.
    * `GetSendingListView` : The funtion is look up the sent email list
    * `DeleteEmailView` : The funtion is delete the email
    * `CheckShippingHistoryView` : The function is mailing History inquiry
* `user` : Include API feature code related to the user
    * `SignupView` : The function is to sign up for membership.
    * `SigninView` : The function issues tokens to users who have successfully logged in.
* `Dockerfile` : Files that record packages, environment variables, etc. that need to be installed in a container
* `docker-compose.yml` : Files for operating multiple containers (api, db) at a time
* `requirements.txt` : Define libraries required for development and deployment
* `wait-for-it.sh` : Scripts for troubleshooting the sequence of operations that depend on django server and db server during deployment

## ERD
URL : https://aquerytool.com:443/aquerymain/index/?rurl=6d5a2e65-ea02-449e-abab-f793d80c5214

Password : c01a08

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/gledong12/Email-subscribe-system

## Requirements
Docker: https://www.docker.com/get-started

## Installation from the git repo
```sh
$ git clone https://github.com/gledong12/Email-subscribe-system
$ cd Email_Subscribe
$ docker-compose up
```
## How to use
url lists are as follows
```
 - /api/v1/signup
 - /api/v1/signin
 - /api/v1/subscribe
 - /api/v1/unsubscribe
 - /api/v1/mail
 - /api/v1/inbox/<int:email_id>
 - /api/v1/deleteemail
 - /api/v1/checkshipping
```
## API test results in Development Server
API test(integration test) used [POSTMAN](https://www.postman.com)<br>
The URL below is a document about integration test in develop server<br>
Please use chrome or safari<br><br>
[The Document about API TEST](https://documenter.getpostman.com/view/14893614/TzY69Zj5)

## How to use the api in Web Browser
Try using a deployed web api !<br>
Please check a document below for how to use the API<br><br>
[The Document about How to use the API](https://www.notion.so/How-to-use-the-API-fde08c71c2944c17a315a8afbc4298a1) <br>

## ISSUE
I met and solved various issues during the project<br>
The URL below is a document about the issue in progress of the project<br><br>
[The Document about ISSUE](https://www.notion.so/Issue-0d1c139318d14fecab30f1302f5fde79)
