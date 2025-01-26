from django import forms

class teampicker(forms.Form):
    teams = forms.MultipleChoiceField(
        choices=[
            ('Arsenal', 'Arsenal'),
            ('Aston Villa', 'Aston Villa'),
            ('Bournemouth', 'Bournemouth'),
            ('Brentford', 'Brentford'),
            ('Brighton', 'Brighton'),
            ('Chelsea', 'Chelsea'),
            ('Crystal Palace', 'Crystal Palace'),
            ('Everton', 'Everton'),
            ('Fulham', 'Fulham'),
            ('Ipswich Town', 'Ipswich Town'),
            ('Leicester City', 'Leicester City'),
            ('Liverpool', 'Liverpool'),
            ('Manchester City', 'Manchester City'),
            ('Manchester United', 'Manchester United'),
            ('Newcastle', 'Newcastle'),
            ('Nottingham Forest', 'Nottingham Forest'),
            ('Southampton', 'Southampton'),
            ('Tottenham', 'Tottenham'),
            ('West Ham', 'West Ham'),
            ('Wolverhampton Wanderers', 'Wolverhampton Wanderers'),
        ],
        widget=forms.CheckboxSelectMultiple,
        label='Select from these teams'
    )
    team_id = forms.IntegerField(widget=forms.HiddenInput(), required = False) 
