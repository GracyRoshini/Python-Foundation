import sys
import os

sys.path.append(os.path.abspath("../p1")) #--or copy the entire path and paste here
from calculation import add #--can directly call the name
import calculation

print('add:',calculation.add(2,4))

import calculation
print("sub:",calculation.sub(4,2))
