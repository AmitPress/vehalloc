from conf.app import get_app_instance
from routers import driver_router
app = get_app_instance()
app.include_router(driver_router.router)