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

	def print_components(self):
		print("Ability: %s (%s)" % (self.__class__.__name__, self))
		print("""	caster: %s (%s)""" % (self.caster.__name__(), self.caster))
		print("""	executed: %s""" % self.executed)
		print("""	success: %s""" % self.success)
		print("""	resolved: %s""" % self.resolved)
		print("""	modifiable: %s""" % self.modifiable)
		print("""	modified_by: %s""" % self.modified_by)
		print("""	actions: [""")

		for action in self.actions:
			print("""		action: %s""" % action)
			print("""			type: %s""" % action.type)
			print("""			target: %s (%s)""" % (action.target.__name__(), action.target))

			if (action.target_action is not None and action.target_action != "*"):
				print("""			target_action: %s (%s)""" % (action.target_action.__name__(), action.target_action))
			else:
				print("""			target_action: %s""" % action.target_action)

			print("""			component: %s""" % action.component)
			print("""			new_value: %s""" % action.new_value)
			print("""			returned_value: %s""" % action.returned_value)

		print("""	]""")
		print("""	return_message: %s""" % self.return_message)
		print("""	priority: %s""" % self.priority)
		print("")

	def resolve(self):
		for action in self.actions:
			if (self.modified_by):
				pass
			else:
				if (action.type == "get"):
					action.returned_value = getattr(action.target, action.component)
					self.return_message += str(self.interpret_results(action))

			self.success = True
			self.resolved = True

	def interpret_results(self):
		NotImplemented


class Action:
	def __init__(self, type, target, component, *new_value):
		self.type = type

		if (isinstance(target, tuple)):
			self.target = target[0]
			self.target_action = target[1]
		else:
			self.target = target
			self.target_action = None

		self.component = component

		if new_value:
			self.new_value = new_value
		else:
			self.new_value = None
		self.returned_value = None




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