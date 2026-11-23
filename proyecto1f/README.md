# 📋 Gestor de tareas (Flask + MySQL)

Aplicación web para organizar tareas por categoría (**trabajo**, **hogar** y **prioritarias**), con fecha límite, botón de completado y barra de búsqueda. Los datos se guardan en MySQL.

## Estructura

```
proyecto1f/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Requisitos previos

En el otro PC necesitas tener instalado:

1. **Python 3.9 o superior** → https://www.python.org/downloads/
   (en el instalador marca la casilla *"Add Python to PATH"*)
2. **MySQL Server 8.x** (o XAMPP/WAMP) → https://dev.mysql.com/downloads/mysql/

## Pasos para ejecutarlo

### 1. Copiar el proyecto

Copia la carpeta del proyecto al otro PC (USB, Drive, Git, etc.).
**No copies la carpeta `venv`**: se crea de nuevo en el paso 2.

### 2. Crear el entorno virtual e instalar dependencias

Abre una terminal dentro de la carpeta del proyecto y ejecuta:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

> En Mac/Linux, el segundo comando es: `source venv/bin/activate`

Si PowerShell bloquea la activación, ejecuta una sola vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 3. Crear la base de datos y el usuario en MySQL

Entra a MySQL con `root` (por consola o Workbench):

```powershell
mysql -u root -p
```

Y ejecuta:

```sql
CREATE DATABASE IF NOT EXISTS tareas_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'USUARIO'@'localhost' IDENTIFIED BY 'CONTRASEÑA';
GRANT ALL PRIVILEGES ON tareas_db.* TO 'USUARIO'@'localhost';
FLUSH PRIVILEGES;
```

Cambia `USUARIO` y `CONTRASEÑA` por los que quieras usar.
Las tablas **se crean solas** al iniciar la aplicación.

### 4. Configurar la conexión en `app.py`

Busca esta línea y ajústala a tu MySQL:

```python
"mysql+pymysql://USUARIO:CONTRASEÑA@127.0.0.1:3306/tareas_db"
```

- `USUARIO` y `CONTRASEÑA`: los del paso anterior.
- `3306`: el puerto de tu MySQL. Es el puerto por defecto; cámbialo solo si tu instalación usa otro (por ejemplo, `3308`).
- Si la contraseña tiene caracteres especiales (`@`, `#`, `/`, `:`), codifícala con `urllib.parse.quote_plus`.

### 5. Ejecutar

```powershell
python app.py
```

Abre en el navegador: **http://127.0.0.1:5000**

## Problemas comunes

| Error | Causa probable |
|---|---|
| `No module named 'flask_sqlalchemy'` | Falta activar el entorno virtual o ejecutar `pip install -r requirements.txt` |
| `Access denied for user ...` | Usuario o contraseña incorrectos en `app.py` |
| `Unknown database 'tareas_db'` | No se creó la base de datos (paso 3) |
| `Can't connect to MySQL server` | MySQL no está iniciado, o el puerto es otro |
| `&&` no es un separador válido | Usa PowerShell antiguo: ejecuta los comandos uno por uno |
