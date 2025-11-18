' ProductionKPITool.bas
' VBA module to calculate KPIs from sheet "production_data"
' Writes results to sheet "kpi_dashboard"

Option Explicit

' Main entry point called from the workbook or a macro button
Public Sub RunProductionKPI()
    On Error GoTo ErrHandler

    Dim wsData As Worksheet
    Dim wsOut As Worksheet
    Dim startDate As Date, endDate As Date
    Dim machine As String
    Dim shiftMinutes As Long

    Set wsData = ThisWorkbook.Worksheets("production_data")
    Set wsOut = ThisWorkbook.Worksheets("kpi_dashboard")

    ' Default shift length in minutes (e.g. 8 hours => 480 minutes)
    shiftMinutes = 480

    ' Show the user form to collect inputs
    ProductionKPIForm.Show vbModal

    ' Retrieve selections filled by the form
    startDate = ProductionKPIForm.StartDate.Value
    endDate = ProductionKPIForm.EndDate.Value
    machine = ProductionKPIForm.cboMachine.Value

    ' Clear previous dashboard
    ClearDashboard wsOut

    ' Filter data and compute KPIs
    Dim totalOutput As Double, totalDefects As Double, totalDowntime As Double
    Dim rowCount As Long

    Call ComputeKPIs(wsData, startDate, endDate, machine, shiftMinutes, totalOutput, totalDefects, totalDowntime, rowCount)

    ' Write results
    Call WriteDashboard(wsOut, startDate, endDate, machine, shiftMinutes, totalOutput, totalDefects, totalDowntime, rowCount)

    MsgBox "KPI Dashboard updated.", vbInformation, "Production KPI Tool"

    Exit Sub

ErrHandler:
    MsgBox "An error occurred: " & Err.Description, vbExclamation, "Error"
End Sub

' ComputeKPIs uses worksheet data and filters by date and machine
Public Sub ComputeKPIs(ws As Worksheet, startDate As Date, endDate As Date, machine As String, shiftMinutes As Long, _
                       ByRef totalOutput As Double, ByRef totalDefects As Double, ByRef totalDowntime As Double, ByRef rowCount As Long)
    Dim lastRow As Long
    Dim r As Long
    Dim d As Date
    Dim outVal As Double, defVal As Double, downVal As Double

    totalOutput = 0
    totalDefects = 0
    totalDowntime = 0
    rowCount = 0

    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row

    For r = 2 To lastRow ' assume headers in row 1
        d = ws.Cells(r, "A").Value
        If d >= startDate And d <= endDate Then
            If machine = "All" Or ws.Cells(r, "C").Value = machine Then
                outVal = NzNum(ws.Cells(r, "D").Value)
                defVal = NzNum(ws.Cells(r, "E").Value)
                downVal = NzNum(ws.Cells(r, "F").Value)

                totalOutput = totalOutput + outVal
                totalDefects = totalDefects + defVal
                totalDowntime = totalDowntime + downVal
                rowCount = rowCount + 1
            End If
        End If
    Next r
End Sub

' Clear dashboard sheet content and basic formatting
Public Sub ClearDashboard(ws As Worksheet)
    ws.Cells.Clear
    ws.Range("A1").Value = "Production KPI Dashboard"
    ws.Range("A1").Font.Bold = True
    ws.Range("A1").Font.Size = 14
End Sub

' WriteDashboard writes KPI values and formats them nicely
Public Sub WriteDashboard(ws As Worksheet, startDate As Date, endDate As Date, machine As String, shiftMinutes As Long, _
                          totalOutput As Double, totalDefects As Double, totalDowntime As Double, rowCount As Long)
    Dim defectRate As Double
    Dim utilization As Double
    Dim efficiencyScore As Double
    Dim shiftsCovered As Double

    If totalOutput = 0 Then
        defectRate = 0
        efficiencyScore = 0
    Else
        defectRate = totalDefects / totalOutput
        efficiencyScore = totalOutput / (totalOutput + totalDefects)
    End If

    ' Estimate shifts covered based on number of rows (if data has per-shift rows)
    If shiftMinutes > 0 Then
        shiftsCovered = rowCount
        If shiftsCovered = 0 Then shiftsCovered = 1 ' avoid division by zero
        utilization = 100 - ((totalDowntime / (shiftMinutes * shiftsCovered)) * 100)
    Else
        utilization = 0
    End If

    ws.Range("A3").Value = "Filters"
    ws.Range("A4").Value = "Start Date"
    ws.Range("B4").Value = startDate
    ws.Range("A5").Value = "End Date"
    ws.Range("B5").Value = endDate
    ws.Range("A6").Value = "Machine"
    ws.Range("B6").Value = machine

    ws.Range("A8").Value = "KPI"
    ws.Range("B8").Value = "Value"

    ws.Range("A9").Value = "Total Output"
    ws.Range("B9").Value = totalOutput

    ws.Range("A10").Value = "Total Defects"
    ws.Range("B10").Value = totalDefects

    ws.Range("A11").Value = "Defect Rate"
    ws.Range("B11").Value = defectRate

    ws.Range("A12").Value = "Machine Utilization (%)"
    ws.Range("B12").Value = utilization

    ws.Range("A13").Value = "Efficiency Score"
    ws.Range("B13").Value = efficiencyScore

    ' Format numbers
    ws.Range("B9").NumberFormat = "#,##0"
    ws.Range("B10").NumberFormat = "#,##0"
    ws.Range("B11").NumberFormat = "0.00%"
    ws.Range("B12").NumberFormat = "0.00%"
    ws.Range("B13").NumberFormat = "0.00%"

    ' Apply basic formatting
    Dim rng As Range
    Set rng = ws.Range("A8:B13")
    rng.Font.Bold = True
    rng.Borders.LineStyle = xlContinuous

    ' Color-code KPI results (simple rules)
    If defectRate > 0.05 Then
        ws.Range("B11").Interior.Color = RGB(255, 200, 200) ' light red
    Else
        ws.Range("B11").Interior.Color = RGB(200, 255, 200) ' light green
    End If

    If utilization < 85 Then
        ws.Range("B12").Interior.Color = RGB(255, 230, 150) ' light orange
    Else
        ws.Range("B12").Interior.Color = RGB(200, 255, 200)
    End If

End Sub
