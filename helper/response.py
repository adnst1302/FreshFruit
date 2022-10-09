resultResponse = {
    'status' : '',
    'message' : '',
    'data' : ''
}

def buildResponse(status, message, data):
    resultResponse['status'] = status
    resultResponse['message'] = message
    resultResponse['data'] = data
    return resultResponse

def setAggreate(data):
    return 0
