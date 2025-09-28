# Online Poll System - ALX ProDev Backend Project

A Django REST API backend for an online polling system with real-time results.

## 🚀 Features

- **Poll Management**: Create and manage polls with multiple options
- **Voting System**: Cast votes with duplicate prevention
- **Real-time Results**: Calculate percentages and vote counts
- **REST API**: Full CRUD operations via API endpoints
- **Admin Interface**: Django admin for easy management

## 📋 API Documentation

### Base URL

http://127.0.0.1:8000/api/
### Endpoints

#### 1. List All Polls
**GET** `/polls/`

**Description**: Get a list of all available polls with their options and vote counts.

**Response:**
```json
{
  "polls": [
    {
      "id": 1,
      "question": "What is your favorite programming language?",
      "total_votes": 15,
      "options": [
        {
          "id": 1,
          "text": "Python",
          "vote_count": 8
        },
        {
          "id": 2, 
          "text": "JavaScript",
          "vote_count": 5
        },
        {
          "id": 3,
          "text": "Ruby",
          "vote_count": 2
        }
      ]
    }
  ]
}

2. Get Poll Details

GET /polls/{id}/

Description: Get detailed information about a specific poll.

Parameters:

id (integer): The ID of the poll

Example: GET /api/polls/1/

Response:
{
  "id": 1,
  "question": "What is your favorite programming language?",
  "total_votes": 15,
  "options": [
    {
      "id": 1,
      "text": "Python",
      "vote_count": 8
    },
    {
      "id": 2,
      "text": "JavaScript", 
      "vote_count": 5
    },
    {
      "id": 3,
      "text": "Ruby",
      "vote_count": 2
    }
  ]
}

3. Vote on Poll
POST /polls/{id}/vote/

Description: Cast a vote for a specific option in a poll.

Parameters:

id (integer): The ID of the poll

Body (form-data):
option_id: 1

Example: POST /api/polls/1/vote/

Success Response (200):
{
  "message": "Vote recorded successfully!",
  "vote_id": 45,
  "option_id": 1,
  "option_text": "Python",
  "poll_id": 1,
  "poll_question": "What is your favorite programming language?"
}
Error Responses:

400 Bad Request: {"error": "option_id is required"}

400 Bad Request: {"error": "You have already voted in this poll"}

400 Bad Request: {"error": "Invalid option_id"}

405 Method Not Allowed: {"error": "POST method required"}

4. Get Poll Results
GET /polls/{id}/results/

Description: Get real-time results with percentages for a poll.

Parameters:

id (integer): The ID of the poll

Example: GET /api/polls/1/results/

Response:
{
  "poll_id": 1,
  "poll_question": "What is your favorite programming language?",
  "total_votes": 15,
  "results": [
    {
      "option_id": 1,
      "option_text": "Python",
      "votes": 8,
      "percentage": 53.33
    },
    {
      "option_id": 2,
      "option_text": "JavaScript",
      "votes": 5,
      "percentage": 33.33
    },
    {
      "option_id": 3,
      "option_text": "Ruby", 
      "votes": 2,
      "percentage": 13.33
    }
  ]
}
🛠️ Technology Stack
Backend: Django 4.2 + Django REST Framework

Database: SQLite (development) / PostgreSQL (production)

Authentication: Session-based with IP duplicate prevention

Documentation: Built-in API docs

📦 Installation & Setup
# 1. Clone repository
git clone https://github.com/Tsi777/online-poll-system.git
cd online-poll-system/backend

# 2. Create virtual environment
python -m venv poll_env

# 3. Activate virtual environment
# Windows:
poll_env\Scripts\activate
# Mac/Linux:
source poll_env/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Create superuser (for admin access)
python manage.py createsuperuser

# 7. Load sample data (optional)
python add_sample_data.py

# 8. Start development server
python manage.py runserver

🎯 Usage
Access Points:
API Root: http://127.0.0.1:8000/

API Documentation: http://127.0.0.1:8000/api/docs/

Admin Interface: http://127.0.0.1:8000/admin/
Testing the API:

View all polls:

curl http://127.0.0.1:8000/api/polls/
View specific poll:

curl http://127.0.0.1:8000/api/polls/1/
Vote on a poll:

curl -X POST http://127.0.0.1:8000/api/polls/1/vote/ -d "option_id=1"
View results:

curl http://127.0.0.1:8000/api/polls/1/results/

🗃️ Database Models
Poll: Stores poll questions and metadata

Option: Stores possible answers for each poll

Vote: Records individual votes with IP-based duplicate prevention

👥 Contributors
Tsi777 - Backend Developer

What Each Section Does:
API Documentation: Shows exactly how to use each endpoint

Installation: Step-by-step setup instructions

Usage: Examples for testing the API

Technology Stack: Shows what technologies you used

Database Models: Explains your data structure
