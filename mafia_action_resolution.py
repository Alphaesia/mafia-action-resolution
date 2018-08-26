import player
import roles

players = []

PlayerA = player.Player("CreepaShadowz", "innocent", roles.Detective())
PlayerB = player.Player("yeroc424", "mafia", roles.RoleCop())
PlayerC = player.Player("Zatharel", "mafia", roles.Roleblocker())

players.extend((PlayerA, PlayerB, PlayerC))

# Cast abilities
PlayerA.cast(PlayerA.role.abilities["investigate"], (PlayerB, PlayerA))
PlayerB.cast(PlayerB.role.abilities["investigate"], (PlayerA, PlayerB))
PlayerC.cast(PlayerC.role.abilities["block"], (PlayerA,))

# Resolve abilities
for player in players:
	for ability in player.cast_abilities:
		ability.resolve()
		ability.print_components()