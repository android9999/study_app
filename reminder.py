import os
import time
import psutil

def is_main_app_running():
    return "python" in (p.name() for p in psutil.process_iter())

def launch_main_app():
    os.system("python main_app.py")

def main():
    while True:
        if not is_main_app_running():
            launch_main_app()
        time.sleep(10 * 60)  # Check every 5 minutes

if __name__ == "__main__":
    main()
