# OrderedDict : keys are always in the order in which they were inserted

from collections import OrderedDict

od = OrderedDict()
od['Harsh'] = 19
od['Manthan'] = 40
od['Sahil'] = 12
print(od)

od.move_to_end('Harsh')
print(od)
od.move_to_end('Sahil', last=False)
print(od)

od.pop('Harsh')
print(od)

od.popitem()
print(od)

