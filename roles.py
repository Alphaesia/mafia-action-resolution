import abilities
import custom_abilities as abilities

class Role:
	def __init__(self):
		self.abilities = None


class Regular(Role):
	def __init__(self):
		super().__init__()


class Detective(Role):
	def investigateAlignment(self, caster, target):
		return abilities.InvestigateAlignment(caster, target)

	def __init__(self):
		super().__init__()
		self.abilities = {"investigate": self.investigateAlignment}

	def __name__(self):
		return "detective"

class RoleCop(Role):
	def investigateRole(self, caster, target):
		return abilities.InvestigateRole(caster, target)

	def __init__(self):
		super().__init__()
		self.abilities = {"investigate": self.investigateRole}

class Roleblocker(Role):
	def blockRole(self, caster, target):
		return abilities.BlockRole(caster, target)

	def __init__(self):
		super().__init__()
		self.abilities = {"block": self.blockRole}