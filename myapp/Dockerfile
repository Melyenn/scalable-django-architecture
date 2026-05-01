FROM python:3.12-slim

# Tránh tạo file .pyc và buffer log
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements trước để tận dụng cache của Docker
COPY requirements.txt /app/

# Nâng cấp pip và cài đặt dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn
COPY . /app/

# Thu thập static files
RUN python manage.py collectstatic --noinput || true

# Entrypoint mặc định
CMD ["gunicorn", "myapp.wsgi:application", "--bind", "0.0.0.0:8000"]