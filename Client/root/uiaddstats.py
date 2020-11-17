import ui, net, localeInfo, player
class AddStats(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.command = ""
		self.text = ""
		self.points = 0
		self.to_add = 0
		self.max = 90
		self.statusTextDict = {
			"STR"	    : localeInfo.PLAYER_STR,
			"DEX"		: localeInfo.PLAYER_DEX,
			"HTH"		: localeInfo.PLAYER_HTH,
			"INT"		: localeInfo.PLAYER_INT,
		}
		self.LoadWindow()
	def __del__(self):
		ui.ScriptWindow.__del__(self)
	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/addstats.py")

		except:
			import exception
			exception.Abort("AddStats.__LoadScript.LoadObject")

		try:
			self.slideBar = self.GetChild("slider")
			self.statsValue = self.GetChild("StatsValue")
			self.GetChild("Board").SetCloseEvent(self.Hide)
			self.GetChild("AcceptButton").SetEvent(ui.__mem_func__(self.Accept))
			self.GetChild("CancelButton").SetEvent(ui.__mem_func__(self.Hide))
			self.slideBar.SetEvent(self.OnChangePoints)
		except:
			import exception
			exception.Abort("AddStats.__LoadScript.BindObject")
		ui.ScriptWindow.SetCenterPosition(self)

	def ResetWindow(self):
		self.slideBar.SetSliderPos(0.0)

	def OnChangePoints(self):
		pos = self.slideBar.GetSliderPos()
		self.to_add = min(abs(int(pos*(self.points-self.max))), player.GetStatus(player.STAT))
		self.statsValue.SetText("%s %d" % (self.text, self.to_add ))

	def Destroy(self):
		self.ClearDictionary()
		self.command = ""
		self.text = ""
		self.points = 0
		self.to_add = 0
		self.max = 0

	def SetData(self, command, points, key):
		self.ResetWindow()
		self.command = command
		self.points = points
		self.text = self.statusTextDict[key]
		self.OnChangePoints()

	def Accept(self):
		net.SendChatPacket("%s %d" % (self.command, self.to_add))
		self.Hide()

	def OnPressEscapeKey(self):
		self.Hide()
		return True

