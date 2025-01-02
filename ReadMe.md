# Basics

## Install Ollama

```
curl -fsSL https://ollama.com/install.sh | sh
```

## Install Model

```bash
ollama pull llama3.2:1b
```

## Run the Model

```bash
OLLAMA_HOST=0.0.0.0 ollama serve 
```

## Communicating

### Using cUrl

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt":"Why is the sky blue?"
}'
```

### Using Python

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
MODEL=llama3.2:1b OLLAMA=localhost:11434 python main.py
```