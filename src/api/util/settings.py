import json
import os

def get_settings():
    """Parses the settings from redis-live.conf.
    """
    # TODO: Consider YAML. Human writable, machine readable.
    CONFIG_PATH = os.environ.get('REDISLIVE_CONF_PATH', "redis-live.conf")
    return json.load(open(CONFIG_PATH))

def get_redis_servers():
    config = get_settings()
    return config["RedisServers"]

def get_redis_stats_server():
    config = get_settings()
    return config["RedisStatsServer"]

def get_data_store_type():
    config = get_settings()
    return config["DataStoreType"]
