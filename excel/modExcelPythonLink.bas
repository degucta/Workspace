Attribute VB_Name = "modExcelPythonLink"
Option Explicit

Public Sub copyText()
      'Call RunPython("import excel_test; excel_test.copy_add_text()")
      Call RunPython("import BookKeepingToolDev; BookKeepingToolDev.copy_add_text()")
End Sub
