<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
  <h1>HysteresisAnalyzer – Energy Dissipation & Cycle Analysis Tool</h1>

  <p>
    <strong>HysteresisAnalyzer</strong> is a Python-based automated post-processing
    tool for calculating <strong>energy dissipation per loading cycle</strong>
    from force–displacement hysteresis data. The script reads experimental or
    numerical results from an Excel file, automatically detects full loading
    cycles, computes the enclosed hysteresis area for each cycle, and exports
    results with plots and data files.
  </p>

  <h2>Features</h2>
  <ul>
    <li><strong>Automatic Cycle Detection:</strong> Identifies full loading cycles based on displacement reversals.</li>
    <li><strong>Energy Dissipation Calculation:</strong> Computes hysteresis loop area using numerical integration.</li>
    <li><strong>Batch Processing:</strong> Handles any number of cycles in a single run.</li>
    <li><strong>Data Export:</strong> Saves each cycle as a separate CSV file.</li>
    <li><strong>Visualization:</strong> Generates force–displacement plots with annotated energy dissipation.</li>
    <li><strong>Organized Output:</strong> Automatically creates folders for cycles, plots, and energy values.</li>
  </ul>

  <h2>Usage Instructions</h2>
  <ol>
    <li>Ensure that Python and the required libraries are installed.</li>
    <li>Place your hysteresis data Excel file in the same directory as the script.
      <ul>
        <li>Column 1: Displacement (mm)</li>
        <li>Column 2: Force (kN)</li>
      </ul>
    </li>
    <li>Update the Excel file name in the script if required:
      <pre><code>file_name = "GlobalResponse_FDCurve.xlsx"</code></pre>
    </li>
    <li>Run the script:
      <pre><code>python hysteresis_analyzer.py</code></pre>
    </li>
    <li>Results will be generated automatically in the output folders.</li>
  </ol>

  <h2>Output Structure</h2>
  <pre><code>
Splitted Cycles/
├── cycle_1.csv
├── cycle_2.csv
├── ...
├── Plots/
│   ├── cycle_1.png
│   ├── cycle_2.png
│   └── ...
└── Areas/
    ├── cycle_1_area.txt
    ├── cycle_2_area.txt
    └── ...
  </code></pre>

  <h2>Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li>pandas</li>
    <li>numpy</li>
    <li>matplotlib</li>
    <li>scipy</li>
  </ul>

  <h2>Applications</h2>
  <ul>
    <li>Cyclic structural testing</li>
    <li>Seismic and hysteresis analysis</li>
    <li>Experimental mechanics</li>
    <li>Finite element post-processing</li>
    <li>Energy-based damage assessment</li>
  </ul>

  <h2>License</h2>
  <p>
    This project is licensed under the <strong>MIT License</strong>.
  </p>
  <p>
    You are free to use, modify, and distribute this software under the terms
    of the MIT License. If you use this software in your research or publications,
    please provide appropriate credit to the developer.
  </p>

  <h2>Developer Information</h2>
  <ul>
    <li><strong>Developer:</strong> Tufail Mabood</li>
    <li><strong>Contact:</strong> <a href="https://wa.me/+923440907874" target="_blank">WhatsApp</a></li>
    <li><strong>Note:</strong> This tool is open-source. Contributions, improvements,
        and validation studies are welcome.</li>
  </ul>
</body>
