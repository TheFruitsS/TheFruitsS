import math
paint_boxes = int(input())
rolls_num = int(input())
pair_gloves = float(input())
brush_price = float(input())

total_paint = paint_boxes * 21.5
total_rolls = rolls_num * 5.20

total_gloves = math.ceil(rolls_num * 0.35) * pair_gloves

total_brush = math.floor(paint_boxes * 0.48) * brush_price

delivery = (total_brush + total_gloves + total_paint + total_rolls) * (1/15)
print(f"This delivery will cost {delivery:.2f} lv.")