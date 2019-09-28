Sub stockchallenge3():

For Each ws In Worksheets

    ' Set Dimensions
  Dim ticker As String
  Dim Total_Vol As Double
  Total_Vol = 0
   Dim openingprice As Double
   Dim closingprice As Double
   Dim percentagechange As Double
   ' insert headers
   ws.Range("H1").Value = "Ticker"
   ws.Range("I1").Value = "Difference"
   ws.Range("J1").Value = "Volume Total"
   ws.Range("K1").Value = "Percentage Change"
   
   
  ' Keep track of the location for ticker in the summary table
  Dim Summary_Table_Row As Integer
  Summary_Table_Row = 2
    
    ' find final row
   RowCount = ws.Cells(Rows.Count, "A").End(xlUp).Row

    ' loop through sheet and extract values
    For i = 2 To RowCount

    ' Check if we are still within the same credit card ticker, if it is not...
    If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
         ' Set the ticker name
      ticker = ws.Cells(i, 1).Value
      
      ' Calulate difference between opening and closing price
      
      openingprice = ws.Cells(Summary_Table_Row, 6).Value
        closingprice = ws.Cells(i, 6).Value
        pricedifference = closingprice - openingprice
            
            If pricedifference = 0 Then
            percentagechange = 0
            Else
            percentagechange = 100 * (pricedifference / openingprice)
            End If
      
     
      Total_Vol = Total_Vol + ws.Cells(i, 7).Value

      ' Print the Credit Card ticker in the Summary Table
      ws.Range("H" & Summary_Table_Row).Value = ticker
    
    ' Print the Credit Card ticker in the Summary Table
      ws.Range("I" & Summary_Table_Row).Value = pricedifference
      ' Print the ticker Amount to the Summary Table
      ws.Range("J" & Summary_Table_Row).Value = Total_Vol
      ws.Range("K" & Summary_Table_Row).Value = percentagechange

      ' Add one to the summary table row
      Summary_Table_Row = Summary_Table_Row + 1
      
      ' Reset the ticker Total
      Total_Vol = 0

    ' If the cell immediately following a row is the same ticker...
    Else

      ' Add to the ticker Total
      Total_Vol = Total_Vol + ws.Cells(i, 7).Value

    End If

  Next i
  
  LastRow = ws.Cells(Rows.Count, "H").End(xlUp).Row
  
' Add the percentage and colors
        For i = 2 To LastRow

                ws.Range("K" & i).NumberFormat = "0.00%"
                
                If ws.Range("I" & i).Value < 0 Then
                    ws.Range("I" & i).Interior.ColorIndex = 3
                
                Else
                    ws.Range("I" & i).Interior.ColorIndex = 4
                
                End If
        Next i
        
        
    
Next ws

End Sub



