document.addEventListener("DOMContentLoaded", () => {
  const startScanButton = document.getElementById("startScan");
  const testConnectionButton = document.getElementById("testConnection");
  const statusAndResultsDiv = document.getElementById("statusAndResults");
  const urlInput = document.getElementById("target");

  if (!crypto.randomUUID) {
      crypto.randomUUID = function () {
          return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
              var r = (crypto.getRandomValues(new Uint8Array(1))[0] % 16) | 0,
                  v = c === 'x' ? r : (r & 0x3) | 0x8;
              return v.toString(16);
          });
      };
  }
  const uuid = crypto.randomUUID();

  const socket = new WebSocket(`ws://${window.location.host}/api/public/ws/?client_id=${uuid}`);

  function addStatusItem(message, className = '') {
      const item = document.createElement('div');
      item.textContent = message;
      item.className = `status-item ${className}`;
      statusAndResultsDiv.appendChild(item);
      statusAndResultsDiv.scrollTop = statusAndResultsDiv.scrollHeight;
  }

  socket.addEventListener("message", (event) => {
      const data = JSON.parse(event.data);
      addStatusItem(data.data);
  });

  startScanButton.addEventListener("click", () => {
      statusAndResultsDiv.innerHTML = '';
      const target = urlInput.value;
      if (!target) return;

      startScanButton.disabled = true;
      fetch("/api/public/startscan", {
          method: "POST",
          headers: {
              "Content-Type": "application/json"
          },
          body: JSON.stringify({ target: target, client_id: uuid })
      })
      .then(response => response.json())
      .then(data => {
          if (data.error) {
              addStatusItem(data.error, 'error');
          } else {
              addStatusItem('Scan initiated. Monitoring progress...', 'success');
          }
      })
      .catch(error => {
          addStatusItem(`Error: ${error.message}`, 'error');
      })
      .finally(() => {
        urlInput.value = '';
    });
  });

  testConnectionButton.addEventListener("click", () => {
      statusAndResultsDiv.innerHTML = '';
      const url = urlInput.value;
      if (!url) return;

      testConnectionButton.disabled = true;
      fetch("/api/public/test", {
          method: "POST",
          headers: {
              "Content-Type": "application/json"
          },
          body: JSON.stringify({ url: url })
      })
      .then(response => {
          if (!response.ok && response.status != 301) {
              addStatusItem(`Target unreachable. Status Code: ${response.status}`, 'error');
          } else {
              addStatusItem(`Target accessible. Status Code: ${response.status}`, 'success');
              startScanButton.disabled = false;
          }
      })
      .catch(error => {
          addStatusItem(`Error: ${error.message}`, 'error');
      })
      .finally(() => {
          testConnectionButton.disabled = false;
      });
  });
});