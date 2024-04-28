Imports System.Threading

<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class MainForm
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    Private WithEvents timer As New Timer(AddressOf ShowButton, Nothing, 2000, Timeout.Infinite)

    Private Sub ShowButton(ByVal state As Object)
        ' Invoke on UI thread to avoid cross-thread operation
        Me.Invoke(Sub()
                      Button1.Visible = True
                      timer.Dispose() ' Dispose the timer to prevent it from firing again
                  End Sub)
    End Sub
    Private Sub MainForm_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Button1.Visible = False ' Hide the button initially
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim selectionForm As New SelectionForm()
        selectionForm.Show()
        Me.Hide()

    End Sub


    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Panel1 = New Panel()
        Button1 = New Button()
        Panel1.SuspendLayout()
        SuspendLayout()
        ' 
        ' Panel1
        ' 
        Panel1.BackgroundImage = My.Resources.Resources.ldc_logo
        Panel1.Controls.Add(Button1)
        Panel1.Location = New Point(1, 0)
        Panel1.Name = "Panel1"
        Panel1.Size = New Size(930, 700)
        Panel1.TabIndex = 0
        ' 
        ' Button1
        ' 
        Button1.BackColor = Color.FromArgb(CByte(179), CByte(239), CByte(220))
        Button1.Cursor = Cursors.Hand
        Button1.FlatAppearance.BorderSize = 0
        Button1.FlatStyle = FlatStyle.Popup
        Button1.Font = New Font("Segoe Script", 15.0F, FontStyle.Bold)
        Button1.Location = New Point(320, 570)
        Button1.Name = "Button1"
        Button1.Size = New Size(215, 58)
        Button1.TabIndex = 0
        Button1.Text = "Let's Begin 🍁"
        Button1.UseVisualStyleBackColor = False
        ' 
        ' MainForm
        ' 
        AutoScaleDimensions = New SizeF(8.0F, 20.0F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(930, 700)
        Controls.Add(Panel1)
        Name = "MainForm"
        Text = "Leaf Disease Classifier"
        Panel1.ResumeLayout(False)
        ResumeLayout(False)
    End Sub
    Friend WithEvents Panel1 As Panel
    Friend WithEvents Button1 As Button

End Class
