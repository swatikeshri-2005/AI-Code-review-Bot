cat > /mnt/user-data/outputs/README.md << 'ENDOFFILE'
# 🤖 AI Code Review Bot

> An AI-powered code review tool built with **FastAPI** + **Claude AI** that analyzes your code for bugs, security vulnerabilities, performance issues, and style improvements.

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi)
![Claude AI](https://img.shields.io/badge/Claude-AI-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## ✨ Features

- 🔍 **Deep Code Analysis** — bugs, logic errors, anti-patterns
- 🔒 **Security Scanning** — SQL injection, hardcoded secrets, vulnerabilities
- ⚡ **Performance Review** — N+1 queries, memory leaks, inefficient loops
- 🎨 **Style & Maintainability** — naming, complexity, best practices
- 📊 **Quality Score** — 1–10 rating with detailed breakdown
- 💡 **Refactor Suggestions** — improved code snippets
- 🌐 **Multi-language** — Python, JavaScript, TypeScript, Java, Go, Rust, C++, SQL, and more

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-code-review-bot.git
cd ai-code-review-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Anthropic API key

Get your key from [console.anthropic.com](https://console.anthropic.com)

**Linux / Mac:**
```bash
export ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx
```

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY="sk-ant-xxxxxxxxxxxxxxxx"
```

**Windows (Command Prompt):**
```cmd
set ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx
```

### 4. Run the server

```bash
uvicorn main:app --reload --port 8000
```

Server is live at → `http://localhost:8000`

---

## 📡 API Reference

### Base URL
```
http://localhost:8000
```

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Service info |
| GET | `/health` | Health check |
| POST | `/review` | Submit code for AI review |

---

### `POST /review`

Submit code for a full AI-powered review.

**Request Body:**
```json
{
  "code": "def get_user(id):\n    query = 'SELECT * FROM users WHERE id = ' + id\n    return db.execute(query)",
  "language": "python",
  "context": "REST API handler"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `code` | string | ✅ Yes | The source code to review |
| `language` | string | ❌ No | Language hint (auto-detected if omitted) |
| `context` | string | ❌ No | Extra context about the code |

**Response:**
```json
{
  "summary": "The code has a critical SQL injection vulnerability and lacks error handling.",
  "score": 3,
  "language": "Python",
  "issues": [
    {
      "severity": "critical",
      "category": "security",
      "line": 2,
      "title": "SQL Injection Vulnerability",
      "description": "User input is concatenated directly into the SQL query.",
      "suggestion": "Use parameterized queries: cursor.execute('SELECT * FROM users WHERE id = %s', (id,))"
    }
  ],
  "strengths": ["Simple function structure"],
  "refactored_snippet": "def get_user(id):\n    query = 'SELECT * FROM users WHERE id = %s'\n    return db.execute(query, (id,))"
}
```

### Severity Levels

| Level | Meaning |
|-------|---------|
| `critical` | Security vulnerabilities, data loss risks |
| `high` | Bugs, major performance issues |
| `medium` | Logic errors, poor patterns |
| `low` | Style, minor improvements |
| `info` | Suggestions, best practices |

---

## 🧪 Try it Out

### Swagger UI (recommended)

Open your browser and go to:

**[http://localhost:8000/docs#/default/review_code_review_post](http://localhost:8000/docs#/default/review_code_review_post)**

Click **POST /review** → **Try it out** → paste your code → **Execute**

### curl

```bash
curl -X POST http://localhost:8000/review \
  -H "Content-Type: application/json" \
  -d '{
    "code": "password = \"admin123\"\nquery = \"SELECT * FROM users WHERE id = \" + user_input",
    "language": "python"
  }'
```

---

## 🗂️ Project Structure

```
ai-code-review-bot/
├── main.py           # FastAPI application & Claude AI integration
├── requirements.txt  # Python dependencies
└── README.md         # Documentation
```

---

## ⚙️ Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ANTHROPIC_API_KEY` | ✅ Yes | API key from [console.anthropic.com](https://console.anthropic.com) |

---

## 📦 Dependencies

```
fastapi==0.115.0
uvicorn[standard]==0.30.6
anthropic>=0.34.0
pydantic>=2.0.0
python-multipart==0.0.9
```

---

## 🔐 Security Note

Never commit your API key to GitHub. Use environment variables or a `.env` file and add it to `.gitignore`:

```bash
echo "ANTHROPIC_API_KEY=your_key_here" > .env
echo ".env" >> .gitignore
```

Then load it in `main.py`:
```python
from dotenv import load_dotenv
load_dotenv()
```

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

<div align="center">
  Built with ❤️ using <a href="https://fastapi.tiangolo.com">FastAPI</a> and <a href="https://www.anthropic.com">Claude AI</a>
</div>
ENDOFFILE
Output

exit code 0