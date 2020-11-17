## search for:
		self.isLoaded = 0

## add under:
		self.interface = None

## search for:
	def __BindObject(self):
		[...]

## add under this function:
	def BindInterface(self, interface):
		self.interface = interface

## search for:
	def __OnClickStatusPlusButton(self, statusKey):

## replace whole function:
	def __OnClickStatusPlusButton(self, statusKey):
		try:
			statusPlusCommand=self.statusPlusCommandDict[statusKey]
			statusValueDict = {
				"STR"		: constInfo.itemStatusPoints[player.ST],
				"DEX"		: constInfo.itemStatusPoints[player.DX],
				"HTH"		: constInfo.itemStatusPoints[player.HT],
				"INT"		: constInfo.itemStatusPoints[player.IQ],
			}
			statusValue=statusValueDict[statusKey]
			self.interface.wndAddStats.SetData(statusPlusCommand, statusValue, statusKey)
			self.interface.wndAddStats.Show()
		except KeyError, msg:
			dbg.TraceError("CharacterWindow.__OnClickStatusPlusButton KeyError: %s", msg)
