FROM python:3.13.5-slim

# Create non-root user that matches Spaces runtime (uid 1000), set HOME
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user PATH=/home/user/.local/bin:$PATH
WORKDIR $HOME/app

# Install deps as the user
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code with correct ownership
COPY --chown=user . .

# Optional: project config; Streamlit also reads $CWD/.streamlit/config.toml
# (this avoids reliance on ~/.streamlit)
COPY --chown=user .streamlit $HOME/app/.streamlit

EXPOSE 8501

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app/python_math_app.py", "--server.port=8501", "--server.address=0.0.0.0"]