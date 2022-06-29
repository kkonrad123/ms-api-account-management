# Description
Account Management tool service allows you to add, delete, retrieve account data by calling the URL with correct HTTP request method.

# Requirements
- Docker

# Deployment
Docker is our main deployment method, run the following to start your service

```
docker build -t new_app_image .
docker run -d --name new_container_name -p 80:80 new_app_image
```

Now that your service is running in the background, you can access it using `http://127.0.0.1/docs`

# Example Requests

## API Resources

  - [GET /health](#api-health)
  - [GET /accounts/[id]](#api-get-account)
  - [POST /accounts/[account_id]](#api-create-account)
  - [DELETE /accounts/[account_id]](#api-delete-account)

### [GET](#api-health) [/health]

Example: http://127.0.0.1/health

Response body:

    {
        "status":true
    }

### [GET](#api-get-account) /accounts/[account_id]

Example: http://127.0.0.1/accounts/1

Response body:

    {
        "name": "joe",
        "balance": 500,
        "active": true,
        "description": null
    }

### [POST](#api-create-account) /accounts/[account_id]

Example: http://127.0.0.1/accounts/4

Request body:

    {
        "name": "new_account",
        "description": "info",
        "balance": 1200,
        "active": true
    }

### [DELETE](#api-delete-account) /accounts/[account_id]

Example: http://127.0.0.1/accounts/1

Response body:

    {
        true
    }


# Improvements
- more functions & tests such as disabling and re-enabling accounts based on the class parameter that is available, or even querying multiple accounts at once with support for filtering.
- publishing python package as artifact and reusing it inside Dockerfile.
- implementing UI for calling the APIs which makes it easier for customers to use.
- applying rate limiting on resources based on your needs.
- having dedicated environments for your APIs that you can test before releasing to prod.
- having SSL certificates enabled on your endpoint and extra security measures such as token validation through various API manager tools.
- better error descriptions for easier use of the API.
- implement monitoring and alerting
- implement logging