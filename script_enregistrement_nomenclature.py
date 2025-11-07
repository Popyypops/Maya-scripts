import maya.cmds as cmd
import os
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget
from PySide2 import QtUiTools, QtWidgets, QtCore
import glob 
import shutil
from pathlib import Path

class SaveFile(QMainWindow):
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

        self.uiFile = f'{self.ui_path}\\fenetre_save.ui'
        
        #load fenetre Ui :

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(self.uiFile, parentWidget=self)
        self.projectPath = cmd.workspace(q = True, rd = 1)
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.file_path = '\\\\Storage01\\Partages\\3D3_23_24\\Z_ETUDIANTS\\Zapping\\Bura_l_infirmiera\\GRP_02_Bura_L_infirmiera' #'D:\\Carlier_Penelope\\GRP_02_Bura_L_infirmiera'
        self.file_name = ''
        self.file_save_name = ''

   #BUTTONS
        self.saveButton = self.ui.findChild(QtWidgets.QPushButton, "saveButton")
        self.saveButton.clicked.connect(self.launchSave)
            
    #LINE EDITS
        self.homePcPath = self.ui.findChild(QtWidgets.QLineEdit, "homePcPath")
        self.propsAutre = self.ui.findChild(QtWidgets.QLineEdit, "props_autre") 

    #SPIN BOXES
        self.shotNumber = self.ui.findChild(QtWidgets.QSpinBox, "shotNumber")
        self.shotNumber.valueChanged.connect(self.shotNumberSelected)
   
    #COMBO BOX
        self.propsList = self.ui.findChild(QtWidgets.QComboBox, "propsList")
        self.propsList.currentIndexChanged.connect(self.comboBoxProps)

    #RADIO BUTTONS

        # selected in groups
        self.projectType = self.ui.findChild(QtWidgets.QButtonGroup, 'projectType')
        self.projectType.buttonClicked.connect(self.projectTypeClicked)

        self.assetElement = self.ui.findChild(QtWidgets.QButtonGroup, 'assetElement')
        self.assetElement.buttonClicked.connect(self.assetElementClicked)

        self.assetStep = self.ui.findChild(QtWidgets.QButtonGroup, 'assetStep')
        self.assetStep.buttonClicked.connect(self.assetStepClicked)

        self.shotStep = self.ui.findChild(QtWidgets.QButtonGroup, 'shotStep')
        self.shotStep.buttonClicked.connect(self.shotStepClicked)

        self.workPlace = self.ui.findChild(QtWidgets.QButtonGroup, 'workPlace')
        self.workPlace.buttonClicked.connect(self.workPlaceClicked)

        self.editPublish = self.ui.findChild(QtWidgets.QButtonGroup, 'editPublish')
        self.editPublish.buttonClicked.connect(self.editOrPublish)


    #Initialisation des valeurs
        self.projectType = None
        self.selectedAssetElement = None
        self.assetStep = None
        self.shotStep = None
        self.workPlace = None
        self.version = None
        self.home_pc_path = None
        self.selected_props = None
        self.shot_number = None


#Asset element :
    def projectTypeClicked (self, button):
        self.projectType = button.text()
        return self.projectType

    def assetElementClicked (self, button):
        self.selectedAssetElement = button.text()
        #self.asset_element_selected_button = button
        return self.selectedAssetElement

    def assetStepClicked (self, button):
        self.assetStep = button.text()
        #self.asset_step_selected_button = button
        return self.assetStep

    def shotStepClicked (self, button):
        self.shotStep = button.text()
        #self.shot_step_selected_button = button
        return self.shotStep

    def workPlaceClicked (self, button):
        self.workPlace = button.text()
        #self.work_place_selected_button = button
        return self.workPlace

    def editOrPublish (self, button):
        self.version = button.text()
        #self.version_selected_button = button
        return self.version

    def shotNumberSelected (self, value):
        self.shot_number = value
        return self.shot_number

    def comboBoxProps (self, index):
        self.selected_props = self.propsList.currentText()
        print (self.selected_props)

        return self.selected_props
        

#Launch save :

    def launchSave(self):
        
        self.home_pc_path = self.homePcPath.text()
        #print (f'les elements sélectionnés sont : {self.projectType} asset : {self.selectedAssetElement} {self.assetStep}, shot :{self.shotStep} , work place :{self.workPlace} version :{self.version} path : {self.home_pc_path} shot {self.shot_number} props :{self.selected_props}') #
        self.file_path = '\\\\Storage01\\Partages\\3D3_23_24\\Z_ETUDIANTS\\Zapping\\Bura_l_infirmiera\\GRP_02_Bura_L_infirmiera' #'D:\\Carlier_Penelope\\GRP_02_Bura_L_infirmiera'
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
                self.file_path = f'{self.file_path}\\character\\Bura\\maya\\scenes'
                self.file_name = 'bura'

            elif self.selectedAssetElement == 'Chara Boubouche':
                self.file_path = f'{self.file_path}\\character\\Boubouche\\maya\\scenes'
                self.file_name = 'boubouche'

            elif self.selectedAssetElement == 'Props':
                self.file_path = f'{self.file_path}\\prop\\maya\\scenes'
                
                if self.propsList.currentText() != 'None':
                    
                    if self.propsList.currentText() == ('Autre que la liste'):
                        self.file_name = self.propsAutre.text()
                    else :
                        self.file_name = f'{self.selected_props}'

                else :
                    missing_propsName = cmd.window(title = 'Missing Props Name')
                    cmd.window(missing_propsName, edit = True, frontWindow = True, widthHeight = (1000, 200))
                    layout = cmd.columnLayout(adjustableColumn=True)
                    cmd.text('\nIl faut choisir un des props')
                    cmd.showWindow(missing_propsName)
                                        


            elif self.selectedAssetElement == 'Set':
                self.file_path = f'{self.file_path}\\set\\maya\\scenes'
                self.file_name = 'set'

            else :
                missing_assetName = cmd.window(title = 'Missing Asset Name')
                cmd.window(missing_assetName, edit = True, frontWindow = True, widthHeight = (1000, 200))
                layout = cmd.columnLayout(adjustableColumn=True)
                cmd.text('\nIl faut choisir un asset')
                cmd.showWindow(missing_assetName)   
                          




            if self.version == 'Edit':
                self.file_path = f'{self.file_path}\\edit'

                if self.assetStep == 'Modé Layout':
                    self.file_path = f'{self.file_path}\\geo'
                    self.file_name = f'{self.file_name}_geo_layout_E'

                elif self.assetStep == 'Modé Finale':
                    self.file_path = f'{self.file_path}\\geo'
                    self.file_name = f'{self.file_name}_geo_finale_E'

                elif self.assetStep == 'Rigg Layout':
                    self.file_path = f'{self.file_path}\\rig'
                    self.file_name = f'{self.file_name}_rigg_layout_E'

                elif self.assetStep == 'Rigg Final':
                    self.file_path = f'{self.file_path}\\rig'
                    self.file_name = f'{self.file_name}_rigg_final_E'

                elif self.assetStep == 'Lookdev':
                    self.file_path = f'{self.file_path}\\lookdev'
                    self.file_name = f'{self.file_name}_lookdev_E'

                elif self.assetStep == 'Lighting':
                    self.file_path = f'{self.file_path}\\lookdev'
                    self.file_name = f'{self.file_name}_lighting_E'

                else :
                    missing_step = cmd.window(title = 'Missing Step')
                    cmd.window(missing_step, edit = True, frontWindow = True, widthHeight = (1000, 200))
                    layout = cmd.columnLayout(adjustableColumn=True)
                    cmd.text('\nIl faut choisir une étape de travail')
                    cmd.showWindow(missing_step)
                    


                #incrémenter les versions
                self.list_increments = []
                for increment in range (1,10) :
                    if not os.path.exists(f'{self.file_path}\\{self.file_name}_v0{increment}.ma') :
                        self.list_increments.append(f'0{increment}')

                if self.list_increments == []:   
                    for increment in range (10,100):
                        if not os.path.exists(f'{self.file_path}\\{self.file_name}_v{increment}.ma') :
                            self.list_increments.append(increment)
                    
                self.smallest_increment = min(self.list_increments)
                self.file_save_name = f'{self.file_name}_v{self.smallest_increment}.ma'

            # save publish :
            elif  self.version == 'Publish':
                self.file_path = f'{self.file_path}\\publish'

                if self.assetStep == 'Modé Layout':
                    self.file_name = f'{self.file_name}_geo_layout_P'

                elif self.assetStep == 'Modé Finale':
                    self.file_name = f'{self.file_name}_geo_finale_P'

                elif self.assetStep == 'Rigg Layout':
                    self.file_name = f'{self.file_name}_rigg_layout_P'

                elif self.assetStep == 'Rigg Final':
                    self.file_name = f'{self.file_name}_rigg_final_P'

                elif self.assetStep == 'Lookdev':
                    self.file_name = f'{self.file_name}_lookdev_P'

                elif self.assetStep == 'Lighting':
                    self.file_name = f'{self.file_name}_lighting_P'

                #print (f'Dans save publish le fichier se nommera : {self.file_name}')

                self.publish_file_path = f'{self.file_path}\\{self.file_name}.ma' # fichier Publish enregistré à la racine du dossier publish
                print (self.publish_file_path)

                if os.path.exists(self.publish_file_path):  #s'il y a déjà un fichier publish à la racine :
                    print(f'il y a deja un fichier publish, son chemin est : \n{self.publish_file_path}')
                    self.list_increments = []

                    if not os.path.exists(f'{self.file_path}\\backup'):
                        os.makedirs(f'{self.file_path}\\backup')

                    for increment in range (1,10) :
                        if not os.path.exists(f'{self.file_path}\\backup\\{self.file_name}_v0{increment}.ma') :
                            self.list_increments.append(f'0{increment}')

                    if self.list_increments ==[]:
                        for increment in range (10,100):
                            if not os.path.exists(f'{self.file_path}\\backup\\{self.file_name}_v{increment}.ma') :
                                self.list_increments.append(increment)

                    self.smallest_increment = min(self.list_increments)
                    
                    os.rename(self.publish_file_path, f'{self.file_path}\\{self.file_name}_v{self.smallest_increment}.ma')
                    shutil.move(f'{self.file_path}\\{self.file_name}_v{self.smallest_increment}.ma', f'{self.file_path}\\backup')
                    
                    self.file_save_name = f'{self.file_name}.ma'

                    print(f'{self.file_save_name}')

    
                else : #s'il n'y a pas de fichier publish à la racine :
                    print(f'il n\'y a pas de fichier publish au chemin : \n{self.publish_file_path}')
                    self.file_save_name = f'{self.file_name}.ma'
            
            #ni edit ni publish cochés :
            else : 
                missing_version = cmd.window(title = 'Missing Version')
                cmd.window(missing_version, edit = True, frontWindow = True, widthHeight = (1000, 200))
                layout = cmd.columnLayout(adjustableColumn=True)
                cmd.text('\nIl faut choisir entre Edit et Publish')
                cmd.showWindow(missing_version)
                

        #SHOTS :
        elif self.projectType == 'Shot':
            
            if str(self.shotNumber.value()) != '2' and str(self.shotNumber.value()) != '3':
                self.shot_number = '1'
                
            self.file_path = f'{self.file_path}\\05_shot\\sq001_sh0{self.shot_number}0\\maya\\scenes'
            self.file_name = f'sq001_sh0{self.shot_number}0'



            if self.shotStep == 'Layout':
                self.file_path = f'{self.file_path}\\layout'
                self.file_name = f'{self.file_name}_anim_layout'

            elif self.shotStep == 'Blocking' :
                self.file_path = f'{self.file_path}\\anim'
                self.file_name = f'{self.file_name}_anim_BLK'

            elif self.shotStep =='Primary' :
                self.file_path = f'{self.file_path}\\anim'
                self.file_name = f'{self.file_name}_anim_PRM'

            elif self.shotStep =='Secondary':
                self.file_path = f'{self.file_path}\\anim'
                self.file_name = f'{self.file_name}_anim_SEC'

            elif self.shotStep =='Lighting':
                self.file_path = f'{self.file_path}\\render'
                self.file_name = f'{self.file_name}_lighting'

            elif self.shotStep =='Rendu':
                self.file_path = f'{self.file_path}\\render'
                self.file_name = f'{self.file_name}_render'

            else : 
                missing_version = cmd.window(title = 'Missing Step')
                cmd.window(missing_version, edit = True, frontWindow = True, widthHeight = (1000, 200))
                layout = cmd.columnLayout(adjustableColumn=True)
                cmd.text('\nIl faut choisir une etape pour le shot')
                cmd.showWindow(missing_version)


            if self.version == 'Edit':
                self.file_path = f'{self.file_path}\\edit'

                #incrémenter les versions
                self.list_increments = []
                for increment in range (1,10) :
                    if not os.path.exists(f'{self.file_path}\\{self.file_name}_E_v0{increment}.ma') :
                        self.list_increments.append(f'0{increment}')
    
                if self.list_increments == []:   
                    for increment in range (10,100):
                        if not os.path.exists(f'{self.file_path}\\{self.file_name}_E_v{increment}.ma') :
                            self.list_increments.append(increment)
                    
                self.smallest_increment = min(self.list_increments)
                self.file_save_name = f'{self.file_name}_E_v{self.smallest_increment}.ma'
    
            elif self.version == 'Publish':
                self.file_path = f'{self.file_path}\\publish'

                self.publish_file_path = f'{self.file_path}\\{self.file_name}_P.ma' # fichier Publish enregistré à la racine du dossier publish
                print (self.publish_file_path)

                if os.path.exists(self.publish_file_path):  #s'il y a déjà un fichier publish à la racine :
                    print(f'il y a deja un fichier publish, son chemin est : \n{self.publish_file_path}')
                    self.list_increments = []

                    if not os.path.exists(f'{self.file_path}\\backup'):
                        os.makedirs(f'{self.file_path}\\backup')

                    for increment in range (1,10) :
                        if not os.path.exists(f'{self.file_path}\\backup\\{self.file_name}_P_v0{increment}.ma') :
                            self.list_increments.append(f'0{increment}')

                    if self.list_increments ==[]:
                        for increment in range (10,100):
                            if not os.path.exists(f'{self.file_path}\\backup\\{self.file_name}_P_v{increment}.ma') :
                                self.list_increments.append(increment)

                    self.smallest_increment = min(self.list_increments)
                    
                    os.rename(self.publish_file_path, f'{self.file_path}\\{self.file_name}_P_v{self.smallest_increment}.ma')
                    shutil.move(f'{self.file_path}\\{self.file_name}_P_v{self.smallest_increment}.ma', f'{self.file_path}\\backup')
                    
                    self.file_save_name = f'{self.file_name}_P.ma'

                    print(f'{self.file_save_name}')

    
                else : #s'il n'y a pas de fichier publish à la racine :
                    print(f'il n\'y a pas de fichier publish au chemin : \n{self.publish_file_path}')
                    self.file_save_name = f'{self.file_name}_P.ma'




            else :
                missing_version = cmd.window(title = 'Missing Version')
                cmd.window(missing_version, edit = True, frontWindow = True, widthHeight = (1000, 200))
                layout = cmd.columnLayout(adjustableColumn=True)
                cmd.text('\nIl faut choisir entre Edit et Publish')
                cmd.showWindow(missing_version)

        #RIEN COCHé
        else :
            missing_project_type = cmd.window(title = 'Missing Project Type')
            cmd.window(missing_project_type, edit = True, frontWindow = True, widthHeight = (1000, 200))
            layout = cmd.columnLayout(adjustableColumn=True)
            cmd.text('\nIl faut choisir entre Asset et Shot')
            cmd.showWindow(missing_project_type)
                        


    #CREATE FILE
        print(f'{self.file_path}\\{self.file_save_name}')

        if self.file_path != '' and self.file_save_name != '':
            if not os.path.exists(self.file_path):
                os.makedirs(self.file_path)
            else :
                print('il existe déjà!')
            
    
            cmd.file(rename = f'{self.file_path}\\{self.file_save_name}')
            cmd.file(save = True, type = 'mayaAscii')
        

            wellSaved = cmd.window(title = 'Well Saved')
            cmd.window(wellSaved, edit = True, frontWindow = True, widthHeight = (300, 200))
            layout = cmd.columnLayout(adjustableColumn=True)
            cmd.text('\n\n\nFichier Sauvegardé! ;)')
            cmd.showWindow(wellSaved)        
        
        self.file_path = '\\\\Storage01\\Partages\\3D3_23_24\\Z_ETUDIANTS\\Zapping\\Bura_l_infirmiera\\GRP_02_Bura_L_infirmiera' #'D:\\Carlier_Penelope\\GRP_02_Bura_L_infirmiera'
        self.file_name = ''
        self.file_save_name = ''

        #print (f'A la fin du script : \nfile_path :{self.file_path} \nfile name : {self.file_name}\nfile save name : {self.file_save_name}')

        






saveFile = SaveFile()
saveFile.show()