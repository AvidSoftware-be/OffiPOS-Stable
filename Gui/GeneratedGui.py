# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BaronPOS", pos = wx.DefaultPosition, size = wx.Size( 1067,705 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer1 = wx.FlexGridSizer( 1, 4, 0, 0 )
		fgSizer1.AddGrowableCol( 2 )
		fgSizer1.AddGrowableRow( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbFuncties = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Functies" ), wx.VERTICAL )
		
		self.btnInloggen = wx.Button( self, wx.ID_ANY, u"Log In", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		sbFuncties.Add( self.btnInloggen, 0, wx.ALL, 1 )
		
		self.btnLogOut = wx.Button( self, wx.ID_ANY, u"Log Uit", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		sbFuncties.Add( self.btnLogOut, 0, wx.ALL, 1 )
		
		self.btnNieuwTicket = wx.Button( self, wx.ID_ANY, u"Nieuw\nTicket", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnNieuwTicket.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		sbFuncties.Add( self.btnNieuwTicket, 0, wx.ALL, 1 )
		
		self.btnAdmin = wx.Button( self, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		sbFuncties.Add( self.btnAdmin, 0, wx.ALL, 1 )
		
		self.btnInOutToggle = wx.ToggleButton( self, wx.ID_ANY, u"In/Out", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnInOutToggle.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		sbFuncties.Add( self.btnInOutToggle, 0, wx.ALL, 1 )
		
		fgSizer1.Add( sbFuncties, 1, wx.EXPAND, 1 )
		
		sbGroepen = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Groepen" ), wx.VERTICAL )
		
		self.pnlGroepen = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnGroupOne = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupOne.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnGroupOne, 0, wx.ALL, 1 )
		
		self.btnGroupThree = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Snacks", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupThree.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnGroupThree, 0, wx.ALL, 1 )
		
		self.btnGroupFive = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Drank", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupFive.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnGroupFive, 0, wx.ALL, 1 )
		
		self.btnGroupSeven = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Eigen\nBer.", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupSeven.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnGroupSeven, 0, wx.ALL, 1 )
		
		bSizer6.Add( bSizer8, 1, wx.EXPAND, 1 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnGroupTwo = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Saus", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupTwo.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnGroupTwo, 0, wx.ALL, 1 )
		
		self.btnGroupFour = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Warme\nSaus", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupFour.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnGroupFour, 0, wx.ALL, 1 )
		
		self.btnGroupSix = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Burgers", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupSix.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnGroupSix, 0, wx.ALL, 1 )
		
		bSizer6.Add( bSizer9, 1, wx.EXPAND, 1 )
		
		self.pnlGroepen.SetSizer( bSizer6 )
		self.pnlGroepen.Layout()
		bSizer6.Fit( self.pnlGroepen )
		sbGroepen.Add( self.pnlGroepen, 1, wx.EXPAND |wx.ALL, 1 )
		
		fgSizer1.Add( sbGroepen, 1, wx.EXPAND, 1 )
		
		sbProducten = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Producten" ), wx.VERTICAL )
		
		self.pnlProducten = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer121 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct11 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct11.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct11, 0, wx.ALL, 1 )
		
		self.btnProduct12 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct12.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct12, 0, wx.ALL, 1 )
		
		self.btnProduct13 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct13.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct13, 0, wx.ALL, 1 )
		
		self.btnProduct14 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct14.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct14, 0, wx.ALL, 1 )
		
		self.btnProduct15 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct15.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct15, 0, wx.ALL, 1 )
		
		self.btnProduct16 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct16.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct16, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct21 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct21.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct21, 0, wx.ALL, 1 )
		
		self.btnProduct22 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct22.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct22, 0, wx.ALL, 1 )
		
		self.btnProduct23 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct23.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct23, 0, wx.ALL, 1 )
		
		self.btnProduct24 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct24.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct24, 0, wx.ALL, 1 )
		
		self.btnProduct25 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct25.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct25, 0, wx.ALL, 1 )
		
		self.btnProduct26 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct26.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct26, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer111, 1, wx.EXPAND, 5 )
		
		bSizer122 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct31 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct31.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct31, 0, wx.ALL, 1 )
		
		self.btnProduct32 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct32.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct32, 0, wx.ALL, 1 )
		
		self.btnProduct33 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct33.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct33, 0, wx.ALL, 1 )
		
		self.btnProduct34 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct34.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct34, 0, wx.ALL, 1 )
		
		self.btnProduct35 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct35.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct35, 0, wx.ALL, 1 )
		
		self.btnProduct36 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct36.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct36, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer122, 1, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct41 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct41.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct41, 0, wx.ALL, 1 )
		
		self.btnProduct42 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct42.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct42, 0, wx.ALL, 1 )
		
		self.btnProduct43 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct43.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct43, 0, wx.ALL, 1 )
		
		self.btnProduct44 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct44.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct44, 0, wx.ALL, 1 )
		
		self.btnProduct45 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct45.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct45, 0, wx.ALL, 1 )
		
		self.btnProduct46 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct46.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct46, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct51 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct51.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct51, 0, wx.ALL, 1 )
		
		self.btnProduct52 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct52.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct52, 0, wx.ALL, 1 )
		
		self.btnProduct53 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct53.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct53, 0, wx.ALL, 1 )
		
		self.btnProduct54 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct54.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct54, 0, wx.ALL, 1 )
		
		self.btnProduct55 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct55.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct55, 0, wx.ALL, 1 )
		
		self.btnProduct56 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct56.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct56, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct61 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct61.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct61, 0, wx.ALL, 1 )
		
		self.btnProduct62 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct62.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct62, 0, wx.ALL, 1 )
		
		self.btnProduct63 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct63.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct63, 0, wx.ALL, 1 )
		
		self.btnProduct64 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct64.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct64, 0, wx.ALL, 1 )
		
		self.btnProduct65 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct65.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct65, 0, wx.ALL, 1 )
		
		self.btnProduct66 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct66.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct66, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		self.pnlProducten.SetSizer( bSizer121 )
		self.pnlProducten.Layout()
		bSizer121.Fit( self.pnlProducten )
		sbProducten.Add( self.pnlProducten, 1, wx.EXPAND |wx.ALL, 1 )
		
		fgSizer1.Add( sbProducten, 1, wx.EXPAND, 1 )
		
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
		self.gOrder.EnableEditing( True )
		self.gOrder.EnableGridLines( False )
		self.gOrder.EnableDragGridSize( False )
		self.gOrder.SetMargins( 0, 0 )
		
		# Columns
		self.gOrder.SetColSize( 0, 50 )
		self.gOrder.SetColSize( 1, 150 )
		self.gOrder.SetColSize( 2, 30 )
		self.gOrder.EnableDragColMove( False )
		self.gOrder.EnableDragColSize( False )
		self.gOrder.SetColLabelSize( 25 )
		self.gOrder.SetColLabelValue( 0, u"#" )
		self.gOrder.SetColLabelValue( 1, u"Product" )
		self.gOrder.SetColLabelValue( 2, u"Prijs" )
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
		self.btnAfrekeken.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer11.Add( self.btnAfrekeken, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 1 )
		
		self.btnAnnuleren = wx.Button( self.pnlRekening, wx.ID_ANY, u"Annuleren", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
		self.btnAnnuleren.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer11.Add( self.btnAnnuleren, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 1 )
		
		fgSizer3.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnQtyPlus = wx.Button( self.pnlRekening, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		self.btnQtyPlus.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.btnQtyPlus.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer12.Add( self.btnQtyPlus, 0, wx.ALL, 5 )
		
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
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnNieuwTicket.Bind( wx.EVT_BUTTON, self.btnNieuwTicketOnButtonClick )
		self.btnInOutToggle.Bind( wx.EVT_TOGGLEBUTTON, self.btnInOutToggleOnToggleButton )
		self.btnGroupOne.Bind( wx.EVT_BUTTON, self.btnGroupOneOnButtonClick )
		self.btnGroupThree.Bind( wx.EVT_BUTTON, self.btnGroupThreeOnButtonClick )
		self.btnGroupFive.Bind( wx.EVT_BUTTON, self.btnGroupFiveOnButtonClick )
		self.btnGroupSeven.Bind( wx.EVT_BUTTON, self.btnGroupSevenOnButtonClick )
		self.btnGroupTwo.Bind( wx.EVT_BUTTON, self.btnGroupTwoOnButtonClick )
		self.btnGroupFour.Bind( wx.EVT_BUTTON, self.btnGroupFourOnButtonClick )
		self.btnGroupSix.Bind( wx.EVT_BUTTON, self.btnGroupSixOnButtonClick )
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
		self.btnAfrekeken.Bind( wx.EVT_BUTTON, self.btnAfrekekenOnButtonClick )
		self.btnAnnuleren.Bind( wx.EVT_BUTTON, self.btnAnnulerenOnButtonClick )
		self.btnQtyPlus.Bind( wx.EVT_BUTTON, self.btnQtyPlusOnButtonClick )
		self.btnQtyMin.Bind( wx.EVT_BUTTON, self.btnQtyMinOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnNieuwTicketOnButtonClick( self, event ):
		event.Skip()
	
	def btnInOutToggleOnToggleButton( self, event ):
		event.Skip()
	
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
	
	def btnProductOnButtonClick( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def btnAfrekekenOnButtonClick( self, event ):
		event.Skip()
	
	def btnAnnulerenOnButtonClick( self, event ):
		event.Skip()
	
	def btnQtyPlusOnButtonClick( self, event ):
		event.Skip()
	
	def btnQtyMinOnButtonClick( self, event ):
		event.Skip()
	

