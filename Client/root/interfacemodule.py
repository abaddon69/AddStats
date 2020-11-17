## search for:
import uiCube

## add under:
import uiaddstats

## search for:
		self.wndGuildBuilding = None

## add under:
		self.wndAddStats = None

## search for:
		self.dlgRefineNew = uiRefine.RefineDialogNew()
		self.dlgRefineNew.Hide()

## add under:
		self.wndAddStats = uiaddstats.AddStats()
		self.wndAddStats.Hide()

		self.wndCharacter.BindInterface(self)
		
## search for:
		self.wndChatLog.Destroy()

## add above:
		if self.wndAddStats:
			self.wndAddStats.Destroy()

## search for:
		del self.wndItemSelect

## add under:
		del self.wndAddStats

