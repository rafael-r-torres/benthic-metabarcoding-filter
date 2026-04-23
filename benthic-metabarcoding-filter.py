# !pip install graphviz
import graphviz
from IPython.display import display, Image

# ==============================================================================
# 1. BUILD THE STATIC FLOWCHART FOR MACROBENTHOS 
# ==============================================================================
dot_macro = graphviz.Digraph(format='png')
dot_macro.attr(rankdir='TB', splines='ortho', nodesep='0.8', ranksep='0.6', fontname='Helvetica', dpi='300')
dot_macro.attr('node', shape='box', style='filled, rounded', fontname='Helvetica', margin='0.2')

# Questions
dot_macro.attr('node', fillcolor='#E3F2FD', color='#1565C0', fontcolor='black')
dot_macro.node('Q1', 'Low Statistical Confidence?\n(e-value > 0.01)')
dot_macro.node('Q2', 'Unmatched / Blank Taxonomic Data?\n• Not found in WoRMS\n• Filtered (Environmental)\n• Kingdom is Blank')
dot_macro.node('Q3', 'Kingdom NOT Animalia?\n• Bacteria, Archaea, Protozoa,\nChromista, Fungi, Plantae')
dot_macro.node('Q4', 'Terrestrial Arthropod?\n• Class: Hexapoda (Insects)\n• Class: Arachnida (Spiders/Mites)\n*Excl: Family Halacaridae (Marine Mites)')
dot_macro.node('Q5', 'Pelagic / Planktonic Taxon?\n• Genera: Tomopteris, Alciopa, Limacina, Creseis, Themisto, Lucifer,\nAcartia, Oithona, Calanus, Centropages, Paracalanus, Temora,\nPenilia, Podon, Parasagitta, Euphausia\n• Class: Thaliacea, Appendicularia\n• Copepoda (except Harpacticoida or benthic tag)\n• Plankton/Nekton (without benthic tag)')
dot_macro.node('Q6', 'Chordata (Vertebrate Fish)?\n*Excl: Ascidiacea (Sea Squirts)\n*Excl: Leptocardii (Lancelets)')
dot_macro.node('Q7', 'Parasitic Ecology?\n• Phylum: Dicyemida\n• Family: Dicyemidae\n• Tag: parasitic')
dot_macro.node('Q8', 'Phylum Tardigrada?\n(Water Bears)')
dot_macro.node('Q9', 'Explicit Benthos Tag?\n• benthos\n• macrobenthos')
dot_macro.node('Q10', 'Typically Benthic Phylum?\n• Annelida, Mollusca, Arthropoda, Echinodermata,\nPlatyhelminthes, Nematoda, Dicyemida, Chordata')

# Discards
dot_macro.attr('node', fillcolor='#ffebee', color='#c62828', fontcolor='#b71c1c', style='filled')
dot_macro.node('D1', 'DISCARD:\nLow Confidence')
dot_macro.node('D2', 'DISCARD:\nUnmatched/Non-Marine')
dot_macro.node('D3', 'DISCARD:\nNot Animalia')
dot_macro.node('D4', 'DISCARD:\nTerrestrial Contaminant')
dot_macro.node('D5', 'DISCARD:\nPelagic Exception')
dot_macro.node('D6', 'DISCARD:\nPelagic Fish')
dot_macro.node('D7', 'DISCARD:\nMeiofauna Exception')

# Keeps & Checks
dot_macro.attr('node', fillcolor='#e8f5e9', color='#2e7d32', fontcolor='#1b5e20')
dot_macro.node('K1', 'KEEP:\nParasite Flag')
dot_macro.node('K2', 'KEEP:\nConfirmed Benthos')
dot_macro.node('K3', 'KEEP:\nTaxonomic Proxy')
dot_macro.attr('node', fillcolor='#fff8e1', color='#fbc02d', fontcolor='#f57f17')
dot_macro.node('R1', 'CHECK:\nManual Review')

dot_macro.node('Start', 'Start: Macrobenthos', fillcolor='#F3E5F5', color='#4A148C')

# Edges
dot_macro.edge('Start', 'Q1', weight='10')
dot_macro.edge('Q1', 'D1', label=' Yes'); dot_macro.edge('Q1', 'Q2', label=' No', weight='10')
dot_macro.edge('Q2', 'D2', label=' Yes'); dot_macro.edge('Q2', 'Q3', label=' No', weight='10')
dot_macro.edge('Q3', 'D3', label=' Yes'); dot_macro.edge('Q3', 'Q4', label=' No', weight='10')
dot_macro.edge('Q4', 'D4', label=' Yes'); dot_macro.edge('Q4', 'Q5', label=' No', weight='10')
dot_macro.edge('Q5', 'D5', label=' Yes'); dot_macro.edge('Q5', 'Q6', label=' No', weight='10')
dot_macro.edge('Q6', 'D6', label=' Yes'); dot_macro.edge('Q6', 'Q7', label=' No', weight='10')
dot_macro.edge('Q7', 'K1', label=' Yes'); dot_macro.edge('Q7', 'Q8', label=' No', weight='10')
dot_macro.edge('Q8', 'D7', label=' Yes'); dot_macro.edge('Q8', 'Q9', label=' No', weight='10')
dot_macro.edge('Q9', 'K2', label=' Yes'); dot_macro.edge('Q9', 'Q10', label=' No', weight='10')
dot_macro.edge('Q10', 'K3', label=' Yes'); dot_macro.edge('Q10', 'R1', label=' No', weight='10')

dot_macro.render('Explicit_Methodology_Flowchart')
display(Image(filename='Explicit_Methodology_Flowchart.png'))


# ==============================================================================
# 2. BUILD THE STATIC FLOWCHART FOR MEIOBENTHOS 
# ==============================================================================
dot_meio = graphviz.Digraph(format='png')
dot_meio.attr(rankdir='TB', splines='ortho', nodesep='0.8', ranksep='0.6', fontname='Helvetica', dpi='300')
dot_meio.attr('node', shape='box', style='filled, rounded', fontname='Helvetica', margin='0.2')

# Questions
dot_meio.attr('node', fillcolor='#E3F2FD', color='#1565C0', fontcolor='black')
dot_meio.node('M_Q1', 'Low Statistical Confidence?\n(e-value > 0.01)')
dot_meio.node('M_Q2', 'Unmatched / Blank Taxonomic Data?\n• Not found in WoRMS\n• Filtered (Environmental)')
dot_meio.node('M_Q3', 'Pelagic / Planktonic Taxon?\n• Genera: Tomopteris, Alciopa, Limacina, Creseis, Themisto, Lucifer,\nAcartia, Oithona, Calanus, Centropages, Paracalanus, Temora,\nPenilia, Podon, Parasagitta, Euphausia\n• Class: Thaliacea, Appendicularia\n• Copepoda (except Harpacticoida or benthic tag)\n• Plankton/Nekton (without benthic tag)')
dot_meio.node('M_Q4', 'Macro-Invertebrate Exception?\nIs it an Arthropod or Echinoderm but NOT explicitly kept?\n*KEPT: Cephalocarida, Branchiopoda, Ostracoda, Mystacocarida,\nHarpacticoida, Cyclopoida, Siphonostomatoida, Syncarida,\nPeracarida, Trombidiformes, Pycnogonida, Holothuroidea\n*REMOVED: All other Arthropoda and Echinodermata')
dot_meio.node('M_Q5', 'Terrestrial Thalassobiont?\nIs it one of the terrestrial beach groups from Fais (2021)?\n(Araneae, Pseudoscorpionida, Chilopoda,\nCollembola, Coleoptera, Diptera)')
dot_meio.node('M_Q6', 'Explicitly in Fais (2021) Phyla List?\nIs it explicitly one of:\nForaminifera, Heliozoa, Ciliophora, Amoebozoa, Porifera, Cnidaria,\nPlatyhelminthes, Gnathostomulida, Rotifera, Micrognathozoa, Nemertea,\nNematoda, Kinorhyncha, Priapulida, Loricifera, Gastrotricha, Tardigrada,\nAnnelida, Sipuncula, Mollusca, Brachiopoda, Bryozoa, Entoprocta,\nChaetognata, Tunicata, Acarina (Marine mites)')

# Discards
dot_meio.attr('node', fillcolor='#ffebee', color='#c62828', fontcolor='#b71c1c', style='filled')
dot_meio.node('M_D1', 'DISCARD:\nLow Confidence')
dot_meio.node('M_D2', 'DISCARD:\nUnmatched Data')
dot_meio.node('M_D3', 'DISCARD:\nPelagic Exception')
dot_meio.node('M_D4', 'DISCARD:\nMacro-Invertebrate')
dot_meio.node('M_D5', 'DISCARD:\nNot in Fais (2021) List')

# Flagged Keeps (Yellow)
dot_meio.attr('node', fillcolor='#fff8e1', color='#fbc02d', fontcolor='#f57f17', style='filled')
dot_meio.node('M_K2', 'KEEP:\nFlagged Terrestrial\n(Possible 30m Contaminant)')

# Keeps
dot_meio.attr('node', fillcolor='#e8f5e9', color='#2e7d32', fontcolor='#1b5e20')
dot_meio.node('M_K1', 'KEEP:\nTable 1.1 Meiofauna')

dot_meio.node('Start', 'Start: Meiobenthos', fillcolor='#E8EAF6', color='#283593')

# Edges
dot_meio.edge('Start', 'M_Q1', weight='10')
dot_meio.edge('M_Q1', 'M_D1', label=' Yes'); dot_meio.edge('M_Q1', 'M_Q2', label=' No', weight='10')
dot_meio.edge('M_Q2', 'M_D2', label=' Yes'); dot_meio.edge('M_Q2', 'M_Q3', label=' No', weight='10')
dot_meio.edge('M_Q3', 'M_D3', label=' Yes'); dot_meio.edge('M_Q3', 'M_Q4', label=' No', weight='10')
dot_meio.edge('M_Q4', 'M_D4', label=' Yes'); dot_meio.edge('M_Q4', 'M_Q5', label=' No', weight='10')
dot_meio.edge('M_Q5', 'M_K2', label=' Yes'); dot_meio.edge('M_Q5', 'M_Q6', label=' No', weight='10')
dot_meio.edge('M_Q6', 'M_K1', label=' Yes'); dot_meio.edge('M_Q6', 'M_D5', label=' No', weight='10')

dot_meio.render('Meiobenthos_Flowchart')
display(Image(filename='Meiobenthos_Flowchart.png'))


# ==============================================================================
# 3. BUILD THE RICH UI HTML FILE (Dual Mode)
# ==============================================================================
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Benthic Methodology Filter (Fais, 2021)</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🌊</text></svg>">

    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #eef2f5; margin: 0; display: flex; justify-content: center; align-items: center; height: 100vh; overflow: hidden; }
        .app-container { display: flex; max-width: 1200px; width: 95vw; background: white; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); height: 90vh; max-height: 650px; overflow: hidden; position: relative; }
        
        .home-panel { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: white; z-index: 10; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
        .home-panel h1 { color: #2c3e50; font-size: 32px; margin-bottom: 40px;}
        .mode-buttons { display: flex; gap: 30px; }
        .mode-card { background: #f8f9fa; border: 2px solid #e0e0e0; border-radius: 12px; padding: 40px; width: 250px; cursor: pointer; transition: 0.3s; }
        .mode-card:hover { border-color: #3498db; transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.05); }
        .mode-card div { font-size: 60px; margin-bottom: 20px; }
        .mode-card h3 { color: #333; margin: 0 0 10px 0; }
        .mode-card p { color: #7f8c8d; font-size: 14px; margin: 0; }

        .main-panel { width: 65%; padding: 30px 40px; display: none; flex-direction: column; position: relative; background: #fff; overflow-y: auto;}
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

        .history-panel { width: 35%; background: #fdfdfd; padding: 30px 25px; display: none; flex-direction: column; border-left: 1px solid #ddd;}
        .history-panel h3 { margin-top: 0; color: #555; text-transform: uppercase; font-size: 13px; letter-spacing: 1px; text-align: center; margin-bottom: 15px; flex-shrink: 0;}
        #historyList { flex-grow: 1; overflow-y: auto; padding-left: 15px; scroll-behavior: smooth; padding-right: 10px;}
        #historyList::-webkit-scrollbar { width: 6px; }
        #historyList::-webkit-scrollbar-track { background: transparent; }
        #historyList::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        #historyList::-webkit-scrollbar-thumb:hover { background: #94a3b8; }

        .tree-trunk { border-left: 3px solid #bdc3c7; padding-left: 25px; position: relative; padding-bottom: 20px; margin-left: 15px; margin-top: 5px;}
        .tree-node { border-radius: 6px; padding: 10px 12px; margin-bottom: 20px; position: relative; font-size: 12px; font-weight: 500; box-shadow: 0 2px 5px rgba(0,0,0,0.05); line-height: 1.4;}
        .tree-node::before { content: ""; position: absolute; left: -28px; top: 16px; width: 25px; height: 3px; background: #bdc3c7; }
        .tree-node::after { content: ""; position: absolute; left: -34px; top: 11px; width: 13px; height: 13px; border-radius: 50%; border: 2px solid #fff; }

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

        <div class="home-panel" id="homeScreen">
            <h1>Select Target Filter</h1>
            <div class="mode-buttons">
                <div class="mode-card" onclick="startApp('macro')">
                    <div>🦀</div>
                    <h3>Macrobenthos</h3>
                    <p>Standard macroscopic filtering logic</p>
                </div>
                <div class="mode-card" onclick="startApp('meio')">
                    <div>🔬</div>
                    <h3>Meiobenthos</h3>
                    <p>Based on explicit lists from Fais (2021) Table 1.1</p>
                </div>
            </div>
        </div>

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
                <button class="btn-sec" onclick="goHome()">🏠 Menu</button>
            </div>
        </div>

        <div class="history-panel" id="historyPanel">
            <h3 id="historyTitle">Live Flowchart Path</h3>
            <div id="historyList"></div>
        </div>

    </div>
    <script>
        // --- 1. MACROBENTHIC LOGIC ---
        const macroLogic = [
            { icon: "📉", title: "Low Statistical Confidence?", details: "<ul><li>e-value > 0.01</li></ul>", yes: "🔴 DISCARD: Low Statistical Confidence" },
            { icon: "🗄️", title: "Unmatched / Blank Taxonomic Data?", details: "<ul><li>Match Status: Not found in WoRMS</li><li>Match Status: Filtered (Environmental)</li><li>Kingdom: [Blank]</li></ul>", yes: "🔴 DISCARD: Unmatched/Non-Marine" },
            { icon: "🐾", title: "Kingdom NOT Animalia?", details: "<ul><li>Kingdom: Bacteria, Archaea, Protozoa, Chromista, Fungi, Plantae</li></ul>", yes: "🔴 DISCARD: Not Animalia" },
            { icon: "🕷️", title: "Terrestrial Arthropod?", details: "<ul><li>Class: Hexapoda (Insects)</li><li>Class: Arachnida (Spiders/Mites)</li><ul><li><em>Exception: Keep Family Halacaridae (Marine Mites)</em></li></ul></ul>", yes: "🔴 DISCARD: Terrestrial Contaminant" },
            { icon: "🦐", title: "Pelagic / Planktonic Taxon?", details: "<ul><li>Genera: Tomopteris, Alciopa, Limacina, Creseis, Themisto, Lucifer, Acartia, Oithona, Calanus, Centropages, Paracalanus, Temora, Penilia, Podon, Parasagitta, Euphausia</li><li>Class: Thaliacea, Appendicularia</li><li>Class: Copepoda (except Harpacticoida or benthic tag)</li><li>Tagged: Plankton or Nekton (without benthic tag)</li></ul>", yes: "🔴 DISCARD: Pelagic Exception" },
            { icon: "🐟", title: "Vertebrate Fish?", details: "<ul><li>Phylum: Chordata</li><ul><li><em>Exception: Keep Class Ascidiacea (Sea Squirts)</em></li><li><em>Exception: Keep Class Leptocardii (Lancelets)</em></li></ul></ul>", yes: "🔴 DISCARD: Pelagic Fish" },
            { icon: "🪱", title: "Parasitic Ecology?", details: "<ul><li>Feeding Method: parasitic</li><li>Ecological Interaction: parasitic</li><li>Phylum: Dicyemida</li><li>Family: Dicyemidae</li></ul>", yes: "🟢 KEEP: Parasite Flag" },
            { icon: "🐻", title: "Phylum Tardigrada?", details: "<ul><li>Phylum: Tardigrada (Water Bears)</li></ul>", yes: "🔴 DISCARD: Meiofauna Exception" },
            { icon: "🦀", title: "Explicit Benthos Tag?", details: "<ul><li>Functional Group: benthos / macrobenthos</li></ul>", yes: "🟢 KEEP: Confirmed Benthos" },
            { icon: "🦑", title: "Typically Benthic Phylum?", details: "<ul><li>Ecological Data: [Blank] or [Not Applicable]</li><li>Annelida, Mollusca, Arthropoda, Echinodermata, Platyhelminthes, Nematoda, Dicyemida, Chordata</li></ul>", yes: "🟢 KEEP: Taxonomic Proxy", no: "🟡 CHECK: Manual Review" }
        ];

        // --- 2. MEIOBENTHIC LOGIC (Fais, 2021) ---
        const meioLogic = [
            { icon: "📉", title: "Low Statistical Confidence?", details: "<ul><li>e-value > 0.01</li></ul>", yes: "🔴 DISCARD: Low Statistical Confidence" },
            { icon: "🗄️", title: "Unmatched / Blank Taxonomic Data?", details: "<ul><li>Match Status: Not found in WoRMS</li><li>Match Status: Filtered (Environmental)</li></ul>", yes: "🔴 DISCARD: Unmatched Data" },
            { icon: "🦐", title: "Pelagic / Planktonic Taxon?", details: "<ul><li>Genera: Tomopteris, Alciopa, Limacina, Creseis, Themisto, Lucifer, Acartia, Oithona, Calanus, Centropages, Paracalanus, Temora, Penilia, Podon, Parasagitta, Euphausia</li><li>Class: Thaliacea, Appendicularia</li><li>Class: Copepoda (except Harpacticoida or benthic tag)</li><li>Tagged: Plankton or Nekton (without benthic tag)</li></ul>", yes: "🔴 DISCARD: Pelagic Exception" },
            { icon: "⚠️", title: "Macro-Invertebrate Exception?", details: "<ul><li>Is it an Arthropod or Echinoderm but NOT explicitly kept below?</li><li><b>KEPT ARTHROPODA:</b> Cephalocarida, Branchiopoda, Ostracoda, Mystacocarida, Harpacticoida, Cyclopoida, Siphonostomatoida, Syncarida, Peracarida, Trombidiformes, Pycnogonida</li><li><b>KEPT ECHINODERMATA:</b> Holothuroidea</li><li><b>REMOVED:</b> All other Arthropods and Echinoderms</li></ul>", yes: "🔴 DISCARD: Macro-Invertebrate Exception" },
            { icon: "🌲", title: "Terrestrial Thalassobiont?", details: "<ul><li>Is it one of the terrestrial beach groups from Fais (2021)?</li><li>(Araneae, Pseudoscorpionida, Chilopoda, Collembola, Coleoptera, Diptera)</li><li><em>Note: These are kept but flagged, as they are likely contaminants at 30m depth.</em></li></ul>", yes: "🟡 KEEP: Flagged Terrestrial (Possible 30m Contaminant)" },
            { icon: "🦠", title: "Explicitly in Fais (2021) Phyla List?", details: "<ul><li><b>REMOVED:</b> Any phylum not explicitly listed here.</li><li><b>KEPT:</b> Foraminifera, Heliozoa, Ciliophora, Amoebozoa, Porifera, Cnidaria, Platyhelminthes, Gnathostomulida, Rotifera, Micrognathozoa, Nemertea, Nematoda, Kinorhyncha, Priapulida, Loricifera, Gastrotricha, Tardigrada, Annelida, Sipuncula, Mollusca, Brachiopoda, Bryozoa, Entoprocta, Chaetognata, Tunicata, Acarina (Marine mites)</li></ul>", yes: "🟢 KEEP: Table 1.1 Meiofauna", no: "🔴 DISCARD: Not in Table 1.1" }
        ];

        let activeLogic = [];
        let currentStep = 0;
        let pathMemory = [];
        let isEnd = false;

        function startApp(mode) {
            document.getElementById("homeScreen").style.display = "none";
            document.getElementById("mainPanel").style.display = "flex";
            document.getElementById("historyPanel").style.display = "flex";
            
            activeLogic = mode === 'macro' ? macroLogic : meioLogic;
            document.getElementById("historyTitle").innerText = mode === 'macro' ? "Macrobenthos Path" : "Meiobenthos Path";
            
            startOver();
        }

        function goHome() {
            document.getElementById("homeScreen").style.display = "flex";
            document.getElementById("mainPanel").style.display = "none";
            document.getElementById("historyPanel").style.display = "none";
        }

        function render() {
            const step = activeLogic[currentStep];
            document.getElementById("btnGroup").style.display = isEnd ? "none" : "flex";
            document.getElementById("mainPanel").style.backgroundColor = isEnd ? "" : "white";
            
            // Background color matches outcome for visual feedback
            if (isEnd) {
                if (step.resultText.includes("🔴")) document.getElementById("mainPanel").style.backgroundColor = "#ffebee"; // Red
                else if (step.resultText.includes("🟢")) document.getElementById("mainPanel").style.backgroundColor = "#e8f5e9"; // Green
                else if (step.resultText.includes("🟡")) document.getElementById("mainPanel").style.backgroundColor = "#fff8e1"; // Yellow
            }

            document.getElementById("qIcon").innerText = step.icon;
            document.getElementById("qTitle").innerHTML = isEnd ? "<strong>"+step.resultText+"</strong>" : step.title;
            document.getElementById("qDetails").innerHTML = isEnd ? "" : step.details;
            document.getElementById("qDetails").style.display = isEnd ? "none" : "block";

            let h = '<div class="tree-trunk">';
            pathMemory.forEach(m => {
                let colorClass = m.c === 'yes' ? 'node-red' : 'node-blue';
                h += `<div class="tree-node ${colorClass}">
                        <strong>${activeLogic[m.idx].title}</strong><br>
                        <span style="font-size:11px; opacity:0.8;">Decision: ${m.c.toUpperCase()}</span>
                      </div>`;
            });

            if (!isEnd) {
                h += `<div class="tree-node node-current">
                        <em style="font-size:11px; color:#888;">Currently Checking:</em><br>
                        <strong>${activeLogic[currentStep].title}</strong>
                      </div>`;
            } else {
                let result = activeLogic[currentStep].resultText;
                let finalClass = result.includes('KEEP') ? (result.includes('🟡') ? 'node-yellow' : 'node-green') : 'node-red';
                h += `<div class="tree-node ${finalClass}">
                        <strong>${result}</strong>
                      </div>`;
            }
            h += '</div>';

            document.getElementById("historyList").innerHTML = h;
            document.getElementById("secControls").style.display = pathMemory.length ? "flex" : "none";

            setTimeout(() => {
                const hList = document.getElementById("historyList");
                hList.scrollTop = hList.scrollHeight;
            }, 10);
        }

        function answer(c) {
            const step = activeLogic[currentStep];
            pathMemory.push({idx: currentStep, c: c});
            if (c === 'yes') {
                isEnd = true;
                step.resultText = step.yes;
            } else if (currentStep === activeLogic.length - 1) {
                isEnd = true;
                step.resultText = step.no || "🟡 CHECK: Manual Review";
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
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ Saved as 'index.html'. Upload this directly to GitHub.")
print("✅ PNG Flowcharts for Macrobenthos and Meiobenthos generated.")
