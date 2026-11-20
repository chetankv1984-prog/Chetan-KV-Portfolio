# Chetan KV — Interactive Portfolio Dashboard

A responsive portfolio powered by Flask (Python), HTML, CSS, JavaScript, Chart.js and SQLite.

## Run in VS Code (Windows)

1. Extract the ZIP and open the `chetan_portfolio` folder in VS Code.
2. Open **Terminal → New Terminal**.
3. Create a virtual environment:
   ```powershell
   py -m venv .venv
   ```
4. Activate it:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, skip it and use `.\.venv\Scripts\python.exe` in the next commands.
5. Install Flask:
   ```powershell
   python -m pip install -r requirements.txt
   ```
6. Run:
   ```powershell
   python app.py
   ```
7. Open **http://127.0.0.1:5000** in your browser.

### Without activation

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

## Folder guide
- `app.py` — Flask server and contact endpoint
- `templates/index.html` — website content and sections
- `static/css/style.css` — theme, cards, responsive layout, animations
- `static/js/app.js` — navigation, filters, typewriter, chart, theme and form
- `static/img/profile.png` — cropped profile photo from the uploaded resume
- `static/files/resume.pdf` — downloadable resume
- `messages.db` — created automatically on first run; contains contact submissions

## Important
- Contact form stores messages **locally** in SQLite. It does **not** send emails. Configure an email service separately for notifications.
- The chart shows skill counts, **not proficiency ratings**.
- Project cards intentionally do not link to guessed repositories. Add your real links in `index.html` when ready.
- Fonts and Chart.js are loaded via CDN; the site still functions without the chart when offline.
- Before public deployment, disable Flask debug mode, configure a production WSGI server, add spam protection and a privacy notice, and protect stored contact data.


## Update: photo-free version
The portrait was removed from the home page and the image asset deleted. A decorative CKV monogram takes its place without changing the dashboard layout. The Flask backend was cleaned up and its email validation checked.

Run from inside `chetan_portfolio` with `python -m pip install -r requirements.txt` then `python app.py`. The contact form stores submissions in a local `messages.db` file; it does not send emails.

## 3D coding animation update
The home-page portrait area now contains a CSS 3D animated code editor, with no portrait image. The other portfolio sections and Flask backend remain unchanged. No extra libraries are required.
