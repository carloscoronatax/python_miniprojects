# This .py is a bunch of practice exercises made by carloscoronatax. Enjoy!

# In this mini-project, I'm creating and organizing a list of clients for a small tax firm.

# This firm has 5 clients.

clients = ['Carlos', 'Alexa', 'Jose', 'Angel', 'Rosa']

# These clients have different companies

companies = ['Berry US', 'CarLEXA', 'JosGarden', 'AFlowerMX', 'Tacos el Gordo']


# A new client is joining today. His name is Jorge and his company name is 'El tocayo'

clients.append('Jorge')
companies.append('EL tocayo')

print(clients)
print(companies)

# Make a new list with clients and companies and add their phone number

complete_list = [['Carlos', 'Berry US', 4434756985], ['Alexa', 'CarLEXA', 4542123643], ['Jose', 'JoseGarden', 9875466598], ['Angel', 'AFlowerMX', 7458967854],
                 ['Rosa', 'Tacos el Gordo', 8788996562]]

print(complete_list)

# Remove company name from Carlos' list

complete_list[0].remove('Berry US')

print(complete_list)

# Change company name to 'Carlos Tacos' and print

complete_list[0].append('Carlos Tacos')

print(complete_list)

# Two more clients recently hired this tax firm as their accountant. Add their details.

final_list = complete_list + [['Ana', 'Anacherries', 7878456663], ['Jimena', 'JBakery', 7889655659]]

# Print final & organized list
print(final_list)




