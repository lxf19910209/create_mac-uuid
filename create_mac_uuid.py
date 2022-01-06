import sys
import uuid
import csv

def get_uuid(mac,count):
    model = 'xxx'
    board = 'xxxx'
    country = 'CN'
    curr_count = 0
    i = 0
    # mac upper
    mac_new = mac.upper()
    #csv header
    header = ["mac", "uuid", "model", "board", "country"]

    with open("%s-%s.csv" %(mac_new,count),"w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        while i < int(count):
            temarr = []
            mac_int = int(mac,16)
            curr_mac_int = mac_int + curr_count
            new_mac_hex = hex(curr_mac_int)[2:]
            if len(new_mac_hex) < 12:
                new_mac_hex = new_mac_hex.zfill(12)

            uu = str(uuid.uuid4())
            u1 = uu[:-12]
            u2 = u1 + new_mac_hex
            temarr.append(new_mac_hex.upper())
            temarr.append(u2)
            temarr.append(model)
            temarr.append(board)
            temarr.append(country)
            print(temarr)
            writer.writerow(temarr)
            curr_count += 2
            i += 1

if __name__ == '__main__':
    if len(sys.argv) == 3:
        mac_addr = sys.argv[1]
        create_count   = sys.argv[2]
    else:
        sys.exit("参数格式不对！")

    if len(mac_addr) == 12:
        mac_up = mac_addr.upper()
        mac_low    = mac_addr.lower()
        get_uuid(mac_low, create_count)
    else:
        sys.exit("MAC输入错误！")
