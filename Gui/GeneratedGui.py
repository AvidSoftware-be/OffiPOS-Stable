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
		
		self.btnInloggen = wx.Button( self, wx.ID_ANY, u"Log In", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbFuncties.Add( self.btnInloggen, 0, wx.ALL, 5 )
		
		self.btnLogOut = wx.Button( self, wx.ID_ANY, u"Log Uit", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbFuncties.Add( self.btnLogOut, 0, wx.ALL, 5 )
		
		self.btnNieuwTicket = wx.Button( self, wx.ID_ANY, u"Nieuw Ticket", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbFuncties.Add( self.btnNieuwTicket, 0, wx.ALL, 5 )
		
		self.btnAdmin = wx.Button( self, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbFuncties.Add( self.btnAdmin, 0, wx.ALL, 5 )
		
		fgSizer1.Add( sbFuncties, 1, wx.EXPAND, 5 )
		
		sbGroepen = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Groepen" ), wx.VERTICAL )
		
		self.btnFrieten = wx.Button( self, wx.ID_ANY, u"Frieten", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		self.btnFrieten.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		sbGroepen.Add( self.btnFrieten, 0, wx.ALL, 1 )
		
		self.btnSnacks = wx.Button( self, wx.ID_ANY, u"Snacks", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		self.btnSnacks.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		sbGroepen.Add( self.btnSnacks, 0, wx.ALL, 1 )
		
		self.btnDrank = wx.Button( self, wx.ID_ANY, u"Drank", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		self.btnDrank.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		sbGroepen.Add( self.btnDrank, 0, wx.ALL, 1 )
		
		self.btnSaus = wx.Button( self, wx.ID_ANY, u"Saus", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		self.btnSaus.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		sbGroepen.Add( self.btnSaus, 0, wx.ALL, 1 )
		
		fgSizer1.Add( sbGroepen, 1, wx.EXPAND, 5 )
		
		sbProducten = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Producten" ), wx.VERTICAL )
		
		fgSizer1.Add( sbProducten, 1, wx.EXPAND, 5 )
		
		sbRekening = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Rekening" ), wx.VERTICAL )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbRekening.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		sbRekening.Add( self.m_grid1, 0, wx.ALL, 5 )
		
		self.btnAfrekeken = wx.Button( self, wx.ID_ANY, u"Afrekenen", wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.btnAfrekeken.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		sbRekening.Add( self.btnAfrekeken, 0, wx.ALL, 5 )
		
		self.btnAnnuleren = wx.Button( self, wx.ID_ANY, u"Annuleren", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
		self.btnAnnuleren.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		sbRekening.Add( self.btnAnnuleren, 0, wx.ALL, 5 )
		
		fgSizer1.Add( sbRekening, 1, wx.EXPAND, 5 )
		
		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnFrieten.Bind( wx.EVT_BUTTON, self.btnFrietenOnButtonClick )
		self.btnSnacks.Bind( wx.EVT_BUTTON, self.btnSnacksOnButtonClick )
		self.btnDrank.Bind( wx.EVT_BUTTON, self.btnDrankOnButtonClick )
		self.btnSaus.Bind( wx.EVT_BUTTON, self.btnSausOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnFrietenOnButtonClick( self, event ):
		event.Skip()
	
	def btnSnacksOnButtonClick( self, event ):
		event.Skip()
	
	def btnDrankOnButtonClick( self, event ):
		event.Skip()
	
	def btnSausOnButtonClick( self, event ):
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
		
		self.btnFrietGroot = wx.Button( self, wx.ID_ANY, u"Groot", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		self.btnFrietGroot.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btnFrietGroot, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btnFrietMidden = wx.Button( self, wx.ID_ANY, u"Midden", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		self.btnFrietMidden.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btnFrietMidden, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btnFrietKlein = wx.Button( self, wx.ID_ANY, u"Klein", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		self.btnFrietKlein.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btnFrietKlein, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btnFrietFamilie = wx.Button( self, wx.ID_ANY, u"Familie", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		self.btnFrietFamilie.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btnFrietFamilie, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		bSizer7.Add( gbSizer1, 1, wx.EXPAND, 1 )
		
		self.SetSizer( bSizer7 )
		self.Layout()
	
	def __del__( self ):
		pass
	

