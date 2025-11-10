def breakdown_time(seconds):
    if not isinstance (seconds,int):
        if isinstance(seconds, float) and seconds.is_integer():
            seconds = int(seconds)
        else:
            return -1
        if seconds < 0:
            return -1     
    if seconds == 0:
        return {}
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    result = {}
    if hours > 0:
        result [3600]= hours
    if minutes > 0:
        result [60]= minutes
    if seconds > 0:
        result [1]= seconds
    return result

        
        
    