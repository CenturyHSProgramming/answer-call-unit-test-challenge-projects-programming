# answerCall.py
# by Matthew McClelland

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall)

# Write function defintion: answerCall()
def answerCall(caller_codes, sameAreaCode, cur_time):

    time_string = cur_time.split(":")[0]
    time = int(time_string)

    if time > 22 or time < 7:
        return False

    if caller_codes == "T":
        return False

    if caller_codes == "U" and sameAreaCode == False:
        return False
   
    if caller_codes == "F" or "R":
        return True

    return False

# Make sure it returns a value

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    test = answerCall("U", False, "08:00")
    print(test)
