# Cloud-Native Full-Stack Energy Analytics Dashboard

This project is a cloud-based full-stack web application designed to collect, process, and visualize energy consumption data. The frontend dashboard allows users to view real-time and historical analytics, while the backend processes data using Python APIs deployed on AWS.

## Features

- Real-time energy consumption monitoring
- Historical data visualization with interactive charts
- RESTful API for data collection and retrieval
- Containerized deployment with Docker
- CI/CD ready for seamless deployment

## Tech Stack

- **Frontend**: React.js with Chart.js for data visualization
- **Backend**: Python FastAPI
- **Database**: SQLite (development), PostgreSQL (production on AWS RDS)
- **Deployment**: Docker, AWS (planned)

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Node.js (for local frontend development)
- Python 3.11+ (for local backend development)

### Running with Docker Compose

1. Clone the repository
2. Navigate to the project directory
3. Run `docker-compose up --build`

The frontend will be available at `http://localhost:3000` and the backend API at `http://localhost:8000`.

### Local Development

#### Backend

1. Navigate to `backend/` directory
2. Create virtual environment: `python -m venv venv`
3. Activate venv: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the server: `python main.py`

#### Frontend

1. Navigate to `frontend/` directory
2. Install dependencies: `npm install`
3. Start the development server: `npm start`

## API Endpoints

- `GET /api/v1/data` - Retrieve energy consumption data
- `POST /api/v1/data` - Collect new energy data
- `GET /api/v1/summary/{period}` - Get consumption summary
- `POST /api/v1/data/generate` - Generate mock data for testing

## Project Structure

```
energy-analytics-dashboard/
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── routes/
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── public/
│   └── src/
├── docs/
├── docker-compose.yml
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
