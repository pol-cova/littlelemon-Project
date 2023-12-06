# LittleLemon Capstone Documentation 🚀

Welcome to the API documentation for [Your API Name]! This documentation provides comprehensive details on how to integrate and use our powerful API.

## Table of Contents 📑

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Endpoints](#endpoints)
  - [Authentication](#authentication)
  - [Request Examples](#request-examples)
- [Response Codes](#response-codes)
- [Testing](#testing)

## Introduction 🌐


## Getting Started 🚀

### Prerequisites 🛠️

Before you start, make sure you have the following installed:

- python
- Insomnia, Postman or API testing tool 

### Installation 💻

1. Clone the repository: `git clone https://github.com/pol-cova/littlelemon-Project.git`
2. Activate virtual enviroment: `(unix) source venv/bin/activate` or `(windows) venv\Scripts\activate`
3. Check migrations `python manage.py makemigrations`
4. Run migrations `python manage.py migrate` 
5. Run API `python manage.py runserver`

## Usage 🤖

### Endpoints 🛤️

Our API provides the following endpoints:

- `/api/menu-items/`: To see the full menu list 
- `/api/menu-items/<int:pk>/`: To see a specific menu item 
- `/api/booking/`: To make a reservation 


### Authentication 🔐

To add items to menu to my API, you need to obtain an Token. Follow these steps:

1. Go to `/auth/users/` if you don't have an user or `/auth/token/login/` 
2. Insert your credentials to get your token
3. Include the API Token in the request header: `Authorization: Token YOUR_TOKEN_KEY`

### Request Examples 📡

Here's a sample cURL request:

```bash
curl -X GET http://localhost:8000/api/menu-items/
```
## Response Codes 📊

- **200 OK**: Successful request
- **401 Unauthorized**: Unauthorized access
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server-side error

## Testing 🧪

We take pride in our comprehensive test coverage for API functionality. To run this test run the command: 

```bash
python manage.py test