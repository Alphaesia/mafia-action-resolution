from abilities import *

class InvestigateAlignment(Ability):
	def __init__(self, caster, targets):
		# Initialises variables from superclass
		super().__init__()

		self.caster = caster
		for target in targets:
			self.actions.append(Action("get", target, "alignment"))

	def interpret_results(self, action):
		return "You investigated %s and found them to be %s. " % (action.target.__name__(), action.returned_value)

class InvestigateRole(Ability):
	def __init__(self, caster, targets):
		# Initialises variables from superclass
		super().__init__()

		self.caster = caster
		for target in targets:
			self.actions.append(Action("get", target, "role"))

	def interpret_results(self, action):
		return "You investigated %s and found them to be a %s. " % (action.target.__name__(), action.returned_value.__class__.__name__)


class BlockRole(Ability):
	def __init__(self, caster, targets):
		# Initialises variables from superclass
		super().__init__()

		self.caster = caster
		for target in targets:
			self.actions.append(Action("alter", (target, "*"), "executed", False))

	def interpret_results(self, action):
		return "You blocked %s" % action.target.__name__()