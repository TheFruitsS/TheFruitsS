class Party:
    def __init__(self):
        self.party_invites = []

party = Party()

party_guests = input()
while party_guests != 'End':
    party.party_invites.append(party_guests)
    party_guests = input()

print(f"Going:{','.join(party.party_invites)}")
print(f"Total:{len(party.party_invites)}")