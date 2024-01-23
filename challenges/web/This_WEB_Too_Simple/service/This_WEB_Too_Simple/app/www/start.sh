#!/bin/bash
# Run the database setup script
python create_db.py

# Start the Flask application
flask run --host=0.0.0.0
