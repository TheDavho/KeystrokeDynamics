import time
import pandas as pd
from pynput.keyboard import Key, Listener

# CSV FORMAT
#   Time  Key  Action
#  13389  s    p
#  13397  s    r

print("Enter your name:")
name = input()
print("-"*15)

header = ['Time', 'Key', 'Action']

record = []
def on_press(key):
    if key != Key.esc:
        key = str(key)
        record.append([time.time(), key, 'p'])
        print(f'pressed {key}, record is: {record}')
    
def on_release(key):
    if key == Key.esc:
        framedRecord = pd.DataFrame(record, columns=header)
        framedRecord.to_csv(f'records/{name}.csv', index=False)
        return False
    record.append([time.time(), key, 'r'])

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
