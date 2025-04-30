from kafka import KafkaConsumer
import json
from shipping_model import save_shipping_record

# Create Kafka consumer without deserializer
consumer = KafkaConsumer(
    "order-confirmed",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest"
)

print("Listening to order-confirmed topic...")

for message in consumer:
    try:
        raw = message.value.decode("utf-8").strip()
        if not raw:
            continue  # Skip blank lines

        data = json.loads(raw)
        print("Received order:", data)
        save_shipping_record(data)

    except json.JSONDecodeError:
        print("Skipped invalid JSON message.")
    except Exception as e:
        print("Error processing message:", e)
