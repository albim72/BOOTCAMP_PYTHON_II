from datetime import datetime,timedelta

class NewBucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0
        
    def __repr__(self):
        return (f'NeBucket(max_quota={self.max_quota}, '
                f'quota_consumed={self.quota_consumed})')
    
    @property
    def quota(self):
        return self.max_quota - self.quota_consumed
    
    @quota.setter
    def quota(self,amount):
        delta = self.max_quota - amount
        if amount == 0:
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta
