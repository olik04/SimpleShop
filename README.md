# Installation
1. Clone the repository
2. Create a virtual environment
   ```commandline
    python -m venv venv
    ```
3. Activate the virtual environment \
For windows:
    ```commandline
     venv\Scripts\activate
     ```
   \
For MacOS/Linux:
    ```commandline
    source venv/bin/activate
    ```
4. Install the requirements
    ```commandline
    python -m pip install -r requirements.txt
    ```
5. Run docker containers \
For Windows:
    ```commandline
    docker-compose up -d
    ```
   \
For MacOS/Linux:
    ```commandline
    docker compose up -d
    ```

6. Run the application
    ```commandline
    python main.py
    ```
7. Open the browser and go to http://localhost:8000/docs