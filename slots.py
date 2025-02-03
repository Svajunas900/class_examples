class SlotExample():
  __slots__ = ["slot_0", "slot_1", "slot_2"]

  def __init__(self):
    self.slot_0 = "SLOT_123"

slot = SlotExample()
slot2 = SlotExample()

slot.slot_1 = "SLOT_321"

# AttributeError
slot.slot_3 = "SLOT_456"


