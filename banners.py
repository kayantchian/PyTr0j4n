from random import choice



figletAsciiAlligator= """
:::::::::  :::   ::: ::::::::::: :::::::::   :::::::  :::::::::::     :::     ::::    ::: 
:+:    :+: :+:   :+:     :+:     :+:    :+: :+:   :+:     :+:        :+:      :+:+:   :+: 
+:+    +:+  +:+ +:+      +:+     +:+    +:+ +:+  :+:+     +:+       +:+ +:+   :+:+:+  +:+ 
+#++:++#+    +#++:       +#+     +#++:++#:  +#+ + +:+     +#+      +#+  +:+   +#+ +:+ +#+ 
+#+           +#+        +#+     +#+    +#+ +#+#  +#+     +#+     +#+#+#+#+#+ +#+  +#+#+# 
#+#           #+#        #+#     #+#    #+# #+#   #+# #+# #+#           #+#   #+#   #+#+# 
###           ###        ###     ###    ###  #######   #####            ###   ###    #### 
"""

figletAsciiBloody = """
 ██▓███  ▓██   ██▓▄▄▄█████▓ ██▀███   ▄▄▄██▀▀▀ ███▄    █ 
▓██░  ██▒ ▒██  ██▒▓  ██▒ ▓▒▓██ ▒ ██▒   ▒██    ██ ▀█   █ 
▓██░ ██▓▒  ▒██ ██░▒ ▓██░ ▒░▓██ ░▄█ ▒   ░██   ▓██  ▀█ ██▒
▒██▄█▓▒ ▒  ░ ▐██▓░░ ▓██▓ ░ ▒██▀▀█▄  ▓██▄██▓  ▓██▒  ▐▌██▒
▒██▒ ░  ░  ░ ██▒▓░  ▒██▒ ░ ░██▓ ▒██▒ ▓███▒   ▒██░   ▓██░
▒▓▒░ ░  ░   ██▒▒▒   ▒ ░░   ░ ▒▓ ░▒▓░ ▒▓▒▒░   ░ ▒░   ▒ ▒ 
░▒ ░      ▓██ ░▒░     ░      ░▒ ░ ▒░ ▒ ░▒░   ░ ░░   ░ ▒░
░░        ▒ ▒ ░░    ░        ░░   ░  ░ ░ ░      ░   ░ ░ 
          ░ ░                 ░      ░   ░            ░ 
          ░ ░                                           
"""


figletAsciiRebel = """

 ███████████             ███████████              █████         ███  █████ █████            
░░███░░░░░███           ░█░░░███░░░█            ███░░░███      ░░░  ░░███ ░░███             
 ░███    ░███ █████ ████░   ░███  ░  ████████  ███   ░░███     █████ ░███  ░███ █ ████████  
 ░██████████ ░░███ ░███     ░███    ░░███░░███░███    ░███    ░░███  ░███████████░░███░░███ 
 ░███░░░░░░   ░███ ░███     ░███     ░███ ░░░ ░███    ░███     ░███  ░░░░░░░███░█ ░███ ░███ 
 ░███         ░███ ░███     ░███     ░███     ░░███   ███      ░███        ░███░  ░███ ░███ 
 █████        ░░███████     █████    █████     ░░░█████░       ░███        █████  ████ █████
░░░░░          ░░░░░███    ░░░░░    ░░░░░        ░░░░░░        ░███       ░░░░░  ░░░░ ░░░░░ 
               ███ ░███                                    ███ ░███                         
              ░░██████                                    ░░██████                          
               ░░░░░░                                      ░░░░░░                           

"""

figletAsciiMerlin = """

   _______    ___  ___   ___________    _______       ______          ___   ___  ___     _____  ___   
  |   __ "\  |"  \/"  | ("     _   ")  /"      \     /    " \        |"  | (: "||_  |   (\"   \|"  \  
  (. |__) :)  \   \  /   )__/  \\__/  |:        |   // ____  \       ||  | |  (__) :|   |.\\   \    | 
  |:  ____/    \\  \/       \\_ /     |_____/   )  /  /    ) :)      |:  |  \____  ||   |: \.   \\  | 
  (|  /        /   /        |.  |      //      /  (: (____/ //    ___|  /       _\ '|   |.  \    \. | 
 /|__/ \      /   /         \:  |     |:  __   \   \        /    /  :|_/ )     /" \_|\  |    \    \ | 
(_______)    |___/           \__|     |__|  \___)   \"_____/    (_______/     (_______)  \___|\____\) 
                                                                                                      
"""

def getBanner():
    return choice([figletAsciiAlligator, figletAsciiBloody, figletAsciiRebel, figletAsciiMerlin])

