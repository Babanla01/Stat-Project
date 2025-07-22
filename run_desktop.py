import subprocess
import threading
import webview
import time
import os

def start_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'statsweb.settings')
    subprocess.Popen(['python', 'manage.py', 'runserver', '127.0.0.1:8000'])

# Start Django server in a new thread
threading.Thread(target=start_django).start()

# Give Django time to start up
time.sleep(2)

# Launch app window
webview.create_window("📊 Statistics Calculator", "http://127.0.0.1:8000", width=1200, height=900)
webview.start()
