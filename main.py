
a = [1,2,3,4,3,4,5,6,74,3,2,3]

# new_array = []
#Creating a test array a
a = [1,2,4,5,2,3,4,2,4]
#Creating a function that takes an empty dictionary b as an parameter
def num_num(b):
  #Create an empty dictionary whiich will be used to store the looped integers
  new_b = {}
  # Performing a for loop to get the individual integers and storing them in the     dictionary
  for num in b:
    # Appending the looped integers inside the empty dictionary
    # Looping the num which is a dictionary to get the individual keys of the re-occurring integers
    if num in new_b.keys():
      # If the key exists, populate by the number then add
      new_b[num] += 1
    else:
      # If not, it gets a default value of 1
      new_b[num] = 1
      
  print(new_b)
  # A variable new value is assigned to the method for retrieving the individual keys
  # Prints the values in a and not inside a dictionary
  new_value = max(new_b, key=new_b.get)
  # new_no = new_b.count(new_value)
  # This gets the individual value from the dictionary
  # if new_value > len(new_b):
  #   print(new_b)
  # else:
  #   print(-1)
  
  print(new_b[new_value])
  new_array = new_b.keys()
  
  if new_array in new_b.keys():
    print(new_b.index(new_array))
  else:
    print(-1)
  
num_num(a)

  
  
  