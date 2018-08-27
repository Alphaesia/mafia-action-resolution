from pprint import PrettyPrinter

import player
import roles

def finalise_abilities(players):
	for player in players:
		for ability in player.cast_abilities:
			ability.connect_to_targets()

def resolve_abilities(players):
	for player in players:
		for ability in player.cast_abilities:
			ability.resolve()
			print(ability.caster.__name__() + ": " + ability.return_message)
		PrettyPrinter(indent=4).pprint(player.get_components())

players = []

PlayerA = player.Player("CreepaShadowz", "innocent", roles.Detective())
PlayerB = player.Player("yeroc424", "mafia", roles.RoleCop())
PlayerC = player.Player("Zatharel", "mafia", roles.Roleblocker())

players.extend((PlayerA, PlayerB, PlayerC))

PlayerA.cast(PlayerA.role.abilities["investigate"], (PlayerB, PlayerA))
PlayerB.cast(PlayerB.role.abilities["investigate"], (PlayerA, PlayerC))
PlayerC.cast(PlayerC.role.abilities["block"], (PlayerA,))

finalise_abilities(players)
resolve_abilities(players)