class Player:
	def __init__(self, name, alignment, role):
		self.name = name
		self.status = "alive"
		self.alignment = alignment
		self.role = role
		self.cast_abilities = []

	def __name__(self):
		return self.name

	def cast(self, ability, target):
		cast_ability_statement = "self.cast_abilities.append(self.role." + str(ability.__name__) + "(self, target))"
		exec(cast_ability_statement)