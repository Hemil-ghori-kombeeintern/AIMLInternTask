# HTTP_REST_API_Complete_Notes

## 1. HTTP Basics

**HTTP = HyperText Transfer Protocol**

HTTP is a communication protocol used between a client and a server.

```
Client ───── HTTP Request ─────> Server
Client <──── HTTP Response ──── Server
```

Common clients:
- Browser
- React application
- Mobile application
- Postman
- Another server

Common servers:
- Node.js + Express
- Python + Flask/FastAPI
- Java + Spring Boot
- PHP

---

## 2. HTTP Request

A request is sent from client to server.

```
HTTP Request
├── Method
├── URL
├── Headers
├── Query Parameters
└── Body
```

Example:

```
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "name": "Hemil",
  "email": "hemil@example.com"
}
```

---

## 3. HTTP Response

A response is sent from server to client.

```
HTTP Response
├── Status Code
├── Headers
└── Body
```

Example:

```
HTTP/1.1 201 Created
Content-Type: application/json

{
  "message": "User created successfully"
}
```

---

## 4. Request-Response Cycle

```
Client
  │
  │ HTTP Request
  ↓
Server
  │
  │ Process request
  │ Database operation
  ↓
Client
  ↑
  │ HTTP Response
```

---

# URL

## 5. URL

**URL = Uniform Resource Locator**

Example:

```
https://api.example.com/users/10
```

Breakdown:

```
https://          → Protocol
api.example.com   → Domain
/users/10         → Path
```

Example with query parameters:

```
https://example.com/api/users?page=2&limit=10
```

```
/api/users        → Path
?page=2&limit=10  → Query parameters
```

---

# HTTP Methods

## 6. Main HTTP Methods

| Method | Purpose |
| --- | --- |
| GET | Read |
| POST | Create |
| PUT | Replace/update |
| PATCH | Partial update |
| DELETE | Delete |

---

## 7. GET

Used to retrieve data.

```
GET /api/users
GET /api/users/10
```

Example response:

```json
{
  "id": 10,
  "name": "Hemil"
}
```

GET should generally not modify server data.

---

## 8. POST

Used to create data.

```
POST /api/users
```

Body:

```json
{
  "name": "Hemil",
  "email": "hemil@example.com"
}
```

Common response:

```
201 Created
```

---

## 9. PUT

PUT generally replaces the resource representation.

```
PUT /api/users/10
```

Body:

```json
{
  "name": "Hemil Ghori",
  "email": "hemil@example.com",
  "age": 22
}
```

---

## 10. PATCH

PATCH is generally used for partial updates.

```
PATCH /api/users/10
```

Body:

```json
{
  "name": "Hemil Ghori"
}
```

### PUT vs PATCH

```
PUT   → Replace
PATCH → Partial update
```

---

## 11. DELETE

Used to delete a resource.

```
DELETE /api/users/10
```

Possible response:

```
204 No Content
```

---

# CRUD

## 12. CRUD Operations

```
Create → POST
Read   → GET
Update → PUT / PATCH
Delete → DELETE
```

Example:

```
POST   /api/users
GET    /api/users
GET    /api/users/10
PUT    /api/users/10
PATCH  /api/users/10
DELETE /api/users/10
```

---

# REST API

## 13. What is REST?

**REST = Representational State Transfer**

REST is an architectural style for designing web APIs.

REST APIs commonly use:
- HTTP methods
- Resources
- URLs/endpoints
- Status codes
- JSON
- Stateless communication

---

## 14. Resources

A resource is something an API manages.

Examples:

```
Users
Products
Orders
Students
Courses
Employees
```

Examples of resource URLs:

```
/api/users
/api/products
/api/orders
/api/students
```

---

## 15. RESTful Endpoints

Examples:

```
GET    /api/users       → Get users
GET    /api/users/10    → Get user 10
POST   /api/users       → Create user
PATCH  /api/users/10   → Update user 10
DELETE /api/users/10   → Delete user 10
```

Prefer resource-based endpoints:

```
/api/users
/api/products
```

Avoid unnecessary verb-based endpoints:

```
/api/getUsers
/api/createUser
/api/deleteUser
```

---

## 16. Nested Resources

For related resources:

```
GET /api/users/10/orders
GET /api/products/20/reviews
```

---

# Parameters

## 17. Query Parameters

Used for filtering, searching, sorting, and pagination.

Examples:

```
GET /api/products?category=laptop
GET /api/products?category=laptop&brand=asus
GET /api/products?page=2&limit=10
GET /api/products?sort=price
GET /api/products?search=laptop
```

---

## 18. Path Parameters

Used to identify a specific resource.

```
GET /api/users/25
```

Express example:

```jsx
app.get("/api/users/:id", (req, res) => {
    console.log(req.params.id);
});
```

For `/api/users/25`:

```
req.params.id → "25"
```

---

## 19. Query vs Path Parameter

### Path parameter

```
/api/users/25
```

```jsx
req.params.id
```

Used to identify a resource.

### Query parameter

```
/api/users?page=2
```

```jsx
req.query.page
```

Used for options such as filtering, sorting, and pagination.

---

# JSON

## 20. What is JSON?

**JSON = JavaScript Object Notation**

JSON is a common format for exchanging structured data.

```json
{
  "name": "Hemil",
  "age": 22,
  "student": true
}
```

---

## 21. JSON Data Types

### String

```json
{
  "name": "Hemil"
}
```

### Number

```json
{
  "age": 22
}
```

### Boolean

```json
{
  "isActive": true
}
```

### Null

```json
{
  "middleName": null
}
```

### Array

```json
{
  "skills": ["Python", "JavaScript", "React"]
}
```

### Object

```json
{
  "address": {
    "city": "Surat",
    "country": "India"
  }
}
```

---

## 22. JSON Rules

Valid JSON:

```json
{
  "name": "Hemil",
  "age": 22
}
```

Important:
- Object keys use double quotes.
- JSON does not support comments.
- JSON supports strings, numbers, booleans, null, arrays, and objects.

---

## 23. JSON Request

```
POST /api/users
Content-Type: application/json
```

```json
{
  "name": "Hemil",
  "email": "hemil@example.com"
}
```

---

## 24. JSON Response

```
HTTP/1.1 201 Created
Content-Type: application/json
```

```json
{
  "success": true,
  "message": "User created successfully",
  "data": {
    "id": 1,
    "name": "Hemil"
  }
}
```

---

# HTTP Headers

## 25. What Are Headers?

Headers provide additional information about a request or response.

Example:

```
Content-Type: application/json
Authorization: Bearer TOKEN
Accept: application/json
```

---

## 26. Content-Type

Tells the server the format of the request body.

```
Content-Type: application/json
```

Other examples:

```
text/html
text/plain
application/json
multipart/form-data
application/x-www-form-urlencoded
```

---

## 27. Accept

Tells the server what response format the client prefers.

```
Accept: application/json
```

---

## 28. Authorization

Used to send authentication credentials/tokens.

```
Authorization: Bearer YOUR_TOKEN
```

Common with JWT authentication.

---

## 29. User-Agent

Provides information about the client.

```
User-Agent: Mozilla/5.0
```

---

## 30. Host

Specifies the server host.

```
Host: example.com
```

---

## 31. Custom Headers

Applications can define custom headers when necessary.

```
X-Request-ID: 12345
```

Prefer standard headers when one already fits the requirement.

---

# HTTP Status Codes

## 32. Status Code Categories

```
1xx → Informational
2xx → Success
3xx → Redirection
4xx → Client error
5xx → Server error
```

---

## 33. Important 2xx Codes

### 200 OK

Request successful.

```
GET /api/users → 200 OK
```

### 201 Created

Resource successfully created.

```
POST /api/users → 201 Created
```

### 202 Accepted

Request accepted for processing.

### 204 No Content

Successful operation with no response body.

---

## 34. Important 3xx Codes

### 301 Moved Permanently

Resource permanently moved.

### 302 Found

Temporary redirect.

### 304 Not Modified

Cached representation is still valid.

---

## 35. Important 4xx Codes

### 400 Bad Request

Request is invalid.

### 401 Unauthorized

Authentication is missing or invalid.

### 403 Forbidden

Server understood the request but refuses authorization.

### 404 Not Found

Requested resource does not exist.

### 405 Method Not Allowed

Method is not supported for the endpoint.

### 409 Conflict

Request conflicts with the current resource state.

Example: duplicate email.

### 422 Unprocessable Content

Request is well-formed but submitted data fails validation.

---

## 36. Important 5xx Codes

### 500 Internal Server Error

Unexpected server-side error.

### 501 Not Implemented

Server does not support the requested functionality.

### 502 Bad Gateway

Gateway/proxy received an invalid upstream response.

### 503 Service Unavailable

Server is temporarily unable to handle the request.

---

## 37. Status Code Cheat Sheet

| Code | Meaning |
| --- | --- |
| 200 | OK |
| 201 | Created |
| 202 | Accepted |
| 204 | No Content |
| 301 | Moved Permanently |
| 304 | Not Modified |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 405 | Method Not Allowed |
| 409 | Conflict |
| 422 | Unprocessable Content |
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |

Memory:

```
2xx → Success
3xx → Redirection/cache
4xx → Client/request problem
5xx → Server problem
```

---

# Postman

## 38. What is Postman?

Postman is a tool for building, sending, testing, and documenting API requests.

```
Postman
   │
   │ HTTP Request
   ↓
Backend API
   │
   │ HTTP Response
   ↓
Postman
```

---

## 39. GET Request in Postman

Example:

```
GET http://localhost:5000/api/users
```

Click **Send**.

---

## 40. POST Request in Postman

Select:

```
POST
```

URL:

```
http://localhost:5000/api/users
```

Go to:

```
Body → raw → JSON
```

Body:

```json
{
  "name": "Hemil",
  "email": "hemil@example.com",
  "age": 22
}
```

Header:

```
Content-Type: application/json
```

Click **Send**.

---

## 41. PUT Request in Postman

```
PUT http://localhost:5000/api/users/1
```

Body:

```json
{
  "name": "Hemil Ghori",
  "email": "hemil@example.com",
  "age": 23
}
```

---

## 42. PATCH Request in Postman

```
PATCH http://localhost:5000/api/users/1
```

Body:

```json
{
  "age": 23
}
```

---

## 43. DELETE Request in Postman

```
DELETE http://localhost:5000/api/users/1
```

Usually no body is required.

---

## 44. Postman Query Parameters

Instead of manually writing:

```
http://localhost:5000/api/users?page=2&limit=10
```

Use:

```
Params
```

| KEY | VALUE |
| --- | --- |
| page | 2 |
| limit | 10 |

---

## 45. Postman Headers

Use the **Headers** tab.

| KEY | VALUE |
| --- | --- |
| Content-Type | application/json |
| Accept | application/json |
| Authorization | Bearer YOUR_TOKEN |

---

## 46. Postman Authentication

For JWT APIs:

```
Authorization
→ Type: Bearer Token
→ Token: YOUR_JWT_TOKEN
```

Postman sends:

```
Authorization: Bearer YOUR_JWT_TOKEN
```

---

## 47. Postman Environment Variables

Create:

```
BASE_URL = http://localhost:5000
```

Use:

```
{{BASE_URL}}/api/users
```

Production:

```
BASE_URL = https://api.example.com
```

---

## 48. Postman Collections

A collection groups related API requests.

```
User API
├── Register
├── Login
├── Get Users
├── Get User
├── Update User
└── Delete User
```

---

## 49. API Testing Checklist

### GET

- Successful request
- Empty result
- Invalid ID

### POST

- Valid data
- Missing required field
- Invalid data
- Duplicate data

### PUT/PATCH

- Valid update
- Invalid ID
- Invalid data

### DELETE

- Valid ID
- Invalid ID
- Already deleted resource

---

# Practical REST API Example

## 50. Student API Endpoints

```
GET     /api/students
GET     /api/students/:id
POST    /api/students
PUT     /api/students/:id
PATCH   /api/students/:id
DELETE  /api/students/:id
```

Student JSON:

```json
{
  "name": "Hemil",
  "email": "hemil@example.com",
  "age": 22,
  "course": "MSc IT"
}
```

---

## 51. Get All Students

```
GET /api/students
```

Response:

```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Hemil",
      "course": "MSc IT"
    }
  ]
}
```

Status:

```
200 OK
```

---

## 52. Get One Student

```
GET /api/students/1
```

---

## 53. Create Student

```
POST /api/students
```

Body:

```json
{
  "name": "Hemil",
  "course": "MSc IT"
}
```

Response:

```json
{
  "success": true,
  "message": "Student created successfully",
  "data": {
    "id": 1,
    "name": "Hemil",
    "course": "MSc IT"
  }
}
```

Status:

```
201 Created
```

---

## 54. Update Student

```
PATCH /api/students/1
```

Body:

```json
{
  "course": "MERN Stack"
}
```

---

## 55. Delete Student

```
DELETE /api/students/1
```

Possible status:

```
200 OK
```

or:

```
204 No Content
```

---

# Complete API Flow

```
                 CLIENT
              React / Postman
                    │
             HTTP Request
                    │
                    ↓
              ┌──────────┐
              │ Express  │
              │  Server  │
              └────┬─────┘
                   │
             Route/Controller
                   │
                   ↓
              ┌──────────┐
              │ Database │
              └────┬─────┘
                   │
                   ↓
              Server Logic
                   │
             HTTP Response
                   │
                   ↓
                 CLIENT
```

---

# Complete Request Example

```
POST /api/students HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Accept: application/json
Authorization: Bearer TOKEN

{
  "name": "Hemil",
  "course": "MSc IT"
}
```

Response:

```
HTTP/1.1 201 Created
Content-Type: application/json

{
  "success": true,
  "message": "Student created successfully",
  "data": {
    "id": 1,
    "name": "Hemil",
    "course": "MSc IT"
  }
}
```

---

# HTTP vs REST vs JSON vs Postman

```
HTTP
 ↓
Communication protocol

REST
 ↓
Architecture/style for designing APIs

JSON
 ↓
Data format

Postman
 ↓
Tool used to test APIs
```

---

### What is HTTP?

A protocol used for communication between clients and servers.

### What is REST API?

An API designed around REST principles and commonly using HTTP methods to operate on resources.

### GET vs POST?

```
GET  → Retrieve
POST → Create/submit data
```

### PUT vs PATCH?

```
PUT   → Replace resource representation
PATCH → Partial modification
```

### 401 vs 403?

```
401 → Authentication problem
403 → Authorization/permission problem
```

### 400 vs 422?

```
400 → Bad/invalid request
422 → Well-formed request but semantically invalid data
```

### What is JSON?

A text-based structured data format commonly used for API data exchange.

### What is a header?

Metadata/instructions associated with an HTTP request or response.

### What is a REST endpoint?

A URL through which a client accesses a particular API resource or operation.

---

---

# Final Revision Sheet

```
HTTP
│
├── Request
│   ├── Method
│   ├── URL
│   ├── Headers
│   ├── Query Params
│   └── Body
│
└── Response
    ├── Status Code
    ├── Headers
    └── Body

HTTP Methods
├── GET    → Read
├── POST   → Create
├── PUT    → Replace
├── PATCH  → Partial Update
└── DELETE → Delete

Status Codes
├── 2xx → Success
├── 3xx → Redirection
├── 4xx → Client/request error
└── 5xx → Server error

REST
├── Resources
├── Endpoints
├── HTTP methods
├── Stateless requests
└── JSON representations

Postman
├── Request
├── Params
├── Headers
├── Body
├── Authorization
├── Environment
└── Collections
```