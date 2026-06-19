# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a REST API using the FastAPI framework so students can practice creating routes, handling JSON requests, and returning structured responses.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description
Set up a FastAPI application and define routes for the API.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Add a root `GET` endpoint that returns a welcome message.
- Add a `GET` endpoint with a path parameter to return details for a specific item.


### 🛠️ Use Request Models and JSON Payloads

#### Description
Define a Pydantic model for API data and build an endpoint that accepts JSON input.

#### Requirements
Completed program should:

- Define a Pydantic model for an item with fields like `id`, `name`, `description`, and `price`.
- Add a `POST` endpoint that accepts the model as request data.
- Return the created item in the response as JSON.


### 🛠️ Add Query Parameters and Error Handling

#### Description
Implement query parameters for filtering and handle invalid or missing data.

#### Requirements
Completed program should:

- Add a `GET` endpoint that accepts query parameters for filtering items.
- Return a list of matching items in JSON format.
- Use HTTP error responses (e.g. `404`) when an item cannot be found.
