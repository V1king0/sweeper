import socket

def sweep_network(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    for i in range(start[3], end[3] + 1):
        address = f"{start[0]}.{start[1]}.{start[2]}.{i}"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((address, 80))
        if result == 0:
            print(f"Active host found at {address}")

if __name__ == "__main__":
    sweep_network("192.168.1.1", "192.168.1.255")

