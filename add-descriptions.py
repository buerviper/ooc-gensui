import yaml
import os
from pathlib import Path


def generate_yaml_description(file_save, file_name):
    if file_name.split("-")[0] == "suikogaiden":
        yaml.dump({'status': '#suikoden #suikogaiden #jrpg', 'spoiler_warning': '',
                   'description': 'Screenshot of Suikogaiden.', 'language': '', 'sensitivity': ''}, file_save)
    elif file_name.split("-")[1] == "01":
        yaml.dump({'status': '#suikoden #jrpg', 'spoiler_warning': '', 'description': 'Screenshot of Suikoden.',
                   'language': '', 'sensitivity': ''}, file_save)
    elif file_name.split("-")[1] == "02":
        yaml.dump(
            {'status': '#suikoden #suikoden2 #jrpg', 'spoiler_warning': '', 'description': 'Screenshot of Suikoden II.',
             'language': '', 'sensitivity': ''}, file_save)
    elif file_name.split("-")[1] == "03":
        yaml.dump({'status': '#suikoden #suikoden3 #jrpg', 'spoiler_warning': '',
                   'description': 'Screenshot of Suikoden III.', 'language': '', 'sensitivity': ''}, file_save)
    elif file_name.split("-")[1] == "04":
        yaml.dump(
            {'status': '#suikoden #suikoden4 #jrpg', 'spoiler_warning': '', 'description': 'Screenshot of Suikoden IV.',
             'language': '', 'sensitivity': ''}, file_save)
    elif file_name.split("-")[1] == "05":
        yaml.dump(
            {'status': '#suikoden #suikoden5 #jrpg', 'spoiler_warning': '', 'description': 'Screenshot of Suikoden V.',
             'language': '', 'sensitivity': ''}, file_save)
    elif file_name.split("-")[1] == "Tactics":
        yaml.dump({'status': '#suikoden #SuikodenTactics #jrpg', 'spoiler_warning': '',
                   'description': 'Screenshot of Suikoden Tactics.', 'language': '', 'sensitivity': ''}, file_save)
    elif file_name.split("-")[1] == "Tierkreis":
        yaml.dump({'status': '#suikoden #SuikodenTierkreis #jrpg', 'spoiler_warning': '',
                   'description': 'Screenshot of Suikoden Tierkreis.', 'language': '', 'sensitivity': ''}, file_save)
    elif file_name.split("-")[1] == "Tsumuji":
        yaml.dump(
            {'status': '#suikoden #SuikodenTsumuji #SuikodenTsumugareshiHyakunenNoToki #jrpg', 'spoiler_warning': '',
             'description': 'Screenshot of Suikoden Tsumugareshi Hyakunen No Toki.', 'language': '', 'sensitivity': ''},
            file_save)


for x in os.listdir("images"):
    if os.path.isfile(os.path.join("images", x)):
        name = Path("images/" + x).stem
        if not os.path.exists("images/descriptions/"+name + ".yml"):
            file_yml = open("images/descriptions/" + name + ".yml", "w")
            generate_yaml_description(file_yml, name)
