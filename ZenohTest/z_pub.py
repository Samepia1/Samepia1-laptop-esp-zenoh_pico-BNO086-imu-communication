import zenoh, random, time
from zenoh.ext import z_serialize

random.seed()


def read_temp():
    return [float(random.randint(0, 100)) for _ in range(6)]


if __name__ == "__main__":
    config = zenoh.Config()
    config.insert_json5("mode", '"client"')
    # config.insert_json5("connect/endpoints", '["tcp/172.20.10.7:7447"]')
    # config.insert_json5("scouting/multicast/enabled", "false")  # Disable peer discovery
    print("Connecting to router...")
    with zenoh.open(config) as session:
        print(f"Connected! Session ID: {session.zid()}")
        key = "imu/data"
        pub = session.declare_publisher(key)
        print(f"Publishing to '{key}'")
        while True:
            t = read_temp()
            payload = z_serialize(t)  # Serialize the list
            print(f"putting data: {t}")
            pub.put(payload)
            time.sleep(1)
