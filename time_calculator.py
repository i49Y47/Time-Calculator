def add_time(start, duration, day_of_week: str = None):
  days = {
    'Sunday': 0,
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6
  }

  tformate = 0 if 'AM' in start else 1

  sH, sM = map(int, start.split()[0].split(':'))
  dH, dM = map(int, duration.split(':'))

  n, dH = divmod(dH, 24)  # Count Number Of Days

  start_in_24f = (sH * 60 + sM) + (12 * 60 * tformate)
  added_in_24f = start_in_24f + (dH * 60 + dM)

  aH, aM = divmod(added_in_24f, 60)
  j, aH = divmod(aH, 24)

  n += j

  if aH == 0:
    new_time = f"12:{str(aM).zfill(2)} AM"
  elif aH < 12:
    new_time = f"{aH}:{str(aM).zfill(2)} AM"
  elif aH == 12:
    new_time = f"12:{str(aM).zfill(2)} PM"
  elif aH < 24:
    new_time = f"{aH-12}:{str(aM).zfill(2)} PM"

  if day_of_week:
    i = (days[day_of_week.title()] + n) % 7
    for k, v in days.items():
      if v == i:
        new_time += f", {k}"
        break

  if n == 1:
    new_time += " (next day)"
  elif n > 1:
    new_time += f" ({n} days later)"

  return new_time
