# Email_Subscribe_System_API

----------
## What is it?
**Email Subscribe System API**  is a system that receives subscription subscriptions along with name, email, and subscription category information and sends mail to subscribers of each category.

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
    * `CheckShippingHistoryView` : The function is mailing History inquiry
* `user` : Include API feature code related to the user
    * `Signup` : The function is to sign up for membership.
    * `Signin` : The function issues tokens to users who have successfully logged in.
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
 - /api/v1/checksubscribe
 - /api/v1/mail
 - /api/v1/inbox/<int:email_id>
 - /api/v1/checkshipping
```