#variables to be defined by user
mast_arm = 'MAST ARM - 45FT BLACK- NMPW'
upright = '1026-BACK PLATE-MAST ARM-18.75IN'
back_plate = '1026-BACK PLATE-MAST ARM-18.75IN'
SH = []
peds = ''
text = ''
part_no = '1033'
manufacturer = 'Valmont'
pole_name = "P4-25'"

# convert user input into CAD commands 
insert_mastarm = '(command ' + '"-insert" ' + '"' + mast_arm + '" '+ '"_s"' + ' ' + '1' + ' ' + '(list 1.89 29.83 -8.98) 0)' + ' "' + part_no + '" '+ "\n" + '"' + manufacturer + '"'

insert_upright = '(command ' + '"-insert" ' + '"' + upright + '" '+ '"_s"' + ' ' + '1' + ' ' + '(list -207 -284.4394 -5) 0)' + ' "' + part_no + '" '+ "\n" + '"' + manufacturer + '"'

insert_bp = '(command ' + '"-view" ' + '"o" ' + '"left")' + "\n" + '(command ' + '"-insert" ' + '"' + back_plate + '" '+ '"_s"' + ' ' + '1' + ' ' + '(list -235 -286 -11.84)' + ' "' + part_no + '" '+ "\n" + '"' + manufacturer + '"'

insert_sh = '(command ' + '"-view" ' + '"o" ' + '"front")' + "\n" + '(command ' + '"-insert" ' + '"' + back_plate + '" '+ '"_s"' + ' ' + '1' + ' ' + '(list 1.89 29.83 -8.98) 0)' + ' "' + part_no + '" '+ "\n" + '"' + manufacturer + '"'

insert_ped = '(command ' + '"-view" ' + '"o" ' + '"left")' + "\n" + '(command ' + '"-insert" ' + '"' + back_plate + '" '+ '"_s"' + ' ' + '1' + ' ' + '(list 1.89 29.83 -8.98) 0)' + ' "' + part_no + '" '+ "\n" + '"' + manufacturer + '"' + '\n' + '(command ' + '"-view" ' + '"o" ' + '"front")' + "\n" + '(command ' + '"-insert" ' + '"' + back_plate + '" '+ '"_s"' + ' ' + '1' + ' ' + '(list 1.89 29.83 -8.98) 0)' + ' "' + part_no + '" '+ "\n" + '"' + manufacturer + '"'

insert_text = 'text' + "\n" + "-1,-311" + "\n" + "10" + "\n" + "0 " + pole_name

'''
(command "-insert" "1073-UPRIGHT-20FT-18IN BC-MNPW-GALV" "_s" 1 (list -207 -284.4394 -5) 0) "1113" 
"Valmont"
(command "-view" "o" "left")
(command "-insert" "1026-BACK PLATE-MAST ARM-18.75IN" "_s" 1 (list -235 -286 -11.84) 0) "1026" 
"Valmont"
(command "-view" "o" "front")
(command "-insert" "1003-ASSY - YELLOW - 130 SIGNAL HEAD W" "_s" 1 (list -195.19 54.5 26.7) 0) "1003" 
"Pelco"
(command "-insert" "1018-ASSY-YELLOW-150A2H LEFT SIGNAL HEAD W" "_s" 1 (list -648 54.5 26.7) 0) "1018" 
"Pelco"
(command "-view" "o" "left")
(command "-insert" "1101-PEDESTRIAN SIGNAL HEAD-YELLOW-DRILLED LEFT" "_s" 1 (list -74.4 -146.32 -20.35) 0) "1088" 
"Pelco"
(command "-view" "o" "front")
(command "-insert" "1101-PEDESTRIAN SIGNAL HEAD-YELLOW-DRILLED LEFT" "_s" 1 (list -47.24 -146.32 -12.8) 0) "1088" 
"Pelco"
text
-1,-311
10
0 P4-25'
'''

print(insert_bp)
