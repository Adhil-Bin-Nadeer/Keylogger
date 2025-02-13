# Keylogger with SQLite3  

This project is a simple **keylogger** that records keystrokes and stores them in an **SQLite3 database** for analysis.  
It logs both normal and special keys, providing timestamps for each entry.  
The database is **reset after every execution**, ensuring only the latest session is stored.  

---

## 📌 Features  
✅ Logs all keystrokes, including special keys (Enter, Space, etc.)  
✅ Stores data in an **SQLite3 database** with timestamps  
✅ Automatically **deletes previous logs** on each execution  
✅ Runs **locally** without external dependencies  

---

## 🛠 Installation & Usage  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/your-username/keylogger-sqlite.git
cd keylogger-sqlite
```

### 2️⃣Install
```sh
pip install -r requirements.txt
```

### 3️⃣Run the kelogger
```sh
python keylogger.py
```

### 📁Project Structure
```bash
/keylogger-sqlite
│── keylogger.py         # Main keylogger script
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
│── .gitignore           # Excludes unnecessary files
```
### ⚠️Disclaimer
This project is intended for educational and research purposes only.
Unauthorized use of keyloggers is illegal and unethical. The author is not responsible for any misuse.


