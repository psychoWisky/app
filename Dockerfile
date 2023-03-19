FROM python
COPY ./requirments.txt .
RUN pip install --upgrade -r requirments.txt
COPY . ./app
EXPOSE 8080
CMD [ "uvicorn", "app.main:testAPI", "--host", "0.0.0.0", "--port", "8080"]