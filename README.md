# ⚡ Trimly — AI-Powered URL Shortener

A full-stack **AI-powered** URL shortener built with **FastAPI**, **Google Gemini AI**, **SQLite**, and vanilla **HTML/CSS/JS**.  
Trim long URLs, get AI-generated summaries, track clicks, generate QR codes, and manage links with a personal account.

---

## 🚀 Live Features

| Feature | Status |
|---|---|
| 🔗 URL Shortening (auto + custom alias) | ✅ |
| 🤖 **AI URL Summarizer (Google Gemini)** | ✅ |
| 🔐 JWT Authentication (Register / Login) | ✅ |
| 👤 User dashboard & personal links | ✅ |
| 📊 Click analytics with Chart.js | ✅ |
| 🖼️ QR Code generator (downloadable PNG) | ✅ |
| 🌙 Dark / Light mode toggle | ✅ |
| 📱 Fully responsive design | ✅ |
| 📄 Swagger API docs at `/docs` | ✅ |

---

## 🤖 AI Feature — URL Summarizer

When a URL is shortened, **Google Gemini AI** automatically generates a one-line description of what the link is about.

```json
POST /shorten
{ "long_url": "https://www.github.com" }

Response:
{
  "short_code": "4E6Mb2",
  "short_url": "http://localhost:8000/4E6Mb2",
  "summary": "GitHub is a platform for hosting code, version control, and collaborative software development.",
  ...
}
```

**How it works:**
- Calls **Gemini API** on every new URL shortened
- Uses **multi-model fallback** — tries `gemini-2.0-flash` → `gemini-2.0-flash-lite` → `gemini-2.5-flash` automatically
- Backfills summaries for older URLs that were created before AI was added
- Gracefully degrades — app works normally even if API key is not set

---

## 📸 Screenshots

### API Docs (Swagger UI)
![Swagger UI](screenshots/SwaggerUI.png)

### Frontend UI
![Frontend UI](screenshots/Frontend.png)

---

## 🛠️ Tech Stack

**Backend**
- [FastAPI](https://fastapi.tiangolo.com/) — Modern Python web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM for database interaction
- [SQLite](https://www.sqlite.org/) — Lightweight database, zero setup
- [Google Gemini AI](https://ai.google.dev/) — AI-powered URL summarization
- [python-jose](https://python-jose.readthedocs.io/) — JWT token generation & validation
- [bcrypt](https://pypi.org/project/bcrypt/) — Secure password hashing
- [qrcode](https://pypi.org/project/qrcode/) — QR code image generation

**Frontend**
- Vanilla HTML / CSS / JavaScript
- [Tailwind CSS](https://tailwindcss.com/) (via CDN)
- [Chart.js](https://www.chartjs.org/) — Analytics bar chart
- [Material Symbols](https://fonts.google.com/icons) — Icons

---

## 📁 Project Structure

```
url-shortener/
│
├── backend/
│   ├── main.py          # FastAPI app & all API routes
│   ├── ai.py            # Google Gemini AI summarizer (multi-model fallback)
│   ├── auth.py          # JWT auth logic (tokens, hashing)
│   ├── models.py        # Database table definitions (User, URL)
│   ├── schemas.py       # Pydantic request/response models
│   ├── database.py      # DB connection, session setup & migrations
│   ├── utils.py         # URL validation & short code generator
│   └── requirements.txt # Python dependencies
│
├── frontend/
│   └── index.html       # Complete UI (single page app)
│
├── db/
│   └── url_shortener.db # SQLite database (auto-created, git-ignored)
│
├── screenshots/         # UI screenshots for README
├── .gitignore
└── README.md
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Divyansh-1210/Trimly-A-Url-Link-shortner.git
cd Trimly-A-Url-Link-shortner
```

### 2. Install dependencies
```bash
pip install -r backend/requirements.txt
```

### 3. Set your Gemini API key
Get a free key at: https://aistudio.google.com/apikey

```bash
# Windows (PowerShell)
$env:GEMINI_API_KEY="your_api_key_here"

# Mac / Linux
export GEMINI_API_KEY="your_api_key_here"
```

### 4. Start the server
```bash
cd backend
uvicorn main:app --reload
```

### 5. Open in browser
```
http://localhost:8000
```

> 📄 Interactive API docs available at: `http://localhost:8000/docs`

---

## 🔑 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `GEMINI_API_KEY` | Google Gemini API key for AI summarization | Optional (app works without it) |

---

## 📌 API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/register` | Create a new user account |
| `POST` | `/login` | Login & receive JWT token |
| `GET` | `/me` | Get current user profile |

### URLs
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/shorten` | Shorten a URL + AI summary (auth optional) |
| `GET` | `/urls` | List all shortened URLs |
| `GET` | `/my-urls` | List only your URLs (auth required) |
| `GET` | `/stats/{code}` | Get click stats for a short URL |
| `GET` | `/summarize/{code}` | Re-generate AI summary for a URL |
| `GET` | `/qr/{code}` | Get QR code PNG for a short URL |
| `GET` | `/{code}` | Redirect to original URL |

---

## 📋 Example Usage

### Shorten a URL (with AI summary)
```json
POST /shorten
{
  "long_url": "https://github.com/Divyansh-1210",
  "custom_code": "my-github"
}
```

**Response:**
```json
{
  "short_code": "my-github",
  "long_url": "https://github.com/Divyansh-1210",
  "short_url": "http://localhost:8000/my-github",
  "summary": "Divyansh Singh's GitHub profile showcasing software development projects.",
  "created_at": "2026-06-06T14:00:00",
  "click_count": 0,
  "owner": "john"
}
```

### Get QR Code
```
GET /qr/my-github
→ Returns PNG image
```

---

## 🔮 Future Improvements

- [x] ~~Deploy on Render (free hosting)~~ ✅ Done
- [ ] Link expiry (auto-delete after N days)
- [ ] Per-link analytics detail page
- [ ] Email verification on register

---

## 👨‍💻 Author

**Divyansh Singh**  
GitHub: [@Divyansh-1210](https://github.com/Divyansh-1210)
