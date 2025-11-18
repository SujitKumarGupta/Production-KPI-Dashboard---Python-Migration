' Helpers.bas
' Utility helper functions used by the VBA modules
Option Explicit

' NzNum returns a numeric value or zero if the cell is empty or non-numeric
Public Function NzNum(val As Variant) As Double
    On Error GoTo ErrHandler
    If IsNumeric(val) Then
        NzNum = CDbl(val)
    ElseIf IsDate(val) Then
        NzNum = 0
    Else
        NzNum = 0
    End If
    Exit Function
ErrHandler:
    NzNum = 0
End Function

' Small function to ensure a string is not empty
Public Function NzStr(val As Variant) As String
    If IsNull(val) Then
        NzStr = ""
    ElseIf Trim(CStr(val)) = "" Then
        NzStr = ""
    Else
        NzStr = CStr(val)
    End If
End Function
