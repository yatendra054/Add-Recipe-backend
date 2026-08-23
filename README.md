# Add-Recipe-backend
 
A full-stack recipe-sharing platform built with **Django** and **Bootstrap**, letting users create, manage, and share recipes — complete with social features, video recipes, an AI cooking assistant, and Redis-powered caching for speed.

## About

If you're new to the application, begin by navigating to the registration page to create an account with your username and password. Once registered, you can log in and start managing your recipes from your profile.

Users can add, update, and delete their own recipes. They can also add recipe videos, organize recipes into different categories, and explore recipes shared by other users.

The application provides social features that allow users to follow other recipe creators, like recipes, comment on recipes, and share their profiles. Users can also explore the most trending recipes based on user engagement.

The application also includes an integrated **AI Assistant** that provides an interactive experience. Users can ask the assistant questions related to recipes, ingredients, cooking methods, and other recipe-related topics.

**Redis** is used for caching frequently accessed recipe and trending content, which helps reduce repeated database queries and improves application performance.


<img src="home/Main_page.png" alt="Image 1" width="35%" height="200" style="display;">

<img src="home/Add_recipe.png" alt="Image 1" width="35%" height="200" style="display;">


<img src="home/about.png" alt="Image 1" width="35%" height="200" style="display;">

<img src="home/profile.png" alt="Image 1" width="35%" height="200" style="display;">


## Features

- User registration and login.
- Add, update, and delete recipes.
- Upload and share recipe videos.
- Categorize recipes for easy discovery.
- Follow other users and explore their recipes.
- Like and comment on recipes.
- Share user profiles.
- Explore trending recipes.
- Integrated AI Assistant for interactive recipe-related queries.
- Redis caching for frequently accessed content.


## Getting Started
 
### Prerequisites
 
- Python 3.10+
- pip
- Redis server (running locally or a hosted instance)
### Installation
 
1. Clone the repository
```bash
   git clone https://github.com/yatendra054/Add-Recipe-backend.git
   cd Add-Recipe-backend
```
 
2. Create and activate a virtual environment
```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
```
 
3. Install dependencies
```bash
   pip install -r requirements.txt
```
 
### Environment Variables
 
Create a `.env` file in the project root with the following (adjust to match your `settings.py`):
 
```env
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
REDIS_URL=redis://127.0.0.1:6379/0
# Add any AI Assistant API keys here, e.g.:
# OPENAI_API_KEY=your-key

```
## Live 
Code version is live [here](https://add-recipe-backennd.onrender.com/)

## Project Structure
 
```
Add-Recipe-backend/
├── Start/              # Project settings/config
├── recepe/             # Core recipe app (models, views, templates)
├── home/               # Static assets / screenshots
├── manage.py
├── requirements.txt
└── README.md
```

I welcome you to join us in making this project even better.By adding some more features.
   
