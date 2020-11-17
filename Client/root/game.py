## search for:
			"MyShopPriceList"		: self.__PrivateShop_PriceList,

## add under:
			"SendRealStatus"        : self.RecvRealStatus,

##search for:
	# PRIVATE_SHOP_PRICE_LIST
	def __PrivateShop_PriceList(self, itemVNum, itemPrice):
		uiPrivateShopBuilder.SetPrivateShopItemPrice(itemVNum, itemPrice)	
	# END_OF_PRIVATE_SHOP_PRICE_LIST

## add under:
	def RecvRealStatus(self, ht, iq, st, dx):
		constInfo.itemStatusPoints[player.HT] = int(ht)
		constInfo.itemStatusPoints[player.IQ] = int(iq)
		constInfo.itemStatusPoints[player.ST] = int(st)
		constInfo.itemStatusPoints[player.DX] = int(dx)