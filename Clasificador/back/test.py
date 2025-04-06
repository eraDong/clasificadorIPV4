from logica import *  # Importar funciones de lógica

# --- Prueba local en VSCode ---
if __name__ == "__main__":
    print("\n🔧 Prueba local del Backend IPv4")
    ip = input("Ingresa una IP (ej. 192.168.1.1): ").strip()
    
    result = analizarIP(ip)
    
    print("\n📊 Resultados:")
    for key, value in result.items():
        print(f"{key}: {value}")