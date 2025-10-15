import secrets

secret_key = secrets.token_urlsafe(32)
print(secret_key)


with open(".env", "w") as f:
    f.write(f"SECRET_KEY={secret_key}\n")

print("SECRET_KEY saved to .env file!")