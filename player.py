import pprint

class Player:
	def __init__(self, name, alignment, role):
		self.name = name
		self.status = "alive"
		self.alignment = alignment
		self.role = role
		self.cast_abilities = []
		self.targetted_by = []

	def get_components(self):
		cast_abilities = []

		for ability in self.cast_abilities:
			cast_abilities.append(ability.get_components())

		components = {
			"name": self.name,
			"status": self.status,
			"alignment": self.alignment,
			"role": (self.role.__class__.__name__, self.role),
			"cast_abilities": cast_abilities,
			"targetted_by": self.targetted_by
		}

		return components

	def __name__(self):
		return self.name

	def cast(self, ability, target):
		cast_ability_statement = "self.cast_abilities.append(self.role." + str(ability.__name__) + "(self, target))"
		exec(cast_ability_statement)

def print_players(players):
	for player in players:
		pprint.PrettyPrinter(indent=4).pprint(player.get_components())