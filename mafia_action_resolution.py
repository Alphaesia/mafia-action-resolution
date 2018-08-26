import player
import roles

players = []

PlayerA = player.Player("CreepaShadowz", "innocent", roles.Detective())
PlayerB = player.Player("yeroc424", "mafia", roles.RoleCop())

players.extend((PlayerA, PlayerB))

# Cast abilities
PlayerA.cast(PlayerA.role.abilities["investigate"], [PlayerB])
PlayerB.cast(PlayerB.role.abilities["investigate"], [PlayerA])

# Resolve abilities
for player in players:
	for ability in player.cast_abilities:
		ability.resolve()
		ability.print_components()