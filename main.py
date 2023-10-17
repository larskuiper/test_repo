from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event,  Create3


# from irobot_edu_sdk.music import Note
# import pandas as pd
robot = Create3(Bluetooth('Robot 4'))
speed = 10

end_x = 121  # Adjust as needed
end_y = 106  # Adjust as needed
navigation_tolerance = 15  # Adjust as needed

async def stop(robot):
    await robot.set_lights_rgb(0, 255, 0)
    await robot.set_wheel_speeds(0, 0)


async def forward(robot):
    await robot.set_lights_rgb(0, 255, 0)
    await robot.set_wheel_speeds(speed, speed)
    # pos = await robot.get_position()


async def forward1(robot):
    await robot.set_lights_rgb(0, 255, 0)
    await robot.set_wheel_speeds(6, 6)


# print('🐢 (x  y  heading) = (', f(pos.x),  f(pos.y), f(pos.heading), ')')

async def backoff(robot):
    await robot.set_lights_rgb(255, 80, 0)
    # await robot.move(-20)
    # await robot.set_wheel_speeds(0,2)
    await robot.turn_left(14)


async def turn_90_degree(robot):
    await robot.set_lights_rgb(255, 80, 0)
    await robot.turn_right(90)


async def turn_33_degree(robot):
    await robot.set_lights_rgb(255, 80, 0)
    await robot.turn_right(33)


async def turn_90_degree_left(robot):
    await robot.set_lights_rgb(255, 80, 0)
    await robot.turn_left(30)


async def turnright(robot):
    await robot.set_lights_rgb(255, 80, 0)
    # await robot.move(-20)
    await robot.set_wheel_speeds(16, 5)
    # await robot.turn_right(30)


async def turnleft(robot):
    await robot.set_lights_rgb(255, 80, 0)
    # await robot.move(-20)
    await robot.set_wheel_speeds(7, 18)
    # await robot.turn_left(30)


@event(robot.when_play)
async def play(robot):
    # end_x = 121  # Adjust as needed
    # end_y = 106  # Adjust as needed
    # navigation_tolerance = 15  # Adjust as needed

    while True:

        sensors = (await robot.get_ir_proximity()).sensors
        sens_left_combined = int(sum(sensors[0:3]) / 3)
        sens_middle_combined = int(sum(sensors[2:5]) / 3)
        sens_right_combined = int(sum(sensors[4:7]) / 3)
        # sens_left_combined = ((int(sensors[0]) + int(sensors[1]) + int(sensors[2])) / 3)
        # sens_middle_combined = ((int(sensors[2]) + int(sensors[3]) + int(sensors[4])) / 3)
        # sens_right_combined = ((int(sensors[4]) + int(sensors[5]) + int(sensors[6])) / 3)
        print(sens_left_combined, sens_middle_combined, sens_right_combined)

        pos = await robot.get_position()
        print('🐢 (x  y  heading) = (', int(pos.x),  int(pos.y), int(pos.heading), ')')

        if abs(pos.x - end_x) <= navigation_tolerance and abs(pos.y - end_y) <= navigation_tolerance:
            print("Reached target coordinates!")
            await robot.set_wheel_speeds(0, 0)
            break
        else:
            # print('🐢 (x  y  heading) = (', f(pos.x),  f(pos.y), f(pos.heading), ')')
            if 600 < sens_left_combined < 1500:  # sens_left_combined > 600 and sens_left_combined < 1100
                print("1")
                await turnright(robot)
                # await forward(robot)
            elif 20 < sens_left_combined < 65:  # check the th 65 sens_left_combined > 20 and sens_left_combined < 70
                print("2")
                await turnleft(robot)
                # await forward(robot)

            elif 650 < sens_right_combined < 800:  # sens_right_combined > 650 and sens_right_combined<1000
                print("4")
                await backoff(robot)
                # await forward(robot)
            elif sens_right_combined < 45 and sens_left_combined < 45 and sens_middle_combined < 100:  # could be 100
                print("5")
                await forward1(robot)
                await turn_90_degree_left(robot)
                await forward1(robot)

            elif sens_middle_combined > 210:  # could be 100 was 200 deze is goed
                print("3")
                await turn_90_degree(robot)
                # await forward(robot)

            elif sens_middle_combined > 200 and sens_right_combined > 600:  # 200 and 600
                await turn_90_degree(robot)

            elif sens_left_combined < 10 and sens_middle_combined < 10 and sens_right_combined < 10:
                await forward(robot)

            else:
                print("6")
                await forward(robot)
            print(sens_left_combined, sens_middle_combined, sens_right_combined)

robot.play()
