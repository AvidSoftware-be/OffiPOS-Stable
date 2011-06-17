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
		self.btnNieuwTicket.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		sbFuncties.Add( self.btnNieuwTicket, 0, wx.ALL, 1 )
		
		self.btnAdmin = wx.Button( self, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		sbFuncties.Add( self.btnAdmin, 0, wx.ALL, 1 )
		
		self.btnInOutToggle = wx.ToggleButton( self, wx.ID_ANY, u"In/Out", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnInOutToggle.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		sbFuncties.Add( self.btnInOutToggle, 0, wx.ALL, 1 )
		
		fgSizer1.Add( sbFuncties, 1, wx.EXPAND, 1 )
		
		sbGroepen = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Groepen" ), wx.VERTICAL )
		
		self.pnlGroepen = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnGroupOne = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Group\nOne", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupOne.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnGroupOne, 0, wx.ALL, 1 )
		
		self.btnGroupThree = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Group\nThree", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupThree.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnGroupThree, 0, wx.ALL, 1 )
		
		self.btnGroupFive = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Group\nFive", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupFive.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnGroupFive, 0, wx.ALL, 1 )
		
		self.btnGroupSeven = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Group\nSeven", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupSeven.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer8.Add( self.btnGroupSeven, 0, wx.ALL, 1 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnRetour = wx.ToggleButton( self.pnlGroepen, wx.ID_ANY, u"Retour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnRetour.SetValue( True ) 
		bSizer18.Add( self.btnRetour, 0, wx.ALIGN_BOTTOM, 0 )
		
		bSizer8.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		bSizer6.Add( bSizer8, 1, wx.EXPAND, 1 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnGroupTwo = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Group\nTwo", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupTwo.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnGroupTwo, 0, wx.ALL, 1 )
		
		self.btnGroupFour = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Group\nFour", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupFour.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnGroupFour, 0, wx.ALL, 1 )
		
		self.btnGroupSix = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Group\nSix", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupSix.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnGroupSix, 0, wx.ALL, 1 )
		
		self.btnGroupEight = wx.Button( self.pnlGroepen, wx.ID_ANY, u"Group\nEight", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnGroupEight.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.btnGroupEight, 0, wx.ALL, 1 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer9.Add( bSizer19, 1, wx.EXPAND, 5 )
		
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
		
		self.btnProduct11 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct11.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct11, 0, wx.ALL, 1 )
		
		self.btnProduct12 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct12.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct12, 0, wx.ALL, 1 )
		
		self.btnProduct13 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct13.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct13, 0, wx.ALL, 1 )
		
		self.btnProduct14 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct14.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct14, 0, wx.ALL, 1 )
		
		self.btnProduct15 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct15.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct15, 0, wx.ALL, 1 )
		
		self.btnProduct16 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct16.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer10.Add( self.btnProduct16, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct21 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct21.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct21, 0, wx.ALL, 1 )
		
		self.btnProduct22 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct22.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct22, 0, wx.ALL, 1 )
		
		self.btnProduct23 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct23.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct23, 0, wx.ALL, 1 )
		
		self.btnProduct24 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct24.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct24, 0, wx.ALL, 1 )
		
		self.btnProduct25 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct25.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct25, 0, wx.ALL, 1 )
		
		self.btnProduct26 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct26.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.btnProduct26, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer111, 1, wx.EXPAND, 5 )
		
		bSizer122 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct31 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct31.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct31, 0, wx.ALL, 1 )
		
		self.btnProduct32 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct32.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct32, 0, wx.ALL, 1 )
		
		self.btnProduct33 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct33.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct33, 0, wx.ALL, 1 )
		
		self.btnProduct34 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct34.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct34, 0, wx.ALL, 1 )
		
		self.btnProduct35 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct35.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct35, 0, wx.ALL, 1 )
		
		self.btnProduct36 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct36.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer122.Add( self.btnProduct36, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer122, 1, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct41 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct41.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct41, 0, wx.ALL, 1 )
		
		self.btnProduct42 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct42.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct42, 0, wx.ALL, 1 )
		
		self.btnProduct43 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct43.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct43, 0, wx.ALL, 1 )
		
		self.btnProduct44 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct44.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct44, 0, wx.ALL, 1 )
		
		self.btnProduct45 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct45.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct45, 0, wx.ALL, 1 )
		
		self.btnProduct46 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct46.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer13.Add( self.btnProduct46, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct51 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct51.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct51, 0, wx.ALL, 1 )
		
		self.btnProduct52 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct52.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct52, 0, wx.ALL, 1 )
		
		self.btnProduct53 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct53.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct53, 0, wx.ALL, 1 )
		
		self.btnProduct54 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct54.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct54, 0, wx.ALL, 1 )
		
		self.btnProduct55 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct55.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct55, 0, wx.ALL, 1 )
		
		self.btnProduct56 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct56.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer14.Add( self.btnProduct56, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct61 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct61.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct61, 0, wx.ALL, 1 )
		
		self.btnProduct62 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct62.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct62, 0, wx.ALL, 1 )
		
		self.btnProduct63 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct63.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct63, 0, wx.ALL, 1 )
		
		self.btnProduct64 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct64.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct64, 0, wx.ALL, 1 )
		
		self.btnProduct65 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct65.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct65, 0, wx.ALL, 1 )
		
		self.btnProduct66 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct66.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer15.Add( self.btnProduct66, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnProduct71 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct71.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer16.Add( self.btnProduct71, 0, wx.ALL, 1 )
		
		self.btnProduct72 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct72.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer16.Add( self.btnProduct72, 0, wx.ALL, 1 )
		
		self.btnProduct73 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct73.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer16.Add( self.btnProduct73, 0, wx.ALL, 1 )
		
		self.btnProduct74 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct74.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer16.Add( self.btnProduct74, 0, wx.ALL, 1 )
		
		self.btnProduct75 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct75.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer16.Add( self.btnProduct75, 0, wx.ALL, 1 )
		
		self.btnProduct76 = wx.Button( self.pnlProducten, wx.ID_ANY, u"Product\nButton", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.btnProduct76.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer16.Add( self.btnProduct76, 0, wx.ALL, 1 )
		
		bSizer121.Add( bSizer16, 1, wx.EXPAND, 5 )
		
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
		
		self.btnQtyPlus = wx.Button( self.pnlRekening, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		self.btnQtyPlus.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.btnQtyPlus.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		self.btnQtyPlus.Hide()
		
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
		self.btnAdmin.Bind( wx.EVT_BUTTON, self.btnAdminOnButtonClick )
		self.btnInOutToggle.Bind( wx.EVT_TOGGLEBUTTON, self.btnInOutToggleOnToggleButton )
		self.btnGroupOne.Bind( wx.EVT_BUTTON, self.btnGroupOneOnButtonClick )
		self.btnGroupThree.Bind( wx.EVT_BUTTON, self.btnGroupThreeOnButtonClick )
		self.btnGroupFive.Bind( wx.EVT_BUTTON, self.btnGroupFiveOnButtonClick )
		self.btnGroupSeven.Bind( wx.EVT_BUTTON, self.btnGroupSevenOnButtonClick )
		self.btnRetour.Bind( wx.EVT_TOGGLEBUTTON, self.btnRetourOnToggleButton )
		self.btnGroupTwo.Bind( wx.EVT_BUTTON, self.btnGroupTwoOnButtonClick )
		self.btnGroupFour.Bind( wx.EVT_BUTTON, self.btnGroupFourOnButtonClick )
		self.btnGroupSix.Bind( wx.EVT_BUTTON, self.btnGroupSixOnButtonClick )
		self.btnGroupEight.Bind( wx.EVT_BUTTON, self.btnGroupEightOnButtonClick )
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
		self.gOrder.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.gOrderOnGridSelectCell )
		self.btnAfrekeken.Bind( wx.EVT_BUTTON, self.btnAfrekekenOnButtonClick )
		self.btnAnnuleren.Bind( wx.EVT_BUTTON, self.btnAnnulerenOnButtonClick )
		self.btnQtyPlus.Bind( wx.EVT_BUTTON, self.btnQtyPlusOnButtonClick )
		self.btnQtyMin.Bind( wx.EVT_BUTTON, self.btnQtyMinOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnNieuwTicketOnButtonClick( self, event ):
		event.Skip()
	
	def btnAdminOnButtonClick( self, event ):
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
	
	def btnRetourOnToggleButton( self, event ):
		event.Skip()
	
	def btnGroupTwoOnButtonClick( self, event ):
		event.Skip()
	
	def btnGroupFourOnButtonClick( self, event ):
		event.Skip()
	
	def btnGroupSixOnButtonClick( self, event ):
		event.Skip()
	
	def btnGroupEightOnButtonClick( self, event ):
		event.Skip()
	
	def btnProductOnButtonClick( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def gOrderOnGridSelectCell( self, event ):
		event.Skip()
	
	def btnAfrekekenOnButtonClick( self, event ):
		event.Skip()
	
	def btnAnnulerenOnButtonClick( self, event ):
		event.Skip()
	
	def btnQtyPlusOnButtonClick( self, event ):
		event.Skip()
	
	def btnQtyMinOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class pnlNumPadBase
###########################################################################

class pnlNumPadBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

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
		
		gSizer51 = wx.GridSizer( 2, 2, 0, 0 )
		
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
		
		gSizer51.Add( gSizer5, 1, 0, 0 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		gSizer4 = wx.GridSizer( 4, 2, 0, 0 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Klantkaart", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		gSizer4.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl4, 0, wx.ALL, 0 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Punten Ticket", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl5, 0, wx.ALL, 0 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Punten op kaart", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer4.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl6, 0, wx.ALL, 0 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Toegekende korting", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer4.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl7, 0, wx.ALL, 0 )
		
		bSizer20.Add( gSizer4, 1, 0, 5 )
		
		gSizer51.Add( bSizer20, 1, 0, 0 )
		
		gSizer3 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.btnCash = wx.Button( self, wx.ID_ANY, u"Cash", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer3.Add( self.btnCash, 0, wx.ALIGN_RIGHT|wx.ALL, 0 )
		
		self.btnAtos = wx.Button( self, wx.ID_ANY, u"Atos", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gSizer3.Add( self.btnAtos, 0, wx.ALL, 0 )
		
		self.btnClr = wx.Button( self, wx.ID_ANY, u"Clr", wx.DefaultPosition, wx.Size( 40,30 ), 0 )
		gSizer3.Add( self.btnClr, 0, wx.ALIGN_BOTTOM|wx.ALIGN_LEFT|wx.ALL, 0 )
		
		self.btnCls = wx.Button( self, wx.ID_ANY, u"Cls", wx.DefaultPosition, wx.Size( 40,30 ), 0 )
		gSizer3.Add( self.btnCls, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL, 0 )
		
		gSizer51.Add( gSizer3, 1, wx.ALIGN_CENTER, 5 )
		
		fgSizer3.Add( gSizer51, 1, wx.EXPAND, 5 )
		
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
	

###########################################################################
## Class AdminDialogBase
###########################################################################

class AdminDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Admin", pos = wx.DefaultPosition, size = wx.Size( 116,82 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.STAY_ON_TOP|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnKasAfsluiten = wx.Button( self, wx.ID_ANY, u"Kas Afsluiten", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.btnKasAfsluiten, 0, wx.ALL, 5 )
		
		self.SetSizer( bSizer17 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnKasAfsluiten.Bind( wx.EVT_BUTTON, self.btnKasAfsluitenOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnKasAfsluitenOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgAskForPriceBase
###########################################################################

class dlgAskForPriceBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Prijs ingeven", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.txtPrice = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,50 ), wx.TE_READONLY|wx.TE_RIGHT )
		self.txtPrice.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer20.Add( self.txtPrice, 0, wx.ALL|wx.EXPAND, 5 )
		
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
		
		bSizer20.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		self.btnClear = wx.Button( self, wx.ID_ANY, u"Clr", wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
		bSizer20.Add( self.btnClear, 0, wx.ALL, 0 )
		
		self.SetSizer( bSizer20 )
		self.Layout()
		bSizer20.Fit( self )
		
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
		self.btnClear.Bind( wx.EVT_BUTTON, self.btnClearOnButtonClick )
	
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
	
	def btnClearOnButtonClick( self, event ):
		event.Skip()
	

