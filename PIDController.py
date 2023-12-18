class PID_Controller:
    
    def __init__(self, P=0, I=0, D=0):
        self.P = P
        self.I = I
        self.D = D
        self.integral = 0
        self.previous_error = 0

    def set_PID(self, P, I, D):
        self.P = P
        self.I = I
        self.D = D

    def Calculate(self, current_error, dt):
        # Calculate proportional term
        proportional = self.P * current_error

        # Calculate integral term
        self.integral += current_error * dt
        integral = self.I * self.integral

        # Calculate derivative term
        derivative = self.D * (current_error - self.previous_error) / dt
        self.previous_error = current_error

        # Total PID calculation
        return proportional + integral + derivative
