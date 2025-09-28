# Online Poll System - ALX ProDev Backend Project

A Django REST API backend for an online polling system with real-time results.

## 🚀 Features

- **Poll Management**: Create and manage polls with multiple options
- **Voting System**: Cast votes with duplicate prevention
- **Real-time Results**: Calculate percentages and vote counts
- **REST API**: Full CRUD operations via API endpoints
- **Admin Interface**: Django admin for easy management

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/polls/` | List all polls |
| GET | `/api/polls/{id}/` | Get poll details |
| POST | `/api/polls/{id}/vote/` | Vote on a poll |
| GET | `/api/polls/{id}/results/` | Get poll results |

## 🛠️ Technology Stack

- **Backend**: Django 4.2 + Django REST Framework
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: Session-based
- **Documentation**: Swagger/OpenAPI

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/Tsi777/online-poll-system.git
cd online-poll-system/backend

# Create virtual environment
python -m venv poll_env
source poll_env/bin/activate  # Windows: poll_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver

🎯 Usage
Access Admin: http://127.0.0.1:8000/admin/

Create Polls: Add polls and options through admin

API Documentation: http://127.0.0.1:8000/api/docs/

Test Endpoints: Use the API endpoints for voting

👥 Contributors
Tsi777 - Backend Developer
[Frontend Partner] - Frontend Developer

📄 License
MIT License - see LICENSE file for details

### Step 3: Add README and Finalize

```powershell
# Add README
git add README.md

# Final commit
git commit -m "docs: add comprehensive README with setup instructions"

# Push to GitHub
git push origin main

Step 4: Prepare for Submission
Create submission checklist:

✅ All API endpoints working

✅ Database models properly designed

✅ Voting system with duplicate prevention

✅ Real-time results calculation

✅ Error handling and validation

✅ Code committed to GitHub

✅ README documentation complete

✅ Admin interface functional

Step 5: Test Complete System One Last Time
Final verification test:
python test_real_system.py

