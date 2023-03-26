import socketio
import time as time

sio = socketio.Client()

# try to connect
try:
    sio.connect('http://localhost:3000')
except Exception as e:
    print(e)
    pass

# Global vars to remember the results by
RESULTS = {}
REQ_IDS = []
FINISHED = None
DONE = False
RESULT = None


# When we get a result message in particular
@sio.on('result')
def on_result(data):
    global RESULTS, REQ_IDS, FINISHED, RESULT, DONE
    
    # Get this request ID
    req_id = data.get('request',{}).get('id')
    new_word = data.get('response','')

    # And if it's not already in results
    if not req_id in RESULTS:
        # then initially stuff it with this data
        RESULTS[req_id] = data
        # and add this request id to the last 
        REQ_IDS.append(req_id)
    # If it's already in results
    else:
        # then simply add the new response word
        RESULTS[req_id]['response'] += new_word    

    FINISHED = str(new_word).strip()
    if FINISHED == "<end>" or FINISHED == "\n":
        DONE = True
        if REQ_IDS and RESULTS:
            # get latest id
            req_id = REQ_IDS[-1]
            # get result dictionary from latest id as key
            result = RESULTS[req_id]
            # return result
            RESULT = result

# Emit the request
def generate(request):
    sio.emit('request', request)
    while not DONE:
        time.sleep(0.01)
    return RESULT




