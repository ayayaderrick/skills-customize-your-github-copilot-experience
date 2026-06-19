"""
Task Management System using SQLAlchemy

This starter code provides a foundation for building a task management system
with SQLAlchemy ORM. Complete the TODO sections to implement the full functionality.
"""

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# Create an in-memory SQLite database for this example
# In production, you'd use: sqlite:////path/to/database.db
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)


# TODO: Define the User model
class User(Base):
    __tablename__ = "users"
    
    # TODO: Add columns: id (primary key), username, email, created_at
    # Hint: Use Column(Integer, primary_key=True), Column(String), Column(DateTime)
    
    # Relationship to projects
    projects = relationship("Project", back_populates="user")
    
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"


# TODO: Define the Project model
class Project(Base):
    __tablename__ = "projects"
    
    # TODO: Add columns: id (primary key), name, description, user_id (foreign key), created_at
    
    # Relationship to user and tasks
    user = relationship("User", back_populates="projects")
    tasks = relationship("Task", back_populates="project")
    
    def __repr__(self):
        return f"<Project(name='{self.name}', user_id={self.user_id})>"


# TODO: Define the Task model
class Task(Base):
    __tablename__ = "tasks"
    
    # TODO: Add columns: id (primary key), title, description, status, project_id (foreign key), created_at, updated_at
    
    # Relationship to project
    project = relationship("Project", back_populates="tasks")
    
    def __repr__(self):
        return f"<Task(title='{self.title}', status='{self.status}')>"


# Create all tables
Base.metadata.create_all(engine)


# CRUD Operations
def create_user(username, email):
    """Create a new user and add to database"""
    # TODO: Implement this function
    # 1. Create a new User instance
    # 2. Add it to the session
    # 3. Commit the transaction
    # 4. Return the user
    pass


def get_projects_by_user(user_id):
    """Retrieve all projects for a specific user"""
    session = Session()
    # TODO: Query projects where user_id matches
    # Hint: use session.query(Project).filter(...)
    pass


def update_task_status(task_id, new_status):
    """Update a task's status"""
    session = Session()
    # TODO: Find the task by ID
    # TODO: Update its status
    # TODO: Update the updated_at timestamp to datetime.now()
    # TODO: Commit the changes
    pass


def delete_task(task_id):
    """Delete a task by ID"""
    session = Session()
    # TODO: Find and delete the task
    # TODO: Commit the changes
    pass


# Query Functions
def get_tasks_by_project(project_id):
    """Retrieve all tasks for a specific project"""
    session = Session()
    # TODO: Query tasks where project_id matches
    # TODO: Return the results
    pass


def count_tasks_by_user(user_id):
    """Count the total number of tasks for a user"""
    session = Session()
    # TODO: Join Users, Projects, and Tasks tables
    # TODO: Filter by user_id and count tasks
    # TODO: Return the count
    pass


def get_incomplete_tasks():
    """Find all incomplete tasks across all projects"""
    session = Session()
    # TODO: Query tasks where status is not 'completed'
    # TODO: Return the results
    pass


# Example usage (uncomment after implementing the functions above)
if __name__ == "__main__":
    # session = Session()
    
    # # Create some sample data
    # user1 = create_user("alice", "alice@example.com")
    # user2 = create_user("bob", "bob@example.com")
    
    # # TODO: Create projects and tasks
    
    # # TODO: Run queries and display results
    
    # session.close()
    pass
