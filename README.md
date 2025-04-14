# Accounting Application

This project is a full-stack accounting application built entirely from scratch. It integrates a Python/Flask backend with an SQLite database (using SQLAlchemy), a performance-critical C module for rapid calculations, and a modern frontend built with HTML, CSS, and JavaScript.

## Features

- **Dynamic Unit Management:** Add, edit, and delete units.
- **Price History Tracking:** Records price changes over time.
- **Collapsible Settings Bar:** Toggle and customize the interface.
- **Dark/Light Mode:** Switch between themes.
- **Real-time Calculations:** Uses a C module for performance-critical operations.
- **Responsive UI:** Built with modern web technologies.

## Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://your-repo-url.git
    cd accounting_app
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Compile the C Module:**

    For Linux/Mac:
    ```bash
    gcc -shared -o extensions/price_calculator.so -fPIC extensions/price_calculator.c
    ```

    For Windows, compile the DLL accordingly.

4. **Run the Application:**

    ```bash
    cd app
    python main.py
    ```

5. **Access the Application:**

   Open your browser and navigate to [http://localhost:5000](http://localhost:5000).

## References

- [Flask Documentation](https://flask.palletsprojects.com/) :contentReference[oaicite:13]{index=13}
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/) :contentReference[oaicite:14]{index=14}
- [MDN Web Docs](https://developer.mozilla.org/) :contentReference[oaicite:15]{index=15}
- [Python ctypes](https://docs.python.org/3/library/ctypes.html) :contentReference[oaicite:16]{index=16}

