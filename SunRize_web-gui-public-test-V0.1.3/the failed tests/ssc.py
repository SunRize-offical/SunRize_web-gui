async function updateMCStatus() {
  try {
    const response = await fetch('mcstatus.txt');
    const text = await response.text();
    document.getElementById('mc-status').innerText = text.trim().toUpperCase();
  } catch (err) {
    document.getElementById('mc-status').innerText = 'UNREACHABLE';
  }
}
setInterval(updateMCStatus, 4000);
updateMCStatus();

