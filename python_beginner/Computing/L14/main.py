def binary_string_to_int(num_servers, num_players, num_admins):
    int_servers = int(num_servers, 2) 
    int_players = int(num_players, 2)
    int_admins = int(num_admins, 2)
    return int_servers, int_players, int_admins
