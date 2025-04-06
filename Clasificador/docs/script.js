document.getElementById('analyzeBtn').addEventListener('click', analyzeIP);

async function analyzeIP() {
    const ip = document.getElementById('ipInput').value.trim();
    const resultCard = document.getElementById('result');
    const btn = document.getElementById('analyzeBtn');
    
    if (!ip) {
        showError("Por favor ingresa una IP");
        return;
    }

    // Mostrar estado de carga
    btn.disabled = true;
    btn.innerHTML = '<span class="loading"></span> Analizando...';
    resultCard.classList.remove('visible');

    try {
        const response = await fetch('http://127.0.0.1:5000/analizar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ip })
        });

        const data = await response.json();

        if (data.error) {
            showError(data.error);
            return;
        }

        // Actualizar UI con resultados
        document.getElementById('result-ip').textContent = data.ip;
        document.getElementById('result-class').textContent = `Clase ${data.class}`;
        
        const typeElement = document.getElementById('result-type');
        typeElement.textContent = data.type;
        typeElement.className = 'tag ' + (data.type.toLowerCase().includes('privada') ? 'private' : 
                              (data.type.includes('Loopback') ? 'loopback' : 'public'));

        // Datos de ejemplo (reemplaza con los reales de tu backend)
        document.getElementById('network').textContent = data.network || "192.168.1.0";
        document.getElementById('broadcast').textContent = data.broadcast || "192.168.1.255";
        document.getElementById('mask').textContent = data.mask || "255.255.255.0";
        document.getElementById('hosts').textContent = data.hosts || "254";

        // Mostrar tarjeta con animación
        resultCard.classList.remove('hidden');
        setTimeout(() => resultCard.classList.add('visible'), 10);

    } catch (error) {
        showError("Error al conectar con el servidor");
        console.error("Error:", error);
    } finally {
        btn.disabled = false;
        btn.textContent = 'Analizar';
    }
}

function showError(message) {
    const resultCard = document.getElementById('result');
    resultCard.innerHTML = `<div class="error">${message}</div>`;
    resultCard.classList.remove('hidden', 'visible');
    resultCard.classList.add('visible');
}