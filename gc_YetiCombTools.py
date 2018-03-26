# ------------------------------------   gc_YetiCombTools_0.05 ----------------------------
# -------------------------------  Gerardo Castellanos - animetria@gmail.com -------------


from maya import cmds
from functools import partial

iconpath = '/repository/software/install/maya/2016/centos-6_x86-64/icons/'

listGroomSelected = []

def gcYetiCombToolsWindows():
	if(cmds.window('YetiCombToolsWindow',q=True,ex=True)):cmds.deleteUI('YetiCombToolsWindow')
	cmds.window('YetiCombToolsWindow',t=u'gc_YetiCombTools_v0.05',iconName=u'hairConstraint.svg', w=400)
	
	
# UI list grooms	
	
	cmds.rowColumnLayout('listGroom_ui',p='YetiCombToolsWindow',nc=1)
	cmds.button(p='listGroom_ui', l=u'UPDATE', c='gcYetiCombToolsWindows()')
	groomSL = cmds.textScrollList('listGroom', p='listGroom_ui',po=True,bgc=[0.1, 0.1, 0.1],h=100, ebg=True, ams=False, append=listGroomNodesG())
	

# UI combs icons
	cmds.rowColumnLayout('brush_row_ui',p='YetiCombToolsWindow',nc=12)
	cmds.iconTextButton('comb_ui', image1= iconpath + 'pgYeti_comb.png', c='selectBrush("0 0")')
	cmds.iconTextButton('direction_ui', image1=iconpath + 'pgYeti_direction.png', c='selectBrush("0 1")')
	cmds.iconTextButton('straighten_ui', image1=iconpath + 'pgYeti_straighten.png', c='selectBrush("0 2")')
	cmds.iconTextButton('smooth_ui', image1=iconpath + 'pgYeti_smooth.png', c='selectBrush("0 3")')
	cmds.iconTextButton('lift_ui', image1=iconpath + 'pgYeti_lift.png', c='selectBrush("0 4")')
	cmds.iconTextButton('move_ui', image1=iconpath + 'pgYeti_move.png', c='selectBrush("0 5")')
	cmds.iconTextButton('scale_ui', image1=iconpath + 'pgYeti_scale.png', c='selectBrush("0 6")')
	cmds.iconTextButton('clumping_ui', image1=iconpath + 'pgYeti_clumping.png', c='selectBrush("0 7")')
	cmds.iconTextButton('twist_ui', image1=iconpath + 'pgYeti_twist.png', c='selectBrush("0 8")')
	cmds.iconTextButton('tangent_ui', image1=iconpath + 'pgYeti_tangent.png', c='selectBrush("0 9")')
	cmds.iconTextButton('sculpt_ui', image1=iconpath + 'pgYeti_sculpt.png', c='selectBrush("3 0")')
	cmds.iconTextButton('trim_ui', image1=iconpath + 'pgYeti_trim.png', c='selectBrush("3 1")')
	
	
# UI Presets
	cmds.rowColumnLayout('presetsStrenght_row_ui',p='YetiCombToolsWindow',nc=8)
	cmds.button('strength_1_button_ui',w=50,l=u'-1', bgc=[0.76, 0.52, 0.52], c='setStrength(-1)')
	cmds.button('strength_2_button_ui',w=50,l=u'-0.5', bgc=[0.76, 0.52, 0.52], c='setStrength(-.5)')
	cmds.button('strength_3_button_ui',w=50,l=u'-0.2', bgc=[0.76, 0.52, 0.52], c='setStrength(-.2)')
	cmds.button('strength_4_button_ui',w=50,l=u'-0.1', bgc=[0.76, 0.52, 0.52], c='setStrength(-.1)')
	cmds.button('strength_5_button_ui',w=50,l=u'0.1',bgc=[0.34, 0.62, 0.34], c='setStrength(.1)')
	cmds.button('strength_6_button_ui',w=50,l=u'0.2',bgc=[0.34, 0.62, 0.34], c='setStrength(.2)')
	cmds.button('strength_7_button_ui',w=50,l=u'0.5',bgc=[0.34, 0.62, 0.34], c='setStrength(.5)')
	cmds.button('strength_8_button_ui',w=50,l=u'1',bgc=[0.34, 0.62, 0.34], c='setStrength(1)')
	
	cmds.rowColumnLayout('presetsStrenghtS_row_ui',p='YetiCombToolsWindow',nc=8)
	cmds.button('strengthS_1_button_ui',w=50,l=u'<<<<', bgc=[0.76, 0.52, 0.52], c='setScale(.5)')
	cmds.button('strengthS_2_button_ui',w=50,l=u'<<<', bgc=[0.76, 0.52, 0.52], c='setScale(.9)')
	cmds.button('strengthS_3_button_ui',w=50,l=u'<<', bgc=[0.76, 0.52, 0.52], c='setScale(.95)')
	cmds.button('strengthS_4_button_ui',w=50,l=u'<', bgc=[0.76, 0.52, 0.52], c='setScale(.99)')
	cmds.button('strengthS_5_button_ui',w=50,l=u'>',bgc=[0.34, 0.62, 0.34], c='setScale(1.01)')
	cmds.button('strengthS_6_button_ui',w=50,l=u'>>',bgc=[0.34, 0.62, 0.34], c='setScale(1.05)')
	cmds.button('strengthS_7_button_ui',w=50,l=u'>>>',bgc=[0.34, 0.62, 0.34], c='setScale(1.1)')
	cmds.button('strengthS_8_button_ui',w=50,l=u'>>>>',bgc=[0.34, 0.62, 0.34], c='setScale(1.5)')
	
	cmds.rowColumnLayout('presetsFalloffs_row_ui',p='YetiCombToolsWindow',nc=8)
	cmds.button('Falloffs_1_button_ui',w=50,l=u'root', bgc=[0.34, 0.56, 0.62], c='setFalloffPower(0.001)')
	cmds.button('Falloffs_2_button_ui',w=50,l=u'0.5', bgc=[0.36, 0.58, 0.64], c='setFalloffPower(0.5)')
	cmds.button('Falloffs_3_button_ui',w=50,l=u'1', bgc=[0.38, 0.60, 0.66], c='setFalloffPower(1)')
	cmds.button('Falloffs_4_button_ui',w=50,l=u'1.5', bgc=[0.40, 0.62, 0.68], c='setFalloffPower(1.5)')
	cmds.button('Falloffs_5_button_ui',w=50,l=u'2',bgc=[0.42, 0.64, 0.70], c='setFalloffPower(2)')
	cmds.button('Falloffs_6_button_ui',w=50,l=u'3',bgc=[0.44, 0.66, 0.72], c='setFalloffPower(3)')
	cmds.button('Falloffs_7_button_ui',w=50,l=u'4',bgc=[0.46, 0.68, 0.74], c='setFalloffPower(4)')
	cmds.button('Falloffs_8_button_ui',w=50,l=u'tip',bgc=[0.48, 0.70, 0.76], c='setFalloffPower(5)')

# UI Fills and Mirror
	cmds.rowColumnLayout('fill_ui',p='YetiCombToolsWindow',nc=2)
	mirrorCB = cmds.checkBox('mirrorBC_ui',l=u'Mirror',v=False, p='fill_ui', onc='mirror(True)', ofc='mirror(False)',w=100)
	cmds.button(p='fill_ui', l=u'FILL', w=300, bgc=[1,0.5,0.5], c='fill()')
	
	cmds.textScrollList(groomSL, e=True, sc=partial(selectGroomNode, groomSL, mirrorCB)) 
	
	cmds.rowColumnLayout('separator_row_ui',p='YetiCombToolsWindow',nc=1)	
	cmds.separator('separator1_ui',p='separator_row_ui',w=400,bgc=[0.0, 1.0, 0.0],ebg=False,st=u'double')
	
	
# UI Scatter	
	
	cmds.rowColumnLayout('scatter_row_ui',p='YetiCombToolsWindow',nc=12)	
	cmds.iconTextButton('add_ui', p='scatter_row_ui', image1= iconpath + 'pgYeti_add.png', c='selectBrush("2 0")')
	cmds.iconTextButton('delete_ui', p='scatter_row_ui', image1= iconpath + 'pgYeti_delete.png', c='selectBrush("2 1")')
	cmds.iconTextButton('scatter_ui', p='scatter_row_ui', image1= iconpath + 'pgYeti_scatter.png', c='selectBrush("2 2")')
	cmds.separator('separator1_ui',p='scatter_row_ui',w=20, ebg=False, st=u'none')
	cmds.iconTextButton('deselect_ui', p='scatter_row_ui', image1= iconpath + 'pgYeti_deselect.png', c='deselectStrands()')
	cmds.iconTextButton('invert_ui', p='scatter_row_ui', image1= iconpath + 'pgYeti_convert.png', c='invertStrands()')
	cmds.separator('separator2_ui',p='scatter_row_ui',w=40, ebg=False, st=u'none')
	cmds.iconTextButton('undo_ui', p='scatter_row_ui', image1= iconpath + 'pgYeti_undo.png', c='undoComb()')
	cmds.iconTextButton('redo_ui', p='scatter_row_ui', image1= iconpath + 'pgYeti_redo.png', c='redoComb()')
	
	cmds.rowColumnLayout('scatterSliders_row_ui',p='YetiCombToolsWindow',nc=1)	
	
	minDistSlider = cmds.floatSliderGrp('minDistance_Slider_ui', p='scatterSliders_row_ui',w=400,f=True,l=u'Min Dist',min=0.001, max=2.0,pre=2,s=.1,v=1.0)
	cmds.floatSliderGrp(minDistSlider , e=True, dc=partial(minDist, minDistSlider))
	
	scatterDensitySlider = cmds.floatSliderGrp('scatterDensity_Slider_ui', p='scatterSliders_row_ui',w=400,f=True,l=u'Density',min=0.001, max=10.0,pre=2,s=.1,v=1.0)
	cmds.floatSliderGrp(scatterDensitySlider , e=True, dc=partial(scatterDensity, scatterDensitySlider))
	
	
	
	cmds.showWindow('YetiCombToolsWindow')

# -------------------------------------------------------   FUNCTIONS -----------------------------------------------------	
	
	
	
def listGroomNodesG():
    listResult=[]
    list = cmds.ls(type="pgYetiGroom")
    for groomn in list:
            listResult.append(cmds.listRelatives(groomn, parent=True, ni=1)[0])
    return listResult
            
def selectGroomNode(groomSL, mirrorCB):
    global listGroomSelected
    listGroomSelected = cmds.textScrollList(groomSL, q=True, si=True )
    listGroomSelected = cmds.listRelatives( listGroomSelected, s=True)
    mirrorvalue = cmds.getAttr(listGroomSelected[0]+'.mirror')
    mirror(mirrorvalue)
    cmds.checkBox(mirrorCB, e=True, v=mirrorvalue)
    cmds.select(listGroomSelected, r=True)	
    
def selectBrush(brush):
    global listGroomSelected
    if listGroomSelected:
        mel.eval('AEpgYetiGroomToolsCombCMD ' + listGroomSelected[0] + ' ' + brush)
    
def setStrength(strength):
    global listGroomSelected
    if listGroomSelected:
        cmds.setAttr(listGroomSelected[0] + '.brushStrength', strength)
        
def setFalloffPower(strength):
    global listGroomSelected
    if listGroomSelected:
        cmds.setAttr(listGroomSelected[0] + '.brushFalloffPower', strength)      
        
def fill():
    global listGroomSelected
    if listGroomSelected:
        mel.eval ('pgYetiCommand -fillGroom '+ listGroomSelected[0])

def mirror(value):
    if listGroomSelected:
        cmds.setAttr(listGroomSelected[0]+'.mirror', value)
        print (listGroomSelected[0]+'.mirror', value)
        
def setScale(scale):
    setStrength(scale)
    selectBrush("0 6")
    
    
        
def deselectStrands():
    global listGroomSelected
    if listGroomSelected:
        mel.eval('pgYetiCommand -deselectAll ' + listGroomSelected[0])

def invertStrands():
    global listGroomSelected
    if listGroomSelected:    
        mel.eval('pgYetiCommand -invertSelected ' + listGroomSelected[0])

def undoComb():
    global listGroomSelected
    if listGroomSelected:    
        mel.eval('pgYetiCommand -undoGroom ' + listGroomSelected[0])

def redoComb():
    global listGroomSelected
    if listGroomSelected:    
        mel.eval('pgYetiCommand -redoGroom ' + listGroomSelected[0])
         
        
def minDist(slider, *arg):
    global listGroomSelected
    val = cmds.floatSliderGrp(slider, q=True, v=True)
    if listGroomSelected:
        cmds.setAttr(listGroomSelected[0] +'.minimumStrandDistance', val)
    
def scatterDensity(slider, *arg):
    global listGroomSelected
    val = cmds.floatSliderGrp(slider, q=True, v=True)
    if listGroomSelected:
        cmds.setAttr(listGroomSelected[0] +'.scatterDensity', val)
        
        
gcYetiCombToolsWindows()