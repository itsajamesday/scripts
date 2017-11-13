from clockwork import clockwork
import sys

api = clockwork.API('')

message = clockwork.SMS(
    to = raw_input('Going too:'),
    from_name = raw_input('Coming from:'),
    message = raw_input('What do we want to say?:'))

response = api.send(message)

if response.success:
    print (response.id)
else:
    print (response.error_code)
    print (response.error_message)
