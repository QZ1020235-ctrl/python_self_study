# 换用 Python 3.12-slim（关键！保留 cgi 模块，无需额外安装）
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖（仅保留 MySQL 必需依赖，无需加 python3-cgi）
RUN apt-get update && apt-get install -y --no-install-recommends \
    pkg-config \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件并安装（用你之前验证过的无冲突 requirements.txt）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . .

RUN mkdir -p /app/static /app/staticfiles

# 收集静态文件
RUN python manage.py collectstatic --noinput

# 暴露端口
EXPOSE 8080

# 启动命令（保持不变）
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "learning_log.wsgi:application"]