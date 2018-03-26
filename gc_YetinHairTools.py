# ----------------------------  gc_YetinHairTools v.0.06 ----------------------
# ----------------------------  by: Gerardo Castellanos -------------------
# ----------------------------  animetria@gmail.com -----------------------


from maya import cmds
from functools import partial

wd=420

# --------------------------------    UI    ----------------------------------

def gcYetinHairTooslWindows():
    if(cmds.window('YetinHairToolWindows',q=True,ex=True)):cmds.deleteUI('YetinHairToolWindows')
    
    cmds.window('YetinHairToolWindows',t=u'gc_YetinHairTools v.0.06', w=wd)
    
    # ------- UPDATE BUTTON 
    cmds.rowColumnLayout('updateDCS_row_ui',p='YetinHairToolWindows',nc=1)
    cmds.button(p='updateDCS_row_ui', l=u'UPDATE', c='YetinHairToolWindows()', w=wd)
    
    cmds.rowColumnLayout('DCS_list_row_ui',p='YetinHairToolWindows',nc=1)	
    dcsSL = cmds.textScrollList('listDCS_scrollList_ui', p='DCS_list_row_ui',po=True,bgc=[0.1, 0.1, 0.1],h=100, ebg=True, ams=True, append=listDCSnodes(), w=wd)
    cmds.textScrollList(dcsSL, e=True, sc=partial(selectDCS, dcsSL)) 	
	
    cmds.button(p='DCS_list_row_ui', l=u'Select Members', c='selectMembersSet()', w=wd)
	
    cmds.rowColumnLayout('createDCS_row_ui',p='YetinHairToolWindows',nc=2)	
    nameTF = cmds.textField("nameTF", p='createDCS_row_ui', tx=u'', w=wd-100)
    cmds.button(p='createDCS_row_ui', l=u'> create', c='createDCS()', w=100)
	
# ---------  UI FOLICLE	
    cmds.frameLayout('Folicle',p='YetinHairToolWindows',cll=True)
	
    # ---- UI Copy from nHair
    #cmds.rowColumnLayout('copy_row_ui',p='Folicle',nc=1)
    #cmds.button(p='copy_row_ui', l=u'Copy values from nHair System', c='testing()', w=wd)
	
	# ---- UI Folicles Behavior
	
	# Sample Density
    cmds.rowColumnLayout('foliclesBehavior_row_ui',p='Folicle',nc=2)
    sampleDensitySlider = cmds.floatSliderGrp('sampleDensity_ui', p='foliclesBehavior_row_ui' ,w=wd-20,f=True,l=u'Sample Density',min=0.001, max=10.0,pre=1,s=.1,v=1.0)
    cmds.button(p='foliclesBehavior_row_ui', l=u'U', c=partial(updateAttr,0,sampleDensitySlider), w=20)

    # ----  UI Override
    cmds.rowColumnLayout('override_row_ui',p='Folicle',nc=6, cs=[[1, 5], [2, 15], [4, 15]])
    
    simmethodOM = cmds.optionMenu( label='Sim Method', w=150)
    cmds.optionMenu(simmethodOM, e=True, changeCommand=partial(simmethod,simmethodOM))

    cmds.menuItem( label='Static' )
    cmds.menuItem( label='Passive' )
    cmds.menuItem( label='Dynamic' )
    
    cmds.button(p='override_row_ui', l=u'override', bgc=[0, 1, 0], c=partial(overrideDyn,True), w=50)
    cmds.button(p='override_row_ui', l=u'override', bgc=[1, 0, 0], c=partial(overrideDyn,False), w=50)
    
    cmds.button(p='override_row_ui', l=u'collide', bgc=[0, 1, 0], c=partial(collide,True), w=50)
    cmds.button(p='override_row_ui', l=u'collide', bgc=[1, 0, 0], c=partial(collide,False), w=50)

    # ----  UI Dynamics
    cmds.rowColumnLayout('Dynamics_row_ui',p='Folicle',nc=3)
	
    dampSlider = cmds.floatSliderGrp('dampSlider_ui', p='Dynamics_row_ui' ,w=wd-40,f=True,l=u'Damp',min=0.001, max=100.0,pre=2,s=.1,v=1.0)
    cmds.button(p='Dynamics_row_ui', l=u'U', c=partial(updateAttr,1,dampSlider), w=20)
    cmds.button(p='Dynamics_row_ui', l=u'H', c=partial(copyAttr,1, dampSlider), w=20, bgc=[1, 1, 0])

	
    stiffnessSlider = cmds.floatSliderGrp('stiffnessSlider_ui', p='Dynamics_row_ui' ,w=wd-40,f=True,l=u'Stiffness',min=0.001, max=1.0,pre=2,s=.1,v=1.0)
    cmds.button(p='Dynamics_row_ui', l=u'U', c=partial(updateAttr,2,stiffnessSlider), w=20)
    cmds.button(p='Dynamics_row_ui', l=u'H', c=partial(copyAttr,2,stiffnessSlider), w=20, bgc=[1, 1, 0])

    curveAttrcSlider = cmds.floatSliderGrp('CurveAttrcSlider_ui', p='Dynamics_row_ui' ,w=wd-40,f=True,l=u'Attraction',min=0.001, max=2.0,pre=2,s=.1,v=0.0)
    cmds.button(p='Dynamics_row_ui', l=u'U', c=partial(updateAttr,3,curveAttrcSlider), w=20)
    cmds.button(p='Dynamics_row_ui', l=u'H', c=partial(copyAttr,3, curveAttrcSlider), w=20, bgc=[1, 1, 0])
	
	
# ---------  UI YETI ATTR

    cmds.frameLayout('YetiAttributes',p='YetinHairToolWindows',cll=True)
    cmds.rowColumnLayout('Yeti_Attibutes_row_ui',p='YetiAttributes',nc=2)

    weightYetiSlider = cmds.floatSliderGrp('weightYetiSlider_ui', p='Yeti_Attibutes_row_ui' ,w=wd-20,f=True,l=u'Weight',min=0, max=1.0,pre=1,s=.1,v=1.0)
    cmds.button(p='Yeti_Attibutes_row_ui', l=u'U', c=partial(updateYetiAttr,0,weightYetiSlider), w=20)	

    innerRadiusSlider = cmds.floatSliderGrp('innerRadiusSlider_ui', p='Yeti_Attibutes_row_ui' ,w=wd-20,f=True,l=u'Inner Radius',min=0, max=10.0,pre=1,s=.1,v=1.0)
    cmds.button(p='Yeti_Attibutes_row_ui', l=u'U', c=partial(updateYetiAttr,1,innerRadiusSlider), w=20)

    outerRadiusSlider = cmds.floatSliderGrp('outerRadiusSlider_ui', p='Yeti_Attibutes_row_ui' ,w=wd-20,f=True,l=u'Outer Radius',min=0, max=10.0,pre=1,s=.1,v=2.0)
    cmds.button(p='Yeti_Attibutes_row_ui', l=u'U', c=partial(updateYetiAttr,2,outerRadiusSlider), w=20)

    baseAttractionSlider = cmds.floatSliderGrp('baseAttractionSlider_ui', p='Yeti_Attibutes_row_ui' ,w=wd-20,f=True,l=u'Base Attraction',min=0, max=1.0,pre=0,s=.1,v=0)
    cmds.button(p='Yeti_Attibutes_row_ui', l=u'U', c=partial(updateYetiAttr,3,baseAttractionSlider), w=20)

    tipAttractionSlider = cmds.floatSliderGrp('tipAttractionSlider_ui', p='Yeti_Attibutes_row_ui' ,w=wd-20,f=True,l=u'Tip Attraction',min=0, max=1.0,pre=0,s=.1,v=0)
    cmds.button(p='Yeti_Attibutes_row_ui', l=u'U', c=partial(updateYetiAttr,4,tipAttractionSlider), w=20)

    cmds.showWindow('YetinHairToolWindows')	

	
# --------------------  Functions -----------------------------------

def listDCSnodes():
    result = cmds.ls('*_DCS',type='objectSet')
    return result
    
def createDCS(*arg):
    name = cmds.textField('nameTF', q=True, text=True)
    if name=='':
        cmds.warning('it needs a name')
        return
    sel = cmds.ls(sl=True)
    sel = cmds.listRelatives(sel, shapes=True)
    if not sel:
        cmds.warning('select curves first')
        return        
    for obj in sel:
        if cmds.objectType(obj)!='nurbsCurve':
            cmds.warning('it only accepts curves')
            return
    cmds.sets(sel, n=name+'_DCS')
    YetinHairToolWindows()

def isRightList():
    list = cmds.ls(sl=True)
    if len(list)==0:
        return False
    for element in list:        
        typeElement = cmds.objectType(element)
        if (typeElement!='objectSet'):
            if typeElement=='transform':
                son = cmds.listRelatives(element, shapes=True)
            else:
                son = [element]                
            sonTypeElement = cmds.objectType(son[0])
            if (sonTypeElement!='nurbsCurve'):
                cmds.warning('wrong selection')
                return False
    return True

def findFolicle(element):
    conectedTo = str(element[0])+'.create'
    folicle =(cmds.listConnections (conectedTo, s=True))
    return folicle
    
def findHairSys(folicle):
    conectedTo = str(folicle[0])+'.currentPosition'
    hairSys = (cmds.listConnections (conectedTo, s=True))
    return hairSys

def listFolicles():
    listFoliclesSel = []
    sel = cmds.ls(sl=True)
    for element in sel:
        typeElement = cmds.objectType(element)
        if (typeElement=='objectSet'):
            listset = cmds.sets(element, q=True)
            print (listset)
            for member in listset:
               print ('member : '+member)
               memberlist = [member]
               listFoliclesSel.append(findFolicle(memberlist))
        else:
           if typeElement=='transform':
                son = cmds.listRelatives(element, shapes=True) 
           else:
                son = [element]   
           listFoliclesSel.append(findFolicle(son))
    return listFoliclesSel 
    
def listCurves():
    listCurves = []
    sel = cmds.ls(sl=True)
    for element in sel:
        typeElement = cmds.objectType(element)
        if (typeElement=='objectSet'):
            listset = cmds.sets(element, q=True)
            print (listset)
            for member in listset:
               memberlist = [member]
               listCurves.append(memberlist)
        else:
           if typeElement=='transform':
                son = cmds.listRelatives(element, shapes=True) 
           else:
                son = [element]   
           listCurves.append(son)
    return listCurves 
    
def selectDCS(scrollList):
    listDCSSelected = cmds.textScrollList(scrollList, q=True, si=True )
    cmds.select(listDCSSelected, r=True)	
    

# ----------------   Folicles Behavior Functions

def simmethod(om, *arg):
    value = cmds.optionMenu(om, q=True, sl=True)
    if isRightList():
        folicles = listFolicles()
        for folicle in folicles:
            cmds.setAttr(folicle[0] + '.simulationMethod',value-1)            
            
def updateAttr(attr, slider, *arg):
    attrList = ['sampleDensity', 'damp', 'stiffness', 'startCurveAttract']
    value = cmds.floatSliderGrp(slider, query=True, v=True)
    if isRightList():
        folicles = listFolicles()
        for folicle in folicles:
            cmds.setAttr(folicle[0] + '.' + attrList[attr],value) 
            
def copyAttr(attr, slider, *arg):
    attrList = ['sampleDensity', 'damp', 'stiffness', 'startCurveAttract']
    if isRightList():
        folicles = listFolicles()
        for folicle in folicles:
            hairSys = findHairSys(folicle)
            value = cmds.getAttr(hairSys[0] + '.' + attrList[attr])
            print (hairSys[0] + '.' + attrList[attr] + '     ' + str(value))
            cmds.setAttr(folicle[0] + '.' + attrList[attr], value)
            #cmds.floatFieldGrp(slider, e=True, v=value)
      
def overrideDyn(value,*arg):
    if isRightList():
        folicles = listFolicles()
        for folicle in folicles:
            cmds.setAttr(folicle[0] + '.overrideDynamics',value)
            
def collide(value,*arg):
    if isRightList():
        folicles = listFolicles()
        for folicle in folicles:
            cmds.setAttr(folicle[0] + '.collide',value)
                   
# ------------------- Yeti Guides Attributes     

def updateYetiAttr(attr, slider, *arg):
    attrList = ['weight', 'innerRadius', 'outerRadius', 'baseAttraction', 'tipAttraction']
    value = cmds.floatSliderGrp(slider, query=True, v=True)
    if isRightList():
        curves = listCurves()
        for curve in curves:
            cmds.setAttr(curve[0] + '.' + attrList[attr],value)       







gcYetinHairTooslWindows()
