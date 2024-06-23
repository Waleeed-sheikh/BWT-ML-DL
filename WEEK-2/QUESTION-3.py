# Question 3
# Write a function `convert_temperature(temp, scale)` that:
# 1. Takes a temperature value and a scale ("C" for Celsius, "F" for Fahrenheit) as inputs.
# 2. Converts the temperature to the other scale.
# 3. Returns the converted temperature.
# 4. Display the converted temperature.


def convert_temperature(temp, scale):
    if scale == "Fahrenheit":
        converted_temp = (temp - 32) * 0.5556
        return converted_temp, "C°"
    elif scale == "Celsius":
        converted_temp = (temp * 1.8) + 32
        return converted_temp, "F°"
    else:
        return None, None

temp, scale = convert_temperature(18, "Fahrenheit")
print("The temperature is: {:.2} {}".format(temp,scale))

# first i thought of just simply converting the temperature from F to C and vice versa and then simply return it.
#def convert_temperature(temp, scale):
   # if scale=="Fahrenheit":
   #  return  (temp - 32) * .5556 
  # elif scale=="Celsius":
      # return (temp * 1.8) + 32 
#print("The temperature is :" , convert_temperature(23,"Fahrenheit"))

#  but then i thought adding the converted scale will make it more neat so then i searched for tuple and used them 
#in the above code i used .format() to add the values in print statement contarary to "f" statement i used in question number 1 or 2

#.2 rounds up the value upto 2 decimal places

