const vscode = require("vscode");
const http = require("http");

function sendLog(status, file) {
    const data = JSON.stringify({
        app_name: "VS Code",
        window_title: file,
        status: status,
        idle_seconds: 0
    });

    const options = {
        hostname: "127.0.0.1",
        port: 5000,
        path: "/log",
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Content-Length": Buffer.byteLength(data)
        }
    };

    const req = http.request(options, (res) => {
        console.log("Sent log:", status);
    });

    req.on("error", (err) => {
        console.log("Error sending log:", err.message);
    });

    req.write(data);
    req.end();
}

function activate(context) {

    console.log("🚀 AI Focus Tracker Activated");

    vscode.window.showInformationMessage("AI Focus Tracker Running");

    vscode.window.onDidChangeActiveTextEditor(editor => {
        if (editor) {
            const file = editor.document.fileName;
            console.log("File changed:", file);

            sendLog("Coding", file);
        }
    });
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};