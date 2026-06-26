# 🚀 Guía de Ejecución del Sistema

## 1. Iniciar XAMPP

Abrir XAMPP y encender:

- Apache
- MySQL

---

## 2. Ejecutar el Backend

Abrir una terminal (CMD):

```bash
cd C:\Users\DELL\Desktop\sistema
node backend/server.js
```

Debe aparecer:

```text
Servidor funcionando en puerto 3001
MySQL conectado
```

---

## 3. Ejecutar el Frontend

Abrir una segunda terminal (CMD):

```bash
cd C:\Users\DELL\Desktop\sistema\frontend
py servidor.py
```

Debe aparecer:

```text
✅ Servidor corriendo en puerto 3000
Esperando pedidos...
```

---

## 4. Abrir el Sistema

En el navegador:

```text
http://localhost:3000/index.html
```

---

## 5. Acceso desde Celular

- Conectar el celular a la misma red WiFi que la computadora.
- Ingresar al módulo QR Menú.
- Escanear el código QR generado por el sistema.
- Acceder al menú digital desde el celular.

---

# ⚠️ Orden Correcto de Inicio

```text
1. XAMPP → Apache + MySQL
2. node backend/server.js
3. py servidor.py
4. http://localhost:3000/index.html
```

---

# ⚠️ Importante

Nunca abrir:

```text
index.html
```

haciendo doble clic.

Siempre acceder mediante:

```text
http://localhost:3000/index.html
```