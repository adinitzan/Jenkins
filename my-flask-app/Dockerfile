M python:3.9-slim

# שלב 2: להגדיר את תיקיית העבודה בקונטיינר
WORKDIR /app

# שלב 3: להעתיק את קובץ requirements.txt לקונטיינר
COPY requirements.txt .

# שלב 4: להתקין את התלויות מתוך requirements.txt
RUN pip install -r requirements.txt

# שלב 5: להעתיק את כל הקבצים לתוך הקונטיינר
COPY . .

# שלב 6: להגדיר את הפורט שיישום Flask ישתמש בו
EXPOSE 5000

# שלב 7: להריץ את אפליקציית Flask
CMD ["python", "app.py"]


