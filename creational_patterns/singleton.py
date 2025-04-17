class SystemSettingsManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(SystemSettingsManager, cls).__new__(cls)
            cls.__instance.settings = {}
        return cls.__instance

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings.get(key)
