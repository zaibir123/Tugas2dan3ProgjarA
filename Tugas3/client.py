import sys
import socket
import logging
import threading
import timeit


def kirim_data(nama="kosong"):
    logging.warning(f"nama {nama}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('0.0.0.0', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode())
        amount_received = 0
        amount_expected = len(message)
        res = ""
        while amount_received < amount_expected:
            data = sock.recv(32)
            amount_received += len(data)
            res += data.decode()
            logging.warning(f"[CLIENT] received {data}")
    finally:
        print(res)
        sock.close()
    return


if __name__=='__main__':
    threads = []
    for i in range(50):
        t = threading.Thread(target=kirim_data, args=(i,))
        threads.append(t)

    start = timeit.default_timer()
    for thr in threads:
        thr.start()
    for thr in threads:
        thr.join()
    stop = timeit.default_timer()
    print('Time: ', stop - start)