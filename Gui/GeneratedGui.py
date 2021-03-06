# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct 12 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.grid

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BaronPOS", pos = wx.DefaultPosition, size = wx.Size( 1067,705 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer1 = wx.FlexGridSizer( 1, 4, 0, 0 )
		fgSizer1.AddGrowableCol( 2 )
		fgSizer1.AddGrowableRow( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbFuncties = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Functies" ), wx.VERTICAL )
		
		self.pnlFuncties = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnHeropen = wx.Button( self.pnlFuncties, wx.ID_ANY, u"Heropen\nLaatste\nTicket", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnHeropen.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer33.Add( self.btnHeropen, 0, wx.ALL, 1 )
		
		self.btnNieuwTicket = wx.Button( self.pnlFuncties, wx.ID_ANY, u"Nieuw\nTicket", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnNieuwTicket.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer33.Add( self.btnNieuwTicket, 0, wx.ALL, 1 )
		
		self.btnInOutToggle = wx.ToggleButton( self.pnlFuncties, wx.ID_ANY, u"In/Out", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnInOutToggle.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer33.Add( self.btnInOutToggle, 0, wx.ALL, 1 )
		
		self.btnAanbDirToggle = wx.ToggleButton( self.pnlFuncties, wx.ID_ANY, u"Aanb. Dir.", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnAanbDirToggle.SetValue( True ) 
		self.btnAanbDirToggle.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer33.Add( self.btnAanbDirToggle, 0, wx.ALL, 1 )
		
		self.btnAdmin = wx.Button( self.pnlFuncties, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.btnAdmin.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer33.Add( self.btnAdmin, 0, wx.ALL, 1 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnRetour = wx.ToggleButton( self.pnlFuncties, wx.ID_ANY, u"Retour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnRetour.SetValue( True ) 
		bSizer18.Add( self.btnRetour, 0, wx.ALIGN_BOTTOM, 0 )
		
		bSizer33.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		self.pnlFuncties.SetSizer( bSizer33 )
		self.pnlFuncties.Layout()
		bSizer33.Fit( self.pnlFuncties )
		sbFuncties.Add( self.pnlFuncties, 1, wx.EXPAND |wx.ALL, 0 )
		
		fgSizer1.Add( sbFuncties, 1, wx.EXPAND, 5 )
		
		self.sbGroepen = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Groepen" ), wx.VERTICAL )
		
		fgSizer1.Add( self.sbGroepen, 1, wx.EXPAND, 1 )
		
		self.sbProducten = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Producten" ), wx.VERTICAL )
		
		fgSizer1.Add( self.sbProducten, 1, wx.EXPAND, 1 )
		
		sbRekening = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Rekening" ), wx.VERTICAL )
		
		self.pnlRekening = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTotal = wx.StaticText( self.pnlRekening, wx.ID_ANY, u"€ 00,00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTotal.Wrap( -1 )
		self.lblTotal.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.lblTotal, 0, wx.ALIGN_RIGHT|wx.ALL, 1 )
		
		self.gOrder = wx.grid.Grid( self.pnlRekening, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.gOrder.CreateGrid( 15, 3 )
		self.gOrder.EnableEditing( False )
		self.gOrder.EnableGridLines( False )
		self.gOrder.EnableDragGridSize( False )
		self.gOrder.SetMargins( 0, 0 )
		
		# Columns
		self.gOrder.EnableDragColMove( False )
		self.gOrder.EnableDragColSize( False )
		self.gOrder.SetColLabelSize( 25 )
		self.gOrder.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gOrder.EnableDragRowSize( True )
		self.gOrder.SetRowLabelSize( 0 )
		self.gOrder.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.gOrder.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer7.Add( self.gOrder, 0, wx.ALL, 1 )
		
		fgSizer3 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnAfrekeken = wx.Button( self.pnlRekening, wx.ID_ANY, u"Afrekenen", wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.btnAfrekeken.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer11.Add( self.btnAfrekeken, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 1 )
		
		self.btnAnnuleren = wx.Button( self.pnlRekening, wx.ID_ANY, u"Annuleren", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
		self.btnAnnuleren.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer11.Add( self.btnAnnuleren, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 1 )
		
		fgSizer3.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnQtyMin = wx.Button( self.pnlRekening, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		self.btnQtyMin.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.btnQtyMin.SetForegroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer12.Add( self.btnQtyMin, 0, wx.ALL, 5 )
		
		fgSizer3.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		bSizer7.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		self.pnlRekening.SetSizer( bSizer7 )
		self.pnlRekening.Layout()
		bSizer7.Fit( self.pnlRekening )
		sbRekening.Add( self.pnlRekening, 1, wx.EXPAND |wx.ALL, 1 )
		
		fgSizer1.Add( sbRekening, 1, wx.EXPAND, 1 )
		
		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 1 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnHeropen.Bind( wx.EVT_BUTTON, self.btnHeropenOnButtonClick )
		self.btnNieuwTicket.Bind( wx.EVT_BUTTON, self.btnNieuwTicketOnButtonClick )
		self.btnInOutToggle.Bind( wx.EVT_TOGGLEBUTTON, self.btnInOutToggleOnToggleButton )
		self.btnAanbDirToggle.Bind( wx.EVT_TOGGLEBUTTON, self.btnAanbDirToggleOnToggleButton )
		self.btnAdmin.Bind( wx.EVT_BUTTON, self.btnAdminOnButtonClick )
		self.btnRetour.Bind( wx.EVT_TOGGLEBUTTON, self.btnRetourOnToggleButton )
		self.gOrder.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.gOrderOnGridSelectCell )
		self.btnAfrekeken.Bind( wx.EVT_BUTTON, self.btnAfrekekenOnButtonClick )
		self.btnAnnuleren.Bind( wx.EVT_BUTTON, self.btnAnnulerenOnButtonClick )
		self.btnQtyMin.Bind( wx.EVT_BUTTON, self.btnQtyMinOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnHeropenOnButtonClick( self, event ):
		event.Skip()
	
	def btnNieuwTicketOnButtonClick( self, event ):
		event.Skip()
	
	def btnInOutToggleOnToggleButton( self, event ):
		event.Skip()
	
	def btnAanbDirToggleOnToggleButton( self, event ):
		event.Skip()
	
	def btnAdminOnButtonClick( self, event ):
		event.Skip()
	
	def btnRetourOnToggleButton( self, event ):
		event.Skip()
	
	def gOrderOnGridSelectCell( self, event ):
		event.Skip()
	
	def btnAfrekekenOnButtonClick( self, event ):
		event.Skip()
	
	def btnAnnulerenOnButtonClick( self, event ):
		event.Skip()
	
	def btnQtyMinOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class PaymentFrameBase
###########################################################################

class PaymentFrameBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.STAY_ON_TOP|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer3 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		gSizer2 = wx.GridSizer( 4, 3, 0, 0 )
		
		self.btnSeven = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnSeven, 0, wx.ALL, 0 )
		
		self.btnEight = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnEight, 0, wx.ALL, 0 )
		
		self.btnNine = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnNine, 0, wx.ALL, 0 )
		
		self.btnFour = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnFour, 0, wx.ALL, 0 )
		
		self.btnFive = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnFive, 0, wx.ALL, 0 )
		
		self.btnSix = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnSix, 0, wx.ALL, 0 )
		
		self.btnOne = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnOne, 0, wx.ALL, 0 )
		
		self.btnTwo = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnTwo, 0, wx.ALL, 0 )
		
		self.btnThree = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnThree, 0, wx.ALL, 0 )
		
		self.btnDot = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnDot, 0, wx.ALL, 0 )
		
		self.btnZero = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnZero, 0, wx.ALL, 0 )
		
		self.btnEnter = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnEnter, 0, wx.ALL, 0 )
		
		fgSizer3.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer4.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		fgSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		gSizer3 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.btnCash = wx.Button( self, wx.ID_ANY, u"Cash", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer3.Add( self.btnCash, 0, wx.ALIGN_RIGHT|wx.ALL, 0 )
		
		self.btnAtos = wx.Button( self, wx.ID_ANY, u"Atos", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer3.Add( self.btnAtos, 0, wx.ALL, 0 )
		
		self.btnClr = wx.Button( self, wx.ID_ANY, u"Clr", wx.DefaultPosition, wx.Size( 40,30 ), 0 )
		gSizer3.Add( self.btnClr, 0, wx.ALIGN_BOTTOM|wx.ALIGN_LEFT|wx.ALL, 0 )
		
		self.btnCls = wx.Button( self, wx.ID_ANY, u"Cls", wx.DefaultPosition, wx.Size( 40,30 ), 0 )
		gSizer3.Add( self.btnCls, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL, 0 )
		
		gbSizer1.Add( gSizer3, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer5 = wx.FlexGridSizer( 5, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Klantnaam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer5.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.txtCustomerName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		fgSizer5.Add( self.txtCustomerName, 0, wx.ALL, 0 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Klantkaart", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		fgSizer5.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txtKantKaart = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer31.Add( self.txtKantKaart, 0, wx.ALL, 0 )
		
		self.btnKlantOpzoeken = wx.Button( self, wx.ID_ANY, u"Opzoeken", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		bSizer31.Add( self.btnKlantOpzoeken, 0, wx.ALL, 0 )
		
		fgSizer5.Add( bSizer31, 1, wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Punten Ticket", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.txtPuntenTicket = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.txtPuntenTicket, 0, wx.ALL, 0 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Punten op kaart", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer5.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.txtPuntenKaart = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer5.Add( self.txtPuntenKaart, 0, wx.ALL, 0 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Nieuw Saldo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer5.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txtNieuwSaldo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer25.Add( self.txtNieuwSaldo, 0, wx.ALL, 0 )
		
		self.btnAddLoyaltyPoints = wx.Button( self, wx.ID_ANY, u"Toevoegen", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		bSizer25.Add( self.btnAddLoyaltyPoints, 0, 0, 0 )
		
		fgSizer5.Add( bSizer25, 1, wx.EXPAND, 5 )
		
		self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"Verworven korting", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )
		fgSizer5.Add( self.m_staticText81, 0, wx.ALL, 5 )
		
		self.txtKorting = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer5.Add( self.txtKorting, 0, wx.ALL, 0 )
		
		self.btnPrintKitchen = wx.Button( self, wx.ID_ANY, u"Keuken\nbon", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		fgSizer5.Add( self.btnPrintKitchen, 0, wx.ALIGN_RIGHT, 5 )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		self.chkPrintKitchen = wx.CheckBox( self, wx.ID_ANY, u"Keukenbon Afd.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.chkPrintKitchen.SetValue(True) 
		bSizer32.Add( self.chkPrintKitchen, 0, wx.ALIGN_RIGHT, 0 )
		
		self.chkPrintTicket = wx.CheckBox( self, wx.ID_ANY, u"Ticket Afd.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.chkPrintTicket.SetValue(True) 
		bSizer32.Add( self.chkPrintTicket, 0, wx.ALIGN_RIGHT, 0 )
		
		fgSizer5.Add( bSizer32, 1, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 0 )
		
		bSizer20.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		gbSizer1.Add( bSizer20, wx.GBPosition( 1, 2 ), wx.GBSpan( 2, 1 ), wx.EXPAND, 5 )
		
		gSizer5 = wx.GridSizer( 4, 2, 0, 0 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Totaal:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gSizer5.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.txtTotal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer5.Add( self.txtTotal, 0, wx.ALL, 0 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Te Betalen:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.txtTotalToPay = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer5.Add( self.txtTotalToPay, 0, wx.ALL, 0 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Betaald:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.txtPayed = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer5.Add( self.txtPayed, 0, wx.ALL, 0 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Terug te geven:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gSizer5.Add( self.m_staticText5, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.txtReturn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer5.Add( self.txtReturn, 0, wx.ALL, 0 )
		
		gbSizer1.Add( gSizer5, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		fgSizer3.Add( gbSizer1, 1, wx.EXPAND, 5 )
		
		bSizer15.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer15 )
		self.Layout()
		bSizer15.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnSeven.Bind( wx.EVT_BUTTON, self.btnSevenOnButtonClick )
		self.btnEight.Bind( wx.EVT_BUTTON, self.btnEightOnButtonClick )
		self.btnNine.Bind( wx.EVT_BUTTON, self.btnNineOnButtonClick )
		self.btnFour.Bind( wx.EVT_BUTTON, self.btnFourOnButtonClick )
		self.btnFive.Bind( wx.EVT_BUTTON, self.btnFiveOnButtonClick )
		self.btnSix.Bind( wx.EVT_BUTTON, self.btnSixOnButtonClick )
		self.btnOne.Bind( wx.EVT_BUTTON, self.btnOneOnButtonClick )
		self.btnTwo.Bind( wx.EVT_BUTTON, self.btnTwoOnButtonClick )
		self.btnThree.Bind( wx.EVT_BUTTON, self.btnThreeOnButtonClick )
		self.btnDot.Bind( wx.EVT_BUTTON, self.btnDotOnButtonClick )
		self.btnZero.Bind( wx.EVT_BUTTON, self.btnZeroOnButtonClick )
		self.btnEnter.Bind( wx.EVT_BUTTON, self.btnEnterOnButtonClick )
		self.btnCash.Bind( wx.EVT_BUTTON, self.btnCashOnButtonClick )
		self.btnAtos.Bind( wx.EVT_BUTTON, self.btnAtosOnButtonClick )
		self.btnClr.Bind( wx.EVT_BUTTON, self.btnClrOnButtonClick )
		self.btnCls.Bind( wx.EVT_BUTTON, self.btnClsOnButtonClick )
		self.txtKantKaart.Bind( wx.EVT_CHAR, self.txtKantKaartOnChar )
		self.txtKantKaart.Bind( wx.EVT_KILL_FOCUS, self.txtKantKaartOnKillFocus )
		self.btnKlantOpzoeken.Bind( wx.EVT_BUTTON, self.btnKlantOpzoekenOnButtonClick )
		self.txtPuntenTicket.Bind( wx.EVT_SET_FOCUS, self.txtPuntenTicketOnSetFocus )
		self.btnAddLoyaltyPoints.Bind( wx.EVT_BUTTON, self.btnAddLoyaltyPointsOnButtonClick )
		self.btnPrintKitchen.Bind( wx.EVT_BUTTON, self.btnPrintKitchenOnButtonClick )
		self.chkPrintKitchen.Bind( wx.EVT_CHECKBOX, self.chkPrintKitchenOnCheckBox )
		self.chkPrintTicket.Bind( wx.EVT_CHECKBOX, self.chkPrintTicketOnCheckBox )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnSevenOnButtonClick( self, event ):
		event.Skip()
	
	def btnEightOnButtonClick( self, event ):
		event.Skip()
	
	def btnNineOnButtonClick( self, event ):
		event.Skip()
	
	def btnFourOnButtonClick( self, event ):
		event.Skip()
	
	def btnFiveOnButtonClick( self, event ):
		event.Skip()
	
	def btnSixOnButtonClick( self, event ):
		event.Skip()
	
	def btnOneOnButtonClick( self, event ):
		event.Skip()
	
	def btnTwoOnButtonClick( self, event ):
		event.Skip()
	
	def btnThreeOnButtonClick( self, event ):
		event.Skip()
	
	def btnDotOnButtonClick( self, event ):
		event.Skip()
	
	def btnZeroOnButtonClick( self, event ):
		event.Skip()
	
	def btnEnterOnButtonClick( self, event ):
		event.Skip()
	
	def btnCashOnButtonClick( self, event ):
		event.Skip()
	
	def btnAtosOnButtonClick( self, event ):
		event.Skip()
	
	def btnClrOnButtonClick( self, event ):
		event.Skip()
	
	def btnClsOnButtonClick( self, event ):
		event.Skip()
	
	def txtKantKaartOnChar( self, event ):
		event.Skip()
	
	def txtKantKaartOnKillFocus( self, event ):
		event.Skip()
	
	def btnKlantOpzoekenOnButtonClick( self, event ):
		event.Skip()
	
	def txtPuntenTicketOnSetFocus( self, event ):
		event.Skip()
	
	def btnAddLoyaltyPointsOnButtonClick( self, event ):
		event.Skip()
	
	def btnPrintKitchenOnButtonClick( self, event ):
		event.Skip()
	
	def chkPrintKitchenOnCheckBox( self, event ):
		event.Skip()
	
	def chkPrintTicketOnCheckBox( self, event ):
		event.Skip()
	

###########################################################################
## Class AdminDialogBase
###########################################################################

class AdminDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Admin", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Kassa" ), wx.VERTICAL )
		
		self.btnKasAfsluiten = wx.Button( self, wx.ID_ANY, u"Kas Afsluiten", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.btnKasAfsluiten, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnKasAfsluitenTest = wx.Button( self, wx.ID_ANY, u"Test Afsluiting", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.btnKasAfsluitenTest, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer17.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Klanten" ), wx.VERTICAL )
		
		self.btnKlantKaartBeheer = wx.Button( self, wx.ID_ANY, u"Klantenbeheer", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.btnKlantKaartBeheer, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer17.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Configuratie" ), wx.VERTICAL )
		
		self.btnBackTrans = wx.Button( self, wx.ID_ANY, u"Backup Transacties", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer7.Add( self.btnBackTrans, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnProgKassa = wx.Button( self, wx.ID_ANY, u"Programmeer Kassa", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer7.Add( self.btnProgKassa, 0, wx.ALL, 5 )
		
		bSizer24.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		bSizer17.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer17 )
		self.Layout()
		bSizer17.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnKasAfsluiten.Bind( wx.EVT_BUTTON, self.btnKasAfsluitenOnButtonClick )
		self.btnKasAfsluitenTest.Bind( wx.EVT_BUTTON, self.btnKasAfsluitenTestOnButtonClick )
		self.btnKlantKaartBeheer.Bind( wx.EVT_BUTTON, self.btnKlantKaartBeheerOnButtonClick )
		self.btnBackTrans.Bind( wx.EVT_BUTTON, self.btnBackTransOnButtonClick )
		self.btnProgKassa.Bind( wx.EVT_BUTTON, self.btnProgKassaOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnKasAfsluitenOnButtonClick( self, event ):
		event.Skip()
	
	def btnKasAfsluitenTestOnButtonClick( self, event ):
		event.Skip()
	
	def btnKlantKaartBeheerOnButtonClick( self, event ):
		event.Skip()
	
	def btnBackTransOnButtonClick( self, event ):
		event.Skip()
	
	def btnProgKassaOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgAskForPriceBase
###########################################################################

class dlgAskForPriceBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Prijs ingeven", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer37 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnDivide = wx.Button( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.Size( 60,30 ), 0 )
		bSizer37.Add( self.btnDivide, 0, 0, 5 )
		
		self.btnMultiply = wx.Button( self, wx.ID_ANY, u"*", wx.DefaultPosition, wx.Size( 60,30 ), 0 )
		bSizer37.Add( self.btnMultiply, 0, 0, 5 )
		
		self.btnSubtract = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 60,30 ), 0 )
		bSizer37.Add( self.btnSubtract, 0, 0, 5 )
		
		self.btnAdd = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 60,30 ), 0 )
		bSizer37.Add( self.btnAdd, 0, 0, 5 )
		
		self.btnEquals = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		bSizer37.Add( self.btnEquals, 0, 0, 5 )
		
		
		bSizer37.AddSpacer( ( 0, 60), 1, wx.EXPAND, 5 )
		
		self.btnBack = wx.Button( self, wx.ID_ANY, u"<-", wx.DefaultPosition, wx.Size( 60,30 ), 0 )
		bSizer37.Add( self.btnBack, 0, 0, 5 )
		
		gbSizer2.Add( bSizer37, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 4, 3, 0, 0 )
		
		self.btnSeven = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnSeven, 0, wx.ALL, 0 )
		
		self.btnEight = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnEight, 0, wx.ALL, 0 )
		
		self.btnNine = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnNine, 0, wx.ALL, 0 )
		
		self.btnFour = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnFour, 0, wx.ALL, 0 )
		
		self.btnFive = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnFive, 0, wx.ALL, 0 )
		
		self.btnSix = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnSix, 0, wx.ALL, 0 )
		
		self.btnOne = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnOne, 0, wx.ALL, 0 )
		
		self.btnTwo = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnTwo, 0, wx.ALL, 0 )
		
		self.btnThree = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnThree, 0, wx.ALL, 0 )
		
		self.btnDot = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnDot, 0, wx.ALL, 0 )
		
		self.btnZero = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnZero, 0, wx.ALL, 0 )
		
		self.btnEnter = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer2.Add( self.btnEnter, 0, wx.ALL, 0 )
		
		bSizer36.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		self.btnClear = wx.Button( self, wx.ID_ANY, u"Clr", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		bSizer36.Add( self.btnClear, 0, wx.ALL|wx.EXPAND, 0 )
		
		gbSizer2.Add( bSizer36, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.txtPrice = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,50 ), wx.TE_READONLY|wx.TE_RIGHT )
		self.txtPrice.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.txtPrice, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		bSizer20.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer20 )
		self.Layout()
		bSizer20.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnDivide.Bind( wx.EVT_BUTTON, self.btnDivideOnButtonClick )
		self.btnMultiply.Bind( wx.EVT_BUTTON, self.btnMultiplyOnButtonClick )
		self.btnSubtract.Bind( wx.EVT_BUTTON, self.btnSubtractOnButtonClick )
		self.btnAdd.Bind( wx.EVT_BUTTON, self.btnAddOnButtonClick )
		self.btnEquals.Bind( wx.EVT_BUTTON, self.btnEqualsOnButtonClick )
		self.btnBack.Bind( wx.EVT_BUTTON, self.btnBackOnButtonClick )
		self.btnSeven.Bind( wx.EVT_BUTTON, self.btnSevenOnButtonClick )
		self.btnEight.Bind( wx.EVT_BUTTON, self.btnEightOnButtonClick )
		self.btnNine.Bind( wx.EVT_BUTTON, self.btnNineOnButtonClick )
		self.btnFour.Bind( wx.EVT_BUTTON, self.btnFourOnButtonClick )
		self.btnFive.Bind( wx.EVT_BUTTON, self.btnFiveOnButtonClick )
		self.btnSix.Bind( wx.EVT_BUTTON, self.btnSixOnButtonClick )
		self.btnOne.Bind( wx.EVT_BUTTON, self.btnOneOnButtonClick )
		self.btnTwo.Bind( wx.EVT_BUTTON, self.btnTwoOnButtonClick )
		self.btnThree.Bind( wx.EVT_BUTTON, self.btnThreeOnButtonClick )
		self.btnDot.Bind( wx.EVT_BUTTON, self.btnDotOnButtonClick )
		self.btnZero.Bind( wx.EVT_BUTTON, self.btnZeroOnButtonClick )
		self.btnEnter.Bind( wx.EVT_BUTTON, self.btnEnterOnButtonClick )
		self.btnClear.Bind( wx.EVT_BUTTON, self.btnClearOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnDivideOnButtonClick( self, event ):
		event.Skip()
	
	def btnMultiplyOnButtonClick( self, event ):
		event.Skip()
	
	def btnSubtractOnButtonClick( self, event ):
		event.Skip()
	
	def btnAddOnButtonClick( self, event ):
		event.Skip()
	
	def btnEqualsOnButtonClick( self, event ):
		event.Skip()
	
	def btnBackOnButtonClick( self, event ):
		event.Skip()
	
	def btnSevenOnButtonClick( self, event ):
		event.Skip()
	
	def btnEightOnButtonClick( self, event ):
		event.Skip()
	
	def btnNineOnButtonClick( self, event ):
		event.Skip()
	
	def btnFourOnButtonClick( self, event ):
		event.Skip()
	
	def btnFiveOnButtonClick( self, event ):
		event.Skip()
	
	def btnSixOnButtonClick( self, event ):
		event.Skip()
	
	def btnOneOnButtonClick( self, event ):
		event.Skip()
	
	def btnTwoOnButtonClick( self, event ):
		event.Skip()
	
	def btnThreeOnButtonClick( self, event ):
		event.Skip()
	
	def btnDotOnButtonClick( self, event ):
		event.Skip()
	
	def btnZeroOnButtonClick( self, event ):
		event.Skip()
	
	def btnEnterOnButtonClick( self, event ):
		event.Skip()
	
	def btnClearOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgKlantBeheerBase
###########################################################################

class dlgKlantBeheerBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Klanten Overzicht", pos = wx.DefaultPosition, size = wx.Size( 750,-1 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		self.grdCustomer = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		
		# Grid
		self.grdCustomer.CreateGrid( 25, 5 )
		self.grdCustomer.EnableEditing( False )
		self.grdCustomer.EnableGridLines( True )
		self.grdCustomer.EnableDragGridSize( False )
		self.grdCustomer.SetMargins( 0, 0 )
		
		# Columns
		self.grdCustomer.AutoSizeColumns()
		self.grdCustomer.EnableDragColMove( False )
		self.grdCustomer.EnableDragColSize( True )
		self.grdCustomer.SetColLabelSize( 30 )
		self.grdCustomer.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grdCustomer.EnableDragRowSize( True )
		self.grdCustomer.SetRowLabelSize( 30 )
		self.grdCustomer.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grdCustomer.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.grdCustomer.SetMinSize( wx.Size( -1,600 ) )
		
		bSizer26.Add( self.grdCustomer, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnBewerk = wx.Button( self, wx.ID_ANY, u"Bewerk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.btnBewerk, 0, wx.ALL, 5 )
		
		self.btnNieuw = wx.Button( self, wx.ID_ANY, u"Nieuw", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.btnNieuw, 0, wx.ALL, 5 )
		
		self.btnVerwijder = wx.Button( self, wx.ID_ANY, u"Verwijder", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.btnVerwijder, 0, wx.ALL, 5 )
		
		self.btnSelect = wx.Button( self, wx.ID_ANY, u"Selecteer", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.btnSelect, 0, wx.ALL, 5 )
		
		bSizer26.Add( bSizer27, 1, wx.EXPAND, 5 )
		
		bSizer23.Add( bSizer26, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer23 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.dlgKlantBeheerBaseOnClose )
		self.grdCustomer.Bind( wx.grid.EVT_GRID_COL_SIZE, self.grdCustomerOnGridColSize )
		self.grdCustomer.Bind( wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.grdCustomerOnGridLabelLeftClick )
		self.btnBewerk.Bind( wx.EVT_BUTTON, self.btnBewerkOnButtonClick )
		self.btnNieuw.Bind( wx.EVT_BUTTON, self.btnNieuwOnButtonClick )
		self.btnVerwijder.Bind( wx.EVT_BUTTON, self.btnVerwijderOnButtonClick )
		self.btnSelect.Bind( wx.EVT_BUTTON, self.btnSelectOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dlgKlantBeheerBaseOnClose( self, event ):
		event.Skip()
	
	def grdCustomerOnGridColSize( self, event ):
		event.Skip()
	
	def grdCustomerOnGridLabelLeftClick( self, event ):
		event.Skip()
	
	def btnBewerkOnButtonClick( self, event ):
		event.Skip()
	
	def btnNieuwOnButtonClick( self, event ):
		event.Skip()
	
	def btnVerwijderOnButtonClick( self, event ):
		event.Skip()
	
	def btnSelectOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgCustomerEditBase
###########################################################################

class dlgCustomerEditBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Klant Beheren", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer6 = wx.FlexGridSizer( 11, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Nr.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer6.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.txtNr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer6.Add( self.txtNr, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Klantkaart", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer6.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txtKlantkaart = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		bSizer30.Add( self.txtKlantkaart, 0, wx.ALL, 5 )
		
		self.txtPunten = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txtPunten.Enable( False )
		
		bSizer30.Add( self.txtPunten, 0, wx.ALL, 5 )
		
		self.btnToevoegen = wx.Button( self, wx.ID_ANY, u"Punten Toevoegen", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.btnToevoegen, 0, wx.ALL, 5 )
		
		fgSizer6.Add( bSizer30, 1, wx.EXPAND, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Naam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer6.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.txtNaam = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 360,-1 ), 0 )
		fgSizer6.Add( self.txtNaam, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Voornaam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer6.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.txtVoornaam = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 360,-1 ), 0 )
		fgSizer6.Add( self.txtVoornaam, 0, wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Adres", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer6.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.txtAdres = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 360,-1 ), 0 )
		fgSizer6.Add( self.txtAdres, 0, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Postcode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer6.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txtPostcode = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.txtPostcode, 0, wx.ALL, 5 )
		
		cmbGemeenteChoices = []
		self.cmbGemeente = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), cmbGemeenteChoices, 0 )
		bSizer29.Add( self.cmbGemeente, 0, wx.ALL, 5 )
		
		fgSizer6.Add( bSizer29, 1, wx.EXPAND, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Tel/GSM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		fgSizer6.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.txtTelefoon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 360,-1 ), 0 )
		fgSizer6.Add( self.txtTelefoon, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Geb. Datum", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		fgSizer6.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.datePickerGeboorte = wx.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer6.Add( self.datePickerGeboorte, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Emailadres", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer6.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.txtEmailadres = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 360,-1 ), 0 )
		fgSizer6.Add( self.txtEmailadres, 0, wx.ALL, 5 )
		
		self.btnOpslaan = wx.Button( self, wx.ID_ANY, u"Opslaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.btnOpslaan, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnOpslaanEnNieuw = wx.Button( self, wx.ID_ANY, u"Opslaan +\nNieuw", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.btnOpslaanEnNieuw, 0, wx.ALL, 5 )
		
		bSizer28.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer28 )
		self.Layout()
		bSizer28.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.txtKlantkaart.Bind( wx.EVT_KILL_FOCUS, self.txtKlantkaartOnKillFocus )
		self.btnToevoegen.Bind( wx.EVT_BUTTON, self.btnToevoegenOnButtonClick )
		self.txtPostcode.Bind( wx.EVT_KILL_FOCUS, self.txtPostcodeOnKillFocus )
		self.btnOpslaan.Bind( wx.EVT_BUTTON, self.btnOpslaanOnButtonClick )
		self.btnOpslaanEnNieuw.Bind( wx.EVT_BUTTON, self.btnOpslaanEnNieuwOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def txtKlantkaartOnKillFocus( self, event ):
		event.Skip()
	
	def btnToevoegenOnButtonClick( self, event ):
		event.Skip()
	
	def txtPostcodeOnKillFocus( self, event ):
		event.Skip()
	
	def btnOpslaanOnButtonClick( self, event ):
		event.Skip()
	
	def btnOpslaanEnNieuwOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class pnlGroepenBase
###########################################################################

class pnlGroepenBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnGroupOne = wx.Button( self, wx.ID_ANY, u"Group\nOne", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupOne.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnGroupOne, 0, wx.ALL, 1 )
		
		self.btnGroupThree = wx.Button( self, wx.ID_ANY, u"Group\nThree", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupThree.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnGroupThree, 0, wx.ALL, 1 )
		
		self.btnGroupFive = wx.Button( self, wx.ID_ANY, u"Group\nFive", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupFive.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnGroupFive, 0, wx.ALL, 1 )
		
		self.btnGroupSeven = wx.Button( self, wx.ID_ANY, u"Group\nSeven", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupSeven.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnGroupSeven, 0, wx.ALL, 1 )
		
		bSizer6.Add( bSizer8, 1, wx.EXPAND, 1 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnGroupTwo = wx.Button( self, wx.ID_ANY, u"Group\nTwo", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupTwo.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnGroupTwo, 0, wx.ALL, 1 )
		
		self.btnGroupFour = wx.Button( self, wx.ID_ANY, u"Group\nFour", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupFour.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnGroupFour, 0, wx.ALL, 1 )
		
		self.btnGroupSix = wx.Button( self, wx.ID_ANY, u"Group\nSix", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupSix.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnGroupSix, 0, wx.ALL, 1 )
		
		self.btnGroupEight = wx.Button( self, wx.ID_ANY, u"Group\nEight", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupEight.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnGroupEight, 0, wx.ALL, 1 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer9.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		bSizer6.Add( bSizer9, 1, wx.EXPAND, 1 )
		
		self.SetSizer( bSizer6 )
		self.Layout()
		bSizer6.Fit( self )
		
		# Connect Events
		self.btnGroupOne.Bind( wx.EVT_BUTTON, self.btnGroupOneOnButtonClick )
		self.btnGroupThree.Bind( wx.EVT_BUTTON, self.btnGroupThreeOnButtonClick )
		self.btnGroupFive.Bind( wx.EVT_BUTTON, self.btnGroupFiveOnButtonClick )
		self.btnGroupSeven.Bind( wx.EVT_BUTTON, self.btnGroupSevenOnButtonClick )
		self.btnGroupTwo.Bind( wx.EVT_BUTTON, self.btnGroupTwoOnButtonClick )
		self.btnGroupFour.Bind( wx.EVT_BUTTON, self.btnGroupFourOnButtonClick )
		self.btnGroupSix.Bind( wx.EVT_BUTTON, self.btnGroupSixOnButtonClick )
		self.btnGroupEight.Bind( wx.EVT_BUTTON, self.btnGroupEightOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnGroupOneOnButtonClick( self, event ):
		event.Skip()
	
	def btnGroupThreeOnButtonClick( self, event ):
		event.Skip()
	
	def btnGroupFiveOnButtonClick( self, event ):
		event.Skip()
	
	def btnGroupSevenOnButtonClick( self, event ):
		event.Skip()
	
	def btnGroupTwoOnButtonClick( self, event ):
		event.Skip()
	
	def btnGroupFourOnButtonClick( self, event ):
		event.Skip()
	
	def btnGroupSixOnButtonClick( self, event ):
		event.Skip()
	
	def btnGroupEightOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class pnlProductenBase
###########################################################################

class pnlProductenBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		bSizer121 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct11 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct11.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct11, 0, wx.ALL, 1 )
		
		self.btnProduct12 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct12.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct12, 0, wx.ALL, 1 )
		
		self.btnProduct13 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct13.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct13, 0, wx.ALL, 1 )
		
		self.btnProduct14 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct14.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct14, 0, wx.ALL, 1 )
		
		self.btnProduct15 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct15.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct15, 0, wx.ALL, 1 )
		
		self.btnProduct16 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct16.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct16, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct21 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct21.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct21, 0, wx.ALL, 1 )
		
		self.btnProduct22 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct22.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct22, 0, wx.ALL, 1 )
		
		self.btnProduct23 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct23.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct23, 0, wx.ALL, 1 )
		
		self.btnProduct24 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct24.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct24, 0, wx.ALL, 1 )
		
		self.btnProduct25 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct25.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct25, 0, wx.ALL, 1 )
		
		self.btnProduct26 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct26.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct26, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer111, 1, wx.EXPAND, 5 )
		
		bSizer122 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct31 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct31.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct31, 0, wx.ALL, 1 )
		
		self.btnProduct32 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct32.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct32, 0, wx.ALL, 1 )
		
		self.btnProduct33 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct33.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct33, 0, wx.ALL, 1 )
		
		self.btnProduct34 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct34.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct34, 0, wx.ALL, 1 )
		
		self.btnProduct35 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct35.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct35, 0, wx.ALL, 1 )
		
		self.btnProduct36 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct36.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct36, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer122, 1, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct41 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct41.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct41, 0, wx.ALL, 1 )
		
		self.btnProduct42 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct42.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct42, 0, wx.ALL, 1 )
		
		self.btnProduct43 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct43.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct43, 0, wx.ALL, 1 )
		
		self.btnProduct44 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct44.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct44, 0, wx.ALL, 1 )
		
		self.btnProduct45 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct45.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct45, 0, wx.ALL, 1 )
		
		self.btnProduct46 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct46.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct46, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct51 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct51.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct51, 0, wx.ALL, 1 )
		
		self.btnProduct52 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct52.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct52, 0, wx.ALL, 1 )
		
		self.btnProduct53 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct53.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct53, 0, wx.ALL, 1 )
		
		self.btnProduct54 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct54.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct54, 0, wx.ALL, 1 )
		
		self.btnProduct55 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct55.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct55, 0, wx.ALL, 1 )
		
		self.btnProduct56 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct56.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct56, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct61 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct61.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct61, 0, wx.ALL, 1 )
		
		self.btnProduct62 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct62.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct62, 0, wx.ALL, 1 )
		
		self.btnProduct63 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct63.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct63, 0, wx.ALL, 1 )
		
		self.btnProduct64 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct64.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct64, 0, wx.ALL, 1 )
		
		self.btnProduct65 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct65.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct65, 0, wx.ALL, 1 )
		
		self.btnProduct66 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct66.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct66, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct71 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct71.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer16.Add( self.btnProduct71, 0, wx.ALL, 1 )
		
		self.btnProduct72 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct72.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer16.Add( self.btnProduct72, 0, wx.ALL, 1 )
		
		self.btnProduct73 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct73.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer16.Add( self.btnProduct73, 0, wx.ALL, 1 )
		
		self.btnProduct74 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct74.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer16.Add( self.btnProduct74, 0, wx.ALL, 1 )
		
		self.btnProduct75 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct75.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer16.Add( self.btnProduct75, 0, wx.ALL, 1 )
		
		self.btnProduct76 = wx.Button( self, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct76.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer16.Add( self.btnProduct76, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer121 )
		self.Layout()
		bSizer121.Fit( self )
		
		# Connect Events
		self.btnProduct11.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct12.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct13.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct14.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct15.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct16.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct21.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct22.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct23.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct24.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct25.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct26.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct31.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct32.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct33.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct34.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct35.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct36.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct41.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct42.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct43.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct44.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct45.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct46.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct51.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct52.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct53.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct54.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct55.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct56.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct61.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct62.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct63.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct64.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct65.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct66.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct71.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct72.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct73.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct74.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct75.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
		self.btnProduct76.Bind( wx.EVT_BUTTON, self.btnProductOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnProductOnButtonClick( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

###########################################################################
## Class dlgProgScreenBase
###########################################################################

class dlgProgScreenBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Programmatie Knoppen", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		self.fgSizer7.SetFlexibleDirection( wx.BOTH )
		self.fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.sbGroepen = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Groepen" ), wx.VERTICAL )
		
		self.fgSizer7.Add( self.sbGroepen, 1, wx.EXPAND, 5 )
		
		self.sbProducten = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Producten" ), wx.VERTICAL )
		
		self.fgSizer7.Add( self.sbProducten, 1, wx.EXPAND, 5 )
		
		self.SetSizer( self.fgSizer7 )
		self.Layout()
		self.fgSizer7.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class dlgProductEditBase
###########################################################################

class dlgProductEditBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Product Bewerken", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Id", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer8.Add( self.m_staticText21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txtProductNo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.txtProductNo.Enable( False )
		
		bSizer38.Add( self.txtProductNo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btnSearch = wx.Button( self, wx.ID_ANY, u"Zoek", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer38.Add( self.btnSearch, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.colourPicker = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL )
		bSizer38.Add( self.colourPicker, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		fgSizer8.Add( bSizer38, 1, wx.EXPAND, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Omschrijving", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		fgSizer8.Add( self.m_staticText22, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txtOmschrijving = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 360,-1 ), 0 )
		fgSizer8.Add( self.txtOmschrijving, 0, wx.ALL, 5 )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Scherm Omschrijving", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		fgSizer8.Add( self.m_staticText27, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txtSchermOmschrijving = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 360,-1 ), 0 )
		fgSizer8.Add( self.txtSchermOmschrijving, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Prijs BTW In", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer8.Add( self.m_staticText23, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txtPrijs = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.txtPrijs, 0, wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Korting indien optie (%)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		fgSizer8.Add( self.m_staticText29, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txtKorting = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.txtKorting, 0, wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Groep", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		fgSizer8.Add( self.m_staticText24, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		chGroepChoices = []
		self.chGroep = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), chGroepChoices, 0 )
		self.chGroep.SetSelection( 0 )
		fgSizer8.Add( self.chGroep, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"BTW Eat In", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		fgSizer8.Add( self.m_staticText25, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		chBTWInChoices = []
		self.chBTWIn = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chBTWInChoices, 0 )
		self.chBTWIn.SetSelection( 0 )
		fgSizer8.Add( self.chBTWIn, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"BTW Take Out", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		fgSizer8.Add( self.m_staticText26, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		chBTWOutChoices = []
		self.chBTWOut = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chBTWOutChoices, 0 )
		self.chBTWOut.SetSelection( 0 )
		fgSizer8.Add( self.chBTWOut, 0, wx.ALL, 5 )
		
		
		fgSizer8.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_grid4 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid4.CreateGrid( 5, 5 )
		self.m_grid4.EnableEditing( True )
		self.m_grid4.EnableGridLines( True )
		self.m_grid4.EnableDragGridSize( False )
		self.m_grid4.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid4.EnableDragColMove( False )
		self.m_grid4.EnableDragColSize( True )
		self.m_grid4.SetColLabelSize( 30 )
		self.m_grid4.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid4.EnableDragRowSize( True )
		self.m_grid4.SetRowLabelSize( 80 )
		self.m_grid4.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid4.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid4.SetMinSize( wx.Size( -1,150 ) )
		
		fgSizer8.Add( self.m_grid4, 0, wx.ALL, 5 )
		
		self.chkAskForPrice = wx.CheckBox( self, wx.ID_ANY, u"Om prijs vragen", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.chkAskForPrice, 0, wx.ALL, 5 )
		
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.chkTreatAsOption = wx.CheckBox( self, wx.ID_ANY, u"Als optie behandelen", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.chkTreatAsOption, 0, wx.ALL, 5 )
		
		self.chkReverseSign = wx.CheckBox( self, wx.ID_ANY, u"Teken Omdraaien", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.chkReverseSign, 0, wx.ALL, 5 )
		
		fgSizer8.Add( bSizer34, 1, wx.EXPAND, 5 )
		
		
		fgSizer8.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnOpslaan = wx.Button( self, wx.ID_ANY, u"Opslaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.btnOpslaan, 0, wx.ALL, 5 )
		
		self.btnDelete = wx.Button( self, wx.ID_ANY, u"Verwijder", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.btnDelete, 0, wx.ALL, 5 )
		
		fgSizer8.Add( bSizer37, 1, wx.EXPAND, 5 )
		
		self.SetSizer( fgSizer8 )
		self.Layout()
		fgSizer8.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnSearch.Bind( wx.EVT_BUTTON, self.btnSearchOnButtonClick )
		self.btnOpslaan.Bind( wx.EVT_BUTTON, self.btnOpslaanOnButtonClick )
		self.btnDelete.Bind( wx.EVT_BUTTON, self.btnDeleteOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnSearchOnButtonClick( self, event ):
		event.Skip()
	
	def btnOpslaanOnButtonClick( self, event ):
		event.Skip()
	
	def btnDeleteOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgDeleteProductBase
###########################################################################

class dlgDeleteProductBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Product Verwijderen", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Wenst u het product te verwijderen of\nenkel los te koppelen van de knop?", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText29.Wrap( -1 )
		bSizer39.Add( self.m_staticText29, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnDelete = wx.Button( self, wx.ID_ANY, u"Verwijder", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.btnDelete, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnUnCouple = wx.Button( self, wx.ID_ANY, u"Loskoppelen", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.btnUnCouple, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnCancel = wx.Button( self, wx.ID_ANY, u"Annuleren", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnCancel.SetDefault() 
		bSizer40.Add( self.btnCancel, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer39.Add( bSizer40, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer39 )
		self.Layout()
		bSizer39.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnDelete.Bind( wx.EVT_BUTTON, self.btnDeleteOnButtonClick )
		self.btnUnCouple.Bind( wx.EVT_BUTTON, self.btnUnCoupleOnButtonClick )
		self.btnCancel.Bind( wx.EVT_BUTTON, self.btnCancelOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnDeleteOnButtonClick( self, event ):
		event.Skip()
	
	def btnUnCoupleOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgSelectProductBase
###########################################################################

class dlgSelectProductBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Selecteer Product", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid3 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid3.CreateGrid( 25, 5 )
		self.m_grid3.EnableEditing( False )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( True )
		self.m_grid3.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid3.AutoSizeColumns()
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid3.SetRowSize( 0, 25 )
		self.m_grid3.SetRowSize( 1, 25 )
		self.m_grid3.SetRowSize( 2, 25 )
		self.m_grid3.SetRowSize( 3, 25 )
		self.m_grid3.SetRowSize( 4, 25 )
		self.m_grid3.SetRowSize( 5, 25 )
		self.m_grid3.SetRowSize( 6, 25 )
		self.m_grid3.SetRowSize( 7, 25 )
		self.m_grid3.SetRowSize( 8, 25 )
		self.m_grid3.SetRowSize( 9, 25 )
		self.m_grid3.SetRowSize( 10, 25 )
		self.m_grid3.SetRowSize( 11, 25 )
		self.m_grid3.SetRowSize( 12, 25 )
		self.m_grid3.SetRowSize( 13, 25 )
		self.m_grid3.SetRowSize( 14, 25 )
		self.m_grid3.SetRowSize( 15, 25 )
		self.m_grid3.SetRowSize( 16, 25 )
		self.m_grid3.SetRowSize( 17, 25 )
		self.m_grid3.SetRowSize( 18, 25 )
		self.m_grid3.SetRowSize( 19, 25 )
		self.m_grid3.SetRowSize( 20, 25 )
		self.m_grid3.SetRowSize( 21, 25 )
		self.m_grid3.SetRowSize( 22, 25 )
		self.m_grid3.SetRowSize( 23, 25 )
		self.m_grid3.SetRowSize( 24, 25 )
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid3.SetMinSize( wx.Size( -1,600 ) )
		
		bSizer42.Add( self.m_grid3, 0, wx.ALL, 5 )
		
		bSizer43 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnSelect = wx.Button( self, wx.ID_ANY, u"Selecteer", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.btnSelect, 0, wx.ALL, 5 )
		
		bSizer42.Add( bSizer43, 1, wx.EXPAND, 5 )
		
		bSizer41.Add( bSizer42, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer41 )
		self.Layout()
		bSizer41.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnSelect.Bind( wx.EVT_BUTTON, self.btnSelectOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnSelectOnButtonClick( self, event ):
		event.Skip()
	

