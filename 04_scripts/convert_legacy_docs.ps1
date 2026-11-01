$ErrorActionPreference = 'Stop'
# Run from a Windows session with Microsoft Word installed. Original DOCs stay read-only.
$taskRoot = Split-Path $PSScriptRoot -Parent
$outDir = Join-Path $PSScriptRoot 'extracted_sources'
New-Item -ItemType Directory -Path $outDir -Force | Out-Null
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
    foreach ($file in (Get-ChildItem -LiteralPath (Join-Path $taskRoot '01_raw_data') | Where-Object Extension -eq '.doc')) {
        $document = $null
        try {
            $document = $word.Documents.Open($file.FullName, $false, $true)
            [string]$targetPath = Join-Path $outDir ($file.BaseName + '.docx')
            $document.SaveAs2($targetPath, 16)
        } finally {
            if ($null -ne $document) { $document.Close(0) }
        }
    }
} finally { $word.Quit() }
