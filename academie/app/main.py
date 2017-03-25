from repo.actorRepo import actorRepo
from repo.castRepo import castRepo
from repo.movieRepo import movieRepo
from domain.Actor import *
from domain.Movie import *
from domain.Cast import *
from controller import *
from controller.castController import *
from console.ui import *
import re

movieRepo = movieRepo()
actorRepo = actorRepo()
castRepo = castRepo()
movieController = movieController(movieRepo)
actorController = actorController(actorRepo)
castController = castController(castRepo)

ui = UI(movieController, actorController, castController)
ui.mainMenu()
