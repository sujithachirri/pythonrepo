import psutil
# result01 = psutil.cpu_times()
# print(result01)
# result02 = psutil.cpu_stats()
# print(result02)
# result04 = psutil.disk_partitions()
# print(result04)
# result05 = psutil.net_io_counters()
# print(result05)

network_stats=psutil.net_io_counters(pernic=False)
bytes_sent=getattr(network_stats,'bytes_sent')
bytes_recv=getattr(network_stats,'bytes_recv')

print("bytes sent = {0} | bytes received = {1}".format(bytes_sent,bytes_recv))


