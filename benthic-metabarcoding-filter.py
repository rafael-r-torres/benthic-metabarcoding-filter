import graphviz
from IPython.display import display, Image

# --- 1. BUILD THE STATIC FLOWCHART (Complete Transparency Mode) ---
dot = graphviz.Digraph(format='png')
dot.attr(rankdir='TB', splines='ortho', nodesep='0.8', ranksep='0.6', fontname='Helvetica', dpi='300')
dot.attr('node', shape='box', style='filled, rounded', fontname='Helvetica', margin='0.2')

# Questions
dot.attr('node', fillcolor='#E3F2FD', color='#1565C0', fontcolor='black')
dot.node('Q1', 'Low Statistical Confidence?\n(e-value > 0.01)')
dot.node('Q2', 'Unmatched / Blank Taxonomic Data?\n• Not found in WoRMS\n• Filtered (Environmental)\n• Kingdom is Blank')
dot.node('Q3', 'Kingdom NOT Animalia?\n• Bacteria, Archaea, Protozoa,\nChromista, Fungi, Plantae')
dot.node('Q4', 'Terrestrial Arthropod?\n• Class: Hexapoda (Insects)\n• Class: Arachnida (Spiders/Mites)\n*Excl: Family Halacaridae (Marine Mites)')
dot.node('Q5', 'Pelagic / Planktonic Taxon?\n• Genera: Tomopteris, Alciopa, Limacina, Creseis, Themisto, Lucifer,\nAcartia, Oithona, Calanus, Centropages, Paracalanus, Temora,\nPenilia, Podon, Parasagitta, Euphausia\n• Class: Thaliacea, Appendicularia\n• Copepoda (without Benthos tag)\n• Plankton/Nekton (without Benthos tag)')
dot.node('Q6', 'Chordata (Vertebrate Fish)?\n*Excl: Ascidiacea (Sea Squirts)\n*Excl: Leptocardii (Lancelets)')
dot.node('Q7', 'Parasitic Ecology?\n• Phylum: Dicyemida\n• Family: Dicyemidae\n• Tag: parasitic')
dot.node('Q8', 'Phylum Tardigrada?\n(Water Bears)')
dot.node('Q9', 'Explicit Benthos Tag?\n• benthos\n• macrobenthos')
dot.node('Q10', 'Typically Benthic Phylum?\n• Annelida, Mollusca, Arthropoda, Echinodermata,\nPlatyhelminthes, Nematoda, Dicyemida, Chordata')

# Discards
dot.attr('node', fillcolor='#ffebee', color='#c62828', fontcolor='#b71c1c', style='filled')
dot.node('D1', 'DISCARD:\nLow Confidence'); dot.node('D2', 'DISCARD:\nUnmatched/Non-Marine')
dot.node('D3', 'DISCARD:\nNot Animalia'); dot.node('D4', 'DISCARD:\nTerrestrial Contaminant')
dot.node('D5', 'DISCARD:\nPelagic Exception'); dot.node('D6', 'DISCARD:\nPelagic Fish')

# Keeps & Checks
dot.attr('node', fillcolor='#e8f5e9', color='#2e7d32', fontcolor='#1b5e20')
dot.node('K1', 'KEEP:\nParasite Flag'); dot.node('K4', 'KEEP:\nTardigrada (still keep?)')
dot.node('K2', 'KEEP:\nConfirmed Benthos'); dot.node('K3', 'KEEP:\nTaxonomic Proxy')
dot.attr('node', fillcolor='#fff8e1', color='#fbc02d', fontcolor='#f57f17')
dot.node('R1', 'CHECK:\nManual Review')

dot.node('Start', 'Start: Taxon Record', fillcolor='#F3E5F5', color='#4A148C')

# Edges
dot.edge('Start', 'Q1', weight='10')
dot.edge('Q1', 'D1', label=' Yes'); dot.edge('Q1', 'Q2', label=' No', weight='10')
dot.edge('Q2', 'D2', label=' Yes'); dot.edge('Q2', 'Q3', label=' No', weight='10')
dot.edge('Q3', 'D3', label=' Yes'); dot.edge('Q3', 'Q4', label=' No', weight='10')
dot.edge('Q4', 'D4', label=' Yes'); dot.edge('Q4', 'Q5', label=' No', weight='10')
dot.edge('Q5', 'D5', label=' Yes'); dot.edge('Q5', 'Q6', label=' No', weight='10')
dot.edge('Q6', 'D6', label=' Yes'); dot.edge('Q6', 'Q7', label=' No', weight='10')
dot.edge('Q7', 'K1', label=' Yes'); dot.edge('Q7', 'Q8', label=' No', weight='10')
dot.edge('Q8', 'K4', label=' Yes'); dot.edge('Q8', 'Q9', label=' No', weight='10')
dot.edge('Q9', 'K2', label=' Yes'); dot.edge('Q9', 'Q10', label=' No', weight='10')
dot.edge('Q10', 'K3', label=' Yes'); dot.edge('Q10', 'R1', label=' No', weight='10')

dot.render('Explicit_Methodology_Flowchart')
display(Image(filename='Explicit_Methodology_Flowchart.png'))


# --- 2. BUILD THE RICH UI HTML FILE ---
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Explicit Methodology Filter</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🪱</text></svg>">
    
    <style>
        /* PERFECT CENTER & NO SCROLL BODY */
        body { 
            font-family: 'Segoe UI', sans-serif; 
            background: #eef2f5; 
            margin: 0; 
            display: flex; 
            justify-content: center; 
            align-items: center; /* Vertically centers the app */
            height: 100vh; /* Locks body exactly to window height */
            overflow: hidden; /* Disables outer page scrolling */
        }
        
        /* ADAPTIVE APP CONTAINER */
        .app-container { 
            display: flex; 
            max-width: 1200px; 
            width: 95vw; 
            background: white; 
            border-radius: 12px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.1); 
            height: 90vh; /* Takes up 90% of screen height */
            max-height: 650px; /* Caps maximum height so it stays compact */
            overflow: hidden; 
        }
        
        /* Main Panel (LEFT) */
        .main-panel { width: 65%; padding: 30px 40px; display: flex; flex-direction: column; position: relative; background: #fff; overflow-y: auto;}
        .icon-container { height: 80px; font-size: 60px; display: flex; justify-content: center; align-items: center; margin-bottom: 10px;}
        .question-container { flex-grow: 1; text-align: center; display: flex; flex-direction: column; justify-content: center;}
        .question-container h2 { font-weight: 600; color: #333; font-size: 24px; margin-bottom: 15px;}
        .details-box { text-align: left; background: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #3498db; display: inline-block; margin: 0 auto; width: 90%; font-size: 14px;}
        .details-box ul { margin: 5px 0 0 20px; padding: 0; }
        .details-box li { margin-bottom: 6px; color: #444;}
        .button-container { display: flex; justify-content: center; gap: 20px; margin-top: 25px; padding-bottom: 10px;}
        button { width: 160px; padding: 15px; font-size: 18px; font-weight: bold; cursor: pointer; border: none; border-radius: 8px; color: white; transition: 0.2s;}
        .btn-yes { background-color: #e74c3c; }
        .btn-no { background-color: #3498db; }
        .btn-yes:hover { background-color: #c0392b; }
        .btn-no:hover { background-color: #2980b9; }
        .secondary-controls { display: flex; justify-content: center; gap: 10px; border-top: 1px solid #eee; padding-top: 15px; margin-top: 5px;}
        .btn-sec { background: #95a5a6; color: white; padding: 8px 16px; font-size: 13px; width: auto;}

        /* History Panel (RIGHT) */
        .history-panel { width: 35%; background: #fdfdfd; padding: 30px 25px; display: flex; flex-direction: column; border-left: 1px solid #ddd;}
        .history-panel h3 { margin-top: 0; color: #555; text-transform: uppercase; font-size: 13px; letter-spacing: 1px; text-align: center; margin-bottom: 15px; flex-shrink: 0;}
        
        /* SCROLLABLE LIST */
        #historyList { flex-grow: 1; overflow-y: auto; padding-left: 15px; scroll-behavior: smooth; padding-right: 10px;}
        
        /* Custom Scrollbar for sleek UI */
        #historyList::-webkit-scrollbar { width: 6px; }
        #historyList::-webkit-scrollbar-track { background: transparent; }
        #historyList::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        #historyList::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
        
        /* The Tree Trunk and Nodes */
        .tree-trunk { border-left: 3px solid #bdc3c7; padding-left: 25px; position: relative; padding-bottom: 20px; margin-left: 15px; margin-top: 5px;}
        .tree-node {
            border-radius: 6px; padding: 10px 12px; margin-bottom: 20px;
            position: relative; font-size: 12px; font-weight: 500;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05); line-height: 1.4;
        }
        .tree-node::before {
            content: ""; position: absolute; left: -28px; top: 16px; width: 25px; height: 3px; background: #bdc3c7;
        }
        .tree-node::after {
            content: ""; position: absolute; left: -34px; top: 11px; width: 13px; height: 13px;
            border-radius: 50%; border: 2px solid #fff;
        }
        
        /* Node Colors matching Graphviz */
        .node-blue { background: #E3F2FD; color: #1565C0; border: 1px solid #90CAF9; }
        .node-blue::after { background: #3498db; }
        .node-red { background: #ffebee; color: #c62828; border: 1px solid #ef9a9a; }
        .node-red::after { background: #e74c3c; }
        .node-green { background: #e8f5e9; color: #2e7d32; border: 1px solid #a5d6a7; }
        .node-green::after { background: #2ecc71; }
        .node-yellow { background: #fff8e1; color: #f57f17; border: 1px solid #ffe082; }
        .node-yellow::after { background: #f1c40f; }
        .node-current { background: #fff; color: #555; border: 2px dashed #aaa; }
        .node-current::after { background: #fff; border: 2px solid #aaa; }
    </style>
</head>
<body>
    <div class="app-container">
        
        <div class="main-panel" id="mainPanel">
            <div class="icon-container" id="qIcon">📉</div>
            <div class="question-container">
                <h2 id="qTitle">Loading...</h2>
                <div class="details-box" id="qDetails"></div>
            </div>
            <div class="button-container" id="btnGroup">
                <button class="btn-yes" onclick="answer('yes')">YES</button>
                <button class="btn-no" onclick="answer('no')">NO</button>
            </div>
            <div class="secondary-controls" id="secControls">
                <button class="btn-sec" onclick="goBack()">⟵ Back</button>
                <button class="btn-sec" onclick="startOver()">↻ Restart</button>
            </div>
        </div>

        <div class="history-panel">
            <h3>Live Flowchart Path</h3>
            <div id="historyList"></div>
        </div>

    </div>
    <script>
        const logic = [
            { icon: "📉", title: "Low Statistical Confidence?", details: "<ul><li>e-value > 0.01</li></ul>", yes: "🔴 DISCARD: Low Statistical Confidence" },
            { icon: "🗄️", title: "Unmatched / Blank Taxonomic Data?", details: "<ul><li>Match Status: Not found in WoRMS</li><li>Match Status: Filtered (Environmental)</li><li>Kingdom: [Blank]</li></ul>", yes: "🔴 DISCARD: Unmatched/Non-Marine" },
            { icon: "🐾", title: "Kingdom NOT Animalia?", details: "<ul><li>Kingdom: Bacteria</li><li>Kingdom: Archaea</li><li>Kingdom: Protozoa</li><li>Kingdom: Chromista</li><li>Kingdom: Fungi</li><li>Kingdom: Plantae</li></ul>", yes: "🔴 DISCARD: Not Animalia" },
            { icon: "🕷️", title: "Terrestrial Arthropod?", details: "<ul><li>Class: Hexapoda (Insects)</li><li>Class: Insecta</li><li>Class: Arachnida (Spiders/Mites)</li><ul><li><em>Exception: Keep Family Halacaridae (Marine Mites)</em></li></ul></ul>", yes: "🔴 DISCARD: Terrestrial Contaminant" },
            { icon: "🦐", title: "Pelagic / Planktonic Taxon?", details: "<ul><li>Genera: Tomopteris, Alciopa, Limacina, Creseis, Themisto, Lucifer, Acartia, Oithona, Calanus, Centropages, Paracalanus, Temora, Penilia, Podon, Parasagitta, Euphausia</li><li>Class: Thaliacea</li><li>Class: Appendicularia</li><li>Class: Copepoda (without benthic life stage tag)</li><li>Tagged: Plankton or Nekton (without benthic life stage tag)</li></ul>", yes: "🔴 DISCARD: Pelagic Exception" },
            { icon: "🐟", title: "Vertebrate Fish?", details: "<ul><li>Phylum: Chordata</li><ul><li><em>Exception: Keep Class Ascidiacea (Sea Squirts)</em></li><li><em>Exception: Keep Class Leptocardii (Lancelets)</em></li></ul></ul>", yes: "🔴 DISCARD: Pelagic Fish" },
            { icon: "🪱", title: "Parasitic Ecology?", details: "<ul><li>Feeding Method: parasitic</li><li>Ecological Interaction: parasitic</li><li>Phylum: Dicyemida</li><li>Family: Dicyemidae</li></ul>", yes: "🟢 KEEP: Parasite Flag" },
            { icon: "🔬", title: "Phylum Tardigrada?", details: "<ul><li>Phylum: Tardigrada (Water Bears)</li></ul>", yes: "🟢 KEEP: Tardigrada (still keep?)" },
            { icon: "🦀", title: "Explicit Benthos Tag?", details: "<ul><li>Functional Group: benthos</li><li>Functional Group: macrobenthos</li></ul>", yes: "🟢 KEEP: Confirmed Benthos" },
            { icon: "🦑", title: "Typically Benthic Phylum?", details: "<ul><li>Ecological Data: [Blank] or [Not Applicable]</li><li>Phylum: Annelida</li><li>Phylum: Mollusca</li><li>Phylum: Arthropoda</li><li>Phylum: Echinodermata</li><li>Phylum: Platyhelminthes</li><li>Phylum: Nematoda</li><li>Phylum: Dicyemida</li><li>Phylum: Chordata</li></ul>", yes: "🟢 KEEP: Taxonomic Proxy", no: "🟡 CHECK: Manual Review" }
        ];

        let currentStep = 0, pathMemory = [], isEnd = false;

        function render() {
            const step = logic[currentStep];
            document.getElementById("btnGroup").style.display = isEnd ? "none" : "flex";
            document.getElementById("mainPanel").style.backgroundColor = isEnd ? "" : "white";
            document.getElementById("qIcon").innerText = step.icon;
            document.getElementById("qTitle").innerHTML = isEnd ? "<strong>"+step.resultText+"</strong>" : step.title;
            document.getElementById("qDetails").innerHTML = isEnd ? "" : step.details;
            document.getElementById("qDetails").style.display = isEnd ? "none" : "block";

            // Build the right-side flowchart using the FULL title
            let h = '<div class="tree-trunk">';
            pathMemory.forEach(m => {
                let colorClass = m.c === 'yes' ? 'node-red' : 'node-blue';
                h += `<div class="tree-node ${colorClass}">
                        <strong>${logic[m.idx].title}</strong><br>
                        <span style="font-size:11px; opacity:0.8;">Decision: ${m.c.toUpperCase()}</span>
                      </div>`;
            });
            
            // Add the current or final node to the flowchart
            if (!isEnd) {
                h += `<div class="tree-node node-current">
                        <em style="font-size:11px; color:#888;">Currently Checking:</em><br>
                        <strong>${logic[currentStep].title}</strong>
                      </div>`;
            } else {
                let result = logic[currentStep].resultText;
                let finalClass = result.includes('KEEP') ? 'node-green' : (result.includes('DISCARD') ? 'node-red' : 'node-yellow');
                h += `<div class="tree-node ${finalClass}">
                        <strong>${result}</strong>
                      </div>`;
            }
            h += '</div>';
            
            document.getElementById("historyList").innerHTML = h;
            document.getElementById("secControls").style.display = pathMemory.length ? "flex" : "none";
            
            // Auto-scroll the flowchart to the bottom using a slight delay to ensure rendering
            setTimeout(() => {
                const hList = document.getElementById("historyList");
                hList.scrollTop = hList.scrollHeight;
            }, 10);
        }

        function answer(c) {
            const step = logic[currentStep];
            pathMemory.push({idx: currentStep, c: c});
            if (c === 'yes') {
                isEnd = true;
                step.resultText = step.yes;
                document.getElementById("mainPanel").style.backgroundColor = "#ffebee";
            } else if (currentStep === logic.length - 1) {
                isEnd = true;
                step.resultText = "🟡 CHECK: Manual Review";
                document.getElementById("mainPanel").style.backgroundColor = "#fff8e1";
            } else {
                currentStep++;
            }
            render();
        }

        function goBack() {
            if (!pathMemory.length) return;
            isEnd = false;
            currentStep = pathMemory.pop().idx;
            render();
        }

        function startOver() {
            pathMemory = []; currentStep = 0; isEnd = false; render();
        }
        
        // Initialize
        render();
    </script>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)
    
print("✅ Saved as 'index.html'. Upload this directly to GitHub.")
