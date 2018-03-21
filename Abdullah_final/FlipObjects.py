import maya.cmds as cmds
"sit pivot point to center"
#store selections in ordered list
selectionList = cmds.ls( orderedSelection=True)
selectionStored= cmds.ls( orderedSelection=True)
print 'Selected items: %s' % ( selectionList )
selectionListInteger=int(len(selectionList))
print selectionListInteger
# center pivot point to (0,0,0) space
cmds.move(0,0,0,".scalePivot",".rotatePivot",absolute=True)


#count the list >extract first index>apply the effect>repeat
for EachObject in range(selectionListInteger):
    targetName = selectionList[0]
    # clear selction the selection indivisually
    cmds.select(clear=True)
    cmds.select(targetName,add=True)
    print targetName
    # check it's a Trasform node
    print cmds.objectType(targetName)
    # store scales to flip the X-scale for the object 
    sx=cmds.getAttr(targetName+".scaleX")
    sy=cmds.getAttr(targetName+".scaleY")
    sz=cmds.getAttr(targetName+".scaleZ")
    print "Result:(%s,%s,%s)" %(sx,sy,sz)
    #free pivote point to center then flip on X axies
    cmds.xform(scale=(sx*-1,sy,sz))
    selectionList.remove( targetName )
    cmds.select(targetName,d=True)

#lastly select the list again    
cmds.select(selectionStored,add=True)
