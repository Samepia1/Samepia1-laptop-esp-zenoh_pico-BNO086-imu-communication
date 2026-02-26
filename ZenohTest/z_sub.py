import zenoh, time
import logging
from zenoh.ext import z_deserialize

logging.basicConfig(level=logging.DEBUG)


def listener(sample):
    # by default zenoh wraps the payload in a 
    # zenoh.sample to read the data read sample.payload
    # des = z_deserialize(list[float], sample.payload)
    print(sample.payload.to_bytes().decode('utf-8').strip())


if __name__ == "__main__":
    config = zenoh.Config()
    config.insert_json5("mode", '"client"')
    config.insert_json5("connect/endpoints", '["tcp/10.243.82.169:7447"]')
    config.insert_json5("scouting/multicast/enabled", "false")  # Disable peer discovery
    print("Connecting to router...")
    with zenoh.open(config) as session:
        print(f"Connected! Session ID: {session.zid()}")
        key = "imu/data"
        sub = session.declare_subscriber(key, listener)
        print(f"Subscribed to '{key}', waiting for messages...")
        time.sleep(10000)
