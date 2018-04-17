from bot import boi_up, boi_down

def get_input(type=''):
    dat_input = input().strip()
    if type == 'int':
        try:
            dat_input = int(dat_input)
            return dat_input
        except ValueError:
            return -1
    else:
        return dat_input


a = '0'
print("hit enter to stop")
boi_up()
while (a=='0'):
    a = get_input()
boi_down()
print('shutting down')
