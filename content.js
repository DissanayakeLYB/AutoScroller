// Listen for scroll commands from the background script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.command === "scrollUp") {
      window.scrollBy(0, -100); // Scroll up
    } else if (request.command === "scrollDown") {
      window.scrollBy(0, 100); // Scroll down
    }
  });
  