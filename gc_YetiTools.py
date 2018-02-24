# ----------------------------  cg_YetiTools  v.0.13 ----------------------
# ----------------------------  by: Gerardo Castellanos -------------------
# ----------------------------  animetria@gmail.com -----------------------


from maya import cmds
from functools import partial

listGroomsSelected = cmds.ls(type="pgYetiGroom")
listYetiSelected = cmds.ls(type="pgYetiMaya")


# ---------------------------------------------   UI -----------------------------------------------------------------------------



def gcYetiToolsWindows():
	if(cmds.window('gcYetiTools_ui',q=True,ex=True)):cmds.deleteUI('gcYetiTools_ui')
	cmds.window('gcYetiTools_ui',t=u'gc_YetiTools v0.13',s=True,mnb=False,mxb=False,mbv=True,wh=(300, 300),vis=True,rtf=True)
	#cmds.columnLayout(adj=True,cal=u'center')

# SELECTION UI
	cmds.frameLayout('selection',p='gcYetiTools_ui',po=True,l=u'Selection',fn=u'boldLabelFont')
	#cmds.checkBox(l=u'only connected',v=True)
	cmds.button(p='selection', l=u'UPDATE', c='gcYetiToolsWindows()')	
	
	cmds.rowColumnLayout('rowSel', p='selection',en=True,ann=u'yetigroom', nc=2)	
	
	
	
	cmds.rowColumnLayout("selectObj", p='selection',nc=5, cw=[[1, 60], [2, 60], [3, 60], [4, 270], [5, 60]])
	cmds.button(p='selectObj', l=u'Groom >', c='objFromGroom(listGroomsSelected)')
	cmds.button(p='selectObj', l=u'Proxy >', c='defineProxy()')	
	cmds.button(p='selectObj', l=u'Sel >', c='defineObj()')	
	objTF = cmds.textField("objTF", p='selectObj', tx=u'', w=300)
	cmds.button(p='selectObj',l=u'> Sel', c='selObj()', w=30)
	objFromGroom(listGroomNodes())	
	
	
#  MESH CONECCTIONS UI
	
	cmds.frameLayout('Objects',p='gcYetiTools_ui', cll=True,l=u'Mesh Connections',w=520)
	
	cmds.rowColumnLayout('yeticonnection', p='Objects', en=True, nc=2, cw=[[1, 260],[2, 260]])
	
	#disconnect
	cmds.button(l=u'yeti disconnect', w=200, c='disconnectYeti(objCurrent(), listYetiSelected)')	
	cmds.button(l=u'groom disconnect', w=200, c='disconnectGroom(objCurrent(), listGroomsSelected)')	
	#connect    
	cmds.button(l=u'yeti connect', w=200, c='connectYeti(objCurrent(), listYetiSelected)')
	cmds.button(l=u'groom connect', w=200, c='connectGroom(objCurrent(), listGroomsSelected)')	
	


# YETI TOOLS UI
	
	cmds.frameLayout('Yeti',p='gcYetiTools_ui',cll=True,l=u'Yeti Nodes Functions',w=520)	
	cmds.rowColumnLayout('displatyYetyiRow', p='Yeti', en=True, nc=1, cw=[[1, 520]])
	visYetiCB = cmds.checkBox('visyeti',l=u'Visible',v=False, p='displatyYetyiRow', onc='visyeti(True)', ofc='visyeti(False)')

	cmds.rowColumnLayout('viewYeti', p='Yeti', en=True, nc=1, cw=[[1, 520]])
	
	ViewDensitySliderS = cmds.floatSliderGrp('ViewDensitySlider_ui', p='viewYeti',w=520,f=True,l=u'Viewport Density',min=0.1, max=100.0,pre=1,s=1,v=1.0)
	cmds.floatSliderGrp(ViewDensitySliderS , e=True, dc=partial(ViewDensity, ViewDensitySliderS)) 
	
	ViewWidthSliderS = cmds.floatSliderGrp('ViewWidthSlider_ui', p='viewYeti',w=520,f=True,l=u'Viewport Width',min=0.01, max=10.0,pre=2,s=.1,v=1.0)
	cmds.floatSliderGrp(ViewWidthSliderS , e=True, dc=partial(ViewWidth, ViewWidthSliderS)) 
	
	cmds.rowColumnLayout('colorsPreviewRow', p='Yeti', en=True, nc=12)
	cmds.button(l=u'', p='colorsPreviewRow', w=52, bgc=[1.0, 1.0, 1.0], c='yeticolor([1.0, 1.0, 1.0])')
	cmds.button(l=u'', p='colorsPreviewRow', w=52, bgc=[0, 0, 0], c='yeticolor([0, 0, 0])')
	cmds.button(l=u'', p='colorsPreviewRow', w=52, bgc=[1, 0, 0], c='yeticolor([1, 0, 0])')
	cmds.button(l=u'', p='colorsPreviewRow', w=52, bgc=[0, 1, 0], c='yeticolor([0, 1, 0])')
	cmds.button(l=u'', p='colorsPreviewRow', w=52, bgc=[0, 0, 1], c='yeticolor([0, 0, 1])')
	cmds.button(l=u'', p='colorsPreviewRow', w=52, bgc=[1, 1, 0], c='yeticolor([1, 1, 0])')
	cmds.button(l=u'', p='colorsPreviewRow', w=52, bgc=[1, 0, 1], c='yeticolor([1, 0, 1])')
	cmds.button(l=u'', p='colorsPreviewRow', w=52, bgc=[0, 1, 1], c='yeticolor([0, 1, 1])')
	cmds.button(l=u'', p='colorsPreviewRow', w=52, bgc=[1, .7, 0], c='yeticolor([1, .7, 0])')
	cmds.button(l=u'', p='colorsPreviewRow', w=52, bgc=[.4, .3, .2], c='yeticolor([.4, .3, .2])')



# GROOM TOOLS UI
	
	cmds.frameLayout('Groom',p='gcYetiTools_ui',cll=True,l=u'Groom Nodes Functions',w=520)
	
	cmds.rowColumnLayout('rofRow', p='Groom', en=True, nc=2, cw=[[1, 520]])
	RoIs = cmds.floatSliderGrp('ROIfloatSlider_ui', p='rofRow',w=520,f=True,l=u'Radius Of Influence',max=4.0,pre=2,s=0.01,v=0.0)
	cmds.floatSliderGrp(RoIs, e=True, dc=partial(RoI, RoIs)) 

	cmds.rowColumnLayout('displatyGroomRow', p='Groom', en=True, nc=5, cw=[[1, 104],[2, 104],[3, 104], [4, 104], [5, 104]])
	visGroomCB = cmds.checkBox('visgroom',l=u'Visible',v=False, p='displatyGroomRow', onc='visgroom(True)', ofc='visgroom(False)')
	displaystrandsCB = cmds.checkBox('displaystrands',l=u'Strands',v=False, p='displatyGroomRow', onc='displaystrands(True)', ofc='displaystrands(False)')
	displaySegmentsCB = cmds.checkBox('displaySegments',l=u'Segments',v=False, p='displatyGroomRow', onc='displaySegments(True)', ofc='displaySegments(False)')
	displayattrCB = cmds.checkBox('displayattr',l=u'Attributes',v=False, p='displatyGroomRow', onc='displayattr(True)', ofc='displayattr(False)')
	displayHeatCB = cmds.checkBox('displayHeat',l=u'as Heat Map',v=False, p='displatyGroomRow', onc='displayHeat(True)', ofc='displayHeat(False)')
	
	cmds.rowColumnLayout('groomFunctions', p='Groom', en=True, nc=2, cw=[[1, 260],[2, 260]])
	cmds.button(l=u'Rest Pose', w=200, c='restPose(listGroomsSelected)')
	cmds.button(l=u'Convert to Curves', w=200, c='convertToCurves(listGroomsSelected)')
	cmds.button(l=u'Delete default attributes', w=200, c='deleteDA(listGroomsSelected)')
	

# Scroll List of Yeti & Grooms Nodes	

	yetiSL = cmds.textScrollList('listYeti', p='rowSel', po=True,bgc=[0.1, 0.1, 0.1],ebg=True, ams=True, append=listYetiNodes())
	cmds.textScrollList(yetiSL, e=True, sc=partial(selectNodeYeti, yetiSL, visYetiCB) )
	
	groomSL = cmds.textScrollList('listGroom', p='rowSel', po=True,bgc=[0.1, 0.1, 0.1],ebg=True, ams=True, append=listGroomNodes())
	cmds.textScrollList(groomSL, e=True, sc=partial(selectNodeGroom, groomSL, visGroomCB, displaystrandsCB, displaySegmentsCB, displayattrCB, displayHeatCB)) 

	
# UPDATE CHARACTER UI
	
	cmds.frameLayout('Update',p='gcYetiTools_ui',cll=True,l=u'Update Character',w=520)
	#cmds.text(l=u'Make sure your character reference is unlocked',ww=False, p='steps')
	
	cmds.rowColumnLayout('UpdateInfo', p='Update', en=True, nc=1, cw=[[1, 520]])
	
	cmds.text(l=u'be sure your character reference is unlocked \n select all yeti and grooms nodes :',ww=False, p='UpdateInfo')
	
	
	cmds.rowColumnLayout('steps', p='Update', en=True, nc=2, cw=[[1, 160],[2, 360]])
	
	cmds.text(l=u'step 1 :',ww=False, p='steps')
	cmds.button(p='steps', l=u'create Proxy Groom Object', c='createProxyGroomObject()')	
	cmds.text(l=u'step 2 :',ww=False, p='steps')		
	cmds.text(l=u'Update your model/reference, unlock it \n select your new mesh \n select yeti & grooms nodes',ww=False, p='steps')	
	cmds.text(l=u'step 3 :',ww=False, p='steps')
	cmds.button(p='steps', l=u'adapt proxy', c='createBS()')	
	cmds.text(l=u'step 4 :',ww=False, p='steps')
	cmds.button(p='steps', l=u'attach fur', c='installYeti()')	
	
	
# UPDATE MODEL	
	cmds.frameLayout('Object',p='gcYetiTools_ui',cll=True,l=u'Object',w=520)
	
	cmds.rowColumnLayout('TextRefObj', p='Object', en=True, nc=2, cw=[[1, 260],[2, 260]])
	
	cmds.button(p='TextRefObj', l=u'create Texture Ref Obj', c='createTRO(objCurrent())')
	cmds.button(p='TextRefObj', l=u'delete Texture Ref Obj', c='deleteTRO(objCurrent())')		
	

# ------------------------------------------------  FUNCTIONS ------------------------------------------------------------------

  
	
# ------------------------   SELECTIONS FUNCTIONS

# list of all yeti nodes 
def listYetiNodes():
    listResult=[]
    list = cmds.ls(type="pgYetiMaya")
    for yetin in list:
            listResult.append(cmds.listRelatives(yetin, parent=True, ni=1)[0])
    listResult.sort()
    return listResult
            
# list of all groom nodes            
def listGroomNodes():
    listResult=[]
    list = cmds.ls(type="pgYetiGroom")
    for groomn in list:
            listResult.append(cmds.listRelatives(groomn, parent=True, ni=1)[0])
    return listResult
            
# select the groom or yetis from the scrool list            
def selectNodeYeti(this_textScrollList, visCB):
    global listYetiSelected
    res = cmds.textScrollList( this_textScrollList, q=True, si=True )
    listYetiSelected = res
    listYetiSelected.sort()
    vis = cmds.getAttr (listYetiSelected[0]+'.visibility')
    cmds.checkBox(visCB, e=True, v=vis)
    cmds.select(res)
    
def selectNodeGroom(this_textScrollList, visCB, displaystrandsCB, displaySegmentsCB, displayattrCB, displayHeatCB):
    global listGroomsSelected
    res = cmds.textScrollList( this_textScrollList, q=True, si=True )
    listGroomsSelected = res
    listYetiSelected.sort()
    vis = cmds.getAttr (listGroomsSelected[0]+'.visibility')
    cmds.checkBox(visCB, e=True, v=vis)
    DS = cmds.getAttr (listGroomsSelected[0]+'.displayStrands')
    cmds.checkBox(displaystrandsCB, e=True, v=DS)
    DSg = cmds.getAttr (listGroomsSelected[0]+'.displayStrandSegments')
    cmds.checkBox(displaySegmentsCB, e=True, v=DSg)
    DA = cmds.getAttr (listGroomsSelected[0]+'.displayPaintValue')
    cmds.checkBox(displayattrCB, e=True, v=DA)
    DH = cmds.getAttr (listGroomsSelected[0]+'.displayPaintValueAsHeatMap')
    cmds.checkBox(displayHeatCB, e=True, v=DH)

    cmds.select(res)    

# return the name of current object (from field object)    
def objCurrent():
    return (cmds.textField("objTF", q=True, text=True))
    
    
    
# Select an object from Groom list    
def objFromGroom(listGroomsSelected):
    objSelected = objCurrent()
    if (len(listGroomsSelected)>0):
        groom = str(listGroomNodes()[0])+'Shape.inputGeometry'
        objT=(cmds.listConnections (groom, s=True))
        if (objT):
            obj= cmds.listRelatives (objT[0])
            cmds.textField("objTF", edit=True, text=obj[0])
            objSelected = obj[0]

# Select the Proxy as Object
def defineProxy():
    proxy=cmds.ls('ProxyGroomShape')
    if (proxy):
        cmds.textField("objTF", edit=True, text=proxy[0])
    else:
        cmds.warning('There is not Proxy in the scene')
           

# select the geometry	
def defineObj(*args):
    global objSelected
    listSel = cmds.ls(sl=True)
    if listSel is None:
         cmds.warning('Please select an object')
    if len(listSel)==1:
        if cmds.objectType(listSel[0]) == 'transform':
            listSel = cmds.listRelatives (listSel[0])
        if cmds.objectType(listSel[0]) == 'mesh' :
            cmds.textField("objTF", edit=True, text=listSel[0])
            objSelected = listSel[0]
        else:
            cmds.warning('Select a right object')
        
    else: 
         cmds.warning('Select only one object') 
         
# select mesh
def selObj(*args):
    objSel = cmds.textField("objTF", q=True, text=True)
    if objSel:
        objT = cmds.listRelatives(objSel, p=True)
        cmds.select(objT)
    else:
        cmds.warning('No object to select')


# ------------------------   MESH CONNECTIONS FUNCTIONS
        
def connectYeti(obj, listYetiSelected):
    print (listYetiSelected)
    for yeti in listYetiSelected:
        mel.eval('pgYetiAddGeometry("' + str(obj) +'", "'+ str(yeti) + '")')
        
def disconnectYeti(obj,listYetiSelected):
    
    for yeti in listYetiSelected:
        mel.eval('pgYetiRemoveGeometry("' + str(obj) +'", "'+ str(yeti) + 'Shape")') 
        
def connectGroom(obj, listGroomsSelected):
    for groom in listGroomsSelected:
        objMesh = str(obj)+'.worldMesh[0]'
        groomIG = str(groom)+'.inputGeometry'
        cmds.connectAttr(objMesh, groomIG, f=True)
        
def disconnectGroom(obj, listGroomsSelected):
    for groom in listGroomsSelected:
        objMesh = str(obj)+'.worldMesh[0]'
        groomIG = str(groom)+'.inputGeometry'
        cmds.disconnectAttr(objMesh, groomIG)



# ------------------------   YETI FUNCTIONS


def visyeti(check):
    global listYetiSelected
    for yeti in listYetiSelected:
        if check:
            cmds.setAttr(yeti +'.visibility', 1)
        else:
            cmds.setAttr(yeti +'.visibility', 0)
            
def ViewDensity(slider, arg):
    global listYetiSelected
    val = cmds.floatSliderGrp(slider, q=True, v=True)
    for yeti in listYetiSelected:
        cmds.setAttr(yeti +'.viewportDensity', val)

def ViewWidth(slider, arg):
    global listYetiSelected
    val = cmds.floatSliderGrp(slider, q=True, v=True)
    for yeti in listYetiSelected:
        cmds.setAttr(yeti +'.viewportWidth', val)
   
      
def yeticolor(color):
    global listYetiSelected
    for yeti in listYetiSelected:
        cmds.setAttr(yeti + '.color', color[0],color[1],color[2], type='double3')
        print (color)
  


# ------------------------   GROOMS FUNCTIONS

def RoI(slider, arg):
    global listGroomsSelected
    val = cmds.floatSliderGrp(slider, q=True, v=True)
    for groom in listGroomsSelected:
        cmds.setAttr(groom +'.radiusOfInfluence', val)

def visgroom(check):
    global listGroomsSelected
    for groom in listGroomsSelected:
        if check:
            cmds.setAttr(groom +'.visibility', 1)
        else:
            cmds.setAttr(groom +'.visibility', 0)     

def displaystrands(check):
    global listGroomsSelected
    for groom in listGroomsSelected:
        if check:
            cmds.setAttr(groom +'.displayStrands', 1)
        else:
            cmds.setAttr(groom +'.displayStrands', 0)    

def displaySegments(check):
    global listGroomsSelected
    for groom in listGroomsSelected:
        if check:
            cmds.setAttr(groom +'.displayStrandSegments', 1)
        else:
            cmds.setAttr(groom +'.displayStrandSegments', 0)       

def displayattr(check):
    global listGroomsSelected
    for groom in listGroomsSelected:
        if check:
            cmds.setAttr(groom +'.displayPaintValue', 1)
        else:
            cmds.setAttr(groom +'.displayPaintValue', 0)       

def displayHeat(check):
    global listGroomsSelected
    for groom in listGroomsSelected:
        if check:
            cmds.setAttr(groom +'.displayPaintValueAsHeatMap', 1)
        else:
            cmds.setAttr(groom +'.displayPaintValueAsHeatMap', 0)       

def restPose(listGroomsSelected):
    if listGroomsSelected:
        for groom in listGroomsSelected:
            cmds.select(groom)            
            mel.eval ('pgYetiSaveGroomRestPoseOnSelected;');
        cmds.select(listGroomsSelected)

def convertToCurves(listGroomsSelected):
    if listGroomsSelected:
        for groom in listGroomsSelected:
            curvesg=[]
            cmds.select(groom)
            mel.eval('pgYetiConvertGroomToCurves;')
            curvesg = cmds.ls(str(groom)+'Shape*', type='transform')
            cmds.group (curvesg, n=str(groom)+'Curves_GRP')
            
            
def deleteDA(listGroomsSelected):
    attList = ['lengthWeight','innerRadius', 'outerRadius', 'attractionBias', 'randomAttraction', 'weight', 'baseAttraction', 'twist','density','surfaceDirectionLimit','staticLength','surfaceDirectionLimitFalloff','tipAttraction']
    if listGroomsSelected:
        for groom in listGroomsSelected:
            for att in attList:
                groomS = cmds.listRelatives(groom, s=True)
                cmds.select(groomS)
                mel.eval('pgYetiCommand -removeAttribute "' + att +'"')
    else:
        cmds.warning(' Please, select a groom first ')
        
        
        
            
# ------------------------   UPDATE CHARACTER FUNCTIONS

# UI step 1
def createProxyGroomObject(*arg):
    # create a proxy from mesh
    global listGroomsSelected, listYetiSelected
    obj=cmds.listRelatives(objCurrent(), p=True)
    cmds.duplicate(obj[0], n='ProxyGroom')
    cmds.parent('ProxyGroom', w=True)
    cmds.select('ProxyGroom')    

    # disconnect yeti & groom from model
    disconnectYeti(objCurrent(), listYetiNodes())
    #disconnectGroom()
    
    # reset pose to groom
    restPose(listGroomNodes())       
    
    # connect yeti & groom to  Proxy 
    proxy = cmds.ls('ProxyGroom')[0]
    connectGroom(proxy, listGroomNodes())
    
    # screate texture reference object (TRO) from Proxy
    cmds.select('ProxyGroom')
    cmds.CreateTextureReferenceObject()
    disconnectYeti('ProxyGroomShape_reference', listYetiNodes())
    
# UI step 2
    # do it manually
    
    
# UI step 3       
def createBS():
    # create blendshapes from update to proxy and active it
    print (str(objSelected))
    blendShapeProxy = cmds.blendShape(str(objSelected), 'ProxyGroom', n='blendShapeProxy')
    cmds.setAttr('blendShapeProxy.' + str(objSelected), 1)
  
   
# UI step 4

def installYeti(): 
    #disconnect yeti and grooms from proxy
    disconnectYeti('ProxyGroomShape', listYetiNodes()) 
    disconnectGroom("ProxyGroomShape", listGroomNodes())
  
    #reset pose to groom 
    restPose(listGroomsSelected)
    
    #delete proxy and TRO
    cmds.delete( 'ProxyGroom_reference')
    cmds.delete ('ProxyGroom')
       
    #connect yeti & groom to update
    print ('go to connect yetis')
    connectYeti(objCurrent(),listYetiNodes())
    print ('go to connect grooms')
    connectGroom(objCurrent(), listGroomNodes())

       
# Create a Texture Reference Object
def createTRO(obj):
    #print (cmds.objExists(str(obj)+'_reference'))

    if obj and not(cmds.objExists(str(obj)+'_reference')):
        objT=cmds.listRelatives(obj, p=True)
        cmds.select(objT)
        cmds.CreateTextureReferenceObject()
    else:
        cmds.warning ('there is not an object selected or there is a texture reference object already')
   

# Delete a TRO
def deleteTRO(obj):
    objT=cmds.listRelatives(obj, p=True)
    print ((str(objT)+'_reference'))
    if obj and (cmds.objExists(str(objT[0])+'_reference')) :
        cmds.delete(str(objT[0])+'_reference') 
        
gcYetiToolsWindows()