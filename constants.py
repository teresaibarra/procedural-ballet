##########################
#                        #
#     BODY DIRECTIONS    #
#                        #
##########################
ENFACE = 'ENFACE'
EFFACE = 'EFFACE'
CROISE = 'CROISE'

##########################
#                        #
#   NUM FOOT ARRANGMENT  #
#                        #
##########################
ONE_FOOT = 'ONE_FOOT'
TWO_FEET = 'TWO_FEET'
NO_FEET = 'NO_FEET'

##########################
#                        #
#   MOVEMENT DIRECTIONS  #
#                        #
##########################
RIGHT = 'RIGHT'
LEFT = 'LEFT'
FORWARD = 'FORWARD'
BACKWARD = 'BACKWARD'

##########################
#                        #
#     FEET POSITIONS     #
#                        #
##########################
SECOND = 'SECOND'
FIFTH = 'FIFTH'

##########################
#                        #
#  ACTIVE LEG POSITIONS  #
#                        #
##########################
EN_LAIR = 'EN_LAIR'
A_TERRE = 'A_TERRE'

##########################
#                        #
#    A TERRE POSITIONS   #
#                        #
##########################
FRONT = 'FRONT'
SIDE = 'SIDE'
BACK = 'BACK'

##########################
#                        #
#    EN LAIR POSITIONS   #
#                        #
##########################
BATTEMENT = 'BATTEMENT'
ATTITUDE = 'ATTITUDE'
PASSE = 'PASSE'
COUPE = 'COUPE'

##########################
#                        #
#       PARAMETERS       #
#                        #
##########################

# ROUTINE_LENGTH does not include the START_END_POSITION, which is added to the
# beginning and end of the routine for uniformity
ROUTINE_LENGTH = 10

# START_END_POSITION is the configuration that the routine begins and ends with
START_END_POSITION = {
    'body_direction': CROISE,
    'num_feet': TWO_FEET,
    'attributes': {
        'front_foot': RIGHT,
        'ground_postiion': FIFTH
    }
}
