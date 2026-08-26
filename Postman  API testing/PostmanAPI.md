# Postman_API_Testing_Complete_Notes

## 1. What is Postman?

**Postman** is a tool used to develop, test, and debug APIs.

You can use Postman to:
- Send HTTP requests
- Test GET, POST, PUT, PATCH, DELETE
- Send query/path parameters
- Send headers and JSON bodies
- Test authentication and JWT
- Inspect responses and status codes
- Create collections and environments
- Write automated API tests

---

# 2. HTTP Request and Response

An API interaction looks like:

```
Client
  |
  | HTTP Request
  v
Server / API
  |
  | HTTP Response
  v
Client
```

### Request contains

```
HTTP Method
URL
Headers
Parameters
Body
Authentication
```

Example:

```
POST /api/users
Content-Type: application/json
Authorization: Bearer YOUR_TOKEN
```

Request body:

```json
{
  "name": "Hemil",
  "email": "hemil@example.com",
  "password": "123456"
}
```

### Response contains

```
Status Code
Headers
Body
```

Example:

```
201 Created
Content-Type: application/json
```

Response body:

```json
{
  "message": "User created successfully",
  "user": {
    "id": 1,
    "name": "Hemil",
    "email": "hemil@example.com"
  }
}
```

---

# 3. Postman Interface

Important sections:

```
Workspace
Collections
Requests
Method
URL
Params
Authorization
Headers
Body
Scripts
Tests
Response
```

Common request tabs:

```
Params
Authorization
Headers
Body
Scripts
Settings
```

---

# 4. Create a Collection

A **Collection** organizes related API requests.

Example:

```
Backend API
├── Auth
│   ├── Register
│   └── Login
├── Users
│   ├── Get Users
│   ├── Get User
│   ├── Update User
│   └── Delete User
└── Products
    ├── Get Products
    └── Create Product
```

### Why use collections?

- Organize API requests
- Reuse requests
- Store related tests
- Run multiple requests
- Share API test suites

---

# 5. Create and Send a Request

Steps:

```
New Request
→ Select HTTP Method
→ Enter URL
→ Add Params / Headers / Body
→ Click Send
→ Check Response
```

Example:

```
GET http://localhost:5000/api/users
```

---

# 6. GET Request

### Definition

`GET` retrieves data.

```
GET http://localhost:5000/api/users
```

Usually no request body is required.

### Response

```
200 OK
```

```json
{
  "success": true,
  "users": [
    {
      "id": 1,
      "name": "Hemil",
      "email": "hemil@example.com"
    },
    {
      "id": 2,
      "name": "Rahul",
      "email": "rahul@example.com"
    }
  ]
}
```

Get one user:

```
GET http://localhost:5000/api/users/1
```

---

# 7. Query Parameters

Query parameters send optional filtering/search information.

Example:

```
GET http://localhost:5000/api/users?city=Surat&age=22
```

In Postman:

```
Params

KEY     VALUE
city    Surat
age     22
```

Common parameters:

```
search
page
limit
sort
filter
category
```

Example:

```
GET /api/products?search=laptop&page=1&limit=10
```

---

# 8. Path Parameters

Path parameters identify a specific resource.

```
GET /api/users/123
```

Here:

```
123 = user ID
```

Backend route example:

```jsx
app.get('/api/users/:id', ...)
```

Access it with:

```jsx
req.params.id
```

---

# 9. POST Request

### Definition

`POST` is commonly used to create a resource.

```
POST http://localhost:5000/api/users
```

In Postman:

```
Body
→ raw
→ JSON
```

Body:

```json
{
  "name": "Hemil",
  "email": "hemil@example.com",
  "password": "123456"
}
```

Header:

```
Content-Type: application/json
```

Response:

```
201 Created
```

```json
{
  "success": true,
  "message": "User created successfully",
  "user": {
    "id": 10,
    "name": "Hemil",
    "email": "hemil@example.com"
  }
}
```

---

# 10. PUT Request

### Definition

`PUT` is commonly used to replace/update a resource.

```
PUT http://localhost:5000/api/users/10
```

Body:

```json
{
  "name": "Hemil Ghori",
  "email": "hemil@example.com",
  "city": "Surat"
}
```

Response:

```
200 OK
```

```json
{
  "success": true,
  "message": "User updated successfully"
}
```

---

# 11. PATCH Request

### Definition

`PATCH` is commonly used for a partial update.

```
PATCH http://localhost:5000/api/users/10
```

Body:

```json
{
  "city": "Ahmedabad"
}
```

Response:

```json
{
  "success": true,
  "message": "User updated successfully"
}
```

### PUT vs PATCH

```
PUT
→ Usually sends the complete resource representation

PATCH
→ Usually sends only fields that need to change
```

Exact behavior depends on the API.

---

# 12. DELETE Request

### Definition

`DELETE` removes a resource.

```
DELETE http://localhost:5000/api/users/10
```

Response:

```
200 OK
```

```json
{
  "success": true,
  "message": "User deleted successfully"
}
```

Another common response:

```
204 No Content
```

---

# 13. HTTP Methods Cheat Sheet

| Method | Purpose | Body |
| --- | --- | --- |
| GET | Read data | Usually no |
| POST | Create data | Usually yes |
| PUT | Replace/update | Usually yes |
| PATCH | Partial update | Usually yes |
| DELETE | Delete data | Usually no |

---

# 14. Request Headers

Headers provide additional information.

Common headers:

```
Content-Type
Accept
Authorization
User-Agent
```

### Content-Type

```
Content-Type: application/json
```

Tells the server that the body contains JSON.

### Accept

```
Accept: application/json
```

Tells the server what response format the client accepts.

### Authorization

```
Authorization: Bearer YOUR_JWT_TOKEN
```

Used for authenticated APIs.

---

# 15. JSON Request Body

In Postman:

```
Body
→ raw
→ JSON
```

Example:

```json
{
  "name": "Hemil",
  "email": "hemil@example.com",
  "age": 22,
  "skills": ["Python", "MERN", "SQL"]
}
```

JSON data types:

```
String
Number
Boolean
Array
Object
null
```

Example:

```json
{
  "name": "Hemil",
  "age": 22,
  "isActive": true,
  "skills": ["Python", "SQL"],
  "address": {
    "city": "Surat"
  },
  "middleName": null
}
```

---

# 16. Form Data

Use:

```
Body
→ form-data
```

Useful for:

- Form fields
- Files
- Images
- Documents

Example:

```
KEY       VALUE
name      Hemil
email     hemil@example.com
profile   profile.jpg
```

For a file, change the field type from `Text` to `File`.

---

# 17. Authentication

Authentication verifies who the user is.

Common API authentication methods:

```
API Key
Bearer Token
JWT
Basic Auth
OAuth 2.0
```

For MERN backend APIs, JWT Bearer authentication is especially important.

---

# 18. JWT Authentication

JWT means **JSON Web Token**.

Typical flow:

```
Login
  ↓
Server validates email/password
  ↓
Server generates JWT
  ↓
Client receives JWT
  ↓
Client sends JWT with protected requests
  ↓
Server verifies JWT
  ↓
Access granted / denied
```

---

# 19. Login Request

Example:

```
POST http://localhost:5000/api/auth/login
```

Body:

```json
{
  "email": "hemil@example.com",
  "password": "123456"
}
```

Response:

```json
{
  "success": true,
  "message": "Login successful",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

# 20. Send JWT Token

For a protected API:

```
GET http://localhost:5000/api/profile
```

### Using Authorization tab

In Postman:

```
Authorization
→ Type: Bearer Token
→ Token: YOUR_JWT_TOKEN
```

Postman sends:

```
Authorization: Bearer YOUR_JWT_TOKEN
```

### Using Headers

```
KEY             VALUE
Authorization  Bearer YOUR_JWT_TOKEN
```

---

# 21. Protected API Responses

Successful:

```
200 OK
```

```json
{
  "success": true,
  "user": {
    "id": 10,
    "name": "Hemil",
    "email": "hemil@example.com"
  }
}
```

Missing token:

```
401 Unauthorized
```

```json
{
  "success": false,
  "message": "Authentication required"
}
```

Invalid/expired token:

```
401 Unauthorized
```

```json
{
  "success": false,
  "message": "Invalid or expired token"
}
```

---

# 22. HTTP Status Codes

## 2xx — Success

```
200 OK
→ Request succeeded

201 Created
→ Resource created

204 No Content
→ Request succeeded with no response body
```

## 3xx — Redirection

```
301 Moved Permanently
302 Found
304 Not Modified
```

## 4xx — Client Errors

```
400 Bad Request
→ Invalid request/data

401 Unauthorized
→ Authentication missing/invalid

403 Forbidden
→ Authenticated but not allowed

404 Not Found
→ Resource/route not found

409 Conflict
→ Conflicting request/data

422 Unprocessable Content
→ Validation failed
```

## 5xx — Server Errors

```
500 Internal Server Error
→ Server-side error

502 Bad Gateway
→ Invalid response from upstream server

503 Service Unavailable
→ Server temporarily unavailable
```

---

# 23. Check a Response in Postman

After clicking **Send**, inspect:

```
Status
Time
Size
Body
Headers
Cookies
```

Example:

```
Status: 200 OK
Time: 120 ms
Size: 450 B
```

Response body:

```json
{
  "success": true,
  "message": "Users fetched successfully"
}
```

Response header:

```
Content-Type: application/json
```

---

# 24. Postman Variables

Variables make requests reusable.

Example:

```
base_url = http://localhost:5000
jwt_token = YOUR_TOKEN
user_id = 10
```

Use:

```
{{base_url}}/api/users
```

```
{{base_url}}/api/users/{{user_id}}
```

Authorization:

```
Bearer {{jwt_token}}
```

---

# 25. Environments

Create environments such as:

```
Development
Testing
Production
```

Development:

```
base_url = http://localhost:5000
```

Production:

```
base_url = https://api.example.com
```

Request:

```
{{base_url}}/api/users
```

This lets you change environments without editing every request.

---

# 26. Complete CRUD API Testing

Assume:

```
Base URL:
http://localhost:5000
```

## Create

```
POST {{base_url}}/api/users
```

Body:

```json
{
  "name": "Hemil",
  "email": "hemil@example.com",
  "password": "123456"
}
```

Expected:

```
201 Created
```

## Read All

```
GET {{base_url}}/api/users
```

Expected:

```
200 OK
```

## Read One

```
GET {{base_url}}/api/users/1
```

Expected:

```
200 OK
```

## Update

```
PUT {{base_url}}/api/users/1
```

Body:

```json
{
  "name": "Hemil Ghori",
  "email": "hemil@example.com"
}
```

Expected:

```
200 OK
```

## Partial Update

```
PATCH {{base_url}}/api/users/1
```

Body:

```json
{
  "name": "Hemil"
}
```

Expected:

```
200 OK
```

## Delete

```
DELETE {{base_url}}/api/users/1
```

Expected:

```
200 OK
```

or:

```
204 No Content
```

---

# 27. Complete API Testing Flow

```
Register
   ↓
Login
   ↓
Receive JWT
   ↓
Save JWT to variable
   ↓
GET protected data
   ↓
POST new data
   ↓
PUT data
   ↓
PATCH data
   ↓
DELETE data
   ↓
Test invalid requests
   ↓
Verify status codes
   ↓
Verify response JSON
```

---