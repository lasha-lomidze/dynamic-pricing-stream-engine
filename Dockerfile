# 1. Base Image (Your runtime foundation)
FROM python:3.12-slim

# 2. Workspace (Creates and enters your project folder)
WORKDIR /app

# 3. Cache Optimization Part A (Brings only the checklist in)
COPY requirements.txt .

# 4. Dependency Install (Installs packages globally inside the container)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Cache Optimization Part B (Brings your actual code in last)
COPY main.py .

# 6. Runtime Command (Launches your server on container startup)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
