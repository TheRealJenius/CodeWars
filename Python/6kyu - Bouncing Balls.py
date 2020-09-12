def bouncing_ball(h, bounce, window):
    '''
    If all three conditions above are fulfilled, return a positive integer, otherwise return -1.
    - Float parameter "h" in meters must be greater than 0
    - Float parameter "bounce" must be greater than 0 and less than 1
    - Float parameter "window" must be less than h.
    '''
    
    '''
    if (h > 0) and (bounce> 0 and bounce < 1) and (window < h):
        ball_from_window = -1
        
        while h > window:
            ball_from_window += 2
            h = h * bounce                
        return ball_from_window
    '''
        # I'm going to try using recursion instead of the above

    return (2 + bouncing_ball(h * bounce, bounce, window)) if (h > 0) and (bounce> 0 and bounce < 1) and (window < h) else (-1)

#recursion worked =)