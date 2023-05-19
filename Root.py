from UserAndMapData import User
import os
db = User()
db.create_session('creativ', 'car1.png', '1', 'bg1.png')
os.system("python MainEngine.py 1")