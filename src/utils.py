import numpy as np


def preprocess_Crash_ID(crash_id):
    return crash_id


def preprocess_Adjusted_Average_Daily_Traffic_Amount(amount):
    for idx, item in enumerate(amount):
        if item == 'No Data':
            amount[idx] = 0
        else:
            amount[idx] = int(item)
    return np.array(amount)


def preprocess_Commercial_Motor_Vehicle_Flag(flag):
    """
    Convert boolean to int.
        No --> 0
        Yes --> 1
    :param flag:
    :return:
    """
    for idx, item in enumerate(flag):
        if item == 'No':
            flag[idx] = 0
        elif item == 'Yes':
            flag[idx] = 1
        else:
            raise ValueError('Unexpected Value.')

    return np.array(flag)


def preprocess_Crash_Death_Count(count):
    count = [int(c) for c in count]
    return np.array(count)


def preprocess_Crash_Time(time):
    for idx, item in enumerate(time):
        item = int(item)
        item = item // 100 * 60 + item % 100
        item = item // 10
        time[idx] = item
    return np.array(time)


def preprocess_Crash_Total_Injury_Count(count):
    for idx, item in enumerate(count):
        count[idx] = int(item)
    return np.array(count)


def preprocess_Curve_Degrees(degree):
    print(set(degree))
    for idx, item in enumerate(degree):
        if item == 'No Data':
            degree[idx] = 0
        else:
            degree[idx] = int(item)
    return np.array(degree)


def preprocess_Curve_Type(types):
    for idx, item in enumerate(types):
        if item == 'S':
            types[idx] = 0
        elif item == 'N':
            types[idx] = 1
        else:
            types[idx] = 0.5
    return np.array(types)


def preprocess_Day_of_Week(day):
    for idx, item in enumerate(day):
        if item == 'MONDAY':
            day[idx] = 1
        elif item == 'TUESDAY':
            day[idx] = 2
        elif item == 'WEDNESDAY':
            day[idx] = 3
        elif item == 'THURSDAY':
            day[idx] = 4
        elif item == 'FRIDAY':
            day[idx] = 5
        elif item == 'SATURDAY':
            day[idx] = 6
        elif item == 'SUNDAY':
            day[idx] = 7
        else:
            raise ValueError('Unexpected value.')
    return np.array(day)


def preprocess_Inside_Shoulder_Width_on_Divided_Highway(width):
    for idx, item in enumerate(width):
        if item == 'No Data':
            width[idx] = 0
        else:
            width[idx] = int(item)
    return np.array(width)


def preprocess_Latitude(latitude):
    for idx, item in enumerate(latitude):
        if item == 'No Data':
            latitude[idx] = 0
        else:
            latitude[idx] = float(item)
    return np.array(latitude)


def preprocess_Light_Condition(light):
    for idx, item in enumerate(light):
        if item == '1 - DAYLIGHT':
            light[idx] = 1
        elif item == '2 - DARK, NOT LIGHTED':
            light[idx] = 2
        elif item == '3 - DARK, LIGHTED':
            light[idx] = 3
        elif item == '4 - DARK, UNKNOWN LIGHTING':
            light[idx] = 4
        elif item == '5 - DAWN':
            light[idx] = 5
        elif item == '6 - DUSK':
            light[idx] = 6
        else:
            light[idx] = 0
    return np.array(light)


def preprocess_Longitude(longitude):
    for idx, item in enumerate(longitude):
        if item == 'No Data':
            longitude[idx] = 0
        else:
            longitude[idx] = float(item)
    return np.array(longitude)


def preprocess_Manner_of_Collision(manner):
    print('=== manner ===')
    print(set(manner))
    for idx, item in enumerate(manner):
        if item == 'SAME DIRECTION - ONE LEFT TURN-ONE STOPPED':
            pass
        elif item == 'ONE MOTOR VEHICLE - OTHER':
            pass
        elif item == 'SAME DIRECTION - ONE RIGHT TURN-ONE STOPPED':
            pass
        elif item == 'OPPOSITE DIRECTION - ONE STRAIGHT-ONE BACKING':
            pass
        elif item == 'OTHER - BOTH BACKING':
            pass
        elif item == 'OPPOSITE DIRECTION - ONE BACKING-ONE STOPPED':
            pass
        elif item == 'ONE MOTOR VEHICLE - TURNING RIGHT':
            pass
        elif item == 'SAME DIRECTION - ONE STRAIGHT-ONE RIGHT TURN':
            pass
        elif item == 'OTHER - ONE LEFT TURN-ONE ENTERING OR LEAVING PARKING SPACE':
            pass
        elif item == 'ANGLE - ONE RIGHT TURN-ONE LEFT TURN':
            pass
        elif item == 'SAME DIRECTION - BOTH LEFT TURN':
            pass
        elif item == 'OPPOSITE DIRECTION - BOTH GOING STRAIGHT':
            pass
        elif item == 'ANGLE - BOTH RIGHT TURN':
            pass
        elif item == 'ANGLE - ONE STRAIGHT-ONE RIGHT TURN':
            pass
        elif item == 'ONE MOTOR VEHICLE - GOING STRAIGHT':
            pass
        elif item == 'ANGLE - BOTH LEFT TURN':
            pass
        elif item == 'SAME DIRECTION - BOTH RIGHT TURN':
            pass
        elif item == 'ANGLE - BOTH GOING STRAIGHT':
            pass
        elif item == 'OPPOSITE DIRECTION - ONE LEFT TURN-ONE STOPPED':
            pass
        elif item == 'OTHER - BOTH ENTERING OR LEAVING A PARKING SPACE':
            pass
        elif item == 'OTHER - ONE STRAIGHT-ONE ENTERING OR LEAVING PARKING SPACE':
            pass
        elif item == 'OPPOSITE DIRECTION - ONE STRAIGHT-ONE LEFT TURN':
            pass
        elif item == 'ONE MOTOR VEHICLE - TURNING LEFT':
            pass
        elif item == 'SAME DIRECTION - ONE STRAIGHT-ONE STOPPED':
            pass
        elif item == 'ANGLE - ONE RIGHT TURN-ONE STOPPED':
            pass
        elif item == 'ANGLE - ONE STRAIGHT-ONE STOPPED':
            pass
        elif item == 'OPPOSITE DIRECTION - BOTH LEFT TURNS':
            pass
        elif item == 'SAME DIRECTION - ONE STRAIGHT-ONE LEFT TURN':
            pass
        elif item == 'OPPOSITE DIRECTION - ONE STRAIGHT-ONE STOPPED':
            pass
        elif item == 'ANGLE - ONE STRAIGHT-ONE BACKING':
            pass
        elif item == 'SAME DIRECTION - BOTH GOING STRAIGHT-REAR END':
            pass
        elif item == 'OTHER - ONE ENTERING OR LEAVING PARKING SPACE-ONE STOPPED':
            pass
        elif item == 'ONE MOTOR VEHICLE - BACKING':
            pass
        elif item == 'SAME DIRECTION - BOTH GOING STRAIGHT-SIDESWIPE':
            pass
        elif item == 'ANGLE - ONE STRAIGHT-ONE LEFT TURN':
            pass
        elif item == 'OTHER':
            pass
        elif item == 'OPPOSITE DIRECTION - ONE RIGHT TURN-ONE LEFT TURN':
            pass
        elif item == 'ANGLE - ONE LEFT TURN-ONE STOPPED':
            pass
        elif item == 'SAME DIRECTION - ONE RIGHT TURN-ONE LEFT TURN':
            pass
        elif item == 'OPPOSITE DIRECTION - ONE STRAIGHT-ONE RIGHT TURN':
            pass
    return manner


def preprocess_Number_of_Lanes(num_of_lanes):
    num_of_lanes = [0 if item == 'No Data' else int(item) for item in num_of_lanes]
    return np.array(num_of_lanes)


def preprocess_Object_Struck(struck):
    print('=== struck ===')
    print(set(struck))
    return struck


def preprocess_Outside_Shoulder_Width_on_Divided_Highway(width):
    width = [0 if item == 'No Data' else int(item) for item in width]
    return np.array(width)


def preprocess_Property_Damages(properties):
    print('=== property damages ===')
    print(set(properties))
    return properties


def preprocess_Road_Class(road_class):
    for idx, item in enumerate(road_class):
        if item == 'INTERSTATE':
            road_class[idx] = 0
        elif item == 'US & STATE HIGHWAYS':
            road_class[idx] = 1
        elif item == 'TOLLWAY':
            road_class[idx] = 2
        elif item == 'NON TRAFFICWAY':
            road_class[idx] = 3
        elif item == 'OTHER ROADS':
            road_class[idx] = 4
        elif item == 'COUNTY ROAD':
            road_class[idx] = 5
        elif item == 'CITY STREET':
            road_class[idx] = 6
        elif item == 'FARM TO MARKET':
            road_class[idx] = 7
    return np.array(road_class)


def preprocess_Street_Name(street_name):
    print('==== street name ===')
    print(set(street_name))
    return street_name


def preprocess_Street_Number(street_num):
    print('==== street num ===')
    print(set(street_num))
    return street_num


def preprocess_Surface_Condition(condition):
    for idx, item in enumerate(condition):
        if item == '1 - DRY':
            condition[idx] = 1
        elif item == '2 - WET':
            condition[idx] = 2
        elif item == '3 - STANDING WATER':
            condition[idx] = 3
        elif item == '4 - SNOW':
            condition[idx] = 4
        elif item == '5 - SLUSH':
            condition[idx] = 5
        elif item == '6 - ICE':
            condition[idx] = 6
        elif item == '7 - SAND, MUD, DIRT':
            condition[idx] = 7
        else:
            condition[idx] = 0
    return np.array(condition)


def preprocess_Weather_Condition(weather):
    for idx, item in enumerate(weather):
        if item == '1 - CLEAR':
            weather[idx] = 1
        elif item == '2 - CLOUDY':
            weather[idx] = 2
        elif item == '3 - RAIN':
            weather[idx] = 3
        elif item == '4 - SLEET/HAIL':
            weather[idx] = 4
        elif item == '5 - SNOW':
            weather[idx] = 5
        elif item == '6 - FOG':
            weather[idx] = 6
        elif item == '7 - BLOWING SAND/SNOW':
            weather[idx] = 7
        elif item == '8 - SEVERE CROSSWINDS':
            weather[idx] = 8
        else:
            weather[idx] = 0
    return np.array(weather)


def preprocess_Driver_Alcohol_Result(alcohol):
    for idx, item in enumerate(alcohol):
        if item == '1 - POSITIVE':
            alcohol[idx] = 1
        elif item == '2 - NEGATIVE':
            alcohol[idx] = 0
        else:
            alcohol[idx] = 0
    return np.array(alcohol)


def _unique(values):
    print(set(values))
