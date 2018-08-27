class Ability:
	def __init__(self):
		self.caster = None
		self.executed = True
		self.success = None
		self.resolved = False
		self.modifiable = True
		self.modified_by = []
		self.actions = []
		self.return_message = ""
		self.priority = 0

	def get_components(self):
		actions = []

		for action in self.actions:
			actions.append(action.get_components())

		components = {
			"caster": (self.caster.__name__(), self.caster),
			"executed": self.executed,
			"success": self.success,
			"resolved": self.resolved,
			"modifiable": self.modifiable,
			"modified_by": self.modified_by,
			"actions": actions,
			"return_message": self.return_message,
			"priority": self.priority
		}

		return components

	def connect_to_targets(self):
		for action in self.actions:
			action.target.targetted_by.append(self)
			if (action.target_ability == "*"):
				for target_ability in action.target.cast_abilities:
					target_ability.modified_by.append(self)


	def resolve(self, *ability_chain):
		def execute():
			if (action.type == "get"):
					action.returned_value = getattr(action.target, action.component)
					self.return_message += str(self.interpret_results(action))
					self.success = True
					self.resolved = True

		if (not ability_chain):
			print("NO ABILITY CHAIN")

		for action in self.actions:
			if (self.modified_by):
				for ability in self.modified_by:
					if (ability not in ability_chain):
						ability.resolve()
			else:
				execute()

	def interpret_results(self):
		NotImplemented


class Action:
	def __init__(self, type, target, component, *new_value):
		self.type = type

		if (isinstance(target, tuple)):
			self.target = target[0]
			self.target_ability= target[1]
		else:
			self.target = target
			self.target_ability = None

		self.component = component

		if new_value:
			self.new_value = new_value
		else:
			self.new_value = None
		self.returned_value = None

	def get_components(self):
		components = {
			"action": self.__class__.__name__,
			"type": self.type,
			"target": (self.target.__name__(), self.target),
			"target_ability": (self.target_ability.__class__.__name__, self.target_ability),
			"component": self.component,
			"new_value": self.new_value,
			"returned_value": self.returned_value
		}
		return components




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