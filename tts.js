async function generateAudio() {
    const text = document.getElementById('tts-text').value;
    if (!text) {
        alert('Por favor ingresa texto.');
        return;
    }
    const response = await fetch('/tts', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text})
    });
    if (!response.ok) {
        alert('Error al generar el audio');
        return;
    }
    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const downloadLink = document.getElementById('download');
    downloadLink.href = url;
    downloadLink.style.display = 'inline';
}
