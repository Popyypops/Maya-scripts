import maya.cmds as cmd
shapesList = cmd.ls (tr = True)

nameSpace = ''
namespaceList = []
legGeoList = ['Pelvis' ,'PelvisCollar', 'Thigh_lt' ,'Knee_lt' ,'Leg_lt' ,'Foot_lt' ,'Toe_lt' ,'Thigh_rt' ,'Knee_rt' ,'Leg_rt' ,'Foot_rt' ,'Toe_rt']
armGeoList = ['Thumb_01_rt','Hand_rt','Major_02_rt','Thumb_03_rt','Forearm_rt','Index_02_rt','Pinky_02_rt','Index_01_rt','Thumb_02_rt','Major_01_rt','Elbow_rt','Major_03_rt','Pinky_03_rt','Arm_rt','Pinky_01_rt','Index_03_rt','Arm_rt','Shoulder_rt','Index_01_lt','Pinky_03_lt','Elbow_lt','Pinky_02_lt','Forearm_lt','Major_01_lt','Hand_lt','Thumb_03_lt','Pinky_01_lt','Index_03_lt','Major_02_lt','Arm_lt','Major_03_lt','Thumb_02_lt','Thumb_01_lt','Index_02_lt','Shoulder_lt']
bodyGeoList = ['Button','Abs','TorsoCollar','Torso','Collar']
headGeoList = ['Head','Neck','Mask']
alembicNamesList = []

#liste des namespaces de Rig dans la scène
for shape in shapesList :
	if ':' in shape :
		nameSpace = shape.split(':')[0]

	#liste des namespaces de personnages dans la scène
	if 'Su_Rigging' in nameSpace :
		if nameSpace in namespaceList :
			namespaceList = namespaceList
		else : 
			namespaceList.append(nameSpace)
print(f'les namespaces de la scene sont : {namespaceList}')

# création de la liste des géo à sélectionner pour l'export
for namespace in namespaceList:
	alembicName = ''
	alembicExportList = []

	legType = cmd.getAttr(f'{namespace}:CC_Morpho_switch.leg_type')
	charaList = []
	charaOrderedList = []
	alembicBaseName = ''
	if legType == 0 :
		for geo in legGeoList :
			alembicExportList.append(f'{namespace}:GEO_Krow_{geo}')
		if 'Krow' not in charaList :
			charaList.append('Krow')
	elif legType == 1 : 
		for geo in legGeoList :
			alembicExportList.append(f'{namespace}:GEO_Su_{geo}')
		if 'Su' not in charaList :
			charaList.append('Su')
	elif legType == 2 : 
		for geo in legGeoList :
			alembicExportList.append(f'{namespace}:GEO_Fau_{geo}')
		if 'Fau' not in charaList :
			charaList.append('Fau')
	elif legType == 3 : 
		for geo in legGeoList :
			alembicExportList.append(f'{namespace}:GEO_Lykke_{geo}')
		if 'Lykke' not in charaList :
			charaList.append('Lykke')
	print (f'{legType} leg type is {charaList}')

	armType = cmd.getAttr(f'{namespace}:CC_Morpho_switch.arm_type')
	if armType == 0 :
		for geo in armGeoList :
			alembicExportList.append(f'{namespace}:GEO_Krow_{geo}')
		if 'Krow' not in charaList :
			charaList.append('Krow')
	elif armType == 1 : 
		for geo in armGeoList :
			alembicExportList.append(f'{namespace}:GEO_Su_{geo}')
		if 'Su' not in charaList :
			charaList.append('Su')
	elif armType == 2 : 
		for geo in armGeoList :
			alembicExportList.append(f'{namespace}:GEO_Fau_{geo}')
		if 'Fau' not in charaList :
			charaList.append('Fau')
	elif armType == 3 : 
		for geo in armGeoList :
			alembicExportList.append(f'{namespace}:GEO_Lykke_{geo}')
		if 'Lykke' not in charaList :
			charaList.append('Lykke')
	print (f'{armType} arm type is {charaList}')

	bodyType = cmd.getAttr(f'{namespace}:CC_Morpho_switch.body_type')
	if bodyType == 0 :
		for geo in bodyGeoList :
			alembicExportList.append(f'{namespace}:GEO_Krow_{geo}')
		if 'Krow' not in charaList :
			charaList.append('Krow')
	elif bodyType == 1 : 
		for geo in bodyGeoList :
			alembicExportList.append(f'{namespace}:GEO_Su_{geo}')
		if 'Su' not in charaList :
			charaList.append('Su')
	elif bodyType == 2 : 
		for geo in bodyGeoList :
			alembicExportList.append(f'{namespace}:GEO_Fau_{geo}')
		if 'Fau' not in charaList :
			charaList.append('Fau')
	elif bodyType == 3 : 
		for geo in bodyGeoList :
			alembicExportList.append(f'{namespace}:GEO_Lykke_{geo}')
		if 'Lykke' not in charaList :
			charaList.append('Lykke')
	print (f'{bodyType} body type is {charaList}')
	
	headType = cmd.getAttr(f'{namespace}:CC_Morpho_switch.head_type')
	if headType == 0 :
		for geo in headGeoList :
			alembicExportList.append(f'{namespace}:GEO_Krow_{geo}')
		if 'Krow' not in charaList :
			charaList.append('Krow')
	elif headType == 1 : 
		for geo in headGeoList :
			alembicExportList.append(f'{namespace}:GEO_Su_{geo}')
		if 'Su' not in charaList :
			charaList.append('Su')
	elif headType == 2 : 
		for geo in headGeoList :
			alembicExportList.append(f'{namespace}:GEO_Fau_{geo}')
		if 'Fau' not in charaList :
			charaList.append('Fau')
	elif headType == 3 : 
		for geo in headGeoList :
			alembicExportList.append(f'{namespace}:GEO_Lykke_{geo}')
		if 'Lykke' not in charaList :
			charaList.append('Lykke')
	print (f'{headType} head type is {charaList}')

	#print(f'alembic export liste : {alembicExportList}')
	print(f'liste des chara impliqués : {charaList}')


	#rangement des chara dans un ordre unique pour avoir toujours le même et pouvoir compter les itérations
	if 'Lykke' in charaList :
		charaOrderedList.append('Lykke')

	if 'Fau' in charaList :
		charaOrderedList.append('Fau')

	if 'Su' in charaList :
		charaOrderedList.append('Su')

	if 'Krow' in charaList :
		charaOrderedList.append('Krow')


	# nom du set qui contient les éléments concernés par le rig en fonction de la liste des chara impliqués
	for obj in charaOrderedList :
		if 'Lykke' in obj and 'Lykke_' not in alembicBaseName:
			alembicBaseName = f'Lykke_{alembicBaseName}' 		
					
		if 'Fau' in obj and 'Fau_' not in alembicBaseName:
			alembicBaseName = f'Fau_{alembicBaseName}'

		if 'Su' in obj and 'Su_' not in alembicBaseName:
			alembicBaseName = f'Su_{alembicBaseName}'

		if 'Krow' in obj and 'Krow_' not in alembicBaseName:
			alembicBaseName = f'Krow_{alembicBaseName}'
	
	print (alembicBaseName)
	
	iterations = 1
	alembicName = f'{alembicBaseName}0{str(iterations)}_abc'

	for name in alembicNamesList :
		if alembicName == name :
			iterations +=1
			if len(str(iterations)) == 1 :
				alembicName = f'{alembicBaseName}0{str(iterations)}_abc'
			if len(str(iterations)) == 2:
				alembicName = f'{alembicBaseName}{str(iterations)}_abc'

	cmd.select(alembicExportList)
	cmd.sets(name = f'ProductName_{alembicName}')				

	alembicNamesList.append(alembicName)

#print (alembicExportList)
#print(alembicNamesList)

#cmd.select(alembicExportList)
