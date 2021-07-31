import sys


def getBTS(byte): return bin(int.from_bytes(byte, byteorder=sys.byteorder))


def get_src(path):
    arr = []
    with open(path, "rb") as f:
        byte = f.read(1)

        while byte:
            bt = getBTS(byte)
            arr.append(bt)
            byte = f.read(1)

    return arr


def calc(path, arr):
    dest = []
    with open(path, "rb") as f:
        byte = f.read(1)
        c = 0
        arr_len = len(arr)
        while byte:
            bt = getBTS(byte)

            if arr_len > c:
                shift = 0

                if type(arr[c]) == int:
                    shift = arr[c]
                else:
                    shift = int(arr[c], 2)

                r = int(bt, 2) ^ shift

                dest.append(r)

            byte = f.read(1)
            c += 1

    return dest


arr_src = get_src('/home/zx/BC/task3/MyPassword.txt.encrypted')
arr_dest = calc('/home/zx/BC/task3/Note.bmp.encrypted', arr_src)
final = calc('/home/zx/BC/task3/head.bmp', arr_dest)

s = bytes(final)
print(s)

resF = open('out', 'wb')
resF.write(s)
resF.close()
