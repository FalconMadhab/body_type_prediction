import math
import os

def get_bmi(weight, height):
    global bmi
    try:
        if not (weight and height):
            bmi = 'Error!'
            return bmi
        else:
            bmi = math.floor(int(weight) / (float(height) * float(height)))
            return bmi
    except ValueError:
        bmi = 'Error!'
        return bmi

def get_body_shape(bust, waist, hip):
    global body_shape
    try:
        bust = int(bust)
        waist = int(waist)
        hip = int(hip)

        # Waist is at least 25 percent smaller than Hip AND Bust measurement.
        if float(waist) * float(1.25) <= bust & hip:
            body_shape = 'Hourglass'
            return body_shape

        # Hip measurement is more than 5 percent bigger than Bust measurement.
        elif float(hip) * float(1.05) > bust:
            body_shape = 'Pear'
            return body_shape

        # Hip measurement is more than 5 percent smaller than Bust measurement.
        elif float(hip) * float(1.05) < bust:
            body_shape = 'Apple'
            return body_shape

        # Bust, Waist and Hip measurements are within close range.
        high = max(bust, waist, hip)
        low = min(bust, waist, hip)
        difference = high - low

        # Debugging purposes only!
        #print(high, low, difference)

        if difference <= 5:
            body_shape = 'Banana'
            return body_shape
    except ValueError:
        body_shape = 'Error!'
        return body_shape

def get_body_type(index, shape):
    global body_type
    type_descriptor = ''
    try:
        index = int(index)
        if index in range(1, 18):
            type_descriptor = 'A'
        elif index in range(18, 23):
            type_descriptor = 'B'
        elif index in range(23, 29):
            type_descriptor = 'C'
        elif index in range(29, 55):
            type_descriptor = 'D'
        elif index >= 55:
            type_descriptor = 'E'

        # Debugging purposes only!
        #print(index, type_descriptor)

        if shape == 'Error!':
            body_type = 'Error!'
            return body_type
        elif type_descriptor == 'A':
            body_type = 'Skinny'
            return body_type
        elif type_descriptor == 'B':
            body_type = 'Petite'
            return body_type
        elif type_descriptor == 'C' and shape != 'Hourglass':
            body_type = 'Average'
            return body_type
        elif type_descriptor == 'C' and shape == 'Hourglass':
            body_type = 'Curvy'
            return body_type
        elif type_descriptor == 'D' and shape == 'Banana':
            body_type = 'Overweight'
            return body_type
        elif type_descriptor == 'D' and shape == 'Hourglass':
            body_type = 'Overweight - Curvy'
            return body_type
        elif type_descriptor == 'D' and shape == 'Pear':
            body_type = 'Overweight - Bottom Heavy'
            return body_type
        elif type_descriptor == 'D' and shape == 'Apple':
            body_type = 'Overweight - Top Heavy'
            return body_type
        elif type_descriptor == 'E' and shape == 'Banana' or shape == 'Hourglass':
            body_type = 'Super Size'
            return body_type
        elif type_descriptor == 'E' and shape == 'Apple':
            body_type = 'Super Size - Top Heavy'
            return body_type
        elif type_descriptor == 'E' and shape == 'Pear':
            body_type = 'Super Size - Bottom Heavy'
            return body_type
    except ValueError:
        body_type = 'Error!'
        return body_type

height=1.70
weight=80
bust=36
waist=34
hip=36
bmi2 = get_bmi(weight, height)
body_shape2 = get_body_shape(bust, waist, hip)
body_type2 = get_body_type(bmi2, body_shape2)
print(body_type2)