FROM python:3.13.9
WORKDIR /app 
COPY app.py requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "uvicorn","app:app","--host","0.0.0.0","--port","8000" ]