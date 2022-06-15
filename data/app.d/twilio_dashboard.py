"""
twilio_dashboard.py

Creates a simple dashboard to display data from Twilio
"""
from twilio.rest import Client

from deephaven import empty_table
from deephaven.time import to_datetime
from deephaven.plot.figure import Figure

def message_to_datetime(message):
    message_dt_string = message.date_sent.strftime("%Y-%m-%dT%H:%M:%S UTC")
    return to_datetime(message_dt_string)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

messages = client.messages.list()
result = empty_table(len(messages)).update("Message = messages[i]")
result = result.update("DateSent = (DateTime)message_to_datetime(Message)")

binned = result.update("DateSentMinute = lowerBin(DateSent, MINUTE)")

counts = binned.count_by("MessagesPerMinute", by=["DateSentMinute"])

messages_over_time = Figure().plot_xy(series_name="MessagesOverTime", t=counts, x="DateSentMinute", y="MessagesPerMinute").show()
