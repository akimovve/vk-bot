from config import schedule_list, vk_api_token as token
from launcher import Launcher

from schedule.receive_data import ReceiveSchedule


ReceiveSchedule.start(schedule_list)

launcher = Launcher(token)
launcher.start()
