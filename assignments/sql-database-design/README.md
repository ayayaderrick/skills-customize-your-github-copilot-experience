# 📘 Assignment: SQL & Database Design with Python

## 🎯 Objective

Learn how to design relational databases, write SQL queries, and interact with databases from Python using SQLAlchemy. You'll build a task management system that stores, retrieves, and updates data in a persistent database.

## 📝 Tasks

### 🛠️ Design a Database Schema

#### Description
Design and create a relational database schema for a task management system. Your schema should include tables for users, projects, and tasks with appropriate relationships and constraints.

#### Requirements
Completed program should:

- Create a `users` table with fields: `id`, `username`, `email`, and `created_at`
- Create a `projects` table with fields: `id`, `name`, `description`, `user_id` (foreign key), and `created_at`
- Create a `tasks` table with fields: `id`, `title`, `description`, `status`, `project_id` (foreign key), `created_at`, and `updated_at`
- Use appropriate data types (INTEGER, VARCHAR, TEXT, DATETIME, etc.)
- Define primary keys and foreign key relationships
- Add constraints such as NOT NULL and UNIQUE where appropriate

### 🛠️ Create CRUD Operations

#### Description
Implement Create, Read, Update, and Delete (CRUD) operations using SQLAlchemy to interact with your database. Write functions to manage users, projects, and tasks.

#### Requirements
Completed program should:

- Implement a function to create a new user and insert it into the database
- Implement a function to retrieve all projects for a specific user
- Implement a function to update a task's status (e.g., "pending" to "completed")
- Implement a function to delete a task by its ID
- Use SQLAlchemy ORM methods (`.query()`, `.add()`, `.commit()`, `.filter()`, etc.)
- Handle errors appropriately (e.g., task not found)

### 🛠️ Write and Execute Queries

#### Description
Write SQL queries that retrieve meaningful insights from your database. Examples include getting tasks for a specific project, filtering tasks by status, or counting tasks per user.

#### Requirements
Completed program should:

- Write a query to retrieve all tasks for a specific project with their status
- Write a query to count the total number of tasks per user
- Write a query to find all incomplete tasks across all projects
- Display results in a readable format
- Use filtering, sorting, and aggregation functions as appropriate

