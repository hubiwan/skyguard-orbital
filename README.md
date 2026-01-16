# 📱 ctOS Profiler - Advanced OSINT Intelligence Tool

![Python](https://img.shields.io/badge/PYTHON-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/DJANGO-REST-092E20?style=for-the-badge&logo=django&logoColor=white)
![React](https://img.shields.io/badge/REACT-JS-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Capacitor](https://img.shields.io/badge/CAPACITOR-MOBILE-1199EE?style=for-the-badge&logo=capacitor&logoColor=white)

An advanced Open Source Intelligence (OSINT) web and mobile application inspired by the "Profiler" HUD from the Watch Dogs franchise. This tool allows users to scan digital footprints across multiple social platforms in real-time.

---

## 🛠 Tech Stack

This project follows Clean Code principles and a Decoupled Architecture:

* **Backend:** Python 3.x & Django REST Framework (Scalable API).
* **Frontend:** React.js (Component-based UI with Framer Motion animations).
* **Mobile:** Capacitor (Cross-platform native Android integration).
* **Database:** SQLite (Persistent logging of all scan activities).
* **Deployment:** Render.com (Cloud-based Backend Node).

---

## ✨ Key Features

* **Global Data Nodes:** Scans GitHub, Reddit, Facebook, Instagram, Steam, and Linktree.
* **Deep Interception:** Extracts public emails and geolocation data via GitHub API.
* **AI Personality Profiling:** Algorithmic subject analysis based on social presence and bio metadata.
* **Smart Filtering:** Content-analysis engine to eliminate "False Positive" results.
* **Central Data Log:** Automatic database logging of every identified subject (Viewable via Django Admin).

---

## 🚀 Installation & Setup

### 1. Backend Node (Django)

```bash
# Activate environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Start local server
python manage.py runserver
