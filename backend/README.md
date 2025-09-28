# 🗳️ Online Poll System Backend

A complete Django REST API backend for creating polls, voting, and real-time result computation.

## 🚀 Features

- **Poll Management** - Create and manage polls with multiple options
- **Voting System** - Cast votes with proper validation
- **Real-time Results** - Compute vote counts and percentages
- **RESTful API** - Complete CRUD operations
- **API Documentation** - Swagger/OpenAPI documentation

## 📊 API Endpoints

- `GET  /api/polls/` - List all polls
- `GET  /api/polls/{id}/` - Get poll details
- `POST /api/polls/{id}/vote/` - Vote on a poll
- `GET  /api/polls/{id}/results/` - Get poll results

## 🛠️ Technologies Used

- **Django** & **Django REST Framework**
- **PostgreSQL** Database
- **Swagger** for API documentation
- **Unit Testing** with Django Test Framework

## ⚡ Quick Start

```bash
# 1. Setup environment
python -m venv venv
venv\Scripts\activate  # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup database
python manage.py migrate
python manage.py create_sample_data

# 4. Run server
python manage.py runserver
🧪 Testing
bash
python manage.py test polls
📚 API Documentation
Visit /api/swagger/ for interactive API documentation.

🎯 Project Goals Achieved
✅ API Development for poll creation, voting, and results
✅ Database efficiency with optimized schemas
✅ API Documentation with Swagger
✅ Unit Testing with comprehensive test coverage
✅ Real-world application simulating voting systems
