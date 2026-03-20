<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BEU Bulk Result Linker</title>
    <style>
        body { font-family: sans-serif; padding: 20px; text-align: center; background: #f4f4f4; }
        .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); max-width: 500px; margin: auto; }
        input { width: 90%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; }
        button { background: #28a745; color: white; border: none; padding: 10px 20px; cursor: pointer; border-radius: 5px; font-size: 16px; }
        .links { margin-top: 20px; text-align: left; }
        .result-item { background: #e9ecef; padding: 10px; margin: 5px 0; border-radius: 5px; display: flex; justify-content: space-between; }
        a { color: #007bff; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>

<div class="card">
    <h2>🎓 BEU Result Linker</h2>
    <p>URL और रजिस्ट्रेशन रेंज डालें</p>
    
    <input type="text" id="urlInput" placeholder="रिजल्ट का URL यहाँ पेस्ट करें...">
    <input type="number" id="startReg" placeholder="Start Registration No (23153125001)">
    <input type="number" id="endReg" placeholder="End Registration No (23153125010)">
    
    <button onclick="generateLinks()">Generate Links</button>

    <div id="resultLinks" class="links"></div>
</div>

<script>
function generateLinks() {
    let rawUrl = document.getElementById('urlInput').value;
    let start = parseInt(document.getElementById('startReg').value);
    let end = parseInt(document.getElementById('endReg').value);
    let container = document.getElementById('resultLinks');
    
    if(!rawUrl || isNaN(start) || isNaN(end)) {
        alert("कृपया सभी जानकारी सही से भरें!");
        return;
    }

    container.innerHTML = "<h4>रिजल्ट लिंक्स:</h4>";

    for (let i = start; i <= end; i++) {
        // URL में regNo= के बाद वाले नंबर को बदलना
        let newUrl = rawUrl.replace(/(regNo=)(\d+)/, "$1" + i);
        
        let div = document.createElement('div');
        div.className = 'result-item';
        div.innerHTML = `<span>Reg: ${i}</span> <a href="${newUrl}" target="_blank">View & Save PDF</a>`;
        container.appendChild(div);
    }
}
</script>

</body>
</html>
