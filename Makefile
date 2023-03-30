.PHONY: all install-backend backend frontend

all: install-backend backend frontend

install-backend:
	cd backend && pip install -r requirements.txt

backend:
	cd backend && python server.py

frontend:
	python -m webbrowser -t "http://localhost:3001"


