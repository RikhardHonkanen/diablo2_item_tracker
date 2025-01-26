from typing import Optional
import user
import master

class AppContext:
    inventory: Optional[user.UserInventory] = None
    master_data: Optional[master.MasterData] = None

    @classmethod
    def initialize(cls):
        cls.inventory = user.UserInventory()
        cls.master_data = master.MasterData()