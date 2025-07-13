# FastAPI and Gradio Integration Project

This project integrates a FastAPI application with a Gradio demo, providing a simple interface for machine learning models along with a health check endpoint.

## Project Structure

```
fastapi-gradio-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── gradio_app.py    # Gradio demo setup
│   └── api
│       └── health.py    # Health check endpoint
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd fastapi-gradio-app
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:

```bash
uvicorn src.main:app --reload
```

This will start the FastAPI server, and you can access the Gradio demo at `http://localhost:8000`.

## Health Check Endpoint

The application includes a health check endpoint that can be accessed at `http://localhost:8000/health`. This endpoint returns a JSON response indicating the status of the application.

## License

This project is licensed under the MIT License. See the LICENSE file for details.