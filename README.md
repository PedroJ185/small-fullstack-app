FullStack Developer Home Exercise

### How do I get set up? ###

Este projeto foi desenvolvido e testado com as seguintes versões:
*   **Backend:** Python 3.12.10
*   **Frontend:** Vue.js 3.5.12 (Node.js v22.11.0 / npm 10.9.0)
*   **Comunicação:** Axios for HTTP requests and CORS middleware in FastAPI.

---

### How do I start the application
### Backend (Python + FastAPI)

1.  **Criar ambiente virtual:** `python -m venv venv`
2.  **Ativar o ambiente:**
    *   Windows (Git Bash): `source venv/Scripts/activate`
    *   Windows (CMD): `venv\Scripts\activate`
3.  **Instalar dependências:**
    ```bash
    pip install fastapi uvicorn requests
    ```
4.  **Iniciar Servidor:**
    ```bash
    uvicorn main:app --reload
    ```

### Frontend (Vue.js 3)

1.  **Instalar pacotes:**
    ```bash
    npm install
    ```
2.  **Adicionar Axios:** (Caso não esteja no package.json)
    ```bash
    npm install axios
    ```
3.  **Iniciar aplicação:**
    ```bash
    npm run dev
    ```

