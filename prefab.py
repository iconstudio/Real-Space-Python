import behavior.RsBehavior as RsBehavior

class RsPrefab(RsBehavior):
	sprite_index = None
	layer = None

	def __init__(self):
		pass

	def onAwake(self):
		pass

	def onDestroy(self):
		pass
	
	async def onUpdate(self, Time):
		"""onUpdate(time)"""
		pass

	async def onUpdateLater(self, Time):
		"""onUpdateLater(time)"""
		pass
	
	async def onDraw(self, Time):
		"""onDraw(time)"""
		pass

	async def onGUI(self, Time):
		"""onGUI(time)"""
		pass


