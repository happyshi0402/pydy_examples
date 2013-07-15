#Export method calls and namespace
# from three_link_pendulum example ..

from essential import *
from simulate import *
import json
#setting some shapes for the pendulums ..

shape1 = Cylinder('shape1',radius=2,height=10, \
                                color='red')

shape2 = Cylinder('shape2',radius=1,height=12, \
                                color='blue')
                                
shape3 = Cylinder('shape3',radius=3,height=7, \
                                color='green')

#Setting up some vframes ...
                                
frame1 = VisualizationFrame('frame1', link1, shape=shape1)
frame2 = VisualizationFrame('frame2', link2, shape=shape2)

frame3 = VisualizationFrame('frame3', link3, shape=shape3)

scene = Scene('scene1',I,O)
scene.add_visualization_frame([frame1,frame2,frame3])


dynamic_params = alpha + beta + omega + delta
data = scene.generate_json(values_list)

f = open('js/output.json','w')
f.write('var JSONObj=' + json.dumps(data) + ';')

