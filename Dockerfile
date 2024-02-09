FROM metro3230/telebots_basis

WORKDIR /app

COPY app .

CMD ["python3", "bot.py"] 
