from amo_crm_api_client.storage import (
    handle_startup,
    KeyValueStorageConfigModel,
)
from amo_crm_api_client.storage.impl.instances.memory.impl.MemoryKeyValueStorage import (
    MemoryKeyValueStorage,

)
from amo_crm_api_client.storage.impl.instances.memory.impl.MemoryStorageConfigModel import (
    MemoryStorageConfigModel,

)
from amo_crm_api_client.storage.impl.instances.redis.RedisKeyValueStorage import (
    RedisKeyValueStorage,

)


def test_startup_without_parameters() -> None:
    storage_factory = handle_startup()
    storage = storage_factory.get_instance()
    assert isinstance(storage, MemoryKeyValueStorage)


def test_startup_by_settings_for_redis() -> None:
    storage_factory = handle_startup(
        settings={"type": "redis"}
    )
    storage = storage_factory.get_instance()
    assert isinstance(storage, RedisKeyValueStorage)


def test_startup_with_empty_settings_for_redis() -> None:
    storage_factory = handle_startup(
        settings={
            "type": "redis",
            "settings": {},
        }
    )
    storage = storage_factory.get_instance()
    assert isinstance(storage, RedisKeyValueStorage)


def test_startup_with_full_settings_for_redis() -> None:
    storage_factory = handle_startup(
        settings={
            "type": "redis",
            "settings": {
                "host": "127.0.0.1",
                "port": 6379,
            },
        }
    )
    storage = storage_factory.get_instance()
    assert isinstance(storage, RedisKeyValueStorage)


def test_startup_with_full_settings():
    storage_factory = handle_startup(
        settings={
            "type": "memory",
            "settings": {
                "backup_file_path": "path",
                "encryption_key": "encryption_key",
            },
        }
    )
    storage = storage_factory.get_instance()
    assert isinstance(storage, MemoryKeyValueStorage)


def test_startup_with_config():
    storage_config = MemoryStorageConfigModel(
        backup_file_path="path",
        encryption_key="encryption_key",
    )
    config = KeyValueStorageConfigModel(
        type="memory",
        storage_config=storage_config,
    )
    storage_factory = handle_startup(
        config=config,
    )
    storage = storage_factory.get_instance()
    assert isinstance(storage, MemoryKeyValueStorage)