# 🛰️ SkyGuard - Real-time Orbital Tracking System

![Python](https://img.shields.io/badge/PYTHON-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/DJANGO-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Globe.GL](https://img.shields.io/badge/3D_VISUALIZATION-GLOBE.GL-FF3E00?style=for-the-badge&logo=three.js&logoColor=white)
![SQLite](https://img.shields.io/badge/DATABASE-SQLITE-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

**SkyGuard** is an advanced satellite monitoring system leveraging the **SGP4 physical model** for real-time 3D visualization and orbital pass predictions over key global locations.

---

<div align="center">
  <img src="screenshoot.png" alt="SkyGuard Dashboard" width="800" />
  <p><em>Real-time satellite tracking interface with Cyberpunk HUD styling</em></p>
</div>

---

## 🛠 Tech Stack

The project is built as a highly efficient web application without heavy frontend build tools (No-Build step):

* **Backend:** Python 3.12+ & Django 5.0.
* **Physics Engine:** `sgp4` library for orbital mechanics & `requests` for telemetry fetching.
* **Frontend:** HTML5, CSS3 (Cyberpunk HUD Aesthetic), JavaScript (ES6+).
* **Visualization:** `Globe.gl` (Three.js wrapper) loaded via CDN for high-performance 3D rendering.
* **Database:** SQLite (Integrated with Django).

---

## ✨ Key Features

* **Real-time 3D Rendering:** Interactive Earth model with live satellite orbit visualization.
* **SGP4 Implementation:** Custom physics engine calculating accurate trajectories from TLE data.
* **Orbital Predictions:** Algorithms to predict satellite passes over specific geographic locations.
* **Cyberpunk UI:** Immersive "Heads-Up Display" (HUD) interface style.
* **Zero-Config Frontend:** Libraries are loaded directly via CDN, removing the need for `npm` or webpack.

---

## 🚀 Installation & Setup

To run the project locally, you only need Python installed.

### 1. Backend Setup

Open your terminal in the root directory:

```bash
# 1. Install dependencies
pip install django sgp4 requests

# 2. Initialize Database (Migrations)
python manage.py migrate

# 3. Start Development Server
python manage.py runserver

2. Accessing the Application

Once the server is running, open your browser and navigate to:

http://127.0.0.1:8000/

Note: No npm install is required. All 3D libraries are fetched automatically via CDN upon loading the page.
📂 Project Structure

    /backend - Configuration Center: Contains global Django settings (settings.py) and the main URL router.

    /core - Application Logic: Main business logic, database models, and API views (views.py).

    /core/orbital_engine.py - The Heart of the System: Custom SGP4 implementation for TLE fetching, trajectory calculation, and coordinate conversion.

    /core/templates/ - Presentation Layer: Contains index.html which handles the Globe.gl initialization, HUD panels, and AJAX/Fetch API communication.

📄 License

This project is open-source.
