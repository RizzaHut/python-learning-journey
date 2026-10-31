def player_status(health):
    if health <= 0:
        message = "dead"
        return message
    elif health <=5:
        message = "injured"
        return message
    else:
        message = "healthy"
        return message
