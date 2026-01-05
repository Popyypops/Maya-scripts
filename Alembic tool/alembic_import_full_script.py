import maya.cmds as cmd
import os

class ImportAllMorphoAbc():
	def __init__(self):
		super().__init__()
		'''
		self.alembicExportsList = []
		self.KrowIterations = 0
		self.SuIterations = 0
		self.FauIterations = 0
		self.LykkeIterations = 0
		self.CrowdIterations = 0

		self.filePath = cmd.file(q=True, sn=True)
		'''

	def listEachMorpho (self):

		self.alembicExportsList = []
		self.KrowIterations = 0
		self.SuIterations = 0
		self.FauIterations = 0
		self.LykkeIterations = 0
		self.CrowdIterations = 0

		self.filePath = cmd.file(q=True, sn=True)


		self.exportPath = self.filePath.split('/Scenefiles')[0]
		self.exportPath = f'{self.exportPath}/Export'
		#print(exportPath)
		
		self.exportsList = os.listdir(self.exportPath)
		#print(exportsList)
		for folder in self.exportsList :
			if '_abc' in folder :
				if 'Krow_' in folder or 'Su_' in folder or 'Fau_' in folder or 'Lykke_' or 'Crowd_LOW' in folder :
					self.alembicExportsList.append(folder)
		#print(alembicExportsList)
		
		for export in self.exportsList :
			if 'Krow_' in export :
				self.KrowIterations +=1
			if 'Su_' in export :
				self.SuIterations +=1
			if 'Fau_' in export :
				self.FauIterations +=1
			if 'Lykke_' in export :
				self.LykkeIterations +=1
		if 'Crowd_LOW' in self.exportsList  :
			self.CrowdIterations +=1

		
	def importSurfacingMorpho (self):
		if self.KrowIterations >=1 :
			for i in range (self.KrowIterations) :
				cmd.file('\\\\STORAGE03\\Partages\\3D4\\PARHELIA\\Parhelia\\03_Production\\Assets\\Chara\\Krow\\Export\\Surfacing\\master\\Krow_Surfacing_master.ma', namespace = 'Krow_Surfacing', r = True)

		if self.SuIterations >=1 :
			for i in range (self.SuIterations) :
				cmd.file('\\\\STORAGE03\\Partages\\3D4\\PARHELIA\\Parhelia\\03_Production\\Assets\\Chara\\Su\\Export\\Surfacing\\master\\Su_Surfacing_master.ma', namespace = 'Su_Surfacing', r = True)
		
		if self.FauIterations >=1 :
			for i in range (self.FauIterations) :
				cmd.file('\\\\STORAGE03\\Partages\\3D4\\PARHELIA\\Parhelia\\03_Production\\Assets\\Chara\\Fau\\Export\\Surfacing\\master\\Fau_Surfacing_master.ma', namespace = 'Fau_Surfacing', r = True)

		if self.LykkeIterations >=1 :
			for i in range (self.LykkeIterations) :
				cmd.file('\\\\STORAGE03\\Partages\\3D4\\PARHELIA\\Parhelia\\03_Production\\Assets\\Chara\\Lykke\\Export\\Surfacing\\master\\Lykke_Surfacing_master.ma', namespace = 'Lykke_Surfacing', r = True)

		
	def selectionSetsToApplyCacheTo (self):

		self.alembicExportsList = []
		self.objectsList = cmd.ls(tr = True)
		self.surfacingObjectsList = []
		self.charaNamespaceList = []
		self.KrowIterations = 0
		self.SuIterations = 0
		self.FauIterations = 0
		self.LykkeIterations = 0
		self.usedNamespace = ''
		self.listHighest = []
		self.allHighest = False
		self.namespaceDone = []
		
		#remplissage de la liste d'éléments de surfacing dans la scène 
		for obj in self.objectsList :
			if '_Surfacing' in obj :
				if 'Krow_' in obj or 'Su_' in obj or 'Fau_' in obj or 'Lykke_' in obj :
					self.surfacingObjectsList.append(obj)
					#print('ya un des persos!!')
		#print(f'Les objets à texturer sont {surfacingObjectsList}')
		
		for obj in self.surfacingObjectsList :
			self.namespace = obj.split(':')[0]
			if self.namespace not in self.charaNamespaceList :
				self.charaNamespaceList.append(self.namespace)
		#print(f'les namespaces des persos de la scène sont : {charaNamespaceList}')
		
		#récupération de la liste des fichiers présents dans le dossier d'exports pour avoir la liste des alembic
		self.filePath = cmd.file(q=True, sn=True)
		self.exportPath = self.filePath.split('/Scenefiles')[0]
		self.exportPath = f'{self.exportPath}/Export'
		self.exportsList = os.listdir(self.exportPath)
		
		#print(f'les éléments présents dans le dossier exports sont : {self.exportsList}')
		#liste des dossiers d'export alembic => liste des personnages selon leur morpho
		for folder in self.exportsList :
			if '_abc' in folder :
				if 'Krow_' in folder or 'Su_' in folder or 'Fau_' in folder or 'Lykke_' in folder :
					self.alembicExportsList.append(folder)
		#print (f'les dossiers d\'alembic à importer sont : {self.alembicExportsList}')
		
		# liste des personnages et comptage de leurs itérations dans la scène d'anim
		for export in self.exportsList :
			if 'Krow_' in export :
				self.KrowIterations +=1
			if 'Su_' in export :
				self.SuIterations +=1
			if 'Fau_' in export :
				self.FauIterations +=1
			if 'Lykke_' in export :
				self.LykkeIterations +=1
		
		#print(f'la liste des namespaces de perso dans la scene est : {self.charaNamespaceList}')
		
		self.KrowNumber = sum('Krow_' in obj for obj in self.charaNamespaceList)
		self.SuNumber = sum('Su_' in obj for obj in self.charaNamespaceList)
		self.FauNumber = sum('Fau_' in obj for obj in self.charaNamespaceList)
		self.LykkeNumber = sum('Lykke_' in obj for obj in self.charaNamespaceList)
		
		if self.KrowNumber >= self.KrowIterations and self.SuNumber >= self.SuIterations and self.FauNumber >= self.FauIterations and self.LykkeNumber >= self.LykkeIterations  :
			for export in self.alembicExportsList :
				self.charaList = []
				self.setList = []
				#création de la liste des personnages concernés pour le dossier en train d'être analysé
				if 'Krow' in export :
					self.charaList.append('Krow_')
				if 'Su' in export :
					self.charaList.append('Su_')
				if 'Fau' in export :
					self.charaList.append('Fau_')
				if 'Lykke' in export :
					self.charaList.append('Lykke_')
			
				for chara in self.charaList :
					#verification si le premier namespace a été utilisé ou pas encore 
					
					if f'{chara}Surfacing:' not in self.namespaceDone :
						self.usedNamespace = f'{chara}Surfacing:'
						#print(f'first iteration of {chara}')
					else :
						#print(f'at least second iteration of {chara}')
						self.increment = 1
						while f'{chara}Surfacing{self.increment}:' in self.namespaceDone :
							self.increment +=1
						self.usedNamespace = f'{chara}Surfacing{self.increment}'
		
					for obj in self.surfacingObjectsList :
						if self.usedNamespace in obj and 'GP_' not in obj :
							self.setList.append(obj)
							
				#pour chaque alembic, on sélectionne toutes les morphos concernées par cet alembic dans la scène :
				cmd.select(self.setList)
				cmd.sets(name = f'{export}_import')
	
				#rajoute les objets utilisés pour cet alembic à la liste objectListDone
				for obj in self.setList :
					self.namespace = obj.split(':')[0]
					if f'{self.namespace}:' not in self.namespaceDone :
						self.namespaceDone.append(f'{self.namespace}:')
				print(f'les namespaces dejà utilisés sont : {self.namespaceDone}')


		
		else :
			window = cmd.window(title = 'not enough surfacing characters imported!', widthHeight = (300,150))
			cmd.columnLayout(adjustableColumn =True)
			cmd.text(label = f'\n\n not enough surfacing characters imported! \n\nLes éléments de surfacing à importer sont : \n\n{self.KrowIterations} Krow \n{self.SuIterations} Su \n{self.FauIterations} Fau \n{self.LykkeIterations} Lykke \n{self.CrowdIterations} Crowd lowPoly')
			cmd.showWindow(window)





importAllMorphoAbc = ImportAllMorphoAbc()

importAllMorphoAbc.listEachMorpho()
importAllMorphoAbc.importSurfacingMorpho()
importAllMorphoAbc.selectionSetsToApplyCacheTo()