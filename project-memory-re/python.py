import psutil;r=psutil.virtual_memory();e=2**20;z=round;print(f'{z(r[3]/e,2)}MB / {z(r[0]/e,2)}MB')