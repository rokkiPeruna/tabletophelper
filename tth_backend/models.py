from django.db import models

# Create your models here.


# Logic: Application users can play in multiple sessions and different
# tabletop games at the same time, hence they can have multiple game sessions.
# Each game session has a game master or masters and the players, thus individuals
# in game sessions have different roles.

# AppUser represents application user.
class AppUser(models.Model):
  name = models.CharField(max_length=30)
  alias = models.CharField(max_length=30)


# GameSession represents a tabletop game which has a game master(s)
# and players.
class GameSession(models.Model):
  name = models.CharField(max_length=100)
  # TODO: Each session has multiple players/users/NPCs


# Character represents a character in a game session. It can be a user's
# character or an NPC created by the game master(s).
class Character(models.Model):
  name = models.CharField(max_length=100)
  # TODO: Each character has a character sheet and owning user


# SimpleCharacter represents a simple NPC which can used in small, quite
# meaningless encounters, such as bar brawls etc or as passing quards.
class SimpleCharacter(models.Model):
  name = models.CharField(max_length=100)
  # TODO: Each simple character is owned by the game master(s)


# CharacterSheet represents the container which holds all the character data
# in easily serialisable format, such as JSON.
class CharacterSheet(models.Model):
  # TODO: How data is stored?
  pass
