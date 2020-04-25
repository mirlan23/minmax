values=[5,3,1,2,4]
print(values)

def max_val(values):
  return max(list(values))


print(max_val(values))    #>>>5         


def min_val(values):
  return min(list(values))
print(min_val(values))    #>>>1     



#----------------------------------------------------------------------------------

values=[5,4]
def avg(values):
  return sum(values)/len(values)
print(float(avg(values)))      #>>>4.5

#----------------------------------------------------------------------------------

LIST = [1, 4, 33, 100, 113, 107, 120, 155, 256]

def filter_100_120(i):
  if  i <=100 or i>=120 :
    return i
    
filtred_list = list(filter(filter_100_120, LIST))
print(filtred_list)

def filter_even(i):
  if i % 2==0:
    return i

filtred_list = list(filter(filter_even, LIST))
print(filtred_list)


#----------------------------------------------------------------------------------


clock = "Time is {hour}:{minute} minutes"

numbers=(int(input("Введите минуты:  ")))
if numbers < 60:
  minute=numbers
  hour=00
  print(clock.format(hour=hour, minute=minute))


if numbers > 60:
  hour=numbers//60
  minute=numbers-(hour*60)
  
  print(clock.format(hour=hour, minute=minute))
