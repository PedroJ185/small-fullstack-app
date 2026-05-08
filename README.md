FullStack Developer Home Exercise

### How do I get set up? ###

This project was developed and tested with the following versions:
*   **Backend:** Python 3.12.10
*   **Frontend:** Vue.js 3.5.12 (Node.js v22.11.0 / npm 10.9.0)
*   **Communication:** Axios for HTTP requests and CORS middleware in FastAPI.

---

### How do I start the application
### Backend (Python + FastAPI)

1.  **Create a virtual environment:** `python -m venv venv`
2.  **Activate the environment:**
    *   Windows (Git Bash): `source venv/Scripts/activate`
    *   Windows (CMD): `venv\Scripts\activate`
3.  **Install dependencies:**
    ```bash
    pip install fastapi uvicorn requests
    ```
4.  **Start the server:**
    ```bash
    uvicorn main:app --reload
    ```

### Frontend (Vue.js 3)

1.  **Install packages:**
    ```bash
    npm install
    ```
2.  **Add Axios:** (If it is not already included in package.json)
    ```bash
    npm install axios
    ```
3.  **Start the application:**
    ```bash
    npm run dev
    ```

