def group_size(num_popsicles):

  max_popsicles_per_person = 0
  group_size = 1

  for i in range(2, num_popsicles + 1):
    if num_popsicles % i == 0:
      popsicles_per_person = num_popsicles // i

      if popsicles_per_person > max_popsicles_per_person:
        max_popsicles_per_person = popsicles_per_person
        group_size = i
  return group_size

num_popsicles = int(input('Введите количество мороженого: '))
print('Количество человек в группе:', group_size(num_popsicles))