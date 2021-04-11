# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# Part 1: Greet Template, replace the <name> part with the name argument by using replace.
def greet(name, greeting_template = 'Hello, <name>!'):
    greeting = greeting_template.replace('<name>', name)
    
    return greeting
    
    

# Part 2
def force(mass, body = 'earth'):
    planets = {
        'sun' : 274,
        'jupiter' : 24.92,
        'neptune' : 11.15,
        'saturn' : 10.44,
        'earth' : 9.798,
        'uranus' : 8.87,
        'venus' : 8.87,
        'mars' : 3.71,
        'mercury' : 3.7,
        'moon' : 1.62,
        'pluto' : 0.58
        }
    
    body = planets.get(body)
    force = float(mass)*body # Gave warning: Redefining name 'force' from outer scope (line 15), why?
    output = round(force) 
    
    return output


  
  
# Part 3: Gravity
def pull(m1, m2 , d):
    G = 6.674 * (10**-11)
    pull = (G * ((m1 * m2) / d**2)) #Gave warning: Redefining name 'pull' from outer scope (line 40), why?
    
    return pull

