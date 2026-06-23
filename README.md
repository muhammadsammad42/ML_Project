## End to End Machine Learning Project

## Render Deployment

This project is prepared for Render deployment.

### Files added
- render.yaml
- application.py as the Flask entry point

### Render setup
1. Create a new Web Service on Render.
2. Connect this GitHub repository.
3. Use the start command:
   - `gunicorn application:app`