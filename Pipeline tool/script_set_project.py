import maya.cmds as cmd
import os
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget
from PySide2 import QtUiTools, QtWidgets, QtCore
import glob 
import shutil
from pathlib import Path

class SetProject(QMainWindow):
    def __init__ (self):
        super().__init__()
        
        # Recherche fenetre Ui :

        self.root_path = Path.home()/'Documents'

        self.liste_disques = ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:']
        if os.path.exists(f'{self.root_path}\\maya'):
            self.maya_path = f'{self.root_path}\\maya'
        else :
            for disk in self.liste_disques :
                self.new_path = f'{self.root_path}'.replace('C:',f'{disk}')
                if os.path.exists(f'{self.new_path}\\maya'):
                    self.maya_path = f'{self.new_path}\\maya'
    
        self.ui_path = f'{self.maya_path}\\2023\\prefs\\icons\\Zapping_Bura\\UI'

        self.uiFile = f'{self.ui_path}\\fenetre_set.ui' 

        #load fenetre Ui :              
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(self.uiFile, parentWidget=self)
        self.projectPath = cmd.workspace(q = True, rd = 1)
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.file_path = '\\\\Storage01\\Partages\\3D3_23_24\\Z_ETUDIANTS\\Zapping\\Bura_l_infirmiera\\GRP_02_Bura_L_infirmiera' #'D:\\Users\\Carlier\\Documents\\Esma\\3D3\\Zapping\\GRP_02_Bura_L_infirmiera' 
        self.file_name = ''
        self.file_save_name = ''

   #BUTTONS
        self.saveButton = self.ui.findChild(QtWidgets.QPushButton, "saveButton")
        self.saveButton.clicked.connect(self.launchSet)
            
    #LINE EDITS
        self.homePcPath = self.ui.findChild(QtWidgets.QLineEdit, "homePcPath") 

    #SPIN BOXES
        self.shotNumber = self.ui.findChild(QtWidgets.QSpinBox, "shotNumber")
        self.shotNumber.valueChanged.connect(self.shotNumberSelected)

    #RADIO BUTTONS

        # selected in groups
        self.projectType = self.ui.findChild(QtWidgets.QButtonGroup, 'projectType')
        self.projectType.buttonClicked.connect(self.projectTypeClicked)

        self.assetElement = self.ui.findChild(QtWidgets.QButtonGroup, 'assetElement')
        self.assetElement.buttonClicked.connect(self.assetElementClicked)

        self.workPlace = self.ui.findChild(QtWidgets.QButtonGroup, 'workPlace')
        self.workPlace.buttonClicked.connect(self.workPlaceClicked)

    #Initialisation des valeurs
        self.projectType = None
        self.selectedAssetElement = None
        self.workPlace = None
        self.home_pc_path = None
        self.shot_number = None


#Asset element :
    def projectTypeClicked (self, button):
        self.projectType = button.text()
        return self.projectType

    def assetElementClicked (self, button):
        self.selectedAssetElement = button.text()
        #self.asset_element_selected_button = button
        return self.selectedAssetElement

    def workPlaceClicked (self, button):
        self.workPlace = button.text()
        #self.work_place_selected_button = button
        return self.workPlace

    def shotNumberSelected (self, value):
        self.shot_number = value
        return self.shot_number

#Launch set :

    def launchSet(self):
        
        self.home_pc_path = self.homePcPath.text()
        #print (f'les elements sélectionnés sont : {self.projectType} asset : {self.selectedAssetElement} {self.assetStep}, shot :{self.shotStep} , work place :{self.workPlace} version :{self.version} path : {self.home_pc_path} shot {self.shot_number} props :{self.selected_props}') #
        self.file_path = '\\\\Storage01\\Partages\\3D3_23_24\\Z_ETUDIANTS\\Zapping\\Bura_l_infirmiera\\GRP_02_Bura_L_infirmiera' #D:\\Users\\Carlier\\Documents\\Esma\\3D3\\Zapping\\GRP_02_Bura_L_infirmiera'
        self.file_name = ''
        self.file_save_name = ''

    # WORKPLACE
        if self.workPlace == 'Je travaille chez moi':
            self.file_path = f'{self.home_pc_path}\\GRP_02_Bura_L_infirmiera'

            if self.home_pc_path =='':
                missing_homePath = cmd.window(title = 'Missing Home Path')
                cmd.window(missing_homePath, edit = True, frontWindow = True, widthHeight = (1000, 200))
                layout = cmd.columnLayout(adjustableColumn=True)
                cmd.text('\nLe chemin d\'accès à la maison n\'a pas été entré')
                cmd.showWindow(missing_homePath)
                
        
        elif self.workPlace == 'Je travaille à l\'école sur le partage':
            self.file_path = self.file_path

        else :
            missing_workPlace = cmd.window(title = 'Missing Work Place')
            cmd.window(missing_workPlace, edit = True, frontWindow = True, widthHeight = (1000, 200))
            layout = cmd.columnLayout(adjustableColumn=True)
            cmd.text('\nIl faut choisir entre travail à l\'école ou travail chez soi')
            cmd.showWindow(missing_workPlace)  
                              

    # PROJECT TYPE 
        #ASSETS :

        if self.projectType == 'Asset':
            self.file_path = f'{self.file_path}\\04_asset'

            if self.selectedAssetElement == 'Chara Bura':
                self.file_path = f'{self.file_path}\\character\\Bura\\maya'
                self.message = '04_Asset    :     Chara Bura'

            elif self.selectedAssetElement == 'Chara Boubouche':
                self.file_path = f'{self.file_path}\\character\\Boubouche\\maya'
                self.message = '04_Asset    :     Chara Boubouche'

            elif self.selectedAssetElement == 'Props':
                self.file_path = f'{self.file_path}\\prop\\maya'
                self.message = '04_Asset    :     Props'

            elif self.selectedAssetElement == 'Set':
                self.file_path = f'{self.file_path}\\character\\set\\maya'
                self.message = '04_Asset    :     Set'

            else :
                missing_assetName = cmd.window(title = 'Missing Asset Name')
                cmd.window(missing_assetName, edit = True, frontWindow = True, widthHeight = (1000, 200))
                layout = cmd.columnLayout(adjustableColumn=True)
                cmd.text('\nIl faut choisir un asset')
                cmd.showWindow(missing_assetName)   
                          
        #SHOTS :
        elif self.projectType == 'Shot':
            print(self.shot_number)
            if str(self.shotNumber.value()) != '2' and str(self.shotNumber.value()) != '3':
                print(self.shotNumber.value())
                self.shot_number = '1'
                
            self.file_path = f'{self.file_path}\\05_shot\\sq001_sh0{self.shot_number}0\\maya'
            self.message = f'05_Shot  :   sq001_sh0{self.shot_number}0'

              
            #|self.file_path = f'{self.file_path}\\05_shot'

        #RIEN COCHé
        else :
            missing_project_type = cmd.window(title = 'Missing Project Type')
            cmd.window(missing_project_type, edit = True, frontWindow = True, widthHeight = (1000, 200))
            layout = cmd.columnLayout(adjustableColumn=True)
            cmd.text('\nIl faut choisir entre Asset et Shot')
            cmd.showWindow(missing_project_type)
                        


    #SET PROJECT

        if self.file_path != '' :
            if not os.path.exists(self.file_path):
                os.makedirs(self.file_path)
            else :
                print('il existe déjà!')
            
            print (f'{self.file_path}')
            cmd.workspace(f'{self.file_path}',openWorkspace = True)        

            wellSet = cmd.window(title = 'Well Set')
            cmd.window(wellSet, edit = True, frontWindow = True, widthHeight = (300, 200))
            layout = cmd.columnLayout(adjustableColumn=True)
            cmd.text(f'\n\n\nProjet Setté dans : \n{self.message} ;)')
            cmd.showWindow(wellSet)        
        
        self.file_path = '\\\\Storage01\\Partages\\3D3_23_24\\Z_ETUDIANTS\\Zapping\\Bura_l_infirmiera\\GRP_02_Bura_L_infirmiera' #'D:\\Users\\Carlier\\Documents\\Esma\\3D3\\Zapping\\GRP_02_Bura_L_infirmiera' #
        self.file_name = ''
        self.file_save_name = ''

        #print (f'A la fin du script : \nfile_path :{self.file_path} \nfile name : {self.file_name}\nfile save name : {self.file_save_name}')

        

setProject = SetProject()
setProject.show()