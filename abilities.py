class Ability:
	def __init__(self):
		self.caster = None
		self.executed = True
		self.success = None
		self.resolved = False
		self.modifiable = True
		self.modified_by = []
		#self.target = None
		self.actions = []
		self.returned_value = None
		self.return_message = "No result"
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
			print("""			component: %s""" % action.component)
			print("""			new_value: %s""" % action.new_value)

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
					self.returned_value = getattr(action.target, action.component)
					self.interpret_results(action)
					self.success = True
					self.resolved = True

	def interpret_results(self):
		NotImplemented


class Action:
	def __init__(self, type, target, component, *new_value):
		self.type = type
		self.target = target
		self.component = component
		if new_value:
			self.new_value = new_value
		else:
			self.new_value = None




class InvestigateAlignment(Ability):
	def __init__(self, caster, targets):
		# Initialises variables from superclass
		super().__init__()

		self.caster = caster
		for target in targets:
			self.actions.append(Action("get", target, "alignment"))

	def interpret_results(self, action):
		self.return_message = "%s investigated %s and found them to be %s." % (self.caster.__name__(), action.target.__name__(), self.returned_value)

class InvestigateRole(Ability):
	def __init__(self, caster, targets):
		# Initialises variables from superclass
		super().__init__()

		self.caster = caster
		for target in targets:
			self.actions.append(Action("get", target, "role"))
		# self.target = target
		# self.action = Action("get", "role")

	def interpret_results(self, action):
		# Takes the object grabbed by the action and gets the name of its class
		role_name = self.returned_value.__class__.__name__
		self.return_message = "%s investigated %s and found them to be a %s." % (self.caster.__name__(), action.target.__name__(), role_name)


class BlockRole(Ability):
	def __init__(self, caster, targets):
		# Initialises variables from superclass
		super().__init__()

		self.caster = caster
		for target in targets:
			for ability in target.cast_abilities:
				self.actions.append(Action("alter", target.ability, "executed", False))