from django.apps import AppConfig


class CarManagerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "car_manager"

    def ready(self):
        import car_manager.signals  # Import the signals so they are connected