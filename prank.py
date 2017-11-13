from clockwork import clockwork
import sys

api = clockwork.API('')

message = clockwork.SMS(
    to = input('Going to : '),
    from_name = input('Coming from : '),
    message = input('What do we want to say? : '))

response = api.send(message)

if response.success:
    print (response.id)
else:
    print (response.error_code)
    print (response.error_message)
