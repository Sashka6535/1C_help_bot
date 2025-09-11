from aiogram import Router

from Handlers.start import main_router

handlers_routers = Router()

handlers_routers.include_routers(main_router)
