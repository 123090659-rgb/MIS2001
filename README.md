<<<<<<< HEAD
# MIS2001

Student ID: 123090659

## Hands-on 1 — Flask Web App for Local Server Deployment

A minimal self-contained Flask application demonstrating deployment on a local server.

## Project Structure

```
20261112153559/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── README.md
└── templates/
    └── index.html      # The "Hands-on 1" page
```

## 1. Install Dependencies

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 2. Run the App (port 8000, network accessible)

```powershell
python app.py
```

The app starts with `host="0.0.0.0"` and `port=8000`, so it listens on all
network interfaces and other devices on your network can reach it.

## 3. Access the App

- On your own machine: http://127.0.0.1:8000
- From other devices on the same network: http://<your-ip-address>:8000

To find your IP address on Windows:

```powershell
ipconfig
```

Look for the **IPv4 Address** under your active Wi-Fi/Ethernet adapter
(e.g. `192.168.1.100`), then share `http://192.168.1.100:8000`.

## 4. Windows Firewall Note

If others cannot connect, allow port 8000 through the firewall (run as Administrator):

```powershell
New-NetFirewallRule -DisplayName "Flask Hands-on 1" -Direction Inbound -LocalPort 8000 -Protocol TCP -Action Allow
```

## Health Check

`GET /health` returns `{"status": "ok"}` — useful to verify the server is running.
=======
# MIS2001
>>>>>>> origin/main
