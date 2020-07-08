from django.conf import settings


# Needed to build and publish
# ------------------------------------------------------------------------------
SECRET_KEY = "backoffice"

# Specific project configuration
# ------------------------------------------------------------------------------
TITLE = getattr(settings, "BACKOFFICE_TITLE", "backoffice")
URL_NAMESPACE = getattr(settings, "BACKOFFICE_URL_NAMESPACE", "backoffice")
BOOLEAN_TRUE_ICON_CLASSES = getattr(
    settings,
    "BACKOFFICE_BOOLEAN_TRUE_ICON_CLASSES",
    "has-text-success fas fa-check-circle",
)
BOOLEAN_FALSE_ICON_CLASSES = getattr(
    settings,
    "BACKOFFICE_BOOLEAN_FALSE_ICON_CLASSES",
    "has-text-danger fas fa-times-circle",
)

STATUS_FIELDS = getattr(settings, "BACKOFFICE_STATUS_FIELDS", ("status",))
STATUS_TAG_CLASSES = getattr(settings, "BACKOFFICE_STATUS_TAG_CLASSES", {})
DETAILS_URLS = getattr(
    settings,
    "BACKOFFICE_DETAILS_URLS",
    [{"names": ("pk", "id")}, {"names": ("user", "owner")},],
)
SIDEBAR_CONFIG = getattr(settings, "BACKOFFICE_SIDEBAR_CONFIG", [])