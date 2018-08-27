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
			ability.print_components()
			print(ability.actions[0].get_components())

players = []

PlayerA = player.Player("CreepaShadowz", "innocent", roles.Detective())
PlayerB = player.Player("yeroc424", "mafia", roles.RoleCop())
PlayerC = player.Player("Zatharel", "mafia", roles.Roleblocker())

players.extend((PlayerA, PlayerB, PlayerC))

PlayerA.cast(PlayerA.role.abilities["investigate"], (PlayerB, PlayerA))
PlayerB.cast(PlayerB.role.abilities["investigate"], (PlayerA, PlayerB))
PlayerC.cast(PlayerC.role.abilities["block"], (PlayerA,))

finalise_abilities(players)
resolve_abilities(players)

print(PlayerA.targetted_by)