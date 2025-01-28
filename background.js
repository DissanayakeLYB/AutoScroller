const ws = new WebSocket("ws://localhost:8000"); // Connect to Python WebSocket server

ws.onmessage = (event) => {
  if (event.data === "scrollDown") {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.tabs.sendMessage(tabs[0].id, { command: "scrollDown" });
    });
  } else if (event.data === "scrollUp") {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.tabs.sendMessage(tabs[0].id, { command: "scrollUp" });
    });
  }
};
