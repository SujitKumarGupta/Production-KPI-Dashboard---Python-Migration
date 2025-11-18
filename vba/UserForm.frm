VERSION 5.00
Begin VB.Form ProductionKPIForm
   Caption         =   "Production KPI - Filters"
   ClientHeight    =   3000
   ClientLeft      =   120
   ClientTop       =   435
   ClientWidth     =   4650
   Begin VB.Label lblStart
      Caption         =   "Start Date"
      Left            =   240
      Top             =   360
      Width           =   1080
      Height          =   255
   End
   Begin VB.TextBox StartDate
      Left            =   1320
      Top             =   360
      Width           =   1440
      Height          =   255
      Text            =   ""
   End
   Begin VB.Label lblEnd
      Caption         =   "End Date"
      Left            =   240
      Top             =   720
      Width           =   1080
      Height          =   255
   End
   Begin VB.TextBox EndDate
      Left            =   1320
      Top             =   720
      Width           =   1440
      Height          =   255
      Text            =   ""
   End
   Begin VB.Label lblMachine
      Caption         =   "Machine"
      Left            =   240
      Top             =   1080
      Width           =   1080
      Height          =   255
   End
   Begin VB.ComboBox cboMachine
      Left            =   1320
      Top             =   1080
      Width           =   1440
      Height          =   255
   End
   Begin VB.CommandButton btnRun
      Caption         =   "Run"
      Left            =   1320
      Top             =   1620
      Width           =   960
      Height          =   375
   End
   Begin VB.CommandButton btnCancel
      Caption         =   "Cancel"
      Left            =   2400
      Top             =   1620
      Width           =   960
      Height          =   375
   End
End
' Note: In the VB6 / Excel UserForm designer this would be generated automatically.
' The form's runtime code (populate machine list, button handlers) should be added in the workbook module.
