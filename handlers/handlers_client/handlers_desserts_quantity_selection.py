from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Router, types, F
from aiogram.enums import ParseMode

from state.state_client import Client_state
from keyboard.keyboard_client import *

client_desserts_quantity_selection_router = Router()