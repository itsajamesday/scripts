from clockwork import clockwork
import sys

api = clockwork.API('')

message = clockwork.SMS(
    to = sys.argv[1],
    from_name = sys.argv[2],
    message = sys.argv[3])

response = api.send(message)

if response.success:
    print (response.id)
else:
    print (response.error_code)
    print (response.error_message)
