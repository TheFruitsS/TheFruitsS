nylon = int(input())
paint = int(input())
razr = int(input())
hours = int(input())

nylon_price = (nylon + 2) * 1.5
paint_price = (paint * 1.10) * 14.5
razr_price = razr * 5

total_sum = nylon_price + paint_price + razr_price + 0.40
sum_workers = (total_sum * 0.3) * hours

final_sum = total_sum + sum_workers

print(final_sum)