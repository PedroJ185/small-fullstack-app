FullStack Developer Home Exercise

Aplicação Full Stack robusta que consome dados externos das APIs **DummyJSON** (Users e Products), processa-os num servidor **Python** e apresenta-os numa interface **Vue.js** com funcionalidades avançadas de filtragem e análise de dados.

## 📋 Especificações Técnicas (Versões)

Este projeto foi desenvolvido e testado com as seguintes versões:
*   **Backend:** Python 3.12.10
*   **Frontend:** Vue.js 3.5.12 (Node.js v22.11.0 / npm 10.9.0)
*   **Comunicação:** Axios para pedidos HTTP e CORS Middleware no FastAPI.

---

### How do I get set up? ###
### Backend (Python + FastAPI)

1.  **Criar ambiente virtual:** `python -m venv venv`
2.  **Ativar o ambiente:**
    *   Windows (Git Bash): `source venv/Scripts/activate`
    *   Windows (CMD): `venv\Scripts\activate`
3.  **Instalar dependências:**
    ```bash
    pip install fastapi==0.115.4 uvicorn==0.32.0 requests==2.32.3
    ```
5.  **Iniciar Servidor:**
    ```bash
    uvicorn main:app --reload
    ```
    *Aceda à documentação automática da API em: `http://localhost:8000/docs`*

### 3. Frontend (Vue.js 3)
O Frontend oferece uma interface reativa com ordenação personalizada de cargos (Admin > Moderator > User) e filtros em tempo real.

1.  **Entrar na pasta:** `cd ../frontend` (ou `cd frontend` se estiveres na raiz)
2.  **Instalar pacotes:**
    ```bash
    npm install
    ```
3.  **Adicionar Axios:** (Caso não esteja no package.json)
    ```bash
    npm install axios
    ```
4.  **Iniciar aplicação:**
    ```bash
    npm run dev
    ```
    *Aceda à interface em: `http://localhost:5173`*

