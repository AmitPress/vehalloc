from conf.app import get_app_instance
from routers import driver_router, employee_router
app = get_app_instance()
app.include_router(driver_router.router)
app.include_router(employee_router.router)