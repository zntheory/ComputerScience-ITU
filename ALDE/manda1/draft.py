#!/usr/bin/env python

teams, capacity, players = list(map(int,input().split()))

teams_dict = {}
players_dict = {}
propose_queue = []

class Team:
    def __init__(self, _name, _prio_list):
        self.name = _name
        self.prio_list = _prio_list     # teams' priority list = stack
        self.players_names = set()     # current players' names

    def propose(self):
        player_name = self.prio_list.pop(0)
        player = players_dict.get(player_name)
        player.consider(self)

    def accepted(self, player_name):
        self.players_names.add(player_name)

    def rejected(self):
        propose_queue.append(self)

    def dumped(self, player_name):
        self.players_names.remove(player_name)
        self.rejected()


class Player:
    def __init__(self, _name, _prio_map):
        self.name = _name
        self.prio_map = _prio_map     # players' priority list = hashmap
        self.team = None

    def consider(self, proposer_team):
        if self.team is None:
            proposer_team.accepted(self.name)
            self.team = proposer_team
        elif self.prio_map.get(proposer_team.name) < self.prio_map.get(self.team.name):
            self.team.dumped(self.name)
            proposer_team.accepted(self.name)
            self.team = proposer_team
        else:
            proposer_team.rejected()


def proposal_handling():
    while propose_queue:
        team = propose_queue.pop()
        team.propose()
    for team in teams_dict.values():
        _players = " ".join(team.players_names)
        print(team.name + " " + _players)

# - QUEUE -

for x in range(teams):
    line = input().split()
    name, *prio_list = line
    t = Team(name, prio_list)
    teams_dict.update({name: t})
    for y in range(capacity):
        propose_queue.append(t)

for x in range(players):
    line = input().split()
    name, *prio_list = line

    prio_map = {}
    t_val = 0
    for t in prio_list:
        prio_map.update({t: t_val})
        t_val = t_val + 1

    p = Player(name, prio_map)
    players_dict.update({name: p})


# - THE PROPOSAL (2009) -

proposal_handling()

