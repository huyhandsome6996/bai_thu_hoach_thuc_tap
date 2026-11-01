param([Parameter(Mandatory=$true)][string]$InputPath,
      [Parameter(Mandatory=$true)][string]$PdfPath,
      [switch]$UpdateAndSave)
$ErrorActionPreference = 'Stop'
$sourcePath = (Resolve-Path -LiteralPath $InputPath).Path
$pdfTarget = [System.IO.Path]::GetFullPath($PdfPath)
New-Item -ItemType Directory -Path (Split-Path $pdfTarget -Parent) -Force | Out-Null
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
$doc = $null
try {
    $doc = $word.Documents.Open($sourcePath, $false, (-not $UpdateAndSave))
    if ($UpdateAndSave) {
        $doc.Fields.Update() | Out-Null
        foreach ($toc in $doc.TablesOfContents) { $toc.Update() }
        foreach ($tof in $doc.TablesOfFigures) { $tof.Update() }
        # Field refresh can import TOC font settings; enforce the requested body face/size.
        foreach ($styleName in @('TOC 1','TOC 2','TOC 3','TOC 4','Table of Figures')) {
            try { $s=$doc.Styles.Item($styleName); $s.Font.Name='Times New Roman'; $s.Font.Size=13; $s.Font.Color=0; $s.ParagraphFormat.SpaceBefore=0; $s.ParagraphFormat.SpaceAfter=0; $s.ParagraphFormat.LineSpacingRule=5; $s.ParagraphFormat.LineSpacing=14.4 } catch { }
        }
        # Leave room for page numbers when long TOC titles wrap.
        foreach ($toc in $doc.TablesOfContents) {
            $toc.Range.ParagraphFormat.RightIndent=$word.CentimetersToPoints(0.8)
        }
        $doc.Repaginate()
        foreach ($toc in $doc.TablesOfContents) { $toc.UpdatePageNumbers() }
        foreach ($tof in $doc.TablesOfFigures) { $tof.UpdatePageNumbers() }
        $doc.Save()
    }
    $doc.Repaginate()
    $pageCount=$doc.ComputeStatistics(2)
    $doc.ExportAsFixedFormat($pdfTarget,17)
    Write-Output "Word pages: $pageCount"
    Write-Output "PDF: $pdfTarget"
} finally {
    if ($null -ne $doc) { $doc.Close(0) }
    $word.Quit()
}
