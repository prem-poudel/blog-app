# Blog App: React + Django

Author: Prem Poudel

This is a Blog API built using Django REST Framework. It provides user authentication, user-specific blog views, and public blog access. The API is currently integrated into a React frontend, which is still under development.

## Features

- JWT-based user authentication
- Create and manage personal blog posts
- Access public blog posts
- Register, login, and view user list

## Project Structure

The project is organized into multiple Django apps:
- `account/` for user registration and login
- `blog/` for blog operations
- `api/` as the API root

## API Endpoints

### Authentication & User Management (`account/`)

- `POST /register/` — Register a new user
- `POST /login/` — Log in and obtain token
- `GET /users/` — List all registered users (secured)

### Blog APIs (`blog/`)

- `GET /user/` — List blogs created by the authenticated user
- `GET /public/` — List all public blog posts
