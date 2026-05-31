# AI Interaction Log

## Project: Secure Secrets Manager

---

## 1. My Input (Prompts I sent to the AI)

- Asked the AI to guide me step by step through building a Secure Secrets Manager in Flask
- Asked for explanations of each component before moving on
- Asked to explain the difference between bcrypt and Fernet encryption
- Asked to explain JWT and how the decorator pattern works
- Asked for clarification on the project folder structure and what each folder is responsible for
- Asked the AI to write all comments in English

---

## 2. AI Response Summary

- The AI guided me through building the project phase by phase:
  - Phase 1: Project structure and models (user.py, secret.py, share_token.py)
  - Phase 2: Encryption utility (Fernet) and JWT authentication utility
  - Phase 3: Routes for auth, secrets management, and share links
  - Phase 4: Main app.py connecting all blueprints
- The AI explained each concept before providing code
- The AI helped troubleshoot import errors when models were empty
- The AI warned me multiple times to keep .env out of GitHub

---

## 3. Modifications I Made

- Changed all Hebrew comments in the code to English
- Asked clarifying questions about Flask route syntax vs FastAPI syntax
- Learned and understood each file before copying the code
- Managed Git commits manually, adding files one by one to avoid pushing sensitive data

---

## 4. What I Learned

- How Fernet symmetric encryption works vs bcrypt one-way hashing
- How JWT tokens are created and validated
- How Flask Blueprints organize routes into separate files
- The importance of .gitignore for protecting sensitive files
- How one-time expiring share tokens work