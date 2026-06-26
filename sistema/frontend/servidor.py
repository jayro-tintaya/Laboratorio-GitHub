#!/usr/bin/env python3
"""
Servidor simple para El Puerto de la Costa
Recibe pedidos del celular y los reenvía al servidor Node (puerto 3001)
"""
import json
import os
import urllib.request
from http.server import HTTPServer, SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        if self.path == "/api/pedido":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)

            try:
                pedido = json.loads(body)
                mesa  = pedido.get('mesa', '?')
                total = pedido.get('total', 0)
                print(f"\n📱 PEDIDO QR recibido - Mesa: {mesa} - Total: Bs.{total}")

                # ── Reenviar al servidor Node (puerto 3001) ──
                try:
                    req = urllib.request.Request(
                        "http://localhost:3001/api/pedido",
                        data=body,
                        headers={"Content-Type": "application/json"},
                        method="POST"
                    )
                    with urllib.request.urlopen(req, timeout=5) as resp:
                        respuesta = json.loads(resp.read())
                        print(f"✅ Pedido guardado en BD, id: {respuesta.get('pedidoId', '?')}")
                except Exception as e:
                    print(f"⚠️  No se pudo reenviar al Node: {e}")

                # Responder OK al celular
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True}).encode())

            except Exception as e:
                print(f"❌ Error procesando pedido: {e}")
                self.send_response(400)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        # Servir archivos estáticos (index.html, menu-cliente.html, etc.)
        super().do_GET()

    def log_message(self, format, *args):
        # Solo mostrar errores, no cada request
        if len(args) > 1 and args[1] not in ('200', '304'):
            super().log_message(format, *args)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = 3000
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"✅ Servidor corriendo en puerto {port}")
    print(f"   PC:      http://localhost:{port}/index.html")
    print(f"   Celular: usa tu IP de red con puerto {port}")
    print(f"\nEsperando pedidos...\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
