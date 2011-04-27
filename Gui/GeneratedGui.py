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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BaronPOS", pos = wx.DefaultPosition, size = wx.Size( 1172,705 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )
		
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
		
		fgSizer1.Add( sbFuncties, 1, wx.EXPAND, 1 )
		
		sbGroepen = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Groepen" ), wx.VERTICAL )
		
		self.pnlGroepen = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnFrieten = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnFrieten.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnFrieten, 0, wx.ALL, 1 )
		
		self.btnSnacks = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Snacks", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnSnacks.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnSnacks, 0, wx.ALL, 1 )
		
		self.btnDrank = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Drank", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnDrank.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnDrank, 0, wx.ALL, 1 )
		
		self.btnEigenBereidingen = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Eigen\nBer.", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnEigenBereidingen.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnEigenBereidingen, 0, wx.ALL, 1 )
		
		bSizer6.Add( bSizer8, 1, wx.EXPAND, 1 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnSaus = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Saus", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnSaus.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnSaus, 0, wx.ALL, 1 )
		
		self.btnWarmeSaus = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Warme\nSaus", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnWarmeSaus.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnWarmeSaus, 0, wx.ALL, 1 )
		
		self.btnHamburgers = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Burgers", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnHamburgers.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnHamburgers, 0, wx.ALL, 1 )
		
		bSizer6.Add( bSizer9, 1, wx.EXPAND, 1 )
		
		self.pnlGroepen.SetSizer( bSizer6 )
		self.pnlGroepen.Layout()
		bSizer6.Fit( self.pnlGroepen )
		sbGroepen.Add( self.pnlGroepen, 1, wx.EXPAND |wx.ALL, 1 )
		
		fgSizer1.Add( sbGroepen, 1, wx.EXPAND, 1 )
		
		sbProducten = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Producten" ), wx.VERTICAL )
		
		self.pnlProducten = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
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
		self.btnFrieten.Bind( wx.EVT_BUTTON, self.btnFrietenOnButtonClick )
		self.btnSnacks.Bind( wx.EVT_BUTTON, self.btnSnacksOnButtonClick )
		self.btnDrank.Bind( wx.EVT_BUTTON, self.btnDrankOnButtonClick )
		self.btnEigenBereidingen.Bind( wx.EVT_BUTTON, self.btnEigenBereidingenOnButtonClick )
		self.btnSaus.Bind( wx.EVT_BUTTON, self.btnSausOnButtonClick )
		self.btnWarmeSaus.Bind( wx.EVT_BUTTON, self.btnWarmeSausOnButtonClick )
		self.btnHamburgers.Bind( wx.EVT_BUTTON, self.btnHamburgersOnButtonClick )
		self.btnAfrekeken.Bind( wx.EVT_BUTTON, self.btnAfrekekenOnButtonClick )
		self.btnAnnuleren.Bind( wx.EVT_BUTTON, self.btnAnnulerenOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnNieuwTicketOnButtonClick( self, event ):
		event.Skip()
	
	def btnFrietenOnButtonClick( self, event ):
		event.Skip()
	
	def btnSnacksOnButtonClick( self, event ):
		event.Skip()
	
	def btnDrankOnButtonClick( self, event ):
		event.Skip()
	
	def btnEigenBereidingenOnButtonClick( self, event ):
		event.Skip()
	
	def btnSausOnButtonClick( self, event ):
		event.Skip()
	
	def btnWarmeSausOnButtonClick( self, event ):
		event.Skip()
	
	def btnHamburgersOnButtonClick( self, event ):
		event.Skip()
	
	def btnAfrekekenOnButtonClick( self, event ):
		event.Skip()
	
	def btnAnnulerenOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class PanelFrietenBase
###########################################################################

class PanelFrietenBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 648,462 ), style = wx.TAB_TRAVERSAL )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.btnFrietGroot = wx.Button( self, wx.ID_ANY, u"Groot", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnFrietGroot.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btnFrietGroot, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 1 )
		
		self.btnFrietMidden = wx.Button( self, wx.ID_ANY, u"Midden", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnFrietMidden.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btnFrietMidden, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 1 )
		
		self.btnFrietKlein = wx.Button( self, wx.ID_ANY, u"Klein", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnFrietKlein.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btnFrietKlein, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 1 )
		
		self.btnFrietFamilie = wx.Button( self, wx.ID_ANY, u"Familie", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnFrietFamilie.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btnFrietFamilie, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 1 )
		
		bSizer7.Add( gbSizer1, 1, wx.EXPAND, 1 )
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		# Connect Events
		self.btnFrietGroot.Bind( wx.EVT_BUTTON, self.btnFrietGrootOnButtonClick )
		self.btnFrietMidden.Bind( wx.EVT_BUTTON, self.btnFrietMiddenOnButtonClick )
		self.btnFrietKlein.Bind( wx.EVT_BUTTON, self.btnFrietKleinOnButtonClick )
		self.btnFrietFamilie.Bind( wx.EVT_BUTTON, self.btnFrietFamilieOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnFrietGrootOnButtonClick( self, event ):
		event.Skip()
	
	def btnFrietMiddenOnButtonClick( self, event ):
		event.Skip()
	
	def btnFrietKleinOnButtonClick( self, event ):
		event.Skip()
	
	def btnFrietFamilieOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class PanelSnacksBase
###########################################################################

class PanelSnacksBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 420,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnFrikandel = wx.Button( self, wx.ID_ANY, u"Frikandel", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnFrikandel.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer11.Add( self.btnFrikandel, 0, wx.ALL, 1 )
		
		self.btnMexicano = wx.Button( self, wx.ID_ANY, u"Mexicano", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnMexicano.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer11.Add( self.btnMexicano, 0, wx.ALL, 1 )
		
		self.btnKippets = wx.Button( self, wx.ID_ANY, u"Kippets", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnKippets.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer11.Add( self.btnKippets, 0, wx.ALL, 1 )
		
		self.btnMammoet = wx.Button( self, wx.ID_ANY, u"Mammoet", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnMammoet.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer11.Add( self.btnMammoet, 0, wx.ALL, 1 )
		
		self.btnFrikandel4 = wx.Button( self, wx.ID_ANY, u"Frikandel", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnFrikandel4.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer11.Add( self.btnFrikandel4, 0, wx.ALL, 1 )
		
		fgSizer2.Add( bSizer11, 1, wx.EXPAND, 1 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnFrikandel5 = wx.Button( self, wx.ID_ANY, u"Frikandel", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnFrikandel5.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer12.Add( self.btnFrikandel5, 0, wx.ALL, 1 )
		
		fgSizer2.Add( bSizer12, 1, wx.EXPAND, 1 )
		
		bSizer10.Add( fgSizer2, 1, wx.EXPAND, 1 )
		
		self.SetSizer( bSizer10 )
		self.Layout()
		
		# Connect Events
		self.btnFrikandel.Bind( wx.EVT_BUTTON, self.btnFrikandelOnButtonClick )
		self.btnMexicano.Bind( wx.EVT_BUTTON, self.btnMexicanoOnButtonClick )
		self.btnKippets.Bind( wx.EVT_BUTTON, self.btnKippetsOnButtonClick )
		self.btnMammoet.Bind( wx.EVT_BUTTON, self.btnMammoetOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnFrikandelOnButtonClick( self, event ):
		event.Skip()
	
	def btnMexicanoOnButtonClick( self, event ):
		event.Skip()
	
	def btnKippetsOnButtonClick( self, event ):
		event.Skip()
	
	def btnMammoetOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class PanelDrankBase
###########################################################################

class PanelDrankBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class PanelSausBase
###########################################################################

class PanelSausBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class PanelEigenBereidingenBase
###########################################################################

class PanelEigenBereidingenBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class PanelWarmeSausBase
###########################################################################

class PanelWarmeSausBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class PanelHamburgersBase
###########################################################################

class PanelHamburgersBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

