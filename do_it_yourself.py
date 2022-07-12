
logs = open("app_2.log", "r")


def check_device(logs):
    list_defective_device = []
    devices = {}

    for log in logs:
        if 'BIG' in log:
            log = '>'.join(log.split('>')[-1:])
            log_string = log.split(';')
            id = log_string[2]
            status = log_string[-2]

            if id not in list_defective_device:
                if status == 'DD':
                    list_defective_device.append(id)
                    if id in devices.keys():
                        del devices[id]
                else:
                    if id not in devices.keys():
                        devices[id] = 1
                    else:
                        devices[id] = int(devices.get(id)) + 1

    print('List of  defective devices - ', list_defective_device)
    print('Number of defective devices -', len(list_defective_device))

    for id, status in devices.items():
        print(f'Device {id} sent {status} statuses')

    print('Number of devices -', len(devices))


check_device(logs)
