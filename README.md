
````markdown
# Projecte Django - Jugadors del Barça

Aquest projecte és una aplicació web desenvolupada amb **Django** per gestionar informació sobre jugadors del FC Barcelona i els títols que han guanyat.

## Requisits

Per poder executar aquest projecte localment, necessitaràs:

- **Python 3.10 o superior**
- **pip** (gestor de paquets de Python)
- **Django 5.x** (està inclòs a les dependències)

## Instal·lació i Configuració

Seguiu aquests passos per desplegar l'aplicació en el vostre entorn local.

### 1. Clonar el repositori

Primer, clona el repositori al teu ordinador:

```bash
git clone https://github.com/Sgallartfanlo/Framework-Django-SGF.git
cd Framework-Django-SGF
````

### 2. Crear un entorn virtual

És recomanable utilitzar un entorn virtual per aïllar les dependències del projecte:

```bash
python3 -m venv env
source env/bin/activate  # Per a Linux/macOS
env\Scripts\activate     # Per a Windows
```

### 3. Instal·lar les dependències

Un cop l'entorn virtual estigui activat, instal·la totes les dependències del projecte mitjançant el fitxer **`requirements.txt`**:

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de dades

El projecte utilitza una base de dades SQLite per defecte, que no necessita cap configuració especial. Simplement, executa les migracions per crear les taules necessàries:

```bash
python manage.py migrate
```

### 5. Crear un superusuari

Crea un superusuari per poder accedir a l'administrador de Django:

```bash
python manage.py createsuperuser
```

Seguiu les instruccions a la terminal per configurar el nom d'usuari, correu electrònic i contrasenya.

### 6. Arrencar el servidor

Finalment, arrenca el servidor de desenvolupament de Django:

```bash
python manage.py runserver
```

L'aplicació serà accessible a través del navegador a l'URL:

```
http://127.0.0.1:8000/
```

### 7. Accedir a l'Administrador de Django

Accedeix a l'administrador de Django per gestionar jugadors i títols. Fes servir el superusuari que vas crear anteriorment:

```
http://127.0.0.1:8000/admin/
```

### 8. Desplegar en un servidor de producció

Si vols desplegar l'aplicació en un servidor de producció, et recomano seguir les [instruccions oficials de Django per desplegar-lo](https://docs.djangoproject.com/en/stable/howto/deployment/). Aquests són alguns punts clau:

* Configurar un servidor web com **Nginx** o **Apache**.
* Utilitzar **Gunicorn** com a servidor WSGI per executar l'aplicació Django.
* Configurar una base de dades en producció (com PostgreSQL o MySQL).
* Configurar les opcions de seguretat com la variable `ALLOWED_HOSTS` i l'ús de **SSL**.

## Contribució

Si vols contribuir al projecte, pots fer-ho creant un **fork** del repositori i enviant un **pull request** amb els canvis que vulguis afegir.

## Llicència

Aquest projecte es distribueix sota la llicència MIT. Consulta el fitxer **`LICENSE`** per a més detalls.

````

---

### Pasos per crear el fitxer **`README.md`** al teu repositori:

1. A la terminal, crea el fitxer **`README.md`** al directori del teu projecte:
   
```bash
touch README.md
````

2. Obre el fitxer **`README.md`** i enganxa-hi el contingut proporcionat anteriorment.

3. Fes un **commit** del nou fitxer:

```bash
git add README.md
git commit -m "Afegit el fitxer README.md"
git push
```

---

Ara tindràs un **README.md** ben documentat per al teu projecte Django, on es detalla com instal·lar-lo, configurar-lo, i desplegar-lo tant en entorns locals com de producció.

Si tens més preguntes o necessites més personalització en el teu **README**, no dubtis a preguntar! 😊
