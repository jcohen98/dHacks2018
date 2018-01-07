import threading

current_pos = [0, 0]
gyro_val = [0,0,0]
g = 9.81

# define sensor positions
pos_s1 = [0,-105]
pos_s2 = [0,-210]
pos_s3 = [0,-315]
pos_s4 = [135,0]

initval_s1 = 420
initval_s2 = 120
initval_s3 = 420
initval_s4 = 270


def approx_pos(gyro_val, g, time=0.5):
    scale = time*time*g
    for i in range(0,1):
        gyro_val[i] = gyro_val[i]*scale
    current_pos = gyro_val
    return current_pos


def refresh():
    if val_s1-initval_s1!=range(-20,20):
        current_pos[0] = val_s1
        current_pos[1] = -105
    elif val_s2-initval_s2!=range(-20,20):
        current_pos[0] = val_s2
        current_pos[1] = -210
    elif val_s3-initval_s3!=range(-20,20):
        current_pos[0] = val_s3
        current_pos[1] = -315
    elif val_s4-initval_s4!=range(-20,20):
        current_pos[0] = 135
        current_pos[1] = val_s4
    else:
        current_pos = approx_pos(gyro_val, time, g)

threading.Timer(0.5,refresh).start()
